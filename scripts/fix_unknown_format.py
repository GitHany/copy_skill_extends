# -*- coding: utf-8 -*-
"""
修复非标准格式的 commands.json 文件
"""

import json
import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

# 模块名称映射
MODULE_NAMES = {
    "Claude Skills-ccg": "Claude Skills-ccg",
    "Claude Skills-openspec": "Claude Skills-openspec",
    "Claude Skills-providers": "Claude Skills-providers",
    "Claude Skills-superpowers": "Claude Skills-superpowers",
    "Claude Skills-ultrawork": "Claude Skills-ultrawork",
    "DockerCompose": "DockerCompose",
    "DockerCompose 高级模式": "DockerCompose 高级模式",
    "系统监控": "系统监控",
}

MODULE_DESCS = {
    "Claude Skills-ccg": "Claude-Codex-Gemini 三模型协作代码生成模块，利用多个 AI 模型的优势进行智能代码生成和优化",
    "Claude Skills-openspec": "OpenSpec 规范定义模块，用于标准化 API 接口定义和数据模型描述",
    "Claude Skills-providers": "Claude Skills 提供商管理模块，用于配置和管理不同 AI 服务提供商的接入",
    "Claude Skills-superpowers": "Claude Skills 超级能力模块，提供增强的 AI 辅助功能和高级操作命令",
    "Claude Skills-ultrawork": "Claude Skills 超高效工作流模块，提供自动化任务处理和批量操作功能",
    "DockerCompose": "Docker Compose 基础模块，提供多容器应用的定义和运行管理命令",
    "DockerCompose 高级模式": "Docker Compose 高级模式模块，提供生产环境配置、扩展部署和复杂编排功能",
    "系统监控": "系统监控模块，提供 CPU、内存、磁盘、网络等系统资源的实时监控和性能分析命令",
}

def remove_number_prefix(text):
    if not isinstance(text, str):
        return text
    return re.sub(r'^\d+[-.、\s]+', '', text)

def enhance_param(param_name, param_data):
    """增强参数"""
    if not isinstance(param_data, dict):
        param_data = {}
    
    existing_desc = param_data.get('description', '')
    if len(existing_desc) >= 20:
        if not param_data.get('notes'):
            param_data['notes'] = f"{'必填' if param_data.get('required') else '可选'}。请根据实际需求填写"
        return param_data
    
    if not param_data.get('description') or len(param_data.get('description', '')) < 10:
        param_data['description'] = f"{param_name}参数，用于指定命令操作的目标或配置选项"
    if not param_data.get('example') or param_data.get('example') == param_name:
        param_data['example'] = f"my_{param_name.lower()}"
    if not param_data.get('notes'):
        param_data['notes'] = f"{'必填' if param_data.get('required') else '可选'}。请根据实际需求填写"
    
    return param_data

def enhance_command(cmd, module_name):
    """增强单个命令"""
    if 'name' in cmd:
        cmd['name'] = remove_number_prefix(cmd['name'])
    
    desc = cmd.get('description', '')
    if len(desc) < 25:
        name = cmd.get('name', '')
        cmd['description'] = f"{desc}。这是 {module_name} 模块的常用操作命令，适用于日常开发和运维场景"
    
    data = cmd.get('data', {})
    
    if 'params' in data and isinstance(data['params'], dict):
        for param_name, param_data in list(data['params'].items()):
            data['params'][param_name] = enhance_param(param_name, param_data)
    
    if 'extensions' in data and isinstance(data['extensions'], list):
        for ext in data['extensions']:
            if isinstance(ext, dict):
                if 'name' in ext:
                    ext['name'] = remove_number_prefix(ext['name'])
                if 'params' in ext and isinstance(ext['params'], dict):
                    for param_name, param_data in list(ext['params'].items()):
                        ext['params'][param_name] = enhance_param(param_name, param_data)
    
    cmd['data'] = data
    return cmd

def fix_file(file_path, module_name, module_desc):
    """修复文件格式"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False
    
    commands = []
    
    if isinstance(data, dict):
        # 检查是否是单命令格式（有 dirPath 但没有 module）
        if 'dirPath' in data and 'data' in data:
            commands = [data]
        # 检查是否是嵌套 data.commands 格式
        elif 'data' in data and isinstance(data['data'], dict) and 'commands' in data['data']:
            commands = data['data']['commands']
        # 检查是否有 commands 字段
        elif 'commands' in data:
            commands = data['commands']
    elif isinstance(data, list):
        commands = data
    
    # 增强每个命令
    for cmd in commands:
        enhance_command(cmd, module_name)
    
    # 构建标准格式
    result = {
        "module": module_name,
        "version": "1.0",
        "description": module_desc,
        "commands": commands
    }
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"Fixed: {file_path}")
        return True
    except Exception as e:
        print(f"Error writing {file_path}: {e}")
        return False

def main():
    modules_dir = Path(__file__).parent.parent / 'modules'
    
    for dir_name, module_name in MODULE_NAMES.items():
        file_path = modules_dir / dir_name / 'commands.json'
        module_desc = MODULE_DESCS.get(dir_name, f"{module_name} 模块，提供常用的 {module_name} 相关命令和工具")
        fix_file(file_path, module_name, module_desc)

if __name__ == '__main__':
    main()
