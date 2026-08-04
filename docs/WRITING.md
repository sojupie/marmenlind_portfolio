# Publishing with Hugo

This is the private authoring reference for adding portfolio articles. The repository `README.md` remains the public GitHub landing page.

## Create a post

Install Hugo once (`winget install Hugo.Hugo` on Windows), restart the terminal so `hugo` is on `PATH`, then install the CSS dependencies:

```powershell
pnpm install
```

Start the site with:

```powershell
pnpm dev
```

Create a post with `hugo new content content/writing/my-post-title.md`.

Open `http://localhost:1313`, edit the generated Markdown file, and set `draft: false` when it is ready to publish.

```yaml
---
title: "A clear, specific title"
date: 2026-08-03
description: "One sentence used in metadata and at the top of the article."
summary: "A shorter sentence used in article lists."
tags: ["Systems", "Product"]
draft: false
---
```

Everything after the front matter is ordinary Markdown:

```markdown
Opening paragraph.

## Section heading

Body copy with [a link](https://example.com) and an image:

![Useful alternative text](/assets/img/writing/my-post/image.jpg)
```

Put article images in `static/assets/img/writing/my-post/`. They are published at `/assets/img/writing/my-post/`. No template or HTML changes are needed.

## Build

```powershell
pnpm build
```

GitHub Actions builds and deploys the generated `public/` directory after a push.

## Styling

Tailwind CSS v4 is compiled by pnpm. `pnpm dev` runs the Tailwind watcher and Hugo server together. Use utility classes directly in files under `layouts/`. The entry stylesheet is `assets/css/main.css`; keep design tokens, base rules, and any unavoidable shared CSS there. Files under `static/` are copied without processing.
