# Typography & Font Optimization Guide

This project uses custom self-hosted typefaces alongside modern system monospace fonts to achieve a refined editorial aesthetic with ultra-fast page load times.

---

## Font Family Overview

| CSS Variable | Family | Source | Role |
| :--- | :--- | :--- | :--- |
| `--font-sans` | **Roslindale Display** | Self-hosted (`.woff2`) | Page titles, major H1 headings |
| `--font-deck` | **Roslindale Deck** | Self-hosted (`.woff2`) | Intro text, section headers, navbar title |
| `--font-serif` | **Roslindale Text** | Self-hosted (`.woff2`) | Long-form body copy, articles, descriptions |
| `--font-mono` | **SF Mono / ui-monospace** | System font stack | Code snippets, technical metadata, labels |

---

## Self-Hosted Roslindale Fonts

The active fonts served to browsers are stored in `static/assets/fonts/`.

### Active Font Files & Sizes

| File | Weight / Style | Original Size | Subsetted Size | Savings |
| :--- | :--- | :--- | :--- | :--- |
| `RoslindaleDisplay-Medium-Edu.woff2` | Medium (500) | 64.9 KB | **37.3 KB** | **-42.6%** |
| `RoslindaleDisplay-Light-Edu.woff2` | Light (300) | 64.2 KB | **37.0 KB** | **-42.4%** |
| `RoslindaleDeckNarrow-Regular-Edu.woff2` | Regular (400) | 65.7 KB | **37.5 KB** | **-42.9%** |
| `RoslindaleText-Regular-Edu.woff2` | Regular (400) | 60.9 KB | **32.8 KB** | **-46.1%** |
| `RoslindaleText-Italic-Edu.woff2` | Italic (300) | 65.4 KB | **35.9 KB** | **-45.1%** |
| `RoslindaleText-SemiBold-Edu.woff2` | SemiBold (600) | 63.9 KB | **34.8 KB** | **-45.6%** |
| `RoslindaleText-Bold-Edu.woff2` | Bold (700) | 61.8 KB | **32.8 KB** | **-46.9%** |
| **Total Active Fonts** | | **446.7 KB** | **248.1 KB** | **-44.5%** |

> [!NOTE]
> **Pruned Variant:** `RoslindaleDeckNarrow-Medium-Edu.woff2` (66.2 KB) was previously loaded solely for the navbar brand link. The navbar now uses `RoslindaleDeckNarrow-Regular` (`font-normal`), completely eliminating that 66 KB download.

---

## Why and How Fonts Are Subsetted

Commercial typefaces ship with comprehensive character sets (often 1,000+ glyphs) including Cyrillic, Greek, fractions, complex math symbols, and historical ligatures. 

Subsetting strips away all unused tables and glyphs while preserving:
- Full English and Swedish alphabets (including `å`, `ä`, `ö`, `Å`, `Ä`, `Ö`).
- Common European diacritics (`é`, `è`, `ê`, `ü`, `ñ`, etc.).
- Editorial punctuation (curly quotes `‘` `’` `“` `”`, em dash `—`, en dash `–`, ellipsis `…`, bullets `•`).
- Common symbols and currency (`€`, `$`, `£`, `©`, `®`, `°`, `²`, `³`).
- OpenType features (`*`) including standard ligatures, discretionary ligatures, and kerning tables.

### Original Full Font Backup

The complete, un-subsetted `.woff2` files are safely archived in:
```text
assets/fonts_original/
```
These source files are **not** served directly by Hugo (since they reside in `assets/`, not `static/`).

---

## Re-Running or Updating the Subsetting

If you add new content requiring additional Unicode glyphs, or want to update font configurations, run:

```bash
pnpm run subset:fonts
```

Or run Python directly:
```bash
python scripts/subset_fonts.py
```

### Script Requirements
The script uses `fonttools` and `brotli`:
```bash
pip install fonttools brotli
```

### Customizing the Unicode Range
Edit `UNICODE_RANGES` in `scripts/subset_fonts.py`:
```python
UNICODE_RANGES = (
    "U+0020-007E,"   # Basic Latin (ASCII)
    "U+00A0-00FF,"   # Latin-1 Supplement (Swedish å, ä, ö, accents)
    "U+0100-017F,"   # Latin Extended-A
    "U+2000-206F,"   # General Punctuation (quotes, dashes)
    "U+2070-209F,"   # Superscripts and Subscripts
    "U+20A0-20CF,"   # Currency Symbols (€)
    "U+2100-214F,"   # Letterlike Symbols
    "U+2190-21FF"    # Arrows
)
```

---

## System Monospace Font Stack

Rather than downloading 32+ KiB of Google Fonts JetBrains Mono over the network, monospace text uses the native system font stack:

```css
--font-mono: "SF Mono", ui-monospace, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
```

- **macOS / iOS:** Renders in **SF Mono** (crisp San Francisco Monospaced).
- **Windows:** Renders in **Consolas**.
- **Linux:** Renders in **Liberation Mono** or system monospace.
- **Cost:** **0 bytes, 0 HTTP requests, 0 latency**.

---

## Performance & Caching

1. **Preloading Above-the-Fold Fonts:**
   The 3 essential fonts needed for initial paint are preloaded in `<head>` via `layouts/_default/baseof.html`:
   - `RoslindaleDisplay-Medium-Edu.woff2` (H1 title)
   - `RoslindaleText-Regular-Edu.woff2` (Body copy)
   - `RoslindaleDeckNarrow-Regular-Edu.woff2` (Intro paragraph)

2. **HTTP Caching in Production:**
   When deployed behind a CDN or web host, `.woff2` files should be served with immutable caching headers:
   ```http
   Cache-Control: public, max-age=31536000, immutable
   ```
   After initial download, repeat page views and navigation across pages load all fonts instantly with zero network cost.
