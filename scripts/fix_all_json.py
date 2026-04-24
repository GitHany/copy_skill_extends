#!/usr/bin/env python3
"""
修复工具 - 修复所有 commands.json 中的 module 和 dirPath 错误
功能：
  1. 修复 module 字段格式（应该是 "分类/目录名"）
  2. 修复 dirPath 字段（应该是 "/分类/"）
  3. 批量处理所有模块

使用方法：python scripts/fix_all_json.py
说明：
  - 根据 JSON 文件路径自动推断分类
  - 自动修复 module 和 dirPath 字段
  - 输出修复统计信息

import os
import json
from pathlib import Path

MODULES_DIR = Path(r"C:\code\copy_skill_extends\modules")

def get_category_from_path(json_path):
    """根据 JSON 文件路径推断正确的分类"""
    rel_path = json_path.parent.relative_to(MODULES_DIR)
    parts = str(rel_path).split(os.sep)
    if len(parts) >= 1:
        return parts[0]
    return None

def fix_json_file(json_path):
    """修复单个 JSON 文件"""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return False, f"JSON error: {e}"
    
    category = get_category_from_path(json_path)
    if not category:
        return False, "Could not determine category"
    
    fixed = False
    
    # 修复 module 字段
    old_module = data.get('module', '')
    # module 应该是 "分类/目录名"
    dir_name = json_path.parent.name
    expected_module = f"{category}/{dir_name}"
    
    if old_module != expected_module:
        data['module'] = expected_module
        fixed = True
    
    # 修复 dirPath
    expected_dirpath = f"/{category}/"
    for cmd in data.get('commands', []):
        if cmd.get('dirPath') != expected_dirpath:
            cmd['dirPath'] = expected_dirpath
            fixed = True
    
    if fixed:
        try:
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True, f"Fixed: {old_module} -> {expected_module}"
        except Exception as e:
            return False, f"Write error: {e}"
    
    return False, "No changes needed"

def process_directory(category_dir):
    """处理一个分类目录下的所有 JSON 文件"""
    results = []
    category = category_dir.name
    
    for json_path in category_dir.rglob("commands.json"):
        success, msg = fix_json_file(json_path)
        if success or "Fixed" in msg:
            results.append((str(json_path.relative_to(MODULES_DIR)), msg))
    
    return results

def main():
    print("=" * 80)
    print("修复所有 commands.json")
    print("=" * 80)
    
    all_results = []
    
    # 遍历所有分类目录
    for category_dir in MODULES_DIR.iterdir():
        if not category_dir.is_dir() or category_dir.name.startswith('.'):
            continue
        
        print(f"\n处理 {category_dir.name}...")
        results = process_directory(category_dir)
        all_results.extend(results)
        print(f"  修复了 {len(results)} 个文件")
    
    print("\n" + "=" * 80)
    print(f"总计: 修复了 {len(all_results)} 个文件")
    print("=" * 80)

if __name__ == "__main__":
    main()
