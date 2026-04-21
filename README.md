# copy_skill_extends

**开发者命令知识库** — 面向 AI 助手的结构化命令参考，支持 copy_skill Web App。

## 功能特性

- **345+ 命令覆盖**：Linux、Docker、Git、GitHub CLI、Kubernetes、MySQL、Redis、PostgreSQL 等
- **参数完整**：每个命令包含 type/required/description/example/notes
- **双模式支持**：
  - **直接复制**：`params: {}` + 硬编码命令，一键复制
  - **参数化输入**：需要填入的命令展示输入表单
- **高频标记**：常用命令标注【常用】

## 目录结构

```
copy_skill_extends/
├── modules/                    # 各模块独立目录
│   ├── Docker 命令/
│   ├── Git 命令/
│   ├── GitHub CLI 命令/
│   ├── Kubernetes 命令/
│   ├── Linux 命令/
│   ├── MySQL 命令/
│   ├── PostgreSQL 命令/
│   ├── Redis-基本操作/
│   ├── Redis-哈希操作/
│   ├── Redis-列表操作/
│   ├── Redis-有序集合/
│   ├── Redis-服务器命令/
│   ├── Redis-键管理/
│   ├── Redis-集合操作/
│   ├── Claude Skills-oh-my-claude/
│   ├── Claude Skills-ecc/
│   ├── Claude Skills-ccg/
│   ├── Claude Skills-openspec/
│   ├── Claude Skills-providers/
│   ├── Claude Skills-regex/
│   ├── Claude Skills-superpowers/
│   └── Claude Skills-ultrawork/
├── scripts/
│   └── merge_commands.py     # 合并脚本
├── docs/
│   └── public/
│       └── commands.json     # 聚合后的最终文件
├── modules/_registry.json    # 模块注册表
└── README.md
```

## 获取最终的 commands.json

```bash
python scripts/merge_commands.py
```

输出：`docs/public/commands.json`

## commands.json 结构

```json
{
  "data": [
    {
      "dirPath": "/Docker 命令/",
      "name": "docker run 运行容器",
      "keyword": "docker run 启动",
      "description": "创建并启动一个新容器",
      "data": {
        "cmd": "docker run -d --name %{容器名称}% -p %{主机端口}%:%{容器端口}% %{镜像名称}%",
        "extensions": [
          {
            "name": "查看所有容器",
            "cmd": "docker ps -a",
            "params": {},
            "keyword": "docker ps 所有容器"
          },
          {
            "name": "挂载卷",
            "cmd": "docker run -d --name %{容器名称}% -v %{主机路径}%:%{容器路径}% %{镜像}%",
            "params": {
              "容器名称": { "type": "string", "required": true, "description": "容器名称", "example": "myapp", "notes": "常用" },
              "主机路径": { "type": "string", "required": true, "description": "宿主机目录", "example": "/data/logs", "notes": "" },
              "容器路径": { "type": "string", "required": true, "description": "容器内目录", "example": "/app/logs", "notes": "" },
              "镜像": { "type": "string", "required": true, "description": "镜像名称", "example": "nginx", "notes": "" }
            },
            "keyword": "docker run 挂载卷"
          }
        ],
        "params": {
          "容器名称": { "type": "string", "required": true, "description": "容器名称", "example": "myapp", "notes": "" },
          "主机端口": { "type": "string", "required": true, "description": "宿主机端口", "example": "8080", "notes": "" },
          "容器端口": { "type": "string", "required": true, "description": "容器端口", "example": "80", "notes": "" },
          "镜像名称": { "type": "string", "required": true, "description": "镜像名称", "example": "nginx", "notes": "常用" }
        }
      }
    }
  ]
}
```

### 字段说明

| 字段 | 含义 |
|------|------|
| `dirPath` | 分类路径，UI 左侧树形菜单节点 |
| `name` | 命令显示名称 |
| `keyword` | 搜索关键词，空格分隔多个词 |
| `description` | 一句话描述 |
| `cmd` | 带 `%{param}%` 占位符的基础命令 |
| `extensions` | 扩展变体数组 |
| `params` | 参数定义 |

### params 参数定义

| 子字段 | 含义 |
|--------|------|
| `type` | 类型：`string` / `number` / `boolean` |
| `required` | 是否必填：`true` / `false` |
| `description` | 参数中文说明 |
| `example` | 示例值，用于输入框 placeholder |
| `notes` | 使用提示，标注"常用"表示高频命令 |

### extension 渲染规则

| params | cmd | 渲染方式 |
|--------|-----|----------|
| `{}` 空 | 无占位符 | **直接复制**按钮 |
| `{}` 空 | 有占位符 | 展示输入表单 |
| 有内容 | 任意 | 展示输入表单 |

## 模块列表

| 模块 | 命令数 |
|------|--------|
| Linux 命令 | 43 |
| Docker 命令 | 21 |
| Git 命令 | 24 |
| GitHub CLI 命令 | 33 |
| Kubernetes 命令 | 29 |
| MySQL 命令 | 19 |
| PostgreSQL 命令 | 25 |
| Redis-基本操作 | 18 |
| Redis-哈希操作 | 12 |
| Redis-列表操作 | 13 |
| Redis-有序集合 | 13 |
| Redis-服务器命令 | 15 |
| Redis-键管理 | 16 |
| Redis-集合操作 | 15 |
| Claude Skills | 50+ |
| **总计** | **345+** |

## 与 copy_skill 配合使用

1. 在 `copy_skill_extends` 目录运行合并脚本：
   ```bash
   python scripts/merge_commands.py
   ```

2. 将生成的 `docs/public/commands.json` 复制到 `copy_skill/docs/public/`：
   ```bash
   cp docs/public/commands.json /path/to/copy_skill/docs/public/commands.json
   ```

3. 重启 `copy_skill` Web App
