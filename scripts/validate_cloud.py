"""
验证工具 - 验证云平台目录结构
功能：
  1. 自动识别云平台分类目录（根据中文字符识别）
  2. 检查每个子模块的 module 字段格式（应该是 "{云平台}/{模块名}"）
  3. 检查每个子模块的 dirPath 字段（应该是 "/{云平台}/"）
  4. 验证 module 后缀是否与子目录名匹配

使用方法：python scripts/validate_cloud.py
说明：
  - 专门用于验证云平台分类（AWS、Azure、GCP 等）
  - 自动检测中文字符目录
  - 输出详细的验证错误信息

# Find the cloud platform directory
modules_dir = Path(r'C:\code\copy_skill_extends\modules')
cloud_dir = None
for d in modules_dir.iterdir():
    if d.is_dir() and len(d.name) == 3 and ord(d.name[0]) > 127:  # Chinese chars have high ordinals
        cloud_dir = d
        break

if not cloud_dir:
    print('Cloud platform directory not found')
    exit()

# Get the actual directory name bytes for comparison
cloud_dir_name = cloud_dir.name

print(f'Cloud platform dir: {cloud_dir_name} (len={len(cloud_dir_name)})')
subdirs = sorted([s for s in cloud_dir.iterdir() if s.is_dir()])

issues = []
for subdir in subdirs:
    cmd_file = subdir / 'commands.json'
    if not cmd_file.exists():
        issues.append(f'[MISSING] {subdir.name}: commands.json not found')
        continue
    
    try:
        with open(cmd_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Check module field
        if 'module' in data:
            module_val = data['module']
            # Expected format: "云平台/模块名" where 模块名 matches subdir name
            expected_prefix = f'{cloud_dir_name}/'
            if not module_val.startswith(expected_prefix):
                issues.append(f'[MODULE_PREFIX] {subdir.name}: module="{module_val}" does not start with "{expected_prefix}"')
            else:
                # Also check that the module name after prefix matches subdir name
                module_suffix = module_val[len(expected_prefix):]
                if module_suffix != subdir.name:
                    issues.append(f'[MODULE_MISMATCH] {subdir.name}: module suffix "{module_suffix}" does not match directory name')
        
        # Check dirPath
        if 'dirPath' in data:
            expected_dirpath = f'/{cloud_dir_name}/'
            if data['dirPath'] != expected_dirpath:
                issues.append(f'[DIRPATH] {subdir.name}: dirPath="{data["dirPath"]}" should be "{expected_dirpath}"')
        else:
            issues.append(f'[DIRPATH_MISSING] {subdir.name}: dirPath field missing')
            
    except json.JSONDecodeError as e:
        issues.append(f'[JSON_ERROR] {subdir.name}: {str(e)}')
    except Exception as e:
        issues.append(f'[ERROR] {subdir.name}: {str(e)}')

if issues:
    print(f'\nFound {len(issues)} issues:')
    for issue in issues:
        print(issue)
else:
    print('All correct')
