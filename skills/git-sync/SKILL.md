---
name: git-sync
description: 快速将本地代码同步到 GitHub 远程仓库。触发条件：用户说"同步git"、"git同步"、"提交代码"、"push代码"等。在指定目录执行 git add .、git commit（使用当前日期作为提交信息）、git push 三步操作。
---

# Git Sync

快速将 workspace 目录的改动同步到 GitHub。

## 默认配置

- **工作目录**: `/Users/wulei/.openclaw/workspace`
- **提交信息格式**: 当前日期（如 `2026-03-31`）

## 执行步骤

1. 切换到工作目录
2. 执行 `git add .` 暂存所有改动
3. 执行 `git commit -m "当前日期"` 提交（日期格式：YYYY-MM-DD）
4. 执行 `git push` 推送到远程仓库

## 示例

用户说：
- "同步git"
- "提交代码"
- "push 一下"

执行：
```bash
cd /Users/wulei/.openclaw/workspace
git add .
git commit -m "2026-03-31"
git push
```

## 注意事项

- 如果有冲突需要先解决，skill 会提示用户
- 如果没有改动，git 会提示 "nothing to commit"
- 确保 workspace 目录已经初始化了 git 仓库并配置了远程地址
