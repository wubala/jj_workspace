#!/usr/bin/env python3
"""
Tailscale 密钥解析工具
用途：将 Base64 编码的密钥解析成 Tailscale CLI 参数
"""

import base64
import sys
from urllib.parse import unquote


def base64_decode(encoded_str: str) -> str:
    """Base64 解码"""
    try:
        decoded = base64.b64decode(encoded_str).decode('utf-8')
        return unquote(decoded)
    except Exception as e:
        print(f"❌ Base64 解码失败: {e}")
        return ""


def parse_tailscale_command(cmd: str) -> dict:
    """解析 tailscale 命令参数"""
    args = cmd.strip().split()
    
    if not args:
        return {"command": "", "subcommand": "", "options": {}}
    
    result = {
        "command": args[0] if len(args) > 0 else "",
        "subcommand": args[1] if len(args) > 1 else "",
        "options": {}
    }
    
    # 允许多值的参数
    multi_value_keys = {"advertise-routes"}
    
    i = 2  # 从第三个参数开始（跳过 command 和 subcommand）
    while i < len(args):
        arg = args[i]
        
        if arg.startswith("--"):
            key = arg[2:]  # 去掉 "--"
            
            if "=" in key:
                # --key=value 格式
                key, value = key.split("=", 1)
            else:
                # --key value 或 --key (boolean) 格式
                next_arg = args[i + 1] if i + 1 < len(args) else None
                if next_arg and not next_arg.startswith("--"):
                    value = next_arg
                    i += 1  # 跳过下一个参数
                else:
                    value = True
            
            # 处理多值参数
            if key in multi_value_keys:
                if key in result["options"]:
                    existing = result["options"][key]
                    if isinstance(existing, list):
                        existing.append(value)
                    else:
                        result["options"][key] = [existing, value]
                else:
                    result["options"][key] = [value]
            else:
                result["options"][key] = value
        
        i += 1
    
    return result


def print_result(parsed: dict):
    """格式化输出解析结果"""
    print("\n" + "="*60)
    print("📋 解析结果")
    print("="*60)
    
    print(f"\n🔹 命令: {parsed['command']}")
    print(f"🔹 子命令: {parsed['subcommand']}")
    
    if parsed['options']:
        print("\n📦 参数列表:")
        print("-"*60)
        for key, value in parsed['options'].items():
            if isinstance(value, bool):
                print(f"  --{key}")
            elif isinstance(value, list):
                print(f"  --{key} = {', '.join(value)}")
            else:
                print(f"  --{key} = {value}")
    
    # 生成完整命令
    print("\n" + "="*60)
    print("💻 完整命令（可直接复制）")
    print("="*60)
    
    cmd_parts = [parsed['command'], parsed['subcommand']]
    for key, value in parsed['options'].items():
        if isinstance(value, bool):
            cmd_parts.append(f"--{key}")
        elif isinstance(value, list):
            cmd_parts.append(f"--{key}={','.join(value)}")
        else:
            cmd_parts.append(f"--{key}={value}")
    
    print("\n" + " ".join(cmd_parts))
    print()


def main():
    print("="*60)
    print("🔐 Tailscale 密钥解析工具")
    print("="*60)
    
    if len(sys.argv) > 1:
        # 从命令行参数读取
        encoded_str = sys.argv[1]
    else:
        # 交互式输入
        print("\n请输入 Base64 编码的密钥（粘贴后按回车）:")
        print("提示：直接粘贴即可，无需处理换行\n")
        encoded_str = input(">>> ").strip()
    
    if not encoded_str:
        print("❌ 未输入密钥")
        return
    
    # 解码
    decoded = base64_decode(encoded_str)
    if not decoded:
        return
    
    print("\n📝 解码后的原始命令:")
    print("-"*60)
    print(decoded)
    
    # 解析
    parsed = parse_tailscale_command(decoded)
    
    # 输出结果
    print_result(parsed)


if __name__ == "__main__":
    main()
