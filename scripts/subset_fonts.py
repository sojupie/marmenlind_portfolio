#!/usr/bin/env python3
"""
Font Subsetting Script for marmenlind_portfolio
================================================
This script subsets the self-hosted Roslindale fonts from `assets/fonts_original/`
and writes optimized, minimal .woff2 files to `static/assets/fonts/`.

Included Unicode Ranges:
- U+0020-007E: Basic Latin (ASCII printable characters, letters, digits, punctuation)
- U+00A0-00FF: Latin-1 Supplement (Swedish characters: å, ä, ö, Å, Ä, Ö; accents: é, è, etc.; ©, ®, etc.)
- U+0100-017F: Latin Extended-A (European diacritics)
- U+2000-206F: General Punctuation (em-dash —, en-dash –, curly quotes ‘ ’ “ ”, ellipsis …, bullets •)
- U+2070-209F: Superscripts and Subscripts
- U+20A0-20CF: Currency Symbols (€, etc.)
- U+2100-214F: Letterlike Symbols
- U+2190-21FF: Arrows (←, ↑, →, ↓)

Prerequisites:
  pip install fonttools brotli
"""

import os
import sys
from fontTools import subset

# Source directory containing the full original fonts
SRC_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "fonts_original")

# Target directory served by Hugo
DST_DIR = os.path.join(os.path.dirname(__file__), "..", "static", "assets", "fonts")

# Unicode ranges covering English, Swedish, common European characters, typography & symbols
UNICODE_RANGES = (
    "U+0020-007E,"   # Basic Latin
    "U+00A0-00FF,"   # Latin-1 Supplement (Swedish å, ä, ö, Å, Ä, Ö, etc.)
    "U+0100-017F,"   # Latin Extended-A
    "U+2000-206F,"   # General Punctuation (quotes, dashes, spaces)
    "U+2070-209F,"   # Superscripts and Subscripts
    "U+20A0-20CF,"   # Currency Symbols
    "U+2100-214F,"   # Letterlike Symbols
    "U+2190-21FF"    # Arrows
)

# Fonts excluded from production deployment (pruned to reduce payload)
EXCLUDED_FONTS = {
    "RoslindaleDeckNarrow-Medium-Edu.woff2",  # Navbar branding switched to regular Deck Narrow
}


def subset_font(src_path: str, dst_path: str):
    options = subset.Options()
    options.flavor = "woff2"
    options.layout_features = ["*"]  # Preserve kerning, ligatures, and OpenType features
    options.hinting = False          # TrueType hinting is not needed on modern web renderers
    options.desubroutinize = True

    font = subset.load_font(src_path, options)
    subsetter = subset.Subsetter(options=options)
    subsetter.populate(unicodes=subset.parse_unicodes(UNICODE_RANGES))
    subsetter.subset(font)
    subset.save_font(font, dst_path, options)


def main():
    if not os.path.isdir(SRC_DIR):
        print(f"Error: Source directory {SRC_DIR} does not exist.")
        sys.exit(1)

    os.makedirs(DST_DIR, exist_ok=True)

    print("=" * 70)
    print("Marmenlind Portfolio - Font Subsetter")
    print("=" * 70)
    print(f"Source: {os.path.abspath(SRC_DIR)}")
    print(f"Target: {os.path.abspath(DST_DIR)}")
    print("-" * 70)

    total_orig = 0
    total_sub = 0

    files = sorted(os.listdir(SRC_DIR))
    for filename in files:
        if not filename.endswith(".woff2"):
            continue

        src_file = os.path.join(SRC_DIR, filename)
        dst_file = os.path.join(DST_DIR, filename)
        orig_size = os.path.getsize(src_file)

        if filename in EXCLUDED_FONTS:
            # If the excluded font exists in the target folder, delete it
            if os.path.exists(dst_file):
                os.remove(dst_file)
            print(f"  [EXCLUDED] {filename:<38} ({orig_size / 1024:5.1f} KB -> REMOVED)")
            continue

        subset_font(src_file, dst_file)
        sub_size = os.path.getsize(dst_file)
        savings = (orig_size - sub_size) / orig_size * 100

        total_orig += orig_size
        total_sub += sub_size

        print(f"  [SUBSET]   {filename:<38} {orig_size / 1024:5.1f} KB -> {sub_size / 1024:5.1f} KB (-{savings:.1f}%)")

    print("-" * 70)
    print(f"Active Fonts: {total_orig / 1024:5.1f} KB -> {total_sub / 1024:5.1f} KB (-{(total_orig - total_sub) / total_orig * 100:.1f}%)")
    print("=" * 70)
    print("Done! Subsetting complete.")


if __name__ == "__main__":
    main()
