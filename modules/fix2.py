import json
import os

def read_and_fix(filepath):
    """Read original file, extract data, and rewrite with proper JSON"""
    print(f"Processing: {filepath}")

    with open(filepath, 'rb') as f:
        raw = f.read()

    content = raw.decode('utf-8')

    try:
        json.loads(content)
        print(f"  Already valid")
        return True
    except:
        pass

    # Read the original and try to extract structure
    # For now, let's try comma fixes
    import re

    # Fix missing comma before opening brace
    fixed = re.sub(r'(\})([ \t\n]*\{)', r'\1,\2', content)
    fixed = re.sub(r'(\])([ \t\n]*\{)', r'\1,\2', fixed)

    try:
        json.loads(fixed)
        print(f"  Fixed with comma insertion")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(fixed)
        return True
    except:
        pass

    # Try removing trailing commas
    fixed = re.sub(r',\s*([\]}])', r'\1', content)

    try:
        json.loads(fixed)
        print(f"  Fixed trailing commas")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(fixed)
        return True
    except:
        pass

    print(f"  Could not fix automatically")
    return False

files = [
    r"Linux export\commands.json",
    r"Linux find\commands.json",
    r"Linux journalctl\commands.json",
    r"Linux rsync\commands.json",
    r"Linux scp\commands.json",
    r"Linux ssh-keygen\commands.json",
    r"Linux systemctl\commands.json",
    r"Linux ulimit\commands.json",
    r"Linux xargs\commands.json",
    r"Linux 压缩解压\commands.json",
    r"Linux 权限管理\commands.json",
    r"Linux 用户管理\commands.json",
    r"Linux 进程管理\commands.json",
    r"Linux 文本处理\commands.json",
    r"Linux 系统监控\commands.json",
    r"Linux 系统管理\commands.json",
    r"Linux 文件操作\commands.json",
    r"Linux 管道与重定向\commands.json",
]

for f in files:
    if os.path.exists(f):
        read_and_fix(f)
    else:
        print(f"NOT FOUND: {f}")