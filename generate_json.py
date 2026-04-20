# -*- coding: utf-8 -*-
"""
根据 .md 文档重新生成 commands.json
"""

import json
import re
from pathlib import Path

def parse_markdown_table(text):
    """解析 Markdown 表格"""
    lines = text.strip().split('\n')
    if len(lines) < 3:
        return []
    
    # 解析数据行
    results = []
    for line in lines[2:]:  # 跳过表头和分隔行
        cells = [c.strip() for c in line.split('|')[1:-1]]
        # 第一列是场景/说明，第二列是命令
        if len(cells) >= 2:
            results.append({
                'scenario': cells[0],
                'cmd': cells[1]
            })
    
    return results

def extract_command_examples(md_content, category):
    """从 markdown 内容中提取命令示例"""
    commands = []
    
    # 分割每个命令部分
    sections = re.split(r'\n### ', md_content)
    
    for section in sections[1:]:  # 跳过第一个空部分
        lines = section.split('\n')
        if not lines:
            continue
        
        # 提取命令名称和基础命令
        header_match = re.match(r'(.+?) - (.+)', lines[0])
        if not header_match:
            continue
        
        keyword = header_match.group(1).strip()
        description = header_match.group(2).strip()
        
        # 提取基础命令
        base_cmd = ""
        for i, line in enumerate(lines[1:10]):  # 只检查前10行
            line = line.strip()
            if line.startswith('`') and 'git ' in line:
                base_cmd = line.strip('`')
                break
            elif line.startswith('```bash'):
                # 下一行是命令
                if i+1 < len(lines):
                    next_line = lines[i+2].strip() if i+2 < len(lines) else ''
                    if next_line and not next_line.startswith('```'):
                        base_cmd = next_line
                        break
        
        # 如果没找到基础命令，尝试从正文中提取
        if not base_cmd:
            for line in lines[1:]:
                line = line.strip()
                if line.startswith('`') and not line.startswith('``'):
                    base_cmd = line.strip('`')
                    break
        
        # 提取扩展示例
        extensions = []
        table_start = -1
        for i, line in enumerate(lines):
            if '扩展示例' in line:
                table_start = i
                break
        
        if table_start >= 0:
            table_lines = '\n'.join(lines[table_start:])
            examples = parse_markdown_table(table_lines)
            
            for ex in examples:
                cmd = ex['cmd']
                if cmd and cmd.startswith('`'):
                    cmd = cmd.strip('`')
                
                if cmd and ('git ' in cmd or 'docker ' in cmd or 'cd ' in cmd or 'ls ' in cmd):
                    extensions.append({
                        "name": ex['scenario'],
                        "cmd": cmd,
                        "params": {},
                        "keyword": f"{keyword} {ex['scenario']}"
                    })
        
        # 提取参数
        params = {}
        param_pattern = r'%\{([^}]+)\}%'
        all_text = '\n'.join(lines)
        for match in re.finditer(param_pattern, all_text):
            param_name = match.group(1)
            if param_name not in params:
                params[param_name] = {
                    "type": "string",
                    "required": True,
                    "description": f"{param_name}参数",
                    "example": "",
                    "notes": ""
                }
        
        if base_cmd:  # 只添加有基础命令的
            commands.append({
                "dirPath": f"/{category}/",
                "name": f"{keyword} {description}",
                "keyword": keyword,
                "description": description,
                "data": {
                    "cmd": base_cmd,
                    "extensions": extensions,
                    "params": params
                }
            })
    
    return commands

def main():
    docs_dir = Path("docs")
    
    all_commands = []
    
    # Git commands
    git_md = (docs_dir / "git-commands" / "README.md").read_text(encoding='utf-8')
    git_commands = extract_command_examples(git_md, "Git 命令")
    all_commands.extend(git_commands)
    print(f"Git commands: {len(git_commands)}")
    
    # Docker commands
    docker_md = (docs_dir / "docker-commands" / "README.md").read_text(encoding='utf-8')
    docker_commands = extract_command_examples(docker_md, "Docker 命令")
    all_commands.extend(docker_commands)
    print(f"Docker commands: {len(docker_commands)}")
    
    # Linux commands
    linux_md = (docs_dir / "linux-commands" / "README.md").read_text(encoding='utf-8')
    linux_commands = extract_command_examples(linux_md, "Linux 命令")
    all_commands.extend(linux_commands)
    print(f"Linux commands: {len(linux_commands)}")
    
    # 保存为 JSON
    output = {"data": all_commands}
    output_path = docs_dir / "public" / "commands.json"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"\nTotal commands: {len(all_commands)}")
    print(f"Output: {output_path}")

if __name__ == "__main__":
    main()
