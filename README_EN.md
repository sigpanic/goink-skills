# Goink Community Skills

Community-contributed skills for the Goink AI novel-writing assistant. Each skill is a "knowledge card" that teaches the AI a specific writing methodology or workflow.

## Submitting a Skill

1. **Fork** this repository
2. Create a `.md` file under `skills/` (see [.template/skill.md](.template/skill.md))
3. Fill in the YAML frontmatter and body content
4. Submit a Pull Request

## Skill Format

Each skill is a Markdown file with YAML frontmatter:

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | kebab-case identifier, e.g. `dialogue-subtext`. **Filename must match `name`** (e.g. `dialogue-subtext.md`) |
| `description` | Yes | What the skill does and when the AI should invoke it |
| `category` | Yes | Category in Chinese, e.g. 角色, 情节, 文笔, 结构 |
| `mode` | Yes | `auto` (AI can invoke), `manual` (user `/` trigger only), `always` (always active) |
| `author` | Yes | Your name |
| `version` | Yes | Integer, starting from 1 |

The body can use any Markdown: headings, lists, tables, code blocks. The AI receives the body as a system prompt during the conversation.

## Categories

| Category | Scope |
|----------|-------|
| 角色 | Character design, personality, relationships |
| 情节 | Plot structure, conflict, suspense |
| 对白 | Dialogue, subtext, voice |
| 文笔 | Prose style, description,修辞 |
| 结构 | Chapter architecture, pacing |
| 工具 | Writing tools, workflow methods |

## Notes

- `name` must not conflict with built-in skills (check existing ones with `author: builtin`)
- Keep one skill focused on one topic
- Be specific and actionable — the AI follows the content closely
- Submitted skills will be reviewed by maintainers before merging

## License

Skills submitted to this repository are licensed under [CC BY-SA 4.0](LICENSE) — Attribution + ShareAlike.
