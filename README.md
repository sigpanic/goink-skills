<p align="center">
  <img src="https://raw.githubusercontent.com/sigpanic/goink/master/assets/logo-dark.svg#gh-dark-mode-only" alt="Goink Skills" />
  <img src="https://raw.githubusercontent.com/sigpanic/goink/master/assets/logo-light.svg#gh-light-mode-only" alt="Goink Skills" />
</p>

<h1 align="center">Goink 社区技能<br><sub>创作方法论 × 社区贡献 × App 内一键安装</sub></h1>

<p align="center">
  <img src="https://img.shields.io/badge/license-CC_BY--SA_4.0-green?style=for-the-badge" alt="CC BY-SA 4.0" />
  <img src="https://github.com/sigpanic/goink-skills/actions/workflows/update-index.yml/badge.svg" alt="PR Check" />
</p>

<p align="center"><strong><a href="README_EN.md">English Version</a> | 本文档为中文版</strong></p>

<p align="center">
  <strong>这里是 <a href="https://github.com/sigpanic/goink">Goink</a> 桌面 AI 写作系统的社区技能仓库。</strong><br>
  Skills 是 AI 写作助手的"专业知识卡片"，每条 skill 教 AI 一种特定的写作方法论或工作流。
</p>

## 提交你的 Skill

1. **Fork** 本仓库
2. 在 `skills/` 目录下新建一个 `.md` 文件（参考 [.template/skill.md](.template/skill.md)）
3. 填写 YAML frontmatter 和正文内容
4. 提交 Pull Request

PR 合并后，系统会自动更新索引，所有 Goink 用户即可在 App 内浏览和安装你的 Skill。

## Skill 格式

每个 skill 是一个 Markdown 文件，文件头包含 YAML frontmatter：

| 字段 | 必填 | 说明 |
|------|------|------|
| `name` | 是 | kebab-case 唯一标识，如 `dialogue-subtext`。**文件名必须与 `name` 一致**（即 `dialogue-subtext.md`） |
| `description` | 是 | 一句话描述技能 + AI 何时应自动调用它 |
| `category` | 是 | 中文分类，如 角色、情节、文笔、结构 等 |
| `mode` | 是 | `auto`（AI 可自主调用）/ `manual`（仅用户 / 触发）/ `always`（常驻生效） |
| `author` | 是 | 你的名字 |
| `version` | 是 | 整数版本号，从 1 开始 |

正文可以使用完整的 Markdown 语法：标题、列表、表格、代码块等。AI 会将正文作为系统提示注入到会话中。

## 分类参考

| 分类 | 适用范围 |
|------|----------|
| 角色 | 角色设计、性格塑造、人物关系 |
| 情节 | 情节编排、冲突设计、悬念营造 |
| 对白 | 对话写作、潜台词、语气把控 |
| 文笔 | 描写技巧、文风打磨、修辞手法 |
| 结构 | 篇章架构、节奏控制、章节规划 |
| 工具 | 写作辅助工具、流程优化方法 |

## 注意事项

- `name` 不要与已有的 skill 重复（目前内置 skill 使用 `builtin` 作为 author）
- 正文尽量具体、可操作，AI 会严格按正文内容执行
- 保持一条 skill 聚焦一个主题，不要塞入多个不相关的方法论
- 提交后维护者会 review，通过后合并到主仓库

## 许可

提交到本仓库的 skill 采用 [CC BY-SA 4.0](LICENSE) 许可——署名 + 相同方式共享。
