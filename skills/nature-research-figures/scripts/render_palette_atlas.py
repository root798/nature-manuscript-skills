"""Create the offline SVG swatch sheet using only the Python standard library."""
import argparse
import json
from html import escape
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"


def marker(x, y, shape, fill, edge):
    style = f'fill="{fill}" stroke="{edge}" stroke-width="2"'
    if shape == "o":
        return f'<circle cx="{x}" cy="{y}" r="8" {style}/>'
    if shape == "s":
        return f'<rect x="{x-8}" y="{y-8}" width="16" height="16" {style}/>'
    points = [(x, y - 10), (x + 9, y + 7), (x - 9, y + 7)] if shape == "^" else [
        (x, y - 10), (x + 8, y), (x, y + 10), (x - 8, y)]
    return f'<polygon points="{" ".join(f"{a},{b}" for a,b in points)}" {style}/>'


def make_atlas(p):
    width = 1020
    parts = []
    def label(x, y, text, size=15, weight=400, color="#222222"):
        parts.append(f'<text x="{x}" y="{y}" font-family="Arial,Helvetica,sans-serif" '
                     f'font-size="{size}" font-weight="{weight}" fill="{color}">{escape(text)}</text>')
    def section(y, num, name):
        parts.append(f'<path d="M32 {y-23}H988" stroke="#C8C8C8"/>')
        label(32, y, num, 14, 700, "#535C7E")
        label(74, y, name, 20, 700)
    def strip(y, title, colors, label_x=32):
        label(label_x, y + 20, title)
        for index, color in enumerate(colors):
            x = 248 + index * 144
            parts.append(f'<rect x="{x}" y="{y}" width="126" height="25" fill="{color}" '
                         'stroke="#555555" stroke-width="0.6"/>')
            label(x, y + 43, color, 13)
    label(32, 45, "Research figure palettes", 31, 700)
    label(32, 73, "Choose one mapping per scientific variable. Read each row from left to right.")
    section(128, "01", "Paired measurements")
    for j, k in enumerate(("setting_a", "setting_b")):
        s = p["paired"][k]
        y = 155 + 65*j
        parts.append(marker(45, y + 13, s["marker"], s["mark"], p["paired"]["ink"]))
        strip(y, k.replace("_", " ").title(), [s["mark"], s["range"], s["dark"]], label_x=67)
    label(248, 296, "Mark", 13)
    label(392, 296, "Range", 13)
    label(536, 296, "Dark companion", 13)
    strip(315, "Neutral reference / ink / muted", [p["paired"][k] for k in ("control", "ink", "muted")])
    section(405, "02", "Four categories and signed values")
    strip(429, "Categorical key", p["categorical"].values())
    strip(490, "Signed: low → zero → high", p["signed_matrix"]["stops_low_to_high"])
    section(585, "03", "Soft four-colour profile")
    for j, s in enumerate(p["soft_four"].values()):
        x = 48 + 242*j
        parts.append(marker(x, 622, s["marker"], s["fill"], s["edge"]))
        label(x+18, 628, f'Slot {j+1}', 15, 700)
        label(x, 653, s["fill"] + " / " + s["edge"], 14)
    strip(674, "Single accent / soft band", [p["soft_neutrals"][k] for k in ("single_accent","band")])
    section(770, "04", "Alternative and historical scales")
    strip(793, "Optional pair: fills / edges", [p["optional_pair"][k][v]
         for k in ("periwinkle", "mauve") for v in ("fill", "edge")])
    strip(853, "Ordered: low → high", p["historical_scales"]["sequential_low_to_high"])
    strip(913, "Earlier signed scale", p["historical_scales"]["diverging_low_to_high"])
    section(1004, "05", "Archived four-colour settings")
    label(32, 1034, "Variant")
    label(248, 1034, "Slot 1")
    label(426, 1034, "Slot 2")
    label(604, 1034, "Slot 3")
    label(782, 1034, "Slot 4")
    for j, (name, variant) in enumerate(p["archived_four"].items()):
        y = 1070 + 36*j
        label(32, y + 4, name, 16, 700)
        for i, (f, e, m) in enumerate(zip(variant["fills"], variant["edges"], p["archived_four_markers"])):
            x = 256 + 178*i
            parts.append(marker(x, y, m, f, e))
            label(x + 16, y + 4, f, 14)
    label(32, 1302, "Exact edge tones, interval tones, optional line patterns and missing-value marking: palettes.json", 14)
    # No scripts, external fonts, embedded data, author field, or workstation paths.
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="1330" '
            f'viewBox="0 0 {width} 1330" role="img" aria-labelledby="title desc">\n'
            '<title id="title">Scientific figure palette atlas</title>\n'
            '<desc id="desc">Five sections show hex colours, marker shapes, signed ramps, and archived settings.</desc>\n'
            f'<rect width="{width}" height="1330" fill="white"/>\n' + "\n".join(parts) + "\n</svg>\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ASSETS / "palette-atlas.svg")
    args = parser.parse_args()
    palette = json.loads((ASSETS / "palettes.json").read_text(encoding="utf-8"))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(make_atlas(palette), encoding="utf-8")


if __name__ == "__main__":
    main()
