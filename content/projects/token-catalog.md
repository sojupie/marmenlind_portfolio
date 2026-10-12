---
title: 'Token Catalog'
slug: 'token-catalog'
date: 2026-10-11
description: 'Versioned Material Design token data for custom components and agent-assisted development.'
summary: 'A Go pipeline and live web service that captures dynamically loaded Material Design tokens, verifies coverage, detects semantic changes, and publishes data for developers and coding agents.'
year: '2026'
discipline: 'Go / Chromium / SQLite / templ / HTMX'
external_url: 'https://tokencatalog.dev'
external_label: 'Visit Token Catalog'
external_icon: 'open_in_new'
github_url: 'https://github.com/sojupie/tokens'
featured: true
---

<a class="inline-flex items-center gap-1" href="https://tokencatalog.dev" target="_blank" rel="noopener noreferrer"><span class="underline decoration-1 underline-offset-3">Visit Token Catalog</span><span class="material-symbols-outlined text-base! leading-none" aria-hidden="true">open_in_new</span><span class="sr-only"> (opens in new tab)</span></a>

Token Catalog collects design tokens and makes them easier to browse, compare
and download. [Material Design 3](https://tokencatalog.dev/md3/) is the first
supported collection.

The goal is fast, direct access to design data for developers and agents. Tokens,
references and settings are available in readable pages and structured responses
that can be inspected, crawled and fetched with ordinary HTTP clients. Source
links connect the data to the original design guidance.

![Token Catalog showing the Material Design 3 component catalog](/assets/img/token-catalog/catalog.png)

## Browse and download

Find tokens by component or style, inspect their references, and filter values
by platform, theme and other settings. Downloads can include the filtered table,
all values in a table, a whole component, or the collection.

For example, select a Buttons table, choose a platform and theme, then download
“This table, with your filters” to export that selection. Broader download
options include values outside the selected table and filters.

The change log compares retained captures. It shows added, removed and changed
values, including changes to individual settings. Dates record when a change
was observed. Incomplete captures remain marked as partial.

The same data is available through a public JSON API, Markdown responses and
read-only MCP tools. See [usage](https://github.com/sojupie/tokens/blob/main/docs/usage.md) and
[API and agent access](https://github.com/sojupie/tokens/blob/main/docs/reference/agents.md).

## Performance and access

Pages render on the server with the token data already present in the HTML.
Reading pages and fetching JSON do not require JavaScript or an account.
Markdown responses, OpenAPI, discovery files and MCP tools make the same data
available to different clients. Small assets and deferred scripts keep the
browser's initial work limited.

The October 11, 2026 [mobile PageSpeed Insights report](https://pagespeed.web.dev/analysis/https-tokencatalog-dev/91lzhrkat6?hl=en&form_factor=mobile)
scores 100 for performance, accessibility, best practices and SEO, with 4/4
agentic browsing checks passed. The measured largest contentful paint is 1.2 s,
with 0 ms total blocking time and no layout shift.

The captured [Is It Agent Ready?](https://isitagentready.com/) check scores 80/100,
including 100 for discoverability, content and bot access control.
The remaining three checks concern OAuth/OIDC discovery, protected-resource
metadata and agent registration. Token Catalog provides public, read-only access
without accounts or protected APIs, so those authentication features are
deliberately omitted. The lower score reflects those checks being counted as
missing even though the discovery and access checks for the public service pass.

<a href="https://pagespeed.web.dev/analysis/https-tokencatalog-dev/91lzhrkat6?hl=en&amp;form_factor=mobile"><img src="/assets/img/token-catalog/PageSpeedInsights.png" alt="October 11, 2026 mobile PageSpeed Insights report showing four scores of 100 and 4/4 agentic browsing checks" width="420" /></a>
<img src="/assets/img/token-catalog/isitagentready.png" alt="Is It Agent Ready report for Token Catalog showing 80/100 overall and 100 for discoverability, content and bot access control" width="420" />

## How it works

A Go pipeline opens source pages with Chromium, captures their token payloads,
and saves the source URLs, coverage results and SHA-256 hashes. Each snapshot
contains the captured data and the files needed to verify it later.

Publication runs offline. It compares snapshots and builds a SQLite read index
and JSON downloads. The Go server renders pages with templ and HTMX, serving
saved data independently of the crawler and upstream website.

The project grew out of using Material Design in a web application and needing
its token values in a form that could be inspected and consumed directly.
[Architecture](https://github.com/sojupie/tokens/blob/main/docs/architecture.md) explains the pipeline and its boundaries.

## Run locally

Install Go 1.26 or newer and Chrome or Chromium, then run:

```sh
go build -o ./bin/tokens ./cmd/tokens
./bin/tokens crawl
./bin/tokens snapshot create
./bin/tokens publish
./bin/tokens serve --published published --listen 127.0.0.1:8081
```

Open [localhost:8081](http://127.0.0.1:8081). The initial crawl needs network
access. Later starts only need the serve command. On Windows, build
`bin/tokens.exe` and use that executable for the same commands.

See [development](https://github.com/sojupie/tokens/blob/main/docs/development.md) for tests and template changes, or
[deployment](https://github.com/sojupie/tokens/blob/main/docs/operations/deployment.md) for Docker and scheduled updates.

## Scope

The current crawler, extractor and publication format are specific to Material
Design 3. Other design systems would need source adapters, extraction rules and
their own attribution. The catalog can grow to include further collections;
only Material Design 3 is implemented today.

Captures cover the reviewed source-page catalog. Upstream failures and missing
payloads affect coverage. A token's appearance or disappearance in a partial
capture does not establish that its source added or removed it.

## Documentation

- [Using the catalog](https://github.com/sojupie/tokens/blob/main/docs/usage.md)
- [Developing and contributing](https://github.com/sojupie/tokens/blob/main/CONTRIBUTING.md)
- [Architecture](https://github.com/sojupie/tokens/blob/main/docs/architecture.md)
- [CLI, snapshots and publication](https://github.com/sojupie/tokens/blob/main/docs/README.md#reference)
- [Deployment and recovery](https://github.com/sojupie/tokens/blob/main/docs/README.md#operations)
- [Project history](https://github.com/sojupie/tokens/blob/main/docs/history/README.md)

## License and attribution

Project code and original documentation are licensed under [MIT](https://github.com/sojupie/tokens/blob/main/LICENSE).
Material Design 3 data comes from Google and retains its upstream terms.
Bundled fonts, icons and dependencies retain their own licenses.

Token Catalog is an independent project. See [third-party notices](https://github.com/sojupie/tokens/blob/main/THIRD_PARTY_NOTICES.md)
and [licensing and source attribution](https://github.com/sojupie/tokens/blob/main/docs/licensing.md) for the distinction
between the software and the data it publishes.
