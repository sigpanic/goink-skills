#!/usr/bin/env python3
"""Scan skills/*.md files and generate index.json manifest."""

import json
import os
import re
from datetime import datetime, timezone


SKILLS_DIR = "skills"
INDEX_FILE = "index.json"


def parse_frontmatter(path: str) -> dict[str, str]:
    with open(path, encoding="utf-8") as f:
        content = f.read()
    m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return {}
    result = {}
    for line in m.group(1).split("\n"):
        kv = re.match(r"^(\w+):\s*(.*)", line)
        if kv:
            result[kv.group(1)] = kv.group(2).strip()
    return result


def main():
    skills = []
    if not os.path.isdir(SKILLS_DIR):
        print(f"Skills directory '{SKILLS_DIR}' not found, writing empty index")
    else:
        for f in sorted(os.listdir(SKILLS_DIR)):
            if not f.endswith(".md"):
                continue
            path = os.path.join(SKILLS_DIR, f)
            fm = parse_frontmatter(path)
            skills.append({
                "name": os.path.splitext(f)[0],
                "description": fm.get("description", ""),
                "category": fm.get("category", ""),
                "mode": fm.get("mode", ""),
                "author": fm.get("author", ""),
                "file": f,
            })

    index = {
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "skills": skills,
    }

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"Wrote {INDEX_FILE} with {len(skills)} skills")


if __name__ == "__main__":
    main()
