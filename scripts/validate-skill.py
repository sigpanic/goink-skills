#!/usr/bin/env python3
"""Validate a Goink skill markdown file.

Usage: validate-skill.py <file_path> <expected_name>

Reads markdown content from stdin. Exits 0 on success, 1 with error lines on failure.
No external dependencies — uses stdlib only.
"""

import os
import re
import sys


VALID_MODES = {"auto"}  # 贡献层只允许 auto，manual/always 由用户下载后在 App 内自行设置
REQUIRED_FIELDS = ["name", "description", "category", "mode"]
MAX_SIZE = 40 * 1024  # 40KB，防止单个 skill 过大爆 LLM token


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


def validate(file_path: str, expected_name: str, content: str, existing_names: set = None) -> list[str]:
    errors = []

    if not content.strip():
        errors.append(f"- `{file_path}`：文件内容为空")
        return errors

    content_bytes = content.encode("utf-8")
    if len(content_bytes) > MAX_SIZE:
        errors.append(
            f"- `{file_path}`：文件超过 40KB 限制"
            f"（当前 {len(content_bytes) // 1024}KB）"
        )
        return errors

    fields, _ = parse_frontmatter(content)

    for f in REQUIRED_FIELDS:
        if not fields.get(f):
            errors.append(f"- `{file_path}`：缺少必填字段 `{f}`")

    mode = fields.get("mode", "")
    if mode and mode not in VALID_MODES:
        errors.append(
            f"- `{file_path}`：贡献 skill 的 `mode` 必须为 `auto`，"
            f"下载后可在 App 内改为 manual/always（你填了 `{mode}`）"
        )

    name = fields.get("name", "")
    if name and name != expected_name:
        errors.append(
            f"- `{file_path}`：文件名与 frontmatter `name` 不一致"
            f"（文件名 {expected_name}，name {name}）"
        )

    # 重复 name 检查：只对新文件（expected_name 不在已有列表里）
    if existing_names and expected_name not in existing_names:
        if name and name in existing_names:
            errors.append(
                f"- `{file_path}`：skill name `{name}` 与已有 skill 冲突"
            )

    return errors


def main():
    if len(sys.argv) != 3:
        print("Usage: validate-skill.py <file_path> <expected_name>", file=sys.stderr)
        sys.exit(2)

    file_path = sys.argv[1]
    expected_name = sys.argv[2]
    content = sys.stdin.read()

    # 从环境变量读已有 skill name 列表（逗号分隔），用于重复 name 检查
    existing_names_str = os.environ.get("EXISTING_NAMES", "")
    existing_names = set(existing_names_str.split(",")) if existing_names_str else None

    errors = validate(file_path, expected_name, content, existing_names)
    if errors:
        for e in errors:
            print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
