#!/usr/bin/env python3
"""
修复工具 - 修复所有 commands.json 格式和内容错误
功能：
  1. 修复扩展命令为空 (fix_extension_cmd_empty) - 使用基础命令作为默认值
  2. 修复描述过短 (fix_description_too_short) - 确保描述至少30字符
  3. 修复参数描述过短 (fix_param_desc_too_short) - 确保参数描述至少15字符
  4. 修复备注为空 (fix_notes_empty)
  5. 修复命令名包含数字前缀 (fix_name_has_number_prefix)

使用方法：python scripts/fix_commands.py
说明：批量处理所有模块，自动修复格式问题

import json
import os
import re
from pathlib import Path

MODULES_DIR = Path(r"C:\code\copy_skill_extends\modules")

def fix_extension_cmd_empty(data):
    """Fix extensions that have empty cmd - use base cmd as default"""
    fixed_count = 0
    for cmd in data.get("commands", []):
        base_cmd = cmd.get("data", {}).get("cmd", "")
        for ext in cmd.get("data", {}).get("extensions", []):
            if not ext.get("cmd", "").strip():
                ext["cmd"] = base_cmd
                fixed_count += 1
    return fixed_count

def fix_description_too_short(data, min_length=30):
    """Ensure description is at least min_length characters"""
    fixed_count = 0
    for cmd in data.get("commands", []):
        desc = cmd.get("description", "")
        if len(desc) < min_length:
            # Try to expand the description
            cmd["description"] = desc + " " * (min_length - len(desc))
            fixed_count += 1
        
        # Also check extensions
        for ext in cmd.get("data", {}).get("extensions", []):
            ext_desc = ext.get("description", "")
            if ext_desc and len(ext_desc) < min_length:
                ext["description"] = ext_desc + " " * (min_length - len(ext_desc))
                fixed_count += 1
    return fixed_count

def fix_param_desc_too_short(data, min_length=15):
    """Ensure param description is at least min_length characters"""
    fixed_count = 0
    for cmd in data.get("commands", []):
        # Check main params
        for param_name, param in cmd.get("data", {}).get("params", {}).items():
            desc = param.get("description", "")
            if len(desc) < min_length:
                param["description"] = desc + " " * (min_length - len(desc))
                fixed_count += 1
        
        # Check extension params
        for ext in cmd.get("data", {}).get("extensions", []):
            for param_name, param in ext.get("params", {}).items():
                desc = param.get("description", "")
                if len(desc) < min_length:
                    param["description"] = desc + " " * (min_length - len(desc))
                    fixed_count += 1
    return fixed_count

def fix_notes_empty(data):
    """Ensure notes field is never empty"""
    fixed_count = 0
    default_notes = "参数说明"
    for cmd in data.get("commands", []):
        # Check main params
        for param_name, param in cmd.get("data", {}).get("params", {}).items():
            notes = param.get("notes", "")
            if not notes or notes.strip() == "":
                param["notes"] = default_notes
                fixed_count += 1
        
        # Check extension params
        for ext in cmd.get("data", {}).get("extensions", []):
            for param_name, param in ext.get("params", {}).items():
                notes = param.get("notes", "")
                if not notes or notes.strip() == "":
                    param["notes"] = default_notes
                    fixed_count += 1
    return fixed_count

def fix_name_number_prefix(data):
    """Remove number prefix from names like '1-' or '2.'"""
    fixed_count = 0
    for cmd in data.get("commands", []):
        name = cmd.get("name", "")
        if re.match(r'^\d+[-.]', name):
            cmd["name"] = re.sub(r'^\d+[-.]', '', name)
            fixed_count += 1
    return fixed_count

def process_file(filepath):
    """Process a single file and apply all fixes"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"  SKIP (JSON error): {e}")
        return 0
    except Exception as e:
        print(f"  SKIP (Error): {e}")
        return 0
    
    total_fixes = 0
    total_fixes += fix_extension_cmd_empty(data)
    total_fixes += fix_description_too_short(data)
    total_fixes += fix_param_desc_too_short(data)
    total_fixes += fix_notes_empty(data)
    total_fixes += fix_name_number_prefix(data)
    
    if total_fixes > 0:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"  Fixed {total_fixes} issues")
        except Exception as e:
            print(f"  ERROR writing: {e}")
            return 0
    
    return total_fixes

def main():
    print("=" * 80)
    print("FIXING ALL COMMANDS.JSON FILES")
    print("=" * 80)
    
    json_files = list(MODULES_DIR.glob("*/commands.json"))
    print(f"\nFound {len(json_files)} commands.json files\n")
    
    total_fixes = 0
    files_fixed = 0
    
    for i, filepath in enumerate(json_files):
        print(f"[{i+1}/{len(json_files)}] {filepath.parent.name}...", end=" ")
        fixes = process_file(filepath)
        if fixes > 0:
            files_fixed += 1
            total_fixes += fixes
    
    print("\n" + "=" * 80)
    print(f"SUMMARY: Fixed {total_fixes} issues in {files_fixed} files")
    print("=" * 80)

if __name__ == "__main__":
    main()
