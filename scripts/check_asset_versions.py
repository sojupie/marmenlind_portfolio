"""Build isolated copies and verify asset URLs, old links, and content changes."""
import hashlib
from html.parser import HTMLParser
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
VERSION = re.compile(r"\.([0-9a-f]{64})(?=\.[^.]+$)")
PREFIX = "/assets/versioned/"


class AssetLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = set()

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "link" and attributes.get("rel") == "stylesheet":
            assert attributes.get("media") != "print" and "onload" not in attributes, attributes
        self.urls.update(value for key, value in attrs if key in ("src", "href") and value)
        for key, value in attrs:
            if key == "srcset" and value:
                self.urls.update(item.strip().split()[0] for item in value.split(","))


def verify(output):
    versions = {}
    for page in output.rglob("*.html"):
        html = page.read_text()
        assert "fonts.googleapis.com" not in html and "fonts.gstatic.com" not in html, page
        assert "font-display:swap" not in html, page
        links = AssetLinks()
        links.feed(html)
        links.urls.update(re.findall(r'url\(["\']?(/assets/[^)"\']+)', html))
        for url in links.urls:
            path = unquote(urlsplit(url).path)
            if not path.startswith("/assets/"):
                continue
            assert path.startswith(PREFIX), (page, "Unversioned asset", path)
            file = output / path.lstrip("/")
            match = VERSION.search(file.name)
            assert match and file.is_file(), (page, "Missing hashed asset", path)
            assert hashlib.sha256(file.read_bytes()).hexdigest() == match[1], path
            original = "/assets/" + VERSION.sub("", path.removeprefix(PREFIX))
            assert (output / original.lstrip("/")).read_bytes() == file.read_bytes(), original
            versions[original] = path
    assert any(path.endswith(".pdf") for path in versions)
    assert any(path.endswith(".woff2") for path in versions)
    return versions


def main():
    with tempfile.TemporaryDirectory(prefix="portfolio-assets-") as temporary:
        source = Path(temporary) / "site"
        source.mkdir()
        for name in ["assets", "content", "data", "layouts", "static"]:
            shutil.copytree(ROOT / name, source / name)
        shutil.copy2(ROOT / "hugo.toml", source / "hugo.toml")
        output = Path(temporary) / "public"

        def build():
            subprocess.run(["hugo", "--source", str(source), "--destination", str(output),
                            "--cleanDestinationDir", "--quiet"], check=True)
            return verify(output)

        before = build()
        assert build() == before, "Unchanged assets must retain their URLs"
        changed = ["/assets/docs/CV_OLLE_MARMENLIND_RESUME.pdf", "/assets/img/marmeno-logo.png",
                   "/assets/fonts/noto-sans-subset/NotoSans-Regular.woff2"]
        for path in changed:
            file = source / "static" / path.lstrip("/")
            file.write_bytes(file.read_bytes() + b"\n")
        after = build()
        for path in before:
            assert (before[path] != after[path]) == (path in changed), path
        print(f"Verified {len(before)} assets: stable originals, valid hashes, repeatable builds, "
              "and new URLs after PDF, image, and font changes.")


if __name__ == "__main__":
    main()
