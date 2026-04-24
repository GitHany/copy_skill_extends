# -*- coding: utf-8 -*-
"""
检查工具 - 检查参数完整性和占位符使用
功能：
  1. 检测参数占位符使用情况（%{参数名}% 格式）
  2. 统计未填写参数的情况
  3. 检查参数定义的完整性

使用方法：python scripts/check_params.py
说明：
  - 遍历所有模块的 commands.json
  - 检查扩展命令中的参数使用
  - 统计参数定义缺失情况

modules_dir = 'modules'
issues = []

placeholder_pattern = re.compile(r'%\{([^}]+)\}%')

for name in sorted(os.listdir(modules_dir)):
    path = os.path.join(modules_dir, name, 'commands.json')
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            commands = data.get('commands', [])
            if not commands and isinstance(data, dict) and 'commands' in data:
                commands = data['commands']
            
            for cmd in commands:
                cmd_data = cmd.get('data', cmd)
                extensions = cmd_data.get('extensions', [])
                params = cmd_data.get('params', {})
                
                for ext in extensions:
                    ext_cmd = ext.get('cmd', '')
                    ext_params = ext.get('params', {})
                    
                    placeholders = placeholder_pattern.findall(ext_cmd)
                    
                    if placeholders and not ext_params:
                        issues.append(name + ' - ' + ext.get('name', 'unknown') + ': 占位符 ' + str(placeholders) + ' 但无params')
                    elif placeholders and ext_params == {}:
                        issues.append(name + ' - ' + ext.get('name', 'unknown') + ': 占位符 ' + str(placeholders) + ' 但params是空{}')
                        
        except Exception as e:
            print('[ERROR] ' + name + ': ' + str(e))

if issues:
    print('找到 ' + str(len(issues)) + ' 个问题:')
    for issue in issues[:30]:
        print('  - ' + issue)
    if len(issues) > 30:
        print('  ... 还有 ' + str(len(issues) - 30) + ' 个问题')
else:
    print('没有发现有问题')