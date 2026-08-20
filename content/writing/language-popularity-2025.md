---
title: 'Programming-language migration and the staying power of Java'
date: 2026-08-19
description: 'An interpretation of JetBrains Research data on language migration, ecosystem turnover, and the JVM.'
summary: 'What language migration data suggests about Java, Python, TypeScript, Go, Rust, and the JVM ecosystem.'
tags: ['Programming languages', 'Java', 'JVM', 'JetBrains Research']
---

This article is based on [JetBrains Research's analysis of programming-language migration](https://blog.jetbrains.com/research/2026/08/programming-language-migration/). The charts below are from that study but the interpretation below is mine.

<figure>
  <img src="/assets/img/language-popularity-2025/churn_destinations_heatmap.webp" alt="Programming-language migration destinations heatmap">
  <figcaption>Source: <a href="https://blog.jetbrains.com/research/2026/08/programming-language-migration/">JetBrains Research, Programming Language Migration</a>.</figcaption>
</figure>

<h2>Legacy inertia</h2>

<p>– When devs move to a new "main language", Java comes in second place (after Python) despite a practically constant market share. In other words, the JVM ecosystem remains dominant, but with significant turnover.</p>

<p>– In addition, modern and more expressive languages such as Kotlin, Go, and Rust, occasionally imagined as replacements for "legacy Java", never actually displaced Java. Why wipe out a complete and mature ecosystem? Instead, they serve as niche additions to Java monoliths. Go for ease of use and low memory footprint in microservices and network infra, Rust for core services that require strict memory safety, Kotlin for Android (with cool improvements for Native/AOT/KMP), etc. These languages also see the largest transition back to Java, which reinforces the fact that Java remains the core platform they often support rather than replace.</p>

<p>Java/JVM is genuinely good, has seen massive improvements (<a href="https://openjdk.org/jeps/444">virtual threads</a>, <a href="https://openjdk.org/jeps/441">pattern matching</a>, <a href="https://openjdk.org/jeps/409">sealed classes</a>, <a href="https://openjdk.org/jeps/377">ZGC</a>), and will continue to improve with <a href="https://openjdk.org/jeps/401">value objects</a> (a preview of which landed in OpenJDK back in May!), the continuation of <a href="https://openjdk.org/projects/loom/">Project Loom</a>, and more.</p>

<p>Much like how a now "graybeard" language like Lisp brought us concepts that modern devs take for granted, the standout features of today's hot new languages are steadily being absorbed by the JVM. <a href="https://go.dev/tour/concurrency/1">Goroutines</a> and <a href="https://kotlinlang.org/docs/coroutines-overview.html">Kotlin Coroutines</a> inspiring <a href="https://openjdk.org/projects/loom/">Project Loom</a> are just one example. Paul Graham's <a href="https://www.paulgraham.com/icad.html">"Revenge of the Nerds"</a> has transmuted into the unstoppable momentum of the safe corporate giant.</p>

<figure>
  <img src="/assets/img/language-popularity-2025/lang_usage_breakdown.webp" alt="Programming-language usage breakdown">
  <figcaption>Source: <a href="https://blog.jetbrains.com/research/2026/08/programming-language-migration/">JetBrains Research, Programming Language Migration</a>.</figcaption>
</figure>

<p>– Due to the explosion of AI and the concept of "LLM-friendly languages", Python is indeed the primary choice for devs moving to a new main language. BUT its overall net growth in total dev share is quite modest (roughly +0.76% of all devs, or +4% self-relative), and it has large turnover (Python devs most often switch to Java and Go). This shows, in my opinion, that it acts more as an industry-wide transit hub rather than a one-stop shop replacing your typical backend stack. A significant portion of this "switch" is likely driven by the massive increase in high-level orchestration of ML code, which will remain written in good old C++.</p>

<p>– Surprisingly, JS devs remain loyal to pure JS despite the (partially) LLM-driven TypeScript boom 🤔. Is it an identity issue where "TS is just JS with types", so only newcomers label themselves "TypeScripters"?</p>

<p>– Perhaps not <em>as</em> surprising, Rust has incredible mindshare and loyalty but tiny market share, accounting for just 2.1% of global switchers. The data shows basically 0% of C devs and 1% of C++ devs moved to Rust. It has impressive YoY growth, but still operates on a very different scale where much of that growth is driven by newcomers rather than veteran systems engineers seeking an alternative.</p>

<p>Makes me wonder how much of all the heated discussions around Rust vs C++/EverythingElse is actually grounded in real experience and knowledge of both sides...</p>

<figure>
  <img src="/assets/img/language-popularity-2025/lang_net_growth_composition.webp" alt="Composition of net programming-language growth">
  <figcaption>Source: <a href="https://blog.jetbrains.com/research/2026/08/programming-language-migration/">JetBrains Research, Programming Language Migration</a>.</figcaption>
</figure>

<h2>The <em>new</em> "main languages" devs switch to</h2>

<p><strong>Weighted:</strong></p>

<ol>
  <li>Python — 20.9%</li>
  <li>Java — 16.1%</li>
  <li>TypeScript — 13.5%</li>
  <li>JavaScript — 10.5%</li>
  <li>Other — 7.3%</li>
  <li>Go — 7.0%</li>
  <li>C# — 5.7%</li>
  <li>C++ — 4.8%</li>
  <li>Kotlin — 4.1%</li>
  <li>C — 2.5%</li>
  <li>PHP — 2.3%</li>
  <li>Rust — 2.1%</li>
  <li>SQL — 2.0%</li>
  <li>HTML / CSS — 1.3%</li>
</ol>

<p><strong>Unweighted:</strong></p>

<ol>
  <li>Python — 72%</li>
  <li>Java — 60%</li>
  <li>TypeScript — 39%</li>
  <li>JavaScript — 34%</li>
  <li>Other — 33%</li>
  <li>Go — 22%</li>
  <li>C++ — 17%</li>
  <li>C# — 16%</li>
  <li>PHP — 10%</li>
  <li>Kotlin — 8%</li>
  <li>C — 5%</li>
  <li>HTML / CSS — 5%</li>
  <li>Rust — 5%</li>
  <li>SQL — 5%</li>
</ol>

<figure>
  <img src="/assets/img/language-popularity-2025/pl_dynamics_2017_2025.webp" alt="Programming-language usage dynamics from 2017 to 2025">
  <figcaption>Source: <a href="https://blog.jetbrains.com/research/2026/08/programming-language-migration/">JetBrains Research, Programming Language Migration</a>.</figcaption>
</figure>