# -*- coding: utf-8 -*-
"""
转换工具 - 处理列表格式的 commands.json 文件
功能：
  1. 检测列表格式的 commands.json 文件
  2. 转换为标准格式
  3. 增强内容完整性
  4. 包含 Redis 相关参数知识库

使用方法：python scripts/fix_list_files.py
说明：
  - 专门处理非标准列表格式
  - 自动转换为标准 JSON 格式
  - 补充缺失的参数信息

import json
import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

PARAM_KNOWLEDGE = {
    "内容": {"description": "要进行正则验证或匹配的文本内容，可以是邮箱、手机号、URL 或密码等字符串", "example": "test@example.com", "notes": "必填。根据验证类型提供对应格式的内容"},
    "键名": {"description": "Redis 键的名称，用于唯一标识存储的数据。键是二进制安全的字符串", "example": "mylist", "notes": "必填。建议使用命名空间前缀组织键名，如 list:、set:、zset:"},
    "值": {"description": "要存储到 Redis 列表中的数据值，可以是字符串、数字或序列化后的对象", "example": "hello", "notes": "必填。字符串值包含空格需用引号包裹。复杂对象建议序列化为 JSON"},
    "分数": {"description": "Redis 有序集合中用于排序的数值，分数越低排名越靠前。支持浮点数", "example": "100", "notes": "必填。可以是整数或浮点数。相同分数的成员按字典序排列"},
    "成员": {"description": "Redis 有序集合中的成员值，作为唯一标识存储在集合中", "example": "alice", "notes": "必填。成员在集合中唯一，重复添加会更新分数"},
    "起始索引": {"description": "列表或有序集合查询的起始位置索引，从 0 开始。负数表示从末尾倒数", "example": "0", "notes": "必填。0 表示第一个元素，-1 表示最后一个元素，-2 表示倒数第二个"},
    "结束索引": {"description": "列表或有序集合查询的结束位置索引。包含此位置的元素", "example": "-1", "notes": "必填。-1 表示到最后一个元素。起始索引大于结束索引时返回空列表"},
    "索引": {"description": "列表中特定位置的索引值，从 0 开始计数", "example": "0", "notes": "必填。0 为第一个元素。负数索引从末尾开始，-1 为最后一个"},
    "数量": {"description": "要获取或移除的元素个数，必须为正整数", "example": "5", "notes": "必填。超出实际元素数量时返回所有可用元素"},
    "分数1": {"description": "第一个成员的排序分数，用于确定在有序集合中的位置", "example": "100", "notes": "必填。与成员1配对使用"},
    "成员1": {"description": "第一个要添加到有序集合的成员值", "example": "alice", "notes": "必填。与分数1配对使用"},
    "分数2": {"description": "第二个成员的排序分数", "example": "90", "notes": "必填。与成员2配对使用，实现批量添加"},
    "成员2": {"description": "第二个要添加到有序集合的成员值", "example": "bob", "notes": "必填。与分数2配对使用"},
    "新值": {"description": "要替换列表中现有元素的新数据值", "example": "new_value", "notes": "必填。替换后原位置的值将被新值覆盖"},
    "最小分数": {"description": "查询有序集合时的分数范围下限，包含此值", "example": "0", "notes": "必填。支持 -inf 表示负无穷。与最大分数配合实现范围查询"},
    "最大分数": {"description": "查询有序集合时的分数范围上限，包含此值", "example": "100", "notes": "必填。支持 +inf 表示正无穷。与最小分数配合实现范围查询"},
}

def get_example(param_name):
    return PARAM_KNOWLEDGE.get(param_name, {}).get('example', f'my_{param_name}')

def get_notes(param_name):
    return PARAM_KNOWLEDGE.get(param_name, {}).get('notes', '请根据实际需求填写')

def get_desc(param_name):
    return PARAM_KNOWLEDGE.get(param_name, {}).get('description', f'{param_name}参数')

def enhance_param(param_name, param_data):
    """增强参数"""
    if not isinstance(param_data, dict):
        param_data = {}
    
    existing_desc = param_data.get('description', '')
    if len(existing_desc) >= 15 and param_name in PARAM_KNOWLEDGE:
        if not param_data.get('notes'):
            param_data['notes'] = get_notes(param_name)
        return param_data
    
    if param_name in PARAM_KNOWLEDGE:
        param_data['description'] = PARAM_KNOWLEDGE[param_name]['description']
        param_data['example'] = PARAM_KNOWLEDGE[param_name]['example']
        param_data['notes'] = PARAM_KNOWLEDGE[param_name]['notes']
    else:
        if not param_data.get('description') or len(param_data.get('description', '')) < 10:
            param_data['description'] = f"{param_name}参数，用于指定命令操作的目标"
        if not param_data.get('example'):
            param_data['example'] = get_example(param_name)
        if not param_data.get('notes'):
            param_data['notes'] = f"{'必填' if param_data.get('required') else '可选'}。{get_notes(param_name)}"
    
    return param_data

def remove_number_prefix(text):
    if not isinstance(text, str):
        return text
    return re.sub(r'^\d+[-.、\s]+', '', text)

def enhance_command(cmd, module_name):
    """增强单个命令"""
    if 'name' in cmd:
        cmd['name'] = remove_number_prefix(cmd['name'])
    
    # 增强描述
    desc = cmd.get('description', '')
    if len(desc) < 20:
        name = cmd.get('name', '')
        if 'regex' in module_name.lower():
            cmd['description'] = f"{desc}。这是 Claude Skills 正则表达式工具的核心功能，用于快速验证和匹配常见的数据格式。支持邮箱、手机号、URL、密码等多种验证场景"
        elif 'Redis' in module_name:
            cmd['description'] = f"{desc}。这是 Redis 内存数据库列表/有序集合的核心操作命令，用于高性能数据存储和排名管理。适用于消息队列、时间线、排行榜等场景"
        else:
            cmd['description'] = f"{desc}。该命令是 {module_name} 模块的常用操作，掌握其用法对于日常开发非常重要"
    
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

def process_list_file(file_path, module_name, module_desc):
    """处理列表格式的文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            commands = json.load(f)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False
    
    if not isinstance(commands, list):
        print(f"Not a list file: {file_path}")
        return False
    
    for cmd in commands:
        enhance_command(cmd, module_name)
    
    data = {
        "module": module_name,
        "version": "1.0",
        "description": module_desc,
        "commands": commands
    }
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Fixed list format: {file_path}")
        return True
    except Exception as e:
        print(f"Error writing {file_path}: {e}")
        return False

def main():
    files_to_fix = [
        ("Claude Skills-regex", "Claude Skills-regex", "Claude Skills 正则表达式验证模块，提供邮箱、手机号、URL、密码等常见格式的快速验证和匹配功能"),
        ("Redis-列表操作", "Redis-列表操作", "Redis 列表(List)操作模块，提供 LPUSH、RPUSH、LRANGE、LPOP 等列表数据结构的核心操作命令。适用于消息队列、时间线、最新消息等场景"),
        ("Redis-有序集合", "Redis-有序集合", "Redis 有序集合(Sorted Set)操作模块，提供 ZADD、ZRANGE、ZREM、ZSCORE 等有序集合的核心操作命令。适用于排行榜、优先级队列、延时队列等场景"),
    ]
    
    modules_dir = Path(__file__).parent.parent / 'modules'
    
    for dir_name, module_name, module_desc in files_to_fix:
        file_path = modules_dir / dir_name / 'commands.json'
        process_list_file(file_path, module_name, module_desc)

if __name__ == '__main__':
    main()
