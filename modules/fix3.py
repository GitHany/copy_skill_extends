import json
import os
import re

def fix_json_auto(filepath):
    """Try multiple strategies to fix JSON"""
    print(f"\n=== {filepath} ===")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Strategy 1: Remove trailing commas
    fixed = re.sub(r',(\s*[}\]])', r'\1', content)
    try:
        json.loads(fixed)
        print("Strategy 1: Remove trailing commas - SUCCESS")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(fixed)
        return True
    except: pass

    # Strategy 2: Add missing commas between } and {
    fixed = re.sub(r'(\})([ \t\n]*\{)', r'\1,\2', content)
    try:
        json.loads(fixed)
        print("Strategy 2: Add missing commas - SUCCESS")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(fixed)
        return True
    except: pass

    # Strategy 3: Remove extra closing braces at end (common issue)
    # Pattern: }}}}} or more at end of content
    lines = content.split('\n')
    last_line = lines[-1]
    if last_line.strip() == '}':
        # Check if second-to-last line has extra }
        if len(lines) >= 2 and lines[-2].strip().endswith('}}}}'):
            # Try removing one }
            fixed_lines = lines.copy()
            # Find the } pattern and reduce by one
            match = re.search(r'}}}}+$', lines[-2])
            if match:
                fixed_lines[-2] = lines[-2][:len(lines[-2]) - len(match.group()) + 4]  # Keep 4 }
                fixed = '\n'.join(fixed_lines)
                try:
                    json.loads(fixed)
                    print("Strategy 3: Remove extra braces - SUCCESS")
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(fixed)
                    return True
                except: pass

    # Strategy 4: Find and fix specific pattern at end
    # Pattern: notes value followed by too many }
    match = re.search(r'(\"notes\":\s*\"[^\"]*\")(}}}}+)\s*\n\s*\]', content)
    if match:
        fixed = content[:match.start(2)] + '}}}' + content[match.end(2):]
        try:
            json.loads(fixed)
            print("Strategy 4: Fix extra braces at end - SUCCESS")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(fixed)
            return True
        except: pass

    print("All strategies failed")
    return False

# Process files
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
        fix_json_auto(f)
    else:
        print(f"NOT FOUND: {f}")