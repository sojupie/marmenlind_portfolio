#!/usr/bin/env python3
"""Create the small, self-hosted Noto Sans webfont set used by the site."""

from pathlib import Path

from fontTools import subset


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "font-sources" / "Noto_Sans" / "static"
MONO_SOURCE = ROOT / "font-sources" / "static"
TARGET = ROOT / "static" / "assets" / "fonts" / "noto-sans-subset"
UNICODES = (
    "U+0020-007E,"     # Basic Latin
    "U+00A0-00FF,"     # Latin-1 punctuation and symbols
    "U+0100-017F,"     # Latin Extended-A
    "U+2000-206F,"     # General punctuation
    "U+2070-209F,"     # Superscripts and subscripts
    "U+20A0-20CF,"     # Currency symbols
    "U+2100-214F,"     # Letterlike symbols
    "U+2190-21FF"      # Arrows
)

FONTS = {
    "NotoSans-Regular.ttf": "NotoSans-Regular.woff2",
    "NotoSans-Italic.ttf": "NotoSans-Italic.woff2",
    "NotoSans-Medium.ttf": "NotoSans-Medium.woff2",
    "NotoSans-SemiBold.ttf": "NotoSans-SemiBold.woff2",
    "NotoSans-Bold.ttf": "NotoSans-Bold.woff2",
}
MONO_FONTS = {
    "NotoSansMono-Regular.ttf": "NotoSansMono-Regular.woff2",
}


def subset_font(source: Path, target: Path) -> None:
    options = subset.Options()
    options.flavor = "woff2"
    options.layout_features = ["*"]
    options.hinting = False
    options.desubroutinize = True
    font = subset.load_font(source, options)
    subsetter = subset.Subsetter(options=options)
    subsetter.populate(unicodes=subset.parse_unicodes(UNICODES))
    subsetter.subset(font)
    subset.save_font(font, target, options)


def main() -> None:
    TARGET.mkdir(parents=True, exist_ok=True)
    for source_name, target_name in FONTS.items():
        subset_font(SOURCE / source_name, TARGET / target_name)
        print(f"{source_name} -> {target_name}")
    for source_name, target_name in MONO_FONTS.items():
        subset_font(MONO_SOURCE / source_name, TARGET / target_name)
        print(f"{source_name} -> {target_name}")


if __name__ == "__main__":
    main()
