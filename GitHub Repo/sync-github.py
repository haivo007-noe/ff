#!/usr/bin/env python3
"""Sync the GitHub Repo folder from the live vault files.

Run from anywhere:  python3 "GitHub Repo/sync-github.py"
Copies the 6 published files from their vault locations into this folder,
ready to drag onto github.com (Add file -> Upload files -> drag Board + Data).
"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent          # .../Fantasy Football/GitHub Repo
VAULT = HERE.parent                              # .../Fantasy Football
SRC = VAULT / "Fantasy Draft 2026"

FILES = {
    SRC / "Board" / "draft-board.html":      HERE / "Board" / "draft-board.html",
    SRC / "Board" / "research-digest.html":  HERE / "Board" / "research-digest.html",
    SRC / "Board" / "in-season-hub.html":    HERE / "Board" / "in-season-hub.html",
    SRC / "Data" / "players.csv":            HERE / "Data" / "players.csv",
    SRC / "Data" / "research-sidecar.json":  HERE / "Data" / "research-sidecar.json",
    SRC / "Data" / "weekly-sidecar.json":    HERE / "Data" / "weekly-sidecar.json",
    SRC / "Data" / "usage-trends.json":      HERE / "Data" / "usage-trends.json",
    SRC / "Data" / "league-sidecar.json":    HERE / "Data" / "league-sidecar.json",
}

for src, dst in FILES.items():
    if not src.exists():
        print(f"  MISSING source: {src}")
        continue
    dst.parent.mkdir(parents=True, exist_ok=True)
    changed = (not dst.exists()) or src.stat().st_mtime > dst.stat().st_mtime
    shutil.copy2(src, dst)
    print(f"  {'updated' if changed else 'unchanged'}: {dst.relative_to(HERE)}")

print("\nDone. Drag the Board and Data folders onto your GitHub repo's upload page.")
