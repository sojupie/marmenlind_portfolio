---
title: 'B2B Scan-to-Order'
date: 2025-11-30
description: 'Android proof of concept for barcode-driven B2B ordering.'
summary: 'Android proof of concept for barcode-driven B2B ordering, integrating ML Kit scanning with product lookup, order handling, and synchronization.'
year: 'November 2025'
discipline: 'Kotlin / Android / Firestore / REST'
featured: true
weight: 10
external_url: 'https://github.com/sojupie/Scan2Go_PoC'
---

An Android Proof-of-Concept streamlining B2B inventory management via on-device barcode scanning.

<p class="project-links flex flex-wrap gap-4"><a class="inline-flex items-center gap-2 no-underline" href="https://github.com/sojupie/Scan2Go_PoC" target="_blank" rel="noopener noreferrer"><img class="project-github-icon size-8" src="/assets/img/github-invertocat.svg" alt=""/> <span class="underline decoration-1 underline-offset-3">GitHub repository</span><span class="sr-only"> (opens in new tab)</span></a></p>

<a href="https://youtube.com/shorts/-f4jlpWfxGo?feature=share" target="_blank" rel="noopener noreferrer">Video demo</a>

## Project Overview

Designed for field sales reps and store managers to "walk the floor" and restock inventory instantly. By using the phones camera to scan barcodes on shelves and products you the remove to memorize and search for article numbers/product names or navigate complex catalogs.

## Tech Stack

*   **Language:** Kotlin
*   **UI:** Jetpack Compose (Material 3)
*   **Architecture:** MVVM + Repository Pattern
*   **Backend:** Firebase (Auth, Firestore)
*   **Hardware:** Google Code Scanner (ML Kit) via Play Services
*   **Networking:** Retrofit (OpenFoodFacts API fallback)

## Architecture

The app uses a hybrid data strategy. It prioritizes the internal Firestore catalog for pricing/stock. If a scan is unrecognized, it queries the external OpenFoodFacts API to allow users to request new stock items.

*![plant uml diagram](image.png)*

## Key Features

*   **Hybrid Scanning:** Seamlessly handles internal vs. external products.
*   **Real-time State:** Cart badge and totals update instantly via Firestore Snapshot Listeners.
*   **Serverless:** Full Backend-as-a-Service implementation including Anonymous & Google Auth.
*   **Batch Operations:** Atomic writes for order processing to ensure data integrity.

## Disclaimer

This architecture utilizes client-side pricing logic not suitable for a public production release.
