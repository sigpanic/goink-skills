<p align="center">
  <img src="https://raw.githubusercontent.com/sigpanic/goink/master/assets/logo-dark.svg#gh-dark-mode-only" alt="Goink Skills" />
  <img src="https://raw.githubusercontent.com/sigpanic/goink/master/assets/logo-light.svg#gh-light-mode-only" alt="Goink Skills" />
</p>

<h1 align="center">Goink Community Skills<br><sub>Writing Methodologies × Community Contributions × One-Click Install</sub></h1>

<p align="center">
  <img src="https://img.shields.io/badge/license-CC_BY--SA_4.0-green?style=for-the-badge" alt="CC BY-SA 4.0" />
  <img src="https://github.com/sigpanic/goink-skills/actions/workflows/update-index.yml/badge.svg" alt="PR Check" />
</p>

<p align="center"><strong><a href="README.md">中文版</a> | English Version</strong></p>

<p align="center">
  <strong>Community skills repository for <a href="https://github.com/sigpanic/goink">Goink</a>, the desktop AI novel-writing assistant.</strong><br>
  Each skill is a "knowledge card" that teaches the AI a specific writing methodology or workflow.
</p>

## Submitting a Skill

> Please read [CONTRIBUTING.md](CONTRIBUTING.md) first for contribution terms, content policy, and infringement reporting.

1. **Fork** this repository
2. Create a `.md` file under `skills/` (see [.template/skill.md](.template/skill.md))
3. Fill in the YAML frontmatter and body content
4. Submit a Pull Request

Once merged, the index is automatically updated and your skill becomes visible to all Goink users in the app.

## Skill Format

Each skill is a Markdown file with YAML frontmatter:

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | kebab-case identifier, e.g. `dialogue-subtext`. **Filename must match `name`** (e.g. `dialogue-subtext.md`) |
| `description` | Yes | What the skill does and when the AI should invoke it |
| `category` | Yes | Category, e.g. character, plot, dialogue, prose, structure |
| `mode` | Yes | Fixed to `auto`. Can be changed to `manual` (user trigger only) or `always` (always active) in the App after download |
| `author` | No | Your name, can be empty |
| `version` | No | Integer, starting from 1 (defaults to 1) |

The body can use any Markdown: headings, lists, tables, code blocks. The AI receives the body as a system prompt during the conversation.

## Categories

| Category | Scope |
|----------|-------|
| character | Character design, personality, relationships |
| plot | Plot structure, conflict, suspense |
| dialogue | Dialogue, subtext, voice |
| prose | Prose style, description, rhetoric |
| structure | Chapter architecture, pacing |
| tool | Writing tools, workflow methods |

## Notes

- `name` must not conflict with built-in skills (check existing ones with `author: builtin`)
- Keep one skill focused on one topic
- Be specific and actionable — the AI follows the content closely
- Submitted skills will be reviewed by maintainers before merging

## License

Skills submitted to this repository are licensed under [CC BY-SA 4.0](LICENSE) — Attribution + ShareAlike.
