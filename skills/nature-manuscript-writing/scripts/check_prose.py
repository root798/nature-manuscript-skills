#!/usr/bin/env python3
"""Find editorial review points in plain English prose. Never edit the input."""
import argparse
import csv
import json
import re
import sys
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"


def read_rows(path, fields):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        if reader.fieldnames != fields:
            raise ValueError(f"{path.name}: expected columns {', '.join(fields)}")
        for row_number, row in enumerate(reader, 2):
            if None in row or not all((row.get(field) or "").strip() for field in fields):
                raise ValueError(f"{path.name}: incomplete row {row_number}")
            yield row


def literal_phrase(value):
    words = [re.escape(word) for word in value.split()]
    return r"(?<!\w)" + r"\s+".join(words) + r"(?!\w)"


def load_patterns(terms, section):
    patterns = []
    for row in read_rows(ASSETS / "prose-signals.tsv",
                         ["id", "category", "pattern", "review"]):
        patterns.append((row["id"], row["category"], re.compile(row["pattern"], re.I),
                         row["review"]))
    if terms:
        for row in read_rows(terms, ["scope", "avoid", "preferred", "meaning"]):
            if row["scope"] != "*" and row["scope"].casefold() != section.casefold():
                continue
            if row["avoid"].casefold() == row["preferred"].casefold():
                raise ValueError("A term lock must distinguish the avoided and preferred forms.")
            patterns.append(("LOCK", "术语锁", re.compile(literal_phrase(row["avoid"]), re.I),
                             f"核对是否指 {row['meaning']}。若是，采用 {row['preferred']}。"))
    return patterns


def findings(text, patterns):
    for line_number, line in enumerate(text.splitlines(), 1):
        line_hits = []
        for rule, category, pattern, note in patterns:
            for match in pattern.finditer(line):
                line_hits.append((match.start(), rule, category, match.group(), note))
        for offset, rule, category, phrase, note in sorted(line_hits):
            yield dict(line=line_number, column=offset + 1, rule=rule, category=category,
                       match=phrase, review=note)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", help="UTF-8 plain text file, or - for stdin")
    parser.add_argument("--terms", type=Path, help="optional term-lock TSV")
    parser.add_argument("--section", default="Results", help="scope for term locks")
    parser.add_argument("--json", action="store_true", help="return a JSON array")
    parser.add_argument("--strict-terms", action="store_true",
                        help="exit with code 1 if a configured term lock matches")
    args = parser.parse_args()
    try:
        text = sys.stdin.read() if args.file == "-" else Path(args.file).read_text(encoding="utf-8-sig")
        hits = list(findings(text, load_patterns(args.terms, args.section)))
    except (OSError, UnicodeError, ValueError, re.error) as exc:
        parser.error(str(exc))
    if args.json:
        print(json.dumps(hits, ensure_ascii=False, indent=2))
    else:
        for hit in hits:
            print(f"{hit['line']}:{hit['column']} [{hit['rule']}] {hit['match']} — {hit['review']}")
        print(f"{len(hits)} review point(s).")
    return int(args.strict_terms and any(hit["rule"] == "LOCK" for hit in hits))


if __name__ == "__main__":
    sys.exit(main())
