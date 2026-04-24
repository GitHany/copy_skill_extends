# -*- coding: utf-8 -*-
"""
验证工具 - 验证所有 commands.json 文件的 JSON 格式正确性
功能：
  1. 遍历所有模块目录
  2. 验证每个 commands.json 的 JSON 格式
  3. 统计成功和失败的文件数量
  4. 报告错误详情

使用方法：python scripts/validate_all.py
说明：
  - 基础格式验证
  - 检查 JSON 语法错误
  - 统计整体验证结果

import json
from pathlib import Path

def validate_json(file_path):
    """验证单个 JSON 文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return True, None, data
    except json.JSONDecodeError as e:
        return False, f"JSON decode error: {e}", None
    except Exception as e:
        return False, f"Error: {e}", None

def main():
    modules_dir = Path(__file__).parent.parent / 'modules'
    files = sorted(list(modules_dir.glob('*/commands.json')))
    
    success = 0
    failed = 0
    errors = []
    
    for file_path in files:
        valid, error, data = validate_json(file_path)
        if valid:
            success += 1
            # 检查是否为标准格式（字典且有 module 字段）
            if isinstance(data, dict) and 'module' in data:
                pass  # 标准格式
            elif isinstance(data, list):
                errors.append(f"List format (needs fix): {file_path}")
            else:
                errors.append(f"Unknown format: {file_path}")
        else:
            failed += 1
            errors.append(f"Invalid JSON: {file_path} - {error}")
    
    print(f"Validation Results:")
    print(f"  Valid: {success}")
    print(f"  Invalid: {failed}")
    print(f"  Total: {success + failed}")
    
    if errors:
        print(f"\nIssues found:")
        for err in errors:
            print(f"  - {err}")
    else:
        print("\nAll files are valid!")

if __name__ == '__main__':
    main()
