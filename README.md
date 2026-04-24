# copy_skill_extends

**开发者命令知识库** — 面向 AI 助手的结构化命令参考，支持 copy_skill Web App。

## 功能特性

- **64+ 模块覆盖**：Linux、Docker、Git、GitHub CLI、Kubernetes、MySQL、Redis、PostgreSQL、Python、前端包管理器、Claude Skills 等
- **参数完整**：每个命令包含 type/required/description/example/notes
- **双模式支持**：
  - **直接复制**：`params: {}` + 硬编码命令，一键复制
  - **参数化输入**：需要填入的命令展示输入表单
- **扩展用法**：每个命令提供多个常用扩展场景

## 项目结构

```
copy_skill_extends/
├── modules/                          # 模块目录 (64个模块)
│   ├── _registry.json                # 模块注册表，记录所有模块信息
│   ├── Docker 命令/
│   │   ├── commands.json             # 模块命令数据
│   │   └── README.md                 # 模块说明文档
│   ├── Git 命令/
│   ├── GitHub CLI 命令/
│   ├── GitHubActions/
│   ├── Kubernetes 命令/
│   ├── Kubernetes 高级操作/
│   ├── Linux 命令/
│   ├── MySQL 命令/
│   ├── PostgreSQL 命令/
│   ├── Python命令/
│   ├── Redis-基本操作/
│   ├── Redis-哈希操作/
│   ├── Redis-列表操作/
│   ├── Redis-有序集合/
│   ├── Redis-集合操作/
│   ├── Redis-键管理/
│   ├── Redis-服务器命令/
│   ├── SSH远程操作/
│   ├── Shell脚本模板/
│   ├── Nginx命令/
│   ├── Elasticsearch/
│   ├── MongoDB 命令/
│   ├── AI_ML工具/
│   ├── API与认证/
│   ├── CDN与缓存/
│   ├── CI_CD 流水线/
│   ├── Claude Skills-ccg/
│   ├── Claude Skills-ecc/
│   ├── Claude Skills-oh-my-claude/
│   ├── Claude Skills-openspec/
│   ├── Claude Skills-providers/
│   ├── Claude Skills-regex/
│   ├── Claude Skills-superpowers/
│   ├── Claude Skills-ultrawork/
│   ├── DockerCompose/
│   ├── DockerCompose 高级模式/
│   ├── Go 命令/
│   ├── GraphQL 命令/
│   ├── Java Spring Boot/
│   ├── Node.js 后端命令/
│   ├── ORM框架/
│   ├── Python Web框架/
│   ├── React 命令/
│   ├── Tailwind CSS/
│   ├── TypeScript 命令/
│   ├── Vue.js 命令/
│   ├── Web API工具/
│   ├── 前端包管理器/
│   ├── 包管理器/
│   ├── 安全加固/
│   ├── 容器安全/
│   ├── 微服务架构/
│   ├── 搜索引擎/
│   ├── 测试框架/
│   ├── 消息队列/
│   ├── 监控与可观测性/
│   ├── 移动开发/
│   ├── 系统监控/
│   ├── 编辑器命令/
│   ├── 网络诊断/
│   ├── 配置管理/
│   └── Serverless与边缘计算/
├── scripts/                          # 工具脚本目录 (18个工具脚本)
│   ├── 01_分析工具/                  # 代码分析
│   │   └── analyze_commands.py       # 命令分析工具，检查格式和内容错误
│   ├── 02_修复工具/                  # 错误修复
│   │   ├── fix_all_json.py           # 批量修复 module 和 dirPath 字段
│   │   ├── fix_commands.py           # 批量修复命令内容错误
│   │   ├── fix_params.py             # 修复参数格式问题
│   │   ├── fix_list_files.py         # 列表格式转换工具
│   │   ├── fix_unknown_format.py     # 修复非标准格式文件
│   │   └── fix_remaining.py          # 处理未分类模块的重组
│   ├── 03_增强工具/                  # 内容增强
│   │   ├── enhance_all.py            # 批量增强命令描述和参数
│   │   ├── enhance_commands.py        # 标准增强工具
│   │   └── check_params.py           # 参数完整性检查工具
│   ├── 04_合并与分离/                # 数据合并
│   │   ├── merge_commands.py         # 合并所有模块（使用注册表）
│   │   ├── merge_all_commands.py     # 合并所有模块（遍历目录）
│   │   └── split_commands.py         # 分离合并文件为模块化结构
│   ├── 05_重组工具/                  # 目录重组
│   │   └── reorganize_modules.py     # 模块重组脚本，创建二级分类结构
│   ├── 06_验证工具/                  # 格式验证
│   │   ├── validate_all.py           # 批量验证 JSON 格式
│   │   ├── validate_cloud.py         # 云平台目录验证工具
│   │   └── test_verify.py            # 容器编排验证工具
│   └── README.md                     # 脚本工具详细文档
├── docs/
│   └── public/
│       └── commands.json            # 聚合后的最终文件（由 merge_commands.py 生成）
├── commands_standard.json            # 命令数据标准规范参考文件
├── commands_standard_ref.json        # 精简版标准参考（仅 Schema）
├── .gitignore
└── README.md
```

## 文件说明

### 根目录文件

| 文件 | 说明 |
|------|------|
| `commands_standard.json` | 完整的命令数据标准规范，包含 Schema 和参数知识库 |
| `commands_standard_ref.json` | 精简版标准参考，仅包含 JSON Schema 定义 |
| `.gitignore` | Git 忽略规则 |
| `README.md` | 项目说明文档 |

### scripts/ 目录

scripts/ 目录包含 18 个工具脚本，分为 6 大类：

#### 📊 01_分析工具

| 脚本 | 功能 |
|------|------|
| `analyze_commands.py` | 命令分析工具，检查 6 类错误（扩展命令空、描述短、参数描述短、备注空、JSON无效、命令名数字前缀） |

#### 🔧 02_修复工具

| 脚本 | 功能 |
|------|------|
| `fix_all_json.py` | 批量修复 module 和 dirPath 字段格式 |
| `fix_commands.py` | 批量修复命令内容错误（空命令、描述短、备注空等） |
| `fix_params.py` | 修复参数格式问题（列表→字典转换、占位符问题） |
| `fix_list_files.py` | 修复列表格式文件，转换为标准 JSON 格式 |
| `fix_unknown_format.py` | 修复非标准格式文件，补充模块元信息 |
| `fix_remaining.py` | 处理未分类模块，按映射表重新分配分类 |

#### ✨ 03_增强工具

| 脚本 | 功能 |
|------|------|
| `enhance_all.py` | 批量增强命令描述、参数注释和示例完整性（包含参数知识库） |
| `enhance_commands.py` | 标准增强工具，参考 commands_standard.json 标准 |
| `check_params.py` | 参数完整性检查，检测占位符使用情况 |

#### 📦 04_合并与分离

| 脚本 | 功能 |
|------|------|
| `merge_commands.py` | 合并所有模块（使用 _registry.json 注册表）→ docs/public/commands.json |
| `merge_all_commands.py` | 合并所有模块（遍历目录结构）→ commands_merged.json |
| `split_commands.py` | 分离合并文件为模块化结构（反向操作） |

#### 🏗️ 05_重组工具

| 脚本 | 功能 |
|------|------|
| `reorganize_modules.py` | 模块重组脚本，创建二级分类结构（分类/模块） |

#### ✅ 06_验证工具

| 脚本 | 功能 |
|------|------|
| `validate_all.py` | 批量验证所有 commands.json 的 JSON 格式正确性 |
| `validate_cloud.py` | 云平台目录结构验证工具（AWS/Azure/GCP） |
| `test_verify.py` | 容器编排目录结构验证工具 |

**详细文档**：请参考 `scripts/README.md` 获取完整的使用说明和使用流程。

### modules/ 目录

每个模块包含：
- `commands.json` - 模块的命令数据
- `README.md` - 模块说明文档

模块分类：
- **容器编排**：Docker 命令、DockerCompose、DockerCompose 高级模式
- **版本控制**：Git 命令、Git 工作流、GitHub CLI 命令、GitHubActions
- **数据库**：MySQL 命令、PostgreSQL 命令、MongoDB 命令、Redis 系列（7个）、Elasticsearch
- **容器管理**：Kubernetes 命令、Kubernetes 高级操作
- **编程语言**：Python 命令、Python Web框架、Go 命令、Java Spring Boot、Node.js 后端命令
- **前端**：React 命令、Vue.js 命令、TypeScript 命令、Tailwind CSS、前端包管理器
- **服务器**：Nginx命令、SSH远程操作
- **监控**：系统监控、网络诊断、监控与可观测性
- **DevOps**：CI_CD 流水线、安全加固、容器安全、微服务架构
- **AI/ML**：AI_ML工具、Serverless与边缘计算
- **工具**：包管理器、Web API工具、API与认证、GraphQL 命令、编辑器命令、配置管理、测试框架
- **Claude Skills**：11个子模块

### docs/ 目录

| 文件 | 说明 |
|------|------|
| `docs/public/commands.json` | 最终合并的命令数据，由 `merge_commands.py` 生成 |

## 使用方法

### 合并所有模块

```bash
python scripts/merge_commands.py
```

输出：`docs/public/commands.json`

### 增强命令内容

```bash
python scripts/enhance_all.py
```

自动增强所有模块的命令描述和参数注释。

### 验证 JSON 格式

```bash
python scripts/validate_all.py
```

检查所有 commands.json 文件的格式正确性。

## commands.json 标准格式

```json
{
  "module": "模块名称",
  "version": "1.0",
  "description": "模块详细描述（20字以上）",
  "commands": [
    {
      "dirPath": "/分类路径/",
      "name": "命令名称",
      "keyword": "搜索关键词",
      "description": "命令详细描述（30字以上）",
      "data": {
        "cmd": "基础命令模板，使用 %{参数名}% 占位",
        "extensions": [
          {
            "name": "扩展用法名称",
            "cmd": "具体命令",
            "params": {
              "参数名": {
                "type": "string|integer|boolean|array|object",
                "required": "boolean",
                "description": "参数含义说明（15字以上）",
                "example": "真实可用的示例值",
                "notes": "必填说明/默认值/注意事项"
              }
            },
            "keyword": "扩展用法的搜索关键词"
          }
        ],
        "params": {
          "参数名": {
            "type": "string|integer|boolean|array|object",
            "required": "boolean",
            "description": "参数含义说明（15字以上）",
            "example": "真实可用的示例值",
            "notes": "必填说明/默认值/注意事项"
          }
        }
      }
    }
  ]
}
```

## 参数规范

| 字段 | 要求 | 说明 |
|------|------|------|
| `type` | 必填 | 数据类型：string、integer、boolean、array、object |
| `required` | 必填 | 是否必填：true、false |
| `description` | 必填 | 参数含义说明，需 15 字以上，包含参数作用和对命令行为的影响 |
| `example` | 必填 | 真实可用的示例值 |
| `notes` | 必填 | 必填说明/默认值/取值范围/注意事项，禁止为空字符串 |

## 命名规范

- 命令名称：使用 `工具 动作 对象` 格式，如 `docker run 运行容器`
- 参数名称：使用中文名词，如 `容器名称`、`镜像名称`、`主机端口`
- 搜索关键词：用空格分隔，包含同义词和常用组合
- 禁止数字前缀：如 `1-` `2.` 等前缀必须移除