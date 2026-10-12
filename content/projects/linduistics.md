---
title: 'Linduistics (WIP)'
slug: 'linduistics'
date: 2026-10-12
description: 'A work-in-progress application for comparing vocabulary, pronunciation, and meaning across five Germanic languages.'
summary: 'A work-in-progress application comparing pronunciation and word meanings across five Germanic languages, with text analysis and an interactive language map.'
year: '2026 · Work in progress'
discipline: 'Python / Go / PostgreSQL / React / TypeScript'
featured: true
---

Linduistics is under active development and has no public release yet. It combines a searchable lexicon, text analysis, and language games for comparing vocabulary, pronunciation, and meaning across five Germanic languages.

## Pronunciation and meaning

The pronunciation engine uses weighted edit distance, with sound substitution costs based on articulatory features: how and where sounds are produced. A precomputed distance matrix and Numba JIT compilation speed up comparisons, while two-row buffering reduces working memory from quadratic to linear in pronunciation length.

The dataset pipeline finds candidate word pairs through Wiktionary translation links and similar spellings, then uses multilingual embeddings to match specific word meanings. It retains source references and etymology and records ambiguity when a meaning cannot be uniquely matched.

## Dataset builds and interface

I refactored the dataset pipeline while preserving the accepted results for 1.6 million word comparisons. Field-level checks compare rebuilt data against that baseline before publication, including scores, classifications, source references, and row order.

Completed stages are saved so a failed run can restart without repeating earlier work. Before reusing those outputs, the runner checks hashes of the inputs, code, and output files and confirms that the runtime environment is unchanged. An interrupted stage runs again from its beginning.

Classification uses the same PostgreSQL REAL conversion as the original pipeline because small rounding differences near a score threshold can change a word pair's category. Applying that conversion before classification preserves the existing results through the refactor.

Comparisons and related lookup tables are published in one PostgreSQL transaction. If any table fails to load, the entire update rolls back, keeping the previous dataset intact.

The React/TypeScript interface connects to a Go API and Python NLP service. Its interactive 2D/3D map positions languages from pairwise distance data using multidimensional scaling, then refines those positions through iterative stress minimization.
