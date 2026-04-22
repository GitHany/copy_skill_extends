# -*- coding: utf-8 -*-
import json
import os
import re

modules_dir = 'modules'
placeholder_pattern = re.compile(r'%\{([^}]+)\}%')

def fix_module(name):
    path = os.path.join(modules_dir, name, 'commands.json')
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    commands = data.get('commands', [])
    if not commands and isinstance(data, dict) and 'commands' in data:
        commands = data['commands']
    
    fixed_count = 0
    
    for cmd in commands:
        cmd_data = cmd if 'data' not in cmd else cmd.get('data', cmd)
        extensions = cmd_data.get('extensions', [])
        top_params = cmd_data.get('params', {})
        
        if isinstance(top_params, list):
            top_params = {p['name']: p for p in top_params}
        elif top_params is None:
            top_params = {}
        
        for ext in extensions:
            ext_cmd = ext.get('cmd', '')
            placeholders = placeholder_pattern.findall(ext_cmd)
            ext_params = ext.get('params', {})
            
            if placeholders and (not ext_params or ext_params == {}):
                new_params = {}
                for pname in placeholders:
                    if pname in top_params:
                        tp = top_params[pname]
                        new_params[pname] = {
                            "type": tp.get('type', 'string') if isinstance(tp, dict) else 'string',
                            "required": False,
                            "description": tp.get('description', '') if isinstance(tp, dict) else '',
                            "example": tp.get('example', '') if isinstance(tp, dict) else '',
                            "notes": tp.get('notes', '') if isinstance(tp, dict) else ''
                        }
                    else:
                        new_params[pname] = {
                            "type": "string",
                            "required": False,
                            "description": "",
                            "example": "",
                            "notes": ""
                        }
                ext['params'] = new_params
                fixed_count += 1
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return fixed_count

def main():
    total_fixed = 0
    modules_with_issues = ['AWS CLI命令', 'CDN与缓存', 'CI_CD 流水线', 'DockerCompose', 
                          'DockerCompose 高级模式', 'GitHub CLI 命令', 'GitHubActions',
                          'Kubernetes 命令', 'Kubernetes 高级操作', 'Serverless与边缘计算',
                          'Tailwind CSS', 'Vue.js 命令', 'Web API工具', '前端包管理器',
                          '包管理器', '安全加固', '网络诊断']
    
    for name in modules_with_issues:
        path = os.path.join(modules_dir, name, 'commands.json')
        if os.path.exists(path):
            count = fix_module(name)
            print('修复 ' + name + ': ' + str(count) + ' 个')
            total_fixed += count
    
    print('总计修复: ' + str(total_fixed) + ' 个 extension')

main()