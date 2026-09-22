"""Tell IndexNow search engines (Bing, Yandex, Seznam, Naver...) about new or changed pages.

Run after the site is live on GitHub Pages:
    python src/indexnow.py                 # submit every URL in sitemap.xml
    python src/indexnow.py slug-a slug-b   # submit only these pages (e.g. 401k-calculator)
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(__file__))
from content import SITE  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main(slugs):
    base, key = SITE["base_url"], SITE["indexnow_key"]
    if slugs:
        urls = [f"{base}/" if s in ("", "/") else f"{base}/{s.strip('/')}/" for s in slugs]
    else:
        with open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8") as f:
            urls = re.findall(r"<loc>([^<]+)</loc>", f.read())
    body = json.dumps({"host": SITE["domain"], "key": key, "keyLocation": f"{base}/{key}.txt", "urlList": urls}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(f"IndexNow: HTTP {r.status} for {len(urls)} URLs")
    except urllib.error.HTTPError as e:
        print(f"IndexNow: HTTP {e.code} {e.reason}: {e.read().decode(errors='replace')[:300]}")
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
