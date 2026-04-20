# 快速开始指南

欢迎使用 Copy Skill 命令参考知识库！本文档将帮助你快速了解如何使用这些命令和提示词。

## 📚 文档结构

```
docs/
├── claude-skills/        # Claude 技能命令
├── linux-commands/       # Linux 系统命令
├── docker-commands/      # Docker 容器命令
├── git-commands/         # Git 版本控制命令
├── devops-commands/      # 运维命令
├── workflows/            # 工作流
├── prompts/              # 提示词模板
└── software-engineering/ # 软件工程提示词
```

## 🚀 如何使用

### 1. 查找命令

每个命令都包含以下信息：

- **名称**: 命令的简短描述
- **关键词**: 用于搜索的关键词
- **命令**: 可执行的命令模板
- **扩展**: 相关命令变体

### 2. 命令模板

命令使用 `%{变量}%` 格式表示可替换的参数：

```bash
# 示例：grep 搜索
grep "%{查找的内容}%" %{在哪一个文件查找}%

# 替换后：
grep "error" /var/log/app.log
```

### 3. 扩展命令

每个主命令都有相关的扩展命令：

```bash
# 主命令
grep "error" file.log

# 扩展命令
grep -r "error" /var/log/      # 递归搜索
grep -i "error" file.log       # 忽略大小写
grep -n "error" file.log       # 显示行号
```

## 💡 使用场景

### 场景 1：AI 辅助开发

```bash
# 1. 明确需求
/oh-my-claudecode:deep-interview %{想法}%

# 2. 规划方案
/ecc:plan %{需求}%

# 3. 执行开发
/speckit-implement

# 4. 代码审查
/code-review
```

### 场景 2：Docker 部署

```bash
# 1. 构建镜像
docker build -t myapp:v1.0 .

# 2. 运行容器
docker run -d --name myapp -p 8080:80 myapp:v1.0

# 3. 查看日志
docker logs -f myapp

# 4. 进入容器调试
docker exec -it myapp /bin/bash
```

### 场景 3：Git 工作流

```bash
# 1. 创建功能分支
git checkout -b feature/new-feature

# 2. 开发并提交
git add .
git commit -m "feat: add new feature"

# 3. 推送并创建 PR
git push origin feature/new-feature

# 4. 合并到主分支
git checkout main
git merge feature/new-feature
```

## 🔍 搜索技巧

### 按关键词搜索

- Linux 命令：搜索 `linux`, `文件操作`, `磁盘管理`
- Docker 命令：搜索 `docker`, `容器`, `镜像`
- Git 命令：搜索 `git`, `分支`, `合并`

### 按场景搜索

- 开发：`AI工程师`, `后端架构师`, `前端开发者`
- 测试：`API测试`, `性能测试`, `安全测试`
- 运维：`DevOps`, `监控`, `部署`

## 📝 提示词模板

### AI 工程师

```
你是一名AI工程师，精通机器学习模型开发与部署。请帮我：
1. 数据管线搭建：清洗、特征工程、数据版本管理
2. 模型选型：选择最适合业务场景的方案
3. 训练工程化：分布式训练、混合精度、实验管理
4. 模型部署：量化优化、Serving架构、A/B测试
5. LLM应用：Prompt Engineering、RAG架构、Agent系统
```

### 后端架构师

```
你是一名资深后端架构师，请帮我设计一个可扩展的系统架构：
1. 架构模式选型（微服务/模块化单体/事件驱动）
2. 数据库Schema设计与索引优化
3. API架构设计与版本控制
4. 安全措施：认证授权、数据加密、速率限制
5. 监控与可观测性设计
```

### 产品经理

```
你是一名产品经理，请帮我编写PRD：
1. 问题陈述：解决什么用户痛点
2. 目标与成功指标：可衡量的目标
3. 用户画像与故事：核心用户场景
4. 方案概述：关键设计决策
5. 发布计划：分阶段 rollout
6. 回滚标准：异常处理预案
```

## 🎯 最佳实践

### 1. 命令组合使用

```bash
# 查找并处理日志
find /var/log -name "*.log" -mtime +7 -exec gzip {} \;

# 监控并过滤
docker logs -f myapp | grep -i "error"
```

### 2. 参数化模板

```bash
# 定义变量
APP_NAME=myapp
APP_PORT=8080
VERSION=1.0

# 使用变量
docker run -d --name $APP_NAME -p $APP_PORT:80 myapp:$VERSION
```

### 3. 错误处理

```bash
# 检查命令执行结果
if docker ps | grep -q $APP_NAME; then
    echo "Container is running"
else
    echo "Container is not running"
fi
```

## 📊 命令分类统计

| 分类 | 命令数量 | 说明 |
|------|----------|------|
| Claude Skills | 30+ | AI辅助开发技能 |
| Linux 命令 | 40+ | 系统管理命令 |
| Docker 命令 | 25+ | 容器管理命令 |
| Git 命令 | 15+ | 版本控制命令 |
| 软件工程提示词 | 15+ | 专业角色提示词 |
| 工作流 | 10+ | 工作流程模板 |

## 🔗 相关资源

- [完整命令参考表](../references/commands-reference.md)
- [Claude Skills 文档](./claude-skills/README.md)
- [Linux 命令文档](./linux-commands/README.md)
- [Docker 命令文档](./docker-commands/README.md)

## ❓ 常见问题

### Q: 如何自定义命令模板？

A: 复制命令模板，将 `%{变量}%` 替换为实际值即可。

### Q: 如何添加新命令？

A: 在 `commands.json` 中添加新的命令条目，包含名称、关键词、命令和扩展。

### Q: 如何搜索命令？

A: 使用关键词搜索，或浏览对应分类的 README 文件。

---

**提示**: 建议将常用命令收藏或创建快捷方式，提高使用效率。
