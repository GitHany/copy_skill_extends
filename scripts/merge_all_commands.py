#!/usr/bin/env python3
"""
合并工具 - 将所有模块的 commands.json 合并为一个最终文件
功能：
  1. 遍历所有分类目录下的模块
  2. 读取每个模块的 commands.json
  3. 合并所有命令到单一列表
  4. 输出到 commands_merged.json

使用方法：python scripts/merge_all_commands.py
输出：生成 commands_merged.json 文件
说明：
  - 按分类目录结构遍历（modules/{分类}/{模块}/commands.json）
  - 统计模块总数和命令总数
  - 包含错误处理和进度显示
"""

import os
import json
from pathlib import Path

MODULES_DIR = Path(r"C:\code\copy_skill_extends\modules")
OUTPUT_FILE = Path(r"C:\code\copy_skill_extends\commands_merged.json")

def merge_all_commands():
    """合并所有命令"""
    all_commands = []
    module_count = 0
    cmd_count = 0
    
    # 按分类目录遍历
    for category_dir in sorted(MODULES_DIR.iterdir()):
        if not category_dir.is_dir() or category_dir.name.startswith('.'):
            continue
        
        # 遍历该分类下的所有模块
        for module_dir in sorted(category_dir.iterdir()):
            if not module_dir.is_dir():
                continue
            
            json_path = module_dir / "commands.json"
            if not json_path.exists():
                continue
            
            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                module_count += 1
                module_name = data.get('module', module_dir.name)
                commands = data.get('commands', [])
                cmd_count += len(commands)
                
                # 添加到总列表
                for cmd in commands:
                    all_commands.append(cmd)
                    
            except json.JSONDecodeError as e:
                print(f"JSON error in {json_path}: {e}")
            except Exception as e:
                print(f"Error reading {json_path}: {e}")
    
    # 创建最终结构
    merged = {
        "_meta": {
            "version": "2.0",
            "description": "合并后的所有命令集合",
            "total_modules": module_count,
            "total_commands": cmd_count,
            "total_extensions": sum(len(cmd.get('data', {}).get('extensions', [])) for cmd in all_commands)
        },
        "commands": all_commands
    }
    
    # 写入文件
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
    
    print(f"合并完成!")
    print(f"  模块数: {module_count}")
    print(f"  命令数: {cmd_count}")
    print(f"  输出文件: {OUTPUT_FILE}")
    
    return merged

if __name__ == "__main__":
    merge_all_commands()
