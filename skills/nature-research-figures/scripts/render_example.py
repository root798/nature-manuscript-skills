"""Render a paired figure from two readings per setting and specimen.

From the skill directory: python3 scripts/render_example.py --out build
Dependencies: Python 3 and Matplotlib. The default input is synthetic.
"""
import argparse
import csv
import json
import math
import statistics
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

ASSETS = Path(__file__).resolve().parents[1] / "assets"
SETTINGS = ("a", "b")
COLUMNS = ["specimen", "a_first_ms", "a_second_ms", "b_first_ms", "b_second_ms"]


def read_table(path):
    rows = []
    seen = set()
    with path.open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != COLUMNS:
            raise ValueError(f"Expected columns {COLUMNS}")
        for row in reader:
            specimen = row["specimen"].strip()
            if not specimen or specimen in seen:
                raise ValueError(f"Expected a unique specimen identifier at row {reader.line_num}")
            values = [float(row[c]) for c in COLUMNS[1:]]
            if not all(math.isfinite(x) and x >= 0 for x in values):
                raise ValueError(f"Expected finite, non-negative times at row {reader.line_num}")
            seen.add(specimen)
            rows.append((specimen, values[:2], values[2:]))
    if not rows:
        raise ValueError("No specimens in input")
    return rows


def configure(ink):
    plt.rcParams.update({
        "font.family": "sans-serif", "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
        "font.size": 7, "text.color": ink, "axes.labelcolor": ink, "axes.edgecolor": ink,
        "xtick.color": ink, "ytick.color": ink, "axes.linewidth": 0.5,
        "xtick.major.width": 0.5, "ytick.major.width": 0.5,
        "xtick.major.size": 2.5, "ytick.major.size": 2.5, "lines.linewidth": 0.9,
        "axes.spines.top": False, "axes.spines.right": False, "legend.frameon": False,
        "pdf.fonttype": 42, "svg.fonttype": "none", "svg.hashsalt": "paired-figure-v1",
        "savefig.bbox": None, "savefig.facecolor": "white",
    })


def paired_style(palettes, name):
    if name == "archived":
        return palettes["paired"]
    muted = palettes["goal_muted"]
    if name not in muted["pairs"]:
        raise ValueError(f"Unknown pair {name!r}; choose from {', '.join(muted['pairs'])} or archived")
    neutral = muted["neutrals"]
    a, b = muted["pairs"][name]
    style = {"ink": neutral["ink"], "control": neutral["reference"]}
    for key, hue, shape in zip(SETTINGS, (a, b), ("o", "D")):
        family = muted["families"][hue]
        style["setting_" + key] = {"mark": family["fill"], "edge": family["edge"], "range": family["band"],
                                    "marker": shape, "range_linestyle": "-"}
    return style


def render(rows, paired, output):
    configure(paired["ink"])
    height_mm = max(78, 36 + 7 * len(rows))
    fig, (absolute, delta) = plt.subplots(
        1, 2, figsize=(183 / 25.4, height_mm / 25.4), gridspec_kw={"width_ratios": [1.45, 1]}
    )
    fig.subplots_adjust(left=0.085, right=0.965, bottom=0.19, top=0.80, wspace=0.40)
    ids = [row[0] for row in rows]
    handles = []
    for index, key in enumerate(SETTINGS):
        style = paired["setting_" + key]
        off = (-0.13, 0.13)[index]
        for y, row in enumerate(rows):
            values = row[index + 1]
            absolute.hlines(y + off, min(values), max(values), color=style["range"],
                            linewidth=2.2, linestyles=style["range_linestyle"])
            if "edge" in style:
                # The pale band shows the family; its thin spine keeps the two observed limits legible.
                absolute.hlines(y + off, min(values), max(values), color=style["edge"], linewidth=0.55)
            absolute.plot(statistics.mean(values), y + off, marker=style["marker"], ms=4,
                          color=style["mark"], markeredgecolor=style.get("edge", paired["ink"]), markeredgewidth=0.4)
        handles.append(Line2D([], [], marker=style["marker"], linestyle="none",
                              markerfacecolor=style["mark"], markeredgecolor=style.get("edge", paired["ink"]),
                              markeredgewidth=0.4, label="Setting " + key.upper(), markersize=4))
    diffs = [statistics.mean(b) - statistics.mean(a) for _, a, b in rows]
    delta.axvline(0, color=paired["control"], linewidth=0.7, linestyle="--", zorder=0)
    delta.scatter(diffs, range(len(rows)), s=14, marker="o", color=paired["ink"])
    # Include zero and a small margin at both extremes; every mark remains visible.
    lo, hi = min([0, *diffs]), max([0, *diffs])
    margin = max(0.15 * (hi - lo), 0.5)
    delta.set_xlim(lo - margin, hi + margin)
    for ax in (absolute, delta):
        ax.set_ylim(len(rows) - 0.5, -0.5)
        ax.set_yticks(range(len(rows)), labels=ids)
    absolute.set_ylabel("Specimen")
    absolute.set_xlabel("Readout time (ms)")
    delta.set_xlabel("Within-specimen difference, B − A (ms)")
    for letter, ax in zip("ab", (absolute, delta)):
        ax.text(-0.10, 1.055, letter, transform=ax.transAxes, fontweight="bold",
                fontsize=8, va="bottom", ha="left")
    fig.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.45, 0.98),
               ncol=2, handletextpad=0.35, columnspacing=1.5)

    output.mkdir(parents=True, exist_ok=True)
    svg = output / "example-figure.svg"
    fig.savefig(svg, metadata={"Date": None, "Creator": None})
    if "edge" in paired["setting_a"]:
        svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines()) + "\n",
                       encoding="utf-8")
    fig.savefig(output / "example-figure.pdf",
                metadata={"CreationDate": None, "ModDate": None, "Creator": None})
    fig.savefig(output / "example-figure.png", dpi=300)
    plt.close(fig)
    with (output / "example-summary.csv").open("w", encoding="utf-8", newline="") as destination:
        table = csv.writer(destination)
        table.writerow(["specimen", "a_mean_ms", "b_mean_ms", "b_minus_a_ms"])
        for (specimen, a, b), diff in zip(rows, diffs):
            table.writerow([specimen, statistics.mean(a), statistics.mean(b), diff])
    print(f"{len(rows)} paired specimens; mean B − A = {statistics.mean(diffs):.2f} ms")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=ASSETS / "example-readings.csv")
    parser.add_argument("--out", type=Path, default=Path("build"))
    parser.add_argument("--palette", default="slate_clay",
                        help="Two-family key under goal_muted.pairs (e.g. slate_clay, sage_plum), or archived")
    parser.add_argument("--palettes", type=Path, default=ASSETS / "palettes.json",
                        help="Use a manuscript-specific copy of the palette definitions")
    args = parser.parse_args()
    with args.palettes.open(encoding="utf-8") as file:
        palette = json.load(file)
    try:
        style = paired_style(palette, args.palette)
    except ValueError as error:
        parser.error(str(error))
    render(read_table(args.data), style, args.out)


if __name__ == "__main__":
    main()
