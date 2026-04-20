# 完整命令参考表

基于 `commands.json` 的完整命令索引。

## 📊 命令统计

| 分类 | 命令数量 | 文档链接 |
|------|----------|----------|
| Claude Skills | 30+ | [查看](../claude-skills/README.md) |
| 软件工程提示词 | 15+ | [查看](../software-engineering/README.md) |
| Linux 命令 | 40+ | [查看](../linux-commands/README.md) |
| Docker 命令 | 25+ | [查看](../docker-commands/README.md) |
| Git 命令 | 15+ | [查看](../git-commands/README.md) |
| 工作流 | 10+ | [查看](../workflows/README.md) |

---

## 🔍 按关键词搜索

### AI 与机器学习

| 关键词 | 命令 | 说明 |
|--------|------|------|
| RAG | `/speckit-specify` | 编写 RAG 需求规格 |
| 模型部署 | `/ecc:plan` | 规划模型部署方案 |
| Prompt | `/brainstorming` | 头脑风暴 Prompt 设计 |

### 系统架构

| 关键词 | 命令 | 说明 |
|--------|------|------|
| 微服务 | `/opsx:propose` | 提出微服务架构方案 |
| API 设计 | `/speckit-plan` | 制定 API 开发计划 |
| 数据库 | `/speckit-implement` | 实施数据库方案 |

### 前端开发

| 关键词 | 命令 | 说明 |
|--------|------|------|
| React | `/tdd` | 测试驱动开发 React 组件 |
| 性能优化 | `/code-review` | 代码审查性能问题 |
| 组件设计 | `/ecc:plan` | 规划组件架构 |

### 项目管理

| 关键词 | 命令 | 说明 |
|--------|------|------|
| PRD | `/speckit-specify` | 编写产品需求文档 |
| 路线图 | `/opsx:propose` | 提出路线图变更 |
| Sprint | `/speckit-tasks` | 分解 Sprint 任务 |

### 测试

| 关键词 | 命令 | 说明 |
|--------|------|------|
| 单元测试 | `/tdd` | 测试驱动开发 |
| 集成测试 | `/ecc:e2e` | 端到端测试 |
| 性能测试 | `/verify` | 验证循环 |

### 部署运维

| 关键词 | 命令 | 说明 |
|--------|------|------|
| Docker | `docker run` | 运行容器 |
| K8s | `docker-compose up` | 启动服务 |
| CI/CD | `/verify` | 验证部署 |

---

## 📋 完整命令列表

### Claude Skills - Oh-My-Claude

| 名称 | 命令 | 扩展 |
|------|------|------|
| 1-00 安装 | `/plugin marketplace add ...` | 3 |
| 1-01 autopilot | `/oh-my-claudecode:autopilot %{任务}%` | 3 |
| 1-01-1 验证修复 | `/oh-my-claudecode:autopilot 验证...` | 0 |
| 1-01-2 性能优化 | `/oh-my-claudecode:autopilot 优化...` | 0 |
| 1-02 deep-interview | `/oh-my-claudecode:deep-interview %{想法}%` | 2 |
| 1-03 ralph | `/oh-my-claudecode:ralph %{任务}%` | 2 |
| 1-04 ralplan | `/oh-my-claudecode:ralplan %{任务}%` | 2 |
| 1-05 team | `/oh-my-claudecode:team 3:executor %{任务}%` | 2 |

### Claude Skills - Superpowers

| 名称 | 命令 | 扩展 |
|------|------|------|
| 1-00 安装 | `/plugin marketplace add obra/...` | 0 |
| 1-01 brainstorming | `/brainstorming %{需求}%` | 2 |
| 1-02 git-worktrees | `/superpowers:using-git-worktrees` | 3 |
| 1-03 writing-plans | `/superpowers:writing-plans` | 2 |
| 1-04 subagent-driven | `/superpowers:subagent-driven-development` | 0 |
| 1-05 tdd | `/superpowers:test-driven-development` | 2 |
| 1-06 code-review | `/superpowers:requesting-code-review` | 2 |
| 1-07 finishing | `/superpowers:finishing-a-development-branch` | 0 |

### Claude Skills - Everything Claude Code

| 名称 | 命令 | 扩展 |
|------|------|------|
| 1-00 安装 | `/plugin marketplace add affaan-m/...` | 0 |
| 1-01 plan | `/ecc:plan %{需求}%` | 2 |
| 1-03 tdd | `/tdd use context7` | 0 |
| 1-04 code-review | `/code-review` | 2 |
| 1-05 build-fix | `/ecc:build-fix` | 2 |
| 1-06 security-scan | `/security-scan` | 2 |
| 1-07 e2e | `/ecc:e2e` | 0 |
| 1-08 test-coverage | `/test-coverage` | 2 |
| 1-09 verify | `/verify` | 0 |
| 1-10 update-docs | `/update-docs` | 2 |

### Claude Skills - OpenSpec

| 名称 | 命令 | 扩展 |
|------|------|------|
| 1-01 init | `openspec init` | 0 |
| 1-02 propose | `/opsx:propose %{任务}%` | 2 |
| 1-03 apply | `/opsx:apply use context7` | 0 |
| 1-04 archive | `/opsx:archive` | 0 |
| 1-05 explore | `/opsx:explore %{任务}%` | 1 |

### Claude Skills - Spec-Kit

| 名称 | 命令 | 扩展 |
|------|------|------|
| 1-01 specify init | `specify init --here --ai claude` | 0 |
| 1-02 constitution | `/speckit-constitution %{规则}%` | 0 |
| 1-03 specify | `/speckit-specify %{Spec}%` | 2 |
| 1-03-1 specify 完善 | `/speckit-specify 请对当前方案...` | 0 |
| 1-03-2 clarify | `/speckit-clarify` | 0 |
| 1-04 plan | `/speckit-plan` | 0 |
| 1-05 tasks | `/speckit-tasks` | 0 |
| 1-06 implement | `/speckit-implement use context7` | 0 |
| 1-06-1 analyze | `/speckit-analyze` | 0 |

### 软件工程提示词

| 角色 | 命令 | 扩展 |
|------|------|------|
| AI 工程师 | `你是一名AI工程师...` | 3 |
| 后端架构师 | `你是一名资深后端架构师...` | 3 |
| 前端开发者 | `你是一名前端开发专家...` | 3 |
| 软件架构师 | `你是一名软件架构师...` | 3 |
| 产品经理 | `你是一名产品经理...` | 3 |
| 项目经理 | `你是一名高级项目经理...` | 2 |
| API 测试员 | `你是一名API测试专家...` | 3 |
| 内容创作者 | `你是一名内容创作者...` | 2 |
| DevOps 工程师 | `你是一名DevOps工程师...` | 3 |
| DBA | `你是一名数据库管理员...` | 3 |
| 安全工程师 | `你是一名安全工程师...` | 2 |
| 技术文档 | `你是一名技术文档工程师...` | 2 |

### Linux 命令

| 名称 | 命令 | 扩展 |
|------|------|------|
| grep | `grep "%{内容}%" %{文件}%` | 8 |
| find | `find %{目录}% -name "%{文件}%"` | 5 |
| cp | `cp -r %{源}% %{目标}%/` | 3 |
| mv | `mv %{源}% %{目标}%/` | 2 |
| tar | `tar -czvf %{名称}%.tar.gz %{目录}%` | 3 |
| rsync | `rsync -ah --progress %{源}% %{目标}%/` | 3 |
| mkdir | `mkdir -p %{路径}%` | 2 |
| head | `head -n %{行数}% %{文件}%` | 1 |
| tail | `tail -f %{文件}%` | 2 |
| df | `df -h` | 2 |
| du | `du -sh %{目录}%` | 2 |
| htop | `htop` | 2 |
| ifconfig | `ifconfig` | 3 |
| uname | `uname -a` | 2 |
| ls | `ls -la` | 3 |
| cd | `cd %{路径}%` | 2 |
| pip install | `pip install %{库}%` | 5 |

### Docker 命令

| 名称 | 命令 | 扩展 |
|------|------|------|
| docker run | `docker run -d --name %{名称}% ...` | 4 |
| docker ps | `docker ps` | 3 |
| docker stop | `docker stop %{容器}%` | 3 |
| docker rm | `docker rm %{容器}%` | 3 |
| docker logs | `docker logs %{容器}%` | 3 |
| docker exec | `docker exec -it %{容器}% /bin/bash` | 2 |
| docker pull | `docker pull %{镜像}%:%{标签}%` | 2 |
| docker images | `docker images` | 3 |
| docker rmi | `docker rmi %{镜像}%` | 2 |
| docker build | `docker build -t %{镜像}%:%{标签}% %{路径}%` | 3 |
| docker push | `docker push %{镜像}%:%{标签}%` | 0 |
| docker-compose up | `docker-compose up -d` | 3 |
| docker-compose down | `docker-compose down` | 3 |
| docker-compose ps | `docker-compose ps` | 0 |
| docker-compose logs | `docker-compose logs -f %{服务}%` | 2 |
| docker-compose build | `docker-compose build` | 2 |
| docker network | `docker network create %{名称}%` | 3 |
| docker volume | `docker volume create %{名称}%` | 3 |
| docker inspect | `docker inspect %{容器}%` | 2 |
| docker stats | `docker stats` | 2 |
| docker cp | `docker cp %{源}% %{容器}%:%{目标}%` | 1 |

### Git 命令

| 名称 | 命令 | 扩展 |
|------|------|------|
| git pull | `git pull origin %{分支}%` | 2 |
| git reset | `git reset --hard %{修订}%` | 3 |
| git merge | `git merge %{分支}%` | 3 |
| git rev-parse | `git rev-parse HEAD` | 0 |
| git merge --abort | `git merge --abort` | 0 |

### 工作流

| 名称 | 命令 | 说明 |
|------|------|------|
| GSD 步骤 | `Goal → Steps → Do` | 目标-步骤-执行 |
| GSD 实施决策 | `GSD Discuss Phase` | 回顾与决策 |
| GSD 状态 | `Status: Not Started...` | 状态管理 |
| GSD workteams | `GSD Workteams` | 团队协作 |
| GSD worktree | `git worktree add ...` | Git 集成 |
| GSD 会话 | `GSD 会话管理` | 上下文管理 |
| GSD 阶段 | `Phase 1-5` | 分阶段管理 |

---

## 🎯 按场景使用

### 场景 1: 新项目启动

```bash
# 1. 明确需求
/oh-my-claudecode:deep-interview %{想法}%

# 2. 规划方案
/ecc:plan %{需求}%

# 3. 初始化项目
git init
specify init --here --ai claude

# 4. 定义规则
/speckit-constitution %{项目规则}%

# 5. 编写需求
/speckit-specify %{需求 Spec}%

# 6. 分解任务
/speckit-tasks

# 7. 开始开发
/speckit-implement
```

### 场景 2: 功能开发

```bash
# 1. 创建分支
git checkout -b feature/%{功能}%

# 2. 测试驱动开发
/superpowers:test-driven-development

# 3. 编写代码
# ... 开发 ...

# 4. 代码审查
/code-review

# 5. 提交
git add .
git commit -m "feat: %{功能}%"
git push origin feature/%{功能}%
```

### 场景 3: Docker 部署

```bash
# 1. 构建镜像
docker build -t %{应用}%:%{版本}% .

# 2. 运行容器
docker run -d --name %{名称}% -p %{端口}%:80 %{应用}%:%{版本}%

# 3. 查看日志
docker logs -f %{名称}%

# 4. 进入容器
docker exec -it %{名称}% /bin/bash
```

### 场景 4: 问题排查

```bash
# 1. 查看系统状态
htop
df -h
free -h

# 2. 查看日志
docker logs -f %{容器}%
tail -f /var/log/app.log

# 3. 搜索错误
grep -r "ERROR" /var/log/
docker logs %{容器}% | grep -i "error"

# 4. 网络排查
ping %{主机}%
curl -I %{URL}%
```

### 场景 5: 发布上线

```bash
# 1. 验证代码
/verify
/test-coverage

# 2. 构建发布版本
docker build -t %{应用}:%{版本}% .

# 3. 推送镜像
docker push %{应用}:%{版本}%

# 4. 部署
docker-compose up -d

# 5. 更新文档
/update-docs
```

---

## 📖 命令模板说明

### 变量格式

命令中使用 `%{变量}%` 格式表示可替换的参数：

```bash
# 模板
docker run -d --name %{容器名称}% -p %{端口}%:80 %{镜像}%

# 替换后
docker run -d --name myapp -p 8080:80 myapp:v1.0
```

### 扩展命令

每个主命令都有相关扩展命令，提供更多使用场景：

```bash
# 主命令
grep "error" file.log

# 扩展命令
grep -r "error" /var/log/      # 递归搜索
grep -i "error" file.log       # 忽略大小写
grep -n "error" file.log       # 显示行号
```

---

## 🔗 相关资源

- [快速开始指南](../quick-start.md)
- [Claude Skills 文档](../claude-skills/README.md)
- [软件工程提示词](../software-engineering/README.md)
- [Linux 命令文档](../linux-commands/README.md)
- [Docker 命令文档](../docker-commands/README.md)
- [Git 命令文档](../git-commands/README.md)
