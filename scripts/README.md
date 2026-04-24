# 脚本工具目录

本文档详细介绍项目中所有工具脚本的功能和使用方法。

## 目录结构

```
scripts/
├── 01_分析工具/              # 代码分析
├── 02_修复工具/              # 错误修复
├── 03_增强工具/              # 内容增强
├── 04_合并与分离/            # 数据合并
├── 05_重组工具/              # 目录重组
├── 06_验证工具/              # 格式验证
└── README.md                 # 本文档
```

## 脚本分类

### 📊 01_分析工具

#### analyze_commands.py - 命令分析工具
**功能**：
- 检查扩展命令是否为空
- 检查描述长度是否过短（< 30字符）
- 检查参数描述长度（< 15字符）
- 检查备注是否为空
- 检查 JSON 格式有效性
- 检查命令名是否包含数字前缀

**使用方法**：
```bash
python scripts/analyze_commands.py
```

**输出**：
- 生成 `error_report.txt` 文件
- 记录所有检测到的错误

---

### 🔧 02_修复工具

#### fix_all_json.py - 批量修复 JSON 字段
**功能**：
- 修复 `module` 字段格式（应为 "分类/目录名"）
- 修复 `dirPath` 字段（应为 "/分类/"）
- 批量处理所有模块

**使用方法**：
```bash
python scripts/fix_all_json.py
```

**特点**：
- 自动推断分类
- 智能修复字段格式

---

#### fix_commands.py - 批量修复命令内容
**功能**：
- 修复扩展命令为空（使用基础命令作为默认值）
- 修复描述过短（确保至少 30 字符）
- 修复参数描述过短（确保至少 15 字符）
- 修复备注为空
- 修复命令名包含数字前缀

**使用方法**：
```bash
python scripts/fix_commands.py
```

---

#### fix_params.py - 参数修复工具
**功能**：
- 修复列表格式的参数定义
- 转换参数格式为标准字典格式
- 检测并修复参数占位符问题（%{参数名}%）

**使用方法**：
```bash
python scripts/fix_params.py
```

---

#### fix_list_files.py - 列表格式转换工具
**功能**：
- 检测列表格式的 commands.json
- 转换为标准格式
- 增强内容完整性
- 包含 Redis 相关参数知识库

**使用方法**：
```bash
python scripts/fix_list_files.py
```

---

#### fix_unknown_format.py - 非标准格式修复
**功能**：
- 检测非标准格式的 commands.json
- 修复为标准格式
- 补充模块名称和描述
- 包含 Claude Skills 模块映射表

**使用方法**：
```bash
python scripts/fix_unknown_format.py
```

---

#### fix_remaining.py - 剩余模块重组工具
**功能**：
- 处理未分类模块
- 根据预定义映射表重新分配分类
- 支持容器编排、版本控制、数据库等分类

**使用方法**：
```bash
python scripts/fix_remaining.py
```

**⚠️ 注意**：此脚本会修改目录结构，执行前请备份

---

### ✨ 03_增强工具

#### enhance_all.py - 批量增强工具
**功能**：
- 按照标准自动增强命令描述
- 完善参数注释
- 补充示例完整性
- 包含完整的参数知识库

**使用方法**：
```bash
python scripts/enhance_all.py
```

**预定义参数知识库**：
- 通用参数（目录、文件、路径、主机、端口等）
- Docker 参数（容器名称、镜像名称、端口映射等）
- 云平台参数（AWS、Azure、GCP 相关参数）

---

#### enhance_commands.py - 标准增强工具
**功能**：
- 按照 commands_standard.json 标准增强内容
- 包含完整的参数增强知识库
- 批量应用标准规范

**使用方法**：
```bash
python scripts/enhance_commands.py
```

---

#### check_params.py - 参数完整性检查
**功能**：
- 检测参数占位符使用情况（%{参数名}% 格式）
- 统计未填写参数的情况
- 检查参数定义的完整性

**使用方法**：
```bash
python scripts/check_params.py
```

---

### 📦 04_合并与分离

#### merge_commands.py - 合并工具
**功能**：
- 读取 _registry.json 注册表
- 遍历所有注册的模块
- 合并所有命令到单一 JSON 文件
- 输出到 docs/public/commands.json

**使用方法**：
```bash
python scripts/merge_commands.py
```

**输入**：modules/_registry.json
**输出**：docs/public/commands.json

---

#### merge_all_commands.py - 全部合并工具
**功能**：
- 遍历所有分类目录下的模块
- 读取每个模块的 commands.json
- 合并所有命令到单一列表
- 输出到 commands_merged.json

**使用方法**：
```bash
python scripts/merge_all_commands.py
```

**输出**：commands_merged.json
**统计**：显示模块总数和命令总数

---

#### split_commands.py - 分离工具
**功能**：
- 读取合并后的 commands.json
- 按 dirPath 分离为不同模块
- 关联 Markdown 文档
- 恢复模块化结构

**使用方法**：
```bash
python scripts/split_commands.py
```

**输入**：docs/public/commands.json
**输出**：恢复模块目录结构

**⚠️ 注意**：这是 merge_commands.py 的反向操作

---

### 🏗️ 05_重组工具

#### reorganize_modules.py - 模块重组工具
**功能**：
- 将模块重组为二级结构（分类/模块）
- 修改 module 字段为完整路径格式
- 创建中英结合的命名规范
- 批量移动和重组目录结构

**使用方法**：
```bash
python scripts/reorganize_modules.py
```

**包含结构**：
- 容器编排（Docker、Kubernetes 等）
- 版本控制（Git 相关）
- 数据库（MySQL、PostgreSQL、MongoDB、Redis 等）
- 云平台（AWS、Azure、GCP 等）

**⚠️ 警告**：此操作会修改目录结构，执行前请备份

---

### ✅ 06_验证工具

#### validate_all.py - 批量验证工具
**功能**：
- 遍历所有模块目录
- 验证每个 commands.json 的 JSON 格式
- 统计成功和失败的文件数量
- 报告错误详情

**使用方法**：
```bash
python scripts/validate_all.py
```

---

#### validate_cloud.py - 云平台验证工具
**功能**：
- 自动识别云平台分类目录
- 检查 module 字段格式
- 检查 dirPath 字段
- 验证 module 后缀与子目录名匹配

**使用方法**：
```bash
python scripts/validate_cloud.py
```

**适用场景**：AWS、Azure、GCP 等云平台模块验证

---

#### test_verify.py - 容器编排验证工具
**功能**：
- 检查 module 字段格式（应为 "容器编排/{模块名}"）
- 检查 dirPath 字段（应为 "/容器编排/"）
- 验证 JSON 格式有效性

**使用方法**：
```bash
python scripts/test_verify.py
```

**适用场景**：容器编排分类的目录结构验证

---

## 使用流程

### 1. 新增模块后的处理流程

```bash
# 1. 验证新增模块格式
python scripts/validate_all.py

# 2. 分析问题
python scripts/analyze_commands.py

# 3. 修复问题
python scripts/fix_all_json.py
python scripts/fix_commands.py

# 4. 增强内容
python scripts/enhance_all.py

# 5. 合并发布
python scripts/merge_commands.py
```

### 2. 批量修复流程

```bash
# 1. 修复 JSON 字段格式
python scripts/fix_all_json.py

# 2. 修复命令内容
python scripts/fix_commands.py

# 3. 修复参数问题
python scripts/fix_params.py

# 4. 修复非标准格式
python scripts/fix_unknown_format.py

# 5. 处理列表格式
python scripts/fix_list_files.py
```

### 3. 目录重组流程

```bash
# ⚠️ 执行前请先备份
# 1. 重组模块结构
python scripts/reorganize_modules.py

# 2. 处理剩余未分类
python scripts/fix_remaining.py

# 3. 验证重组结果
python scripts/validate_all.py
```

---

## 注意事项

1. **备份**：重组和修复脚本会修改文件，执行前请先备份
2. **顺序**：建议按照流程顺序执行脚本
3. **验证**：每次修改后都应运行验证脚本检查结果
4. **知识库**：增强脚本使用预定义的参数知识库，可根据需要扩展
5. **编码**：所有脚本使用 UTF-8 编码，确保正确处理中文

---

## 依赖

- Python 3.6+
- 无需额外依赖（仅使用标准库）

---

## 扩展知识库

如需扩展参数知识库，可编辑以下脚本：
- `enhance_all.py` - PARAM_KNOWLEDGE 字典
- `enhance_commands.py` - PARAM_KNOWLEDGE 字典
- `fix_list_files.py` - PARAM_KNOWLEDGE 字典

添加新的参数时，建议包含：
- description：参数描述
- example：使用示例
- notes：使用注意事项
