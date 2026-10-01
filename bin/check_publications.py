#!/usr/bin/env python3
"""Check whether the site's publication lists match the papers folder.

Source of truth: PhD\\papers\\{accepted,under_review}. Each PDF there must map
to a bib entry via _data/papers_manifest.yml, and every bib entry must be
backed by a manifest row. Prints a drift report; exit 0 = in sync, 1 = drift.

Run from anywhere:  python portfolio/bin/check_publications.py
"""

import re
import sys
from pathlib import Path

PORTFOLIO = Path(__file__).resolve().parent.parent
PAPERS = PORTFOLIO.parent / "papers"
MANIFEST = PORTFOLIO / "_data" / "papers_manifest.yml"
BIB = {
    "accepted": PORTFOLIO / "_bibliography" / "papers.bib",
    "under_review": PORTFOLIO / "_bibliography" / "under_review.bib",
}


def load_manifest():
    """Parse the simple two-level manifest without needing PyYAML."""
    mapping = {}  # (status, filename) -> bib key
    status = None
    for raw in MANIFEST.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if not line.startswith(" ") and line.endswith(":"):
            status = line[:-1].strip()
        elif status and ":" in line:
            fname, key = line.split(":", 1)
            mapping[(status, fname.strip().strip('"'))] = key.strip().strip('"')
    return mapping


def bib_keys(path):
    text = path.read_text(encoding="utf-8")
    if "%" in re.sub(r"\{[^{}]*\}", "", text):
        print(f"WARNING: '%' found in {path.name} outside braces — "
              "the Ruby BibTeX parser does not support % comments and the "
              "site build WILL fail. Remove it.")
    return set(re.findall(r"@\w+\{\s*([^,\s]+)\s*,", text))


def main():
    problems = []
    manifest = load_manifest()

    for status in ("accepted", "under_review"):
        folder = PAPERS / status
        pdfs = {p.name for p in folder.glob("*.pdf")}
        manifest_files = {f for (s, f) in manifest if s == status}
        keys_in_bib = bib_keys(BIB[status])
        manifest_keys = {manifest[(status, f)] for f in manifest_files}

        for f in sorted(pdfs - manifest_files):
            problems.append(f"NEW PDF not on site: papers\\{status}\\{f}")
        for f in sorted(manifest_files - pdfs):
            where = [s for (s, f2) in manifest if f2 == f and s != status]
            hint = f" (manifest also lists it under {where[0]})" if where else ""
            # Say where it went, if anywhere obvious
            for other in ("accepted", "under_review", "extra"):
                if other != status and (PAPERS / other / f).exists():
                    hint = f" -> file is now in papers\\{other}"
                    break
            problems.append(f"GONE from papers\\{status}: {f}{hint}")
        for k in sorted(manifest_keys - keys_in_bib):
            problems.append(f"Manifest key '{k}' missing from {BIB[status].name}")
        for k in sorted(keys_in_bib - manifest_keys):
            if k == "aps":  # @string leftovers
                continue
            problems.append(
                f"Bib entry '{k}' in {BIB[status].name} has no manifest row "
                "(no backing PDF?)")

    if problems:
        print("PUBLICATIONS OUT OF SYNC:")
        for p in problems:
            print("  -", p)
        print("\nRun the update-publications skill in Claude Code to fix "
              "(or edit _bibliography/*.bib and _data/papers_manifest.yml by hand).")
        return 1
    print("Publications in sync: site matches the papers folder.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
