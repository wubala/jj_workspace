#!/usr/bin/env python3
"""把一句话里的「内容」和「标题」解析出来，写入 Markdown 笔记文件"""

import os
import re
import sys
from datetime import datetime


def parse_command(text: str):
    """从指令中解析出 content 和 title

    预期形态：
    把「xxx」内容给我记下，标题为「yyy」
    也尽量兼容：把「xxx」内容给我记下（没有标题）
    """
    text = text.strip()

    # 先找标题：标题为「yyy」
    title = None
    m_title = re.search(r"标题为[「\"'](.+?)[」\"']", text)
    if m_title:
        title = m_title.group(1).strip()

    # 找内容：「xxx」内容给我记下
    m_content = re.search(r"[把将]?[「\"'](.+?)[」\"']内容给我记下", text)
    content = None
    if m_content:
        content = m_content.group(1).strip()

    # 兜底：如果按上面没解析出来，可以尝试简单规则
    if content is None:
        # 去掉开头的“把”“将”之类，再找“内容给我记下”
        tmp = re.sub(r"^[把将]", "", text)
        parts = tmp.split("内容给我记下", 1)
        if len(parts) == 2:
            content = parts[0].strip(" ：:，,。.")

    # 标题缺失则用当前时间
    if not title:
        title = datetime.now().strftime("%Y-%m-%d %H:%M")

    return content, title


def append_markdown_note(content: str, title: str):
    """以 Markdown 形式追加写入 notes/chat-notes.md"""
    skill_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    notes_dir = os.path.join(skill_dir, "notes")
    os.makedirs(notes_dir, exist_ok=True)

    notes_file = os.path.join(notes_dir, "chat-notes.md")

    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    md = []
    md.append(f"## {title}\n\n")
    md.append(f"> 创建时间：{ts}\n\n")
    md.append(f"{content}\n\n")
    md.append("---\n\n")

    with open(notes_file, "a", encoding="utf-8") as f:
        f.writelines(md)

    print(f"已记录一条笔记：标题《{title}》")


def main():
    if len(sys.argv) < 2:
        print("没有收到原始指令文本。")
        return

    full_text = " ".join(sys.argv[1:]).strip()
    content, title = parse_command(full_text)

    if not content:
        print("没有成功解析出内容部分，请检查指令是否包含『xxx内容给我记下』这样的结构。")
        return

    append_markdown_note(content, title)


if __name__ == "__main__":
    main()
