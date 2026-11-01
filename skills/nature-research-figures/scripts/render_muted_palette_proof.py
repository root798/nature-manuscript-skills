"""Render muted palette alternatives on the same paired data at publication width."""
import argparse
import csv
import json
from html import escape
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"
WIDTH, HEIGHT = 692, 426


def draw_mark(x, y, shape, fill, edge):
    style = f'fill="{fill}" stroke="{edge}" stroke-width="1.25"'
    if shape == "circle":
        return f'<circle cx="{x}" cy="{y}" r="3.6" {style}/>'
    if shape == "square":
        return f'<rect x="{x-3.3}" y="{y-3.3}" width="6.6" height="6.6" {style}/>'
    if shape == "diamond":
        vertices = [(x, y-4.6), (x+4.6, y), (x, y+4.6), (x-4.6, y)]
    elif shape == "triangle":
        vertices = [(x, y-4.6), (x+4.2, y+3.1), (x-4.2, y+3.1)]
    else:
        raise ValueError(f"Unknown shape {shape}")
    points = " ".join(f"{a},{b}" for a, b in vertices)
    return f'<polygon points="{points}" {style}/>'


def palette_proof(palette, rows):
    families = palette["families"]
    neutral = palette["neutrals"]
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="183mm" height="{183*HEIGHT/WIDTH:.3f}mm" '
        f'viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="heading desc">',
        '<title id="heading">Low-chroma colours for research figures</title>',
        '<desc id="desc">Two panels use the same five synthetic specimens with two alternative pairs of colours. '
        'Circles and diamonds distinguish the settings. Each point is a two-reading mean and its bar spans both readings. '
        'Four direct-labelled marker shapes, a magnitude scale and a signed scale show other encodings. '
        'A separate slashed cell marks missing data.</desc>',
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="{neutral["background"]}"/>',
        f'<g font-family="Arial,Helvetica,sans-serif" fill="{neutral["ink"]}">',
    ]

    def text(x, y, label, size=10.5, weight=400, anchor="start"):
        out.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" '
                   f'text-anchor="{anchor}">{escape(str(label))}</text>')

    def line(x1, y1, x2, y2, stroke, width=1, dash=""):
        pattern = f' stroke-dasharray="{dash}"' if dash else ""
        out.append(f'<path d="M{x1},{y1} L{x2},{y2}" fill="none" '
                   f'stroke="{stroke}" stroke-width="{width}"{pattern}/>')

    def panel_title(x, y, letter, title):
        text(x, y, letter, 14, 700)
        text(x+17, y, title, 14, 600)

    def paired_panel(left, letter, pair):
        pair_names = palette["pairs"][pair]
        panel_title(left, 95, letter, " / ".join(k.capitalize() for k in pair_names))
        start, end = left+49, left+297
        observed = [float(row[f"{setting}_{read}_ms"]) for row in rows
                    for setting in ("a", "b") for read in ("first", "second")]
        if min(observed) < 8 or max(observed) > 24:
            raise ValueError("The fixed proof axis is 8–24 ms. Update the axis for a new data set.")
        def x(value):
            return start+(end-start)*(value-8)/16

        for mark, label, dx, name in zip(("circle", "diamond"), ("Setting A", "Setting B"),
                                         (0, 94), pair_names):
            family = families[name]
            out.append(draw_mark(left+5+dx, 115, mark, family["fill"], family["edge"]))
            text(left+17+dx, 119, label)
        text(left, 142, "Specimen", 10)
        for tick in (8, 12, 16, 20, 24):
            line(x(tick), 150, x(tick), 238, neutral["reference"], 0.6, "1.8 3.2")
            text(x(tick), 253, tick, 10, anchor="middle")
        for i, row in enumerate(rows):
            y = 158+i*17
            text(left+17, y+3, row["specimen"], 10.5, anchor="middle")
            for setting, key, shape, shift in zip(("a", "b"), pair_names,
                                                  ("circle", "diamond"), (-3.4, 3.4)):
                family = families[key]
                a, b = sorted(float(row[f"{setting}_{read}_ms"]) for read in ("first", "second"))
                ny = y+shift
                line(x(a), ny, x(b), ny, family["band"], 4.8)
                line(x(a), ny, x(b), ny, family["edge"], 1.1)
                for v in (a, b):
                    line(x(v), ny-2, x(v), ny+2, family["edge"], 1.05)
                out.append(draw_mark(x((a+b)/2), ny, shape, family["fill"], family["edge"]))
        line(start, 238, end, 238, neutral["reference"], 0.8)
        text((start+end)/2, 269, "Readout time (ms)", 10.5, anchor="middle")

    def scale(x, y, stops, label, signed=False):
        text(x, y+9, label, 10.5)
        width = 167
        start = x+91
        for i, colour in enumerate(stops):
            out.append(f'<rect x="{start+i*width/len(stops):.2f}" y="{y}" '
                       f'width="{width/len(stops)+0.02:.2f}" height="13" fill="{colour}"/>')
        line(start, y+13.4, start+width, y+13.4, neutral["reference"], 0.65)
        labels = [(0, "−"), (0.5, "0"), (1, "+")] if signed else [(0, "Low"), (1, "High")]
        for pos, word in labels:
            at = start+pos*width
            line(at, y+13, at, y+16, neutral["reference"], 0.65)
            text(at, y+27, word, 10, anchor="middle")

    text(22, 32, "Low-chroma colours for research figures", 23, 600)
    text(23, 55, "Compare two hue pairs on the same observations. Choose the pair that suits the manuscript.", 12)
    line(22, 70, 670, 70, neutral["reference"], 0.7)
    paired_panel(23, "a", "slate_clay")
    paired_panel(357, "b", "sage_plum")
    line(22, 282, 670, 282, neutral["reference"], 0.7)

    panel_title(23, 305, "c", "Distinguish four specimen types")
    for i, (name, shape, specimen) in enumerate(zip(
            palette["categorical"], ("circle", "square", "triangle", "diamond"),
            ("Bead", "Fibre", "Pellet", "Foam"))):
        family = families[name]
        col = 23+79*i
        out.append(f'<rect x="{col}" y="321" width="62" height="19" fill="{family["fill"]}"/>')
        out.append(draw_mark(col+4.5, 354, shape, family["fill"], family["edge"]))
        text(col+13, 358, specimen, 10.5)
        text(col, 377, family["fill"].upper(), 10)
    panel_title(357, 305, "d", "Encode a magnitude or a change")
    scale(357, 322, palette["sequential"]["sage"], "Magnitude")
    scale(357, 363, palette["diverging"]["clay_to_slate"], "Signed change", signed=True)
    out.append(f'<rect x="642" y="363" width="15" height="13" fill="{neutral["missing"]}" '
               f'stroke="{neutral["reference"]}" stroke-width="0.8"/>')
    line(643, 375, 656, 364, neutral["ink"], 0.9)
    text(649.5, 390, "NA", 10, anchor="middle")
    line(22, 403, 670, 403, neutral["reference"], 0.7)
    text(23, 419, "a, b   Synthetic data. Each point is the mean of two readings. Bars span their range.", 10)
    text(670, 419, "Width 183 mm", 10, anchor="end")
    out.append("</g></svg>")
    return "\n".join(out)+"\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ASSETS/"muted-palette-proof.svg")
    args = parser.parse_args()
    palette = json.loads((ASSETS/"palettes.json").read_text(encoding="utf-8"))["goal_muted"]
    with (ASSETS/"example-readings.csv").open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    args.out.write_text(palette_proof(palette, rows), encoding="utf-8")


if __name__ == "__main__":
    main()
