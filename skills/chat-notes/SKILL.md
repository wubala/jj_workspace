---
name: chat-notes
description: 记录和珺珺聊天中的重点内容到本地 Markdown 文件。触发方式示例："把「xxx」内容给我记下，标题为「yyy」"。当未提供标题时，标题默认为当前时间字符串。
---

# Chat Notes Skill

当用户说类似：

- "把「今天和珺珺讨论 skill 的内容」内容给我记下，标题为「聊天 skill 设计」"

时，提取其中的「xxx」作为正文内容，「yyy」作为标题，执行 `scripts/append_note.py` 脚本，将内容以 Markdown 形式追加写入本地 `notes/chat-notes.md` 文件。
