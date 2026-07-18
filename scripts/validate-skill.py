#!/usr/bin/env python3
"""Validate a Goink skill markdown file.

Usage: validate-skill.py <file_path> <expected_name>

Reads markdown content from stdin. Exits 0 on success, 1 with error lines on failure.
No external dependencies — uses stdlib only.
"""

import re
import sys


VALID_MODES = {"auto", "manual", "always"}
REQUIRED_FIELDS = ["name", "description", "category", "mode"]


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Split YAML frontmatter from body. Returns (fields_dict, body)."""
    if not content.startswith("---"):
        return {}, content
    rest = content[3:]
    idx = rest.find("\n---")
    if idx == -1:
        return {}, content
    fm = rest[:idx]
    body = rest[idx + 4:]
    fields = {}
    for line in fm.strip().split("\n"):
        m = re.match(r"^(\w[\w-]*)\s*:\s*(.*)", line)
        if m:
            fields[m.group(1)] = m.group(2).strip()
    return fields, body


def validate(file_path: str, expected_name: str, content: str) -> list[str]:
    errors = []

    if not content.strip():
        errors.append(f"- `{file_path}`：文件内容为空")
        return errors

    fields, _ = parse_frontmatter(content)

    for f in REQUIRED_FIELDS:
        if not fields.get(f):
            errors.append(f"- `{file_path}`：缺少必填字段 `{f}`")

    mode = fields.get("mode", "")
    if mode and mode not in VALID_MODES:
        errors.append(
            f"- `{file_path}`：`mode` 值 `{mode}` 不合法，应为 auto / manual / always"
        )

    name = fields.get("name", "")
    if name and name != expected_name:
        errors.append(
            f"- `{file_path}`：文件名与 frontmatter `name` 不一致"
            f"（文件名 {expected_name}，name {name}）"
        )

    return errors


def main():
    if len(sys.argv) != 3:
        print("Usage: validate-skill.py <file_path> <expected_name>", file=sys.stderr)
        sys.exit(2)

    file_path = sys.argv[1]
    expected_name = sys.argv[2]
    content = sys.stdin.read()

    errors = validate(file_path, expected_name, content)
    if errors:
        for e in errors:
            print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
