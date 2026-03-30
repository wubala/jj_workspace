# Chat Notes

---

## skill&workspace
**时间：2026-03-26 10:08**

# Skill & Workspace 知识点整理

## 一、Workspace（工作区）

### 1. 什么是 Workspace？
- **Workspace 是 agent 的家**，是唯一的工作目录，用于文件操作和上下文加载
- 与 `~/.openclaw/` 分离，后者存储配置、凭证和会话
- **默认路径**：`~/.openclaw/workspace`（可通过配置修改）

### 2. Workspace 文件结构

| 文件名 | 用途 |
|--------|------|
| `AGENTS.md` | Agent 的操作指令，每个会话开始时加载 |
| `SOUL.md` | 人格、语气和边界定义 |
| `USER.md` | 用户信息，如何称呼等 |
| `IDENTITY.md` | Agent 的名字、风格、emoji |
| `TOOLS.md` | 本地工具和约定的笔记（不影响工具可用性） |
| `HEARTBEAT.md` | 心跳检查的可选小清单 |
| `BOOTSTRAP.md` | 首次运行的初始化仪式（完成后删除） |
| `memory/YYYY-MM-DD.md` | 每日记忆日志 |
| `MEMORY.md` | 精选的长期记忆（仅在主会话加载） |
| `skills/` | 工作区专属技能（优先级最高） |

### 3. Workspace 备份建议
- **使用 Git 私有仓库**备份 workspace
- 不要提交 `~/.openclaw/` 下的内容（配置、凭证等）
- 避免存储 API keys、密码等敏感信息

---

## 二、Skills（技能）

### 1. 什么是 Skill？
- **Skill 是教 agent 如何使用工具的方式**
- 遵循 [AgentSkills](https://agentskills.io) 规范
- 每个 skill 是一个包含 `SKILL.md` 的目录

### 2. Skills 加载位置与优先级

**优先级（从高到低）：**
1. `<workspace>/skills` — 工作区技能（最高优先级）
2. `~/.openclaw/skills` — 本地/管理技能
3. Bundled skills — 内置技能（最低优先级）

### 3. SKILL.md 基本格式

```markdown
---
name: my-skill
description: 技能描述
---

# My Skill

这里写指令，告诉 agent 怎么使用这个技能...
```

### 4. Skills 配置与门控（Gating）

**通过 `metadata.openclaw` 控制加载条件：**
- `requires.bins` — 需要的命令行工具
- `requires.env` — 需要的环境变量
- `requires.config` — 需要的配置项
- `os` — 支持的操作系统
- `always: true` — 始终加载（跳过其他门控）

**在 `~/.openclaw/openclaw.json` 中覆盖配置：**
```json5
{
  skills: {
    entries: {
      "my-skill": {
        enabled: true,
        apiKey: "YOUR_API_KEY",
        env: { MY_VAR: "value" }
      }
    }
  }
}
```

### 5. 创建自定义 Skill

1. 创建目录：`mkdir -p ~/.openclaw/workspace/skills/my-skill`
2. 编写 `SKILL.md`（YAML frontmatter + Markdown 指令）
3. 刷新 OpenClaw 或重启 gateway

### 6. ClawHub（技能市场）
- 网址：https://clawhub.com
- 用于发现、安装、更新技能
- `clawhub install <skill-slug>` — 安装技能
- `clawhub update --all` — 更新所有技能

---

## 三、关键要点

1. **Workspace 是私有的**，应该用 Git 私有仓库备份
2. **Skills 有三级优先级**：workspace > managed > bundled
3. **Skills 可通过 metadata 控制加载条件**，避免不兼容环境
4. **敏感信息**应放在 `~/.openclaw/` 而非 workspace
5. **Memory 系统**：每日日志 + 长期记忆（MEMORY.md）

---

整理时间：2026-03-26
来源：OpenClaw 官方文档

---

## 如何查看隐藏文件
**时间：2026-03-26 10:33**

# Mac 查看隐藏文件夹的方法

## 1. 快捷键（最常用）
在 Finder 中按：
```
⌘ Command + Shift + .
```
再按一次就会重新隐藏。

## 2. 终端命令
```bash
# 显示隐藏文件
defaults write com.apple.finder AppleShowAllFiles -bool true
killall Finder

# 隐藏隐藏文件
defaults write com.apple.finder AppleShowAllFiles -bool false
killall Finder
```

## 3. 直接在终端查看
```bash
ls -la                    # 显示当前目录所有文件（包括隐藏）
ls -la ~/.openclaw/       # 显示指定目录
open ~/.openclaw/         # 在 Finder 中打开隐藏目录
```

## 4. Finder 菜单方式
Finder → 前往 → 前往文件夹（或按 `⌘ Command + Shift + G`）→ 输入路径

**小提示**：隐藏文件/文件夹通常以 `.` 开头，比如 `~/.openclaw/`、`~/.git/` 等

---
