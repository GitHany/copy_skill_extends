import json
import re
import os

def fix_json_file(filepath):
    """Fix JSON file by adding missing commas"""
    print(f"\n=== Processing: {filepath} ===")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # First try simple parse
    try:
        json.loads(content)
        print("Already valid JSON")
        return True
    except json.JSONDecodeError as e:
        print(f"Error: {e}")

    # Try comma insertion fix
    fixed = content
    fixed = re.sub(r'(\})([ \t\n]*\{)', r'\1,\2', fixed)
    fixed = re.sub(r'(\])([ \t\n]*\[)', r'\1,\2', fixed)

    try:
        json.loads(fixed)
        print("Fixed with comma insertion!")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(fixed)
        return True
    except json.JSONDecodeError:
        pass

    # If comma fix fails, need more complex repair
    # Let's rebuild from structure
    print("Trying reconstruction...")
    return False

# Process each file
files = [
    r"C:\code\copy_skill_extends\modules\Linux curl\commands.json",
    r"C:\code\copy_skill_extends\modules\Linux export\commands.json",
    r"C:\code\copy_skill_extends\modules\Linux find\commands.json",
    r"C:\code\copy_skill_extends\modules\Linux journalctl\commands.json",
    r"C:\code\copy_skill_extends\modules\Linux rsync\commands.json",
    r"C:\code\copy_skill_extends\modules\Linux scp\commands.json",
    r"C:\code\copy_skill_extends\modules\Linux ssh-keygen\commands.json",
    r"C:\code\copy_skill_extends\modules\Linux systemctl\commands.json",
    r"C:\code\copy_skill_extends\modules\Linux ulimit\commands.json",
    r"C:\code\copy_skill_extends\modules\Linux xargs\commands.json",
    r"C:\code\copy_skill_extends\modules\Linux 压缩解压\commands.json",
    r"C:\code\copy_skill_extends\modules\Linux 权限管理\commands.json",
    r"C:\code\copy_skill_extends\modules\Linux 用户管理\commands.json",
    r"C:\code\copy_skill_extends\modules\Linux 进程管理\commands.json",
    r"C:\code\copy_skill_extends\modules\Linux 文本处理\commands.json",
    r"C:\code\copy_skill_extends\modules\Linux 系统监控\commands.json",
    r"C:\code\copy_skill_extends\modules\Linux 系统管理\commands.json",
    r"C:\code\copy_skill_extends\modules\Linux 文件操作\commands.json",
    r"C:\code\copy_skill_extends\modules\Linux 管道与重定向\commands.json",
]

for f in files:
    if os.path.exists(f):
        fix_json_file(f)
    else:
        print(f"Not found: {f}")