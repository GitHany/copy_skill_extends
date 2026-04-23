import json
import os
import re

def fix_extra_braces(content):
    """Fix extra closing braces like }}}} -> }}}"""
    # Replace 4+ consecutive } with exactly 3 }
    fixed = re.sub(r'\}{4,}', '}}}', content)
    return fixed

def fix_missing_commas_before_brace(content):
    """Fix missing commas: "prop": value}{ -> "prop": value}, {"""
    # Pattern: "param": {}} followed by " -> missing comma
    fixed = re.sub(r'(\}\")(\s*\{)', r'}\1,\2', content)
    return fixed

def fix_json_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix extra closing braces
    fixed = fix_extra_braces(content)

    # Fix missing commas
    fixed = fix_missing_commas_before_brace(fixed)

    try:
        json.loads(fixed)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(fixed)
        print(f"FIXED: {filepath}")
        return True
    except json.JSONDecodeError as e:
        print(f"STILL BROKEN: {filepath} - {e}")
        return False

files = [
    'C:/code/copy_skill_extends/modules/kubectl version/commands.json',
    'C:/code/copy_skill_extends/modules/Kubernetes ConfigMap 与 Secret/commands.json',
    'C:/code/copy_skill_extends/modules/Kubernetes Deployment/commands.json',
    'C:/code/copy_skill_extends/modules/Kubernetes Ingress/commands.json',
    'C:/code/copy_skill_extends/modules/Kubernetes Pod 管理/commands.json',
    'C:/code/copy_skill_extends/modules/Kubernetes Service/commands.json',
    'C:/code/copy_skill_extends/modules/Kubernetes 集群管理/commands.json',
    'C:/code/copy_skill_extends/modules/Linux cron/commands.json',
    'C:/code/copy_skill_extends/modules/Linux export/commands.json',
    'C:/code/copy_skill_extends/modules/Linux find/commands.json',
    'C:/code/copy_skill_extends/modules/Linux journalctl/commands.json',
    'C:/code/copy_skill_extends/modules/Linux rsync/commands.json',
    'C:/code/copy_skill_extends/modules/Linux scp/commands.json',
    'C:/code/copy_skill_extends/modules/Linux ssh-keygen/commands.json',
    'C:/code/copy_skill_extends/modules/Linux systemctl/commands.json',
    'C:/code/copy_skill_extends/modules/Linux ulimit/commands.json',
    'C:/code/copy_skill_extends/modules/Linux xargs/commands.json',
    'C:/code/copy_skill_extends/modules/Linux 压缩解压/commands.json',
    'C:/code/copy_skill_extends/modules/Linux 文本处理/commands.json',
    'C:/code/copy_skill_extends/modules/Linux 权限管理/commands.json',
]

for f in files:
    fix_json_file(f)