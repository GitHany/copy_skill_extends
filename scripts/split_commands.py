# -*- coding: utf-8 -*-
"""
分离工具 - 将合并的 commands.json 分离成模块化的文件
功能：
  1. 读取合并后的 commands.json
  2. 按 dirPath 分离为不同模块
  3. 关联 Markdown 文档
  4. 恢复模块化结构

使用方法：python scripts/split_commands.py
说明：
  - 是 merge_commands.py 的反向操作
  - 从 docs/public/commands.json 读取
  - 按模块目录结构重新分离

import json
import shutil
from pathlib import Path
from collections import defaultdict

def clean_module_name(dir_path):
    """从 dirPath 提取模块名"""
    path = dir_path.strip('/')
    parts = path.split('/')
    
    # 合并所有路径部分为模块名
    if parts:
        return '-'.join([p.strip() for p in parts if p.strip()])
    return 'uncategorized'

def split_commands_by_module():
    """按模块分离命令并关联 Markdown 文档"""
    source_file = Path(__file__).parent.parent / 'docs' / 'public' / 'commands.json'
    
    with open(source_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    commands = data.get('data', [])
    
    # 按 dirPath 分组
    modules = defaultdict(list)
    
    for cmd in commands:
        dir_path = cmd.get('dirPath', '/')
        module_name = clean_module_name(dir_path)
        modules[module_name].append(cmd)
    
    # 创建 modules 目录
    modules_dir = Path(__file__).parent.parent / 'modules'
    modules_dir.mkdir(exist_ok=True)
    
    # 查找并关联 Markdown 文档
    docs_dir = Path(__file__).parent.parent / 'docs'
    md_mapping = {
        'Linux 命令': 'linux-commands',
        'Git 命令': 'git-commands',
        'Docker 命令': 'docker-commands',
        'MySQL 命令': 'mysql-commands',
        'Redis-列表操作': 'redis-commands',
        'Redis-哈希操作': 'redis-commands',
        'Redis-基本操作': 'redis-commands',
        'Redis-有序集合': 'redis-commands',
        'Redis-服务器命令': 'redis-commands',
        'Redis-键管理': 'redis-commands',
        'Redis-集合操作': 'redis-commands',
    }
    
    print("开始分离命令到模块...\n")
    
    # 保存各个模块的 commands.json
    registry = []
    
    for module_name, module_commands in sorted(modules.items()):
        module_dir = modules_dir / module_name
        module_dir.mkdir(exist_ok=True)
        
        # 保存 commands.json
        output_file = module_dir / 'commands.json'
        module_data = {
            "module": module_name,
            "version": "1.0",
            "description": f"{module_name} 模块命令集合",
            "commands": module_commands
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(module_data, f, ensure_ascii=False, indent=2)
        
        # 关联 Markdown 文档
        md_copied = False
        for md_name, std_name in md_mapping.items():
            if md_name in module_name:
                src_md = docs_dir / std_name / 'README.md'
                if src_md.exists():
                    dst_md = module_dir / 'README.md'
                    shutil.copy2(src_md, dst_md)
                    print(f"✓ 关联 {module_name}/README.md")
                    md_copied = True
                    break
        
        cmd_count = len(module_commands)
        md_indicator = " 📄" if md_copied else ""
        print(f"✓ 创建 {module_name}/commands.json ({cmd_count} 条命令){md_indicator}")
        
        registry.append({
            "name": module_name,
            "path": f"modules/{module_name}/commands.json",
            "count": len(module_commands),
            "has_docs": md_copied
        })
    
    # 保存注册表
    registry_file = modules_dir / '_registry.json'
    with open(registry_file, 'w', encoding='utf-8') as f:
        json.dump({"modules": registry}, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ 生成了 {len(registry)} 个模块")
    print(f"✓ 注册表: modules/_registry.json")

if __name__ == '__main__':
    split_commands_by_module()
