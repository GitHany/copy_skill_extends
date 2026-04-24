"""
验证工具 - 验证特定目录结构（容器编排）
功能：
  1. 检查 module 字段格式是否正确（应该是 "容器编排/{模块名}"）
  2. 检查 dirPath 字段是否正确（应该是 "/容器编排/"）
  3. 验证 JSON 格式有效性

使用方法：python scripts/test_verify.py
说明：
  - 专门用于验证容器编排分类的目录结构
  - 输出详细的错误信息
  - 统计总文件数和问题数量

folder = r"C:\code\copy_skill_extends\modules\容器编排"
os.chdir(folder)

issues = []
total = 0

for root, dirs, files in os.walk('.'):
    for f in files:
        if f == 'commands.json':
            total += 1
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8') as fp:
                    data = json.load(fp)
                    # Check module format
                    module = data.get('module', '')
                    if not module.startswith('容器编排/'):
                        issues.append(f'{path}: module="{module}" 格式错误')
                    # Check dirPath
                    for cmd in data.get('commands', []):
                        if cmd.get('dirPath') != '/容器编排/':
                            issues.append(f'{path}: {cmd.get("name", "unknown")} dirPath="{cmd.get("dirPath", "")}" 错误')
            except json.JSONDecodeError as e:
                issues.append(f'{path}: JSON格式错误 - {e}')
            except Exception as e:
                issues.append(f'{path}: 读取错误 - {e}')

print(f'总文件数: {total}')
print(f'问题数量: {len(issues)}')
for i in issues:
    print(i)
