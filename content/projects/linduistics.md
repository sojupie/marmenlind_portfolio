---
title: 'Linduistics (WIP)'
slug: 'linduistics'
date: 2026-10-12
description: 'A work-in-progress application for comparing vocabulary, pronunciation, and meaning across five Germanic languages.'
summary: 'A work-in-progress lexical analysis platform combining articulatory phonetic comparison, multilingual word-sense alignment, and an interactive language map.'
year: '2026 · Work in progress'
discipline: 'Python / Go / PostgreSQL / React / TypeScript'
featured: true
---

Linduistics is under active development and has no public release yet. It brings together a comparative lexicon, a text inspector, and language games for exploring relationships across five Germanic languages.

## Phonetic comparison and word senses

The phonetic engine compares pronunciations through weighted edit distance over articulatory features. A precomputed sound-distance matrix and Numba JIT compilation support the computation, with rolling buffers keeping working memory linear in pronunciation length.

The dataset pipeline combines translation-graph mining, spelling collisions, and multilingual embeddings to align individual word senses. Each selected sense retains its source identity and etymological evidence, including unresolved ambiguity between entries.

## Dataset builds and interface

Reproducible, resumable builds use field-level regression checks to preserve numerical behavior across Python, Parquet, and PostgreSQL. Comparisons and related lookup tables are published in one transaction.

The React/TypeScript interface connects to a Go API and Python NLP service. An interactive 2D/3D language map uses multidimensional scaling and iterative stress minimization to visualize relationships between languages.
