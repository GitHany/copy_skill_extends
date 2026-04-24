#!/usr/bin/env python3
"""
分析工具 - 检查所有 commands.json 文件中的错误
功能：
  1. 检查扩展命令是否为空 (EXTENSION_CMD_EMPTY)
  2. 检查描述长度是否过短 (DESCRIPTION_TOO_SHORT)
  3. 检查参数描述是否过短 (PARAM_DESC_TOO_SHORT)
  4. 检查备注是否为空 (NOTES_EMPTY)
  5. 检查 JSON 格式是否有效 (INVALID_JSON)
  6. 检查命令名是否包含数字前缀 (NAME_HAS_NUMBER_PREFIX)

使用方法：python scripts/analyze_commands.py
输出：生成 error_report.txt 文件，记录所有错误

import json
import os
import re
from pathlib import Path

MODULES_DIR = Path(r"C:\code\copy_skill_extends\modules")

ERROR_TYPES = {
    "EXTENSION_CMD_EMPTY": [],
    "DESCRIPTION_TOO_SHORT": [],
    "PARAM_DESC_TOO_SHORT": [],
    "NOTES_EMPTY": [],
    "INVALID_JSON": [],
    "NAME_HAS_NUMBER_PREFIX": [],
}

def analyze_file(filepath):
    """Analyze a single commands.json file for errors"""
    errors = {
        "EXTENSION_CMD_EMPTY": [],
        "DESCRIPTION_TOO_SHORT": [],
        "PARAM_DESC_TOO_SHORT": [],
        "NOTES_EMPTY": [],
        "INVALID_JSON": [],
        "NAME_HAS_NUMBER_PREFIX": [],
    }
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        errors["INVALID_JSON"].append(f"JSON parse error: {e}")
        return errors
    except Exception as e:
        errors["INVALID_JSON"].append(f"File read error: {e}")
        return errors
    
    module_name = data.get("module", "Unknown")
    
    for cmd in data.get("commands", []):
        cmd_name = cmd.get("name", "Unknown")
        
        # Check command description
        desc = cmd.get("description", "")
        if len(desc) < 30:
            errors["DESCRIPTION_TOO_SHORT"].append(f"{module_name}/{cmd_name}: '{desc[:50]}...' ({len(desc)} chars)")
        
        # Check command name for number prefix
        name = cmd.get("name", "")
        if re.match(r'^\d+[-.]', name):
            errors["NAME_HAS_NUMBER_PREFIX"].append(f"{module_name}/{cmd_name}: '{name}'")
        
        # Check data section
        data_section = cmd.get("data", {})
        
        # Check extensions
        for i, ext in enumerate(data_section.get("extensions", [])):
            ext_name = ext.get("name", f"ext_{i}")
            
            # Check if cmd is empty
            ext_cmd = ext.get("cmd", "")
            if not ext_cmd or ext_cmd.strip() == "":
                errors["EXTENSION_CMD_EMPTY"].append(f"{module_name}/{cmd_name}/{ext_name}: cmd is empty")
            
            # Check extension description
            ext_desc = ext.get("description", "")
            if ext_desc and len(ext_desc) < 30:
                errors["DESCRIPTION_TOO_SHORT"].append(f"{module_name}/{cmd_name}/{ext_name}: '{ext_desc[:50]}...' ({len(ext_desc)} chars)")
            
            # Check params in extension
            for param_name, param in ext.get("params", {}).items():
                param_desc = param.get("description", "")
                if len(param_desc) < 15:
                    errors["PARAM_DESC_TOO_SHORT"].append(f"{module_name}/{cmd_name}/{ext_name}/{param_name}: '{param_desc}' ({len(param_desc)} chars)")
                
                notes = param.get("notes", "")
                if not notes or notes.strip() == "":
                    errors["NOTES_EMPTY"].append(f"{module_name}/{cmd_name}/{ext_name}/{param_name}")
        
        # Check main params
        for param_name, param in data_section.get("params", {}).items():
            param_desc = param.get("description", "")
            if len(param_desc) < 15:
                errors["PARAM_DESC_TOO_SHORT"].append(f"{module_name}/{cmd_name}/params/{param_name}: '{param_desc}' ({len(param_desc)} chars)")
            
            notes = param.get("notes", "")
            if not notes or notes.strip() == "":
                errors["NOTES_EMPTY"].append(f"{module_name}/{cmd_name}/params/{param_name}")
    
    return errors

def main():
    print("=" * 80)
    print("ANALYZING ALL COMMANDS.JSON FILES")
    print("=" * 80)
    
    all_errors = {k: [] for k in ERROR_TYPES}
    json_files = list(MODULES_DIR.glob("*/commands.json"))
    
    print(f"\nFound {len(json_files)} commands.json files\n")
    
    for filepath in json_files:
        errors = analyze_file(filepath)
        for err_type, err_list in errors.items():
            all_errors[err_type].extend(err_list)
    
    # Print summary
    print("\n" + "=" * 80)
    print("ERROR SUMMARY")
    print("=" * 80)
    
    for err_type, err_list in all_errors.items():
        if err_list:
            print(f"\n{err_type}: {len(err_list)} errors")
            print("-" * 40)
            for err in err_list[:10]:
                print(f"  - {err}")
            if len(err_list) > 10:
                print(f"  ... and {len(err_list) - 10} more")
    
    # Save detailed report
    report_path = Path(r"C:\code\copy_skill_extends\error_report.txt")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("COMMANDS.JSON ERROR REPORT\n")
        f.write("=" * 80 + "\n\n")
        for err_type, err_list in all_errors.items():
            f.write(f"\n{err_type}: {len(err_list)} errors\n")
            f.write("-" * 40 + "\n")
            for err in err_list:
                f.write(f"  - {err}\n")
    
    print(f"\nDetailed report saved to: {report_path}")
    
    return all_errors

if __name__ == "__main__":
    main()
