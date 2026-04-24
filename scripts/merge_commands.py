# -*- coding: utf-8 -*-
"""
合并工具 - 合并所有模块的 commands.json 为最终的 commands.json
功能：
  1. 读取 _registry.json 注册表
  2. 遍历所有注册的模块
  3. 合并所有命令到单一 JSON 文件
  4. 输出到 docs/public/commands.json

使用方法：python scripts/merge_commands.py
说明：
  - 使用 _registry.json 作为模块注册表
  - 按注册表顺序合并
  - 生成最终的公开版本
"""

import json
import sys
from pathlib import Path

# 设置 UTF-8 输出
sys.stdout.reconfigure(encoding='utf-8')

def merge_commands():
    """合并所有模块的命令"""
    modules_dir = Path(__file__).parent.parent / 'modules'
    registry_file = modules_dir / '_registry.json'
    output_file = Path(__file__).parent.parent / 'docs' / 'public' / 'commands.json'
    
    # 读取注册表
    with open(registry_file, 'r', encoding='utf-8') as f:
        registry = json.load(f)
    
    all_commands = []
    
    print("开始合并模块...\n", flush=True)
    
    # 遍历所有模块
    for module_info in registry['modules']:
        module_path = modules_dir / module_info['name'] / 'commands.json'
        
        if module_path.exists():
            with open(module_path, 'r', encoding='utf-8') as f:
                module_data = json.load(f)
            
            # 处理四种可能的格式：
            # 1. {"commands": [...]} - 标准格式
            # 2. [...] - 直接数组格式
            # 3. {dirPath, name, ...} - 单个命令对象
            # 4. {"data": {"commands": [...]}} - 嵌套格式
            if isinstance(module_data, dict) and 'commands' in module_data:
                commands = module_data['commands']
            elif isinstance(module_data, dict) and 'data' in module_data and isinstance(module_data['data'], dict) and 'commands' in module_data['data']:
                commands = module_data['data']['commands']
            elif isinstance(module_data, list):
                commands = module_data
            elif isinstance(module_data, dict) and 'dirPath' in module_data:
                commands = [module_data]
            else:
                commands = []
                print(f"[WARN] {module_info['name']}: 未知格式", flush=True)
            all_commands.extend(commands)
            
            print(f"[OK] {module_info['name']}: {len(commands)} 条命令", flush=True)
        else:
            print(f"[FAIL] {module_info['name']}: 文件不存在", flush=True)
    
    # 排序：按 dirPath 和 name
    all_commands.sort(key=lambda x: (x.get('dirPath', ''), x.get('name', '')))
    
    # 保存最终文件
    output_data = {"data": all_commands}
    
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n[DONE] 合并完成！")
    print(f"[DONE] 总计: {len(all_commands)} 条命令")
    print(f"[DONE] 输出: {output_file}", flush=True)

if __name__ == '__main__':
    merge_commands()
