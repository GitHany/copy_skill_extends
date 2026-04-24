# Git 命令文档

Git 版本控制完整参考文档。

## 📚 目录

- [基础操作](#基础操作)
- [分支管理](#分支管理)
- [远程操作](#远程操作)
- [高级用法](#高级用法)

---

## 基础操作

### git init - 初始化仓库

**基础用法**:
```bash
git init
```

### git clone - 克隆仓库

**基础用法**:
```bash
git clone %{仓库URL}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 克隆指定分支 | `git clone -b %{分支名}% %{URL}%` | 分支名: 分支名称 (例: develop)；URL: 仓库地址 (例: https://github.com/user/repo.git) |
| 浅克隆 | `git clone --depth 1 %{URL}%` | URL: 仓库地址，只克隆最新提交 (例: https://github.com/user/repo.git) |
| 克隆到指定目录 | `git clone %{URL}% %{目录}%` | URL: 仓库地址 (例: https://github.com/user/repo.git)；目录: 本地路径 (例: ./myproject) |
| 初始化为裸仓库 | `git init --bare` | 创建无工作区的仓库，用于服务器 |
| 初始化并指定分支 | `git init -b %{分支名}%` | 分支名: 初始分支名称 (例: main) |

### git status - 查看状态

**基础用法**:
```bash
git status
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 简短输出 | `git status -s` | 简洁格式输出 |
| 显示分支 | `git status -b` | 显示分支信息 |
| 忽略子模块 | `git status --ignore-submodules` | 忽略子模块变更 |

### git add - 添加文件到暂存区

**基础用法**:
```bash
git add %{文件}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 添加所有文件 | `git add .` | 添加所有变更 |
| 交互式添加 | `git add -p` | 逐块选择添加 |
| 添加已跟踪的 | `git add -u` | 只添加已跟踪文件 |
| 强制添加忽略文件 | `git add -f %{文件}%` | 文件: 文件路径 (例: src/index.js) |

### git commit - 提交变更

**基础用法**:
```bash
git commit -m "%{提交信息}%"
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 添加并提交 | `git commit -am "%{提交信息}%"` | 提交信息: 提交说明 (例: 修复登录bug)【常用】 |
| 修改上次提交 | `git commit --amend` | 修改最近提交信息或添加遗漏文件 |
| 交互式提交 | `git commit -p` | 逐块选择提交 |
| 跳过 Hooks | `git commit --no-verify` | 跳过 pre-commit 钩子 |
| 签名提交 | `git commit -S` | GPG 签名提交 |

### git log - 查看提交历史

**基础用法**:
```bash
git log
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 单行显示 | `git log --oneline` | 简洁格式 |
| 图形化显示 | `git log --graph --oneline --all` | 分支图 |
| 最近 N 条 | `git log -n %{数量}%` | 数量: 显示条数 (例: 10) |
| 按作者过滤 | `git log --author="%{作者}%"` | 作者: 作者名称或邮箱 (例: zhangsan) |
| 按日期过滤 | `git log --after="%{开始日期}%" --before="%{结束日期}%"` | 开始日期: 起始日期 (例: 2024-01-01)；结束日期: 截止日期 (例: 2024-12-31) |
| 显示变更文件 | `git log --stat` | 显示文件统计 |
| 查看具体内容 | `git log -p` | 显示 diff |
| 搜索提交信息 | `git log --grep="%{关键词}%"` | 关键词: 搜索词 (例: fix) |
| 显示文件历史 | `git log --follow %{文件名}%` | 文件名: 文件路径 (例: src/app.js) |

### git diff - 查看差异

**基础用法**:
```bash
git diff
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 暂存区差异 | `git diff --staged` | 已 add 的差异 |
| 两个分支差异 | `git diff %{分支1}% %{分支2}%` | 分支1/2: 分支名称 (例: main, develop) |
| 单个文件差异 | `git diff %{文件名}%` | 文件名: 文件路径 (例: src/app.js) |
| 统计变更 | `git diff --stat` | 变更统计 |
| 提交间差异 | `git diff %{提交1}% %{提交2}%` | 提交1/2: 提交引用 (例: HEAD~1, HEAD) |
| 忽略空白差异 | `git diff -w` | 忽略空白字符差异 |

---

## 分支管理

### git branch - 分支操作

**基础用法**:
```bash
git branch %{分支名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看分支列表 | `git branch -a` | 包括远程分支 |
| 删除分支 | `git branch -d %{分支名}%` | 分支名: 分支名称 (例: feature-old)，删除已合并分支 |
| 强制删除 | `git branch -D %{分支名}%` | 分支名: 分支名称 (例: feature-abandon)，强制删除 |
| 重命名分支 | `git branch -m %{旧分支名}% %{新分支名}%` | 旧/新分支名: 原名 (例: old-name)，新名 (例: new-name) |
| 查看已合并分支 | `git branch --merged` | 列出已合并到当前分支的分支 |
| 查看未合并分支 | `git branch --no-merged` | 列出未合并到当前分支的分支 |

### git checkout - 切换分支

**基础用法**:
```bash
git checkout %{分支名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建并切换 | `git checkout -b %{新分支名}%` | 新分支名: 新分支名称 (例: feature/new)【常用】 |
| 切换回上一次 | `git checkout -` | 快速切换到上一分支 |
| 检出文件 | `git checkout %{文件名}%` | 文件名: 文件路径 (例: src/app.js)，恢复文件 |
| 切换到提交 | `git checkout %{提交SHA}%` | 提交SHA: 提交哈希值 (例: a1b2c3d)，分离头指针 |
| 强制检出 | `git checkout --force %{分支名}%` | 分支名: 分支名称 (例: main)，覆盖本地修改 |

### git switch - 切换分支（新版）

**基础用法**:
```bash
git switch %{分支名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建并切换 | `git switch -c %{新分支名}%` | 新分支名: 新分支名称 (例: feature/login)【常用】 |
| 切换远程分支 | `git switch %{远程分支名}%` | 远程分支名: 远程分支 (例: origin/main) |
| 强制切换 | `git switch --discard-changes %{分支名}%` | 分支名: 分支名称 (例: main)，覆盖本地修改 |

### git merge - 合并分支

**基础用法**:
```bash
git merge %{分支名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 中止合并 | `git merge --abort` | 取消合并，回退到合并前状态 |
| 合并不提交 | `git merge --no-commit %{分支名}%` | 分支名: 分支名称 (例: feature/login)，手动确认 |
| squash 合并 | `git merge --squash %{分支名}%` | 分支名: 分支名称 (例: feature/login)，压缩提交 |
| 使用 rebase | `git rebase %{分支名}%` | 变基合并到目标分支 |
| 继续合并 | `git merge --continue` | 解决冲突后继续合并 |

### git tag - 标签管理

**基础用法**:
```bash
git tag %{标签名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建带注释标签 | `git tag -a %{标签名}% -m "%{说明}%"` | 标签名: 标签名称 (例: v1.0.0)；说明: 标签说明 (例: 正式发布版本) |
| 查看标签列表 | `git tag -l` | 列出所有标签 |
| 查看标签详情 | `git tag -d %{标签名}%` | 标签名: 标签名称 (例: v1.0.0) |
| 推送标签 | `git push origin %{标签名}%` | 标签名: 标签名称 (例: v1.0.0) |
| 推送所有标签 | `git push origin --tags` | 批量推送所有标签 |
| 删除标签 | `git tag -d %{标签名}%` | 标签名: 标签名称 (例: v1.0.0)，本地删除 |
| 删除远程标签 | `git push origin --delete tag/%{标签名}%` | 标签名: 标签名称 (例: v1.0.0) |
| 给历史提交打标签 | `git tag -a %{标签名}% %{提交SHA}% -m "%{说明}%"` | 标签名: 标签名 (例: v0.9.0)；提交SHA: 哈希值 (例: a1b2c3d)；说明: 说明 (例: 历史版本) |

---

## 远程操作

### git remote - 远程仓库管理

**基础用法**:
```bash
git remote -v
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 添加远程 | `git remote add %{远程名}% %{URL}%` | 远程名: 远程名称 (例: origin)【常用】；URL: 仓库地址 (例: https://github.com/user/repo.git)【常用】 |
| 修改远程 | `git remote set-url %{远程名}% %{新URL}%` | 远程名: 远程名称 (例: origin)【常用】；新URL: 新仓库地址 (例: https://github.com/user/repo.git) |
| 删除远程 | `git remote remove %{远程名}%` | 远程名: 远程名称 (例: origin) |
| 重命名远程 | `git remote rename %{旧名}% %{新名}%` | 旧名: 原远程名 (例: origin)；新名: 新远程名 (例: upstream) |
| 查看远程信息 | `git remote show %{远程名}%` | 远程名: 远程名称 (例: origin) |

### git fetch - 获取远程更新

**基础用法**:
```bash
git fetch origin
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 获取并修剪 | `git fetch --prune` | 清理已删除的远程分支 |
| 获取所有远程 | `git fetch --all` | 更新所有远程 |
| 获取指定远程 | `git fetch %{远程名}%` | 远程名: 远程仓库名称 (例: origin)【常用】 |

### git pull - 拉取并合并

**基础用法**:
```bash
git pull origin %{分支名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 拉取并 rebase | `git pull --rebase origin %{分支名}%` | 分支名: 分支名称 (例: main)，使用变基替代合并 |
| 仅拉取不合并 | `git fetch origin` | 只获取不合并 |
| 拉取所有远程 | `git pull --all` | 更新所有远程分支 |

### git push - 推送变更

**基础用法**:
```bash
git push origin %{分支名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 设置上游分支 | `git push -u origin %{分支名}%` | 分支名: 分支名称 (例: main)【常用】，首次推送 |
| 强制推送 | `git push --force-with-lease` | 安全强制推送，避免覆盖他人提交 |
| 推送所有分支 | `git push --all` | 推送全部分支 |
| 推送标签 | `git push --tags` | 推送所有标签 |
| 删除远程分支 | `git push origin --delete %{分支名}%` | 分支名: 分支名称 (例: feature-old) |

---

## 高级用法

### git stash - 暂存变更

**基础用法**:
```bash
git stash
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看暂存列表 | `git stash list` | 显示所有暂存 |
| 应用暂存 | `git stash pop` | 应用最近暂存并删除【常用】 |
| 应用但保留 | `git stash apply` | 应用最近暂存保留 |
| 应用指定暂存 | `git stash apply %{暂存名}%` | 暂存名: 暂存名称 (例: stash@{0}) |
| 查看暂存内容 | `git stash show -p` | 显示差异 |
| 创建带名称暂存 | `git stash push -m "%{暂存消息}%"` | 暂存消息: 暂存说明 (例: 临时保存登录功能) |
| 暂存未跟踪文件 | `git stash -u` | 包含未跟踪文件 |
| 暂存所有文件 | `git stash -a` | 包含忽略文件 |
| 删除暂存 | `git stash drop %{暂存名}%` | 暂存名: 暂存名称 (例: stash@{0}) |
| 清空所有暂存 | `git stash clear` | 全部删除 |

### git reset - 重置

**基础用法**:
```bash
git reset --hard %{目标}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 软重置 | `git reset --soft %{目标}%` | 目标: 目标提交 (例: HEAD~1)，保留变更在暂存区 |
| 混合重置 | `git reset --mixed %{目标}%` | 目标: 目标提交 (例: HEAD~1)，保留变更在工作区 |
| 回退一次提交 | `git reset --soft HEAD~1` | 撤销提交，保留变更 |
| 重置单个文件 | `git reset HEAD %{文件名}%` | 文件名: 文件路径 (例: src/app.js)，取消暂存 |
| 仅重置暂存区 | `git reset HEAD` | 取消所有暂存 |

### git revert - 撤销提交

**基础用法**:
```bash
git revert %{提交SHA}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 撤销不自动提交 | `git revert --no-commit %{提交SHA}%` | 提交SHA: 提交哈希值 (例: a1b2c3d)，手动提交 |
| 撤销多个提交 | `git revert %{提交1}% %{提交2}%` | 提交1: 第一个哈希 (例: a1b2c3d)；提交2: 第二个哈希 (例: e4f5g6h) |
| 撤销范围提交 | `git revert %{起始SHA}%..%{结束SHA}%` | 起始SHA: 起始哈希 (例: a1b2c3d)；结束SHA: 结束哈希 (例: e4f5g6h) |
| 继续 revert | `git revert --continue` | 解决冲突后继续 |
| 中止 revert | `git revert --abort` | 取消操作 |

### git cherry-pick - 拣选提交

**基础用法**:
```bash
git cherry-pick %{提交SHA}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 拣选多个提交 | `git cherry-pick %{提交1}% %{提交2}%` | 提交1: 第一个哈希 (例: a1b2c3d)；提交2: 第二个哈希 (例: e4f5g6h) |
| 拣选范围 | `git cherry-pick %{起始SHA}%..%{结束SHA}%` | 起始SHA: 起始哈希 (例: a1b2c3d)；结束SHA: 结束哈希 (例: e4f5g6h) |
| 拣选不自动提交 | `git cherry-pick --no-commit %{提交SHA}%` | 提交SHA: 提交哈希值 (例: a1b2c3d)，手动提交 |
| 继续拣选 | `git cherry-pick --continue` | 解决冲突后继续 |
| 中止拣选 | `git cherry-pick --abort` | 取消操作 |

### git reflog - 操作日志

**基础用法**:
```bash
git reflog
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 显示最近 N 条 | `git reflog -n %{数量}%` | 数量: 显示条数 (例: 20) |
| 显示指定分支日志 | `git reflog show %{分支名}%` | 分支名: 分支名称 (例: main) |

### git bisect - 二分查找

**基础用法**:
```bash
git bisect start
```

**完整流程**:

```bash
# 1. 开始二分查找
git bisect start

# 2. 标记当前为坏
git bisect bad

# 3. 标记已知好版本
git bisect good %{好版本SHA}%

# 4. 测试并标记
git bisect good  # 或 bad

# 5. 找到问题提交后结束
git bisect reset
```

---

## 💡 实用场景示例

### 场景 1: 功能开发工作流

```bash
# 1. 创建功能分支
git checkout -b feature/user-auth

# 2. 开发并提交
git add .
git commit -m "feat: add user authentication"

# 3. 同步主分支变更
git fetch origin
git rebase origin/main

# 4. 推送到远程
git push -u origin feature/user-auth

# 5. 创建 Pull Request (在 GitHub/GitLab 上)

# 6. 合并后删除本地分支
git checkout main
git branch -d feature/user-auth
```

### 场景 2: 紧急 Bug 修复

```bash
# 1. 从 main 创建热修复分支
git checkout -b hotfix/login-error main

# 2. 修复并提交
git add .
git commit -m "fix: resolve login error"

# 3. 推送到远程
git push -u origin hotfix/login-error

# 4. 合并到 main 和 develop
git checkout main
git merge hotfix/login-error
git push origin main

git checkout develop
git merge hotfix/login-error
git push origin develop

# 5. 打标签
git tag -a v1.0.1 -m "Hotfix for login error"
git push origin v1.0.1
```

### 场景 3: 解决冲突

```bash
# 1. 拉取最新代码
git pull origin main

# 2. 如果有冲突，查看冲突文件
git status

# 3. 手动编辑冲突文件
# 查找 <<<<<<<, =======, >>>>>>> 标记

# 4. 解决后标记为已解决
git add %{冲突文件}%

# 5. 完成合并
git commit

# 或使用 rebase
git pull --rebase origin main
# 解决冲突后
git add %{冲突文件}%
git rebase --continue
```

### 场景 4: 撤销错误操作

```bash
# 撤销最后一次提交（保留变更）
git reset --soft HEAD~1

# 撤销最后一次提交（删除变更）
git reset --hard HEAD~1

# 恢复已删除的分支
git branch %{分支名}% %{提交SHA}%

# 恢复已删除的文件
git checkout HEAD~1 -- %{文件}%

# 查看操作历史找回提交
git reflog
```

### 场景 5: 清理仓库

```bash
# 删除已合并的分支
git branch --merged | grep -v "main" | xargs git branch -d

# 清理未跟踪文件
git clean -n        # 预览
git clean -f        # 执行删除
git clean -fd       # 包括目录

# 修剪远程分支引用
git remote prune origin

# 垃圾回收
git gc --prune=now
```

---

## 📊 提交信息规范

### Conventional Commits

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type 类型

| 类型 | 说明 | 示例 |
|------|------|------|
| `feat` | 新功能 | `feat: add user login` |
| `fix` | 修复 Bug | `fix: resolve null pointer` |
| `docs` | 文档变更 | `docs: update README` |
| `style` | 代码格式 | `style: format code` |
| `refactor` | 重构 | `refactor: simplify logic` |
| `test` | 测试相关 | `test: add unit tests` |
| `chore` | 构建/工具 | `chore: update dependencies` |
| `perf` | 性能优化 | `perf: improve query speed` |
| `ci` | CI/CD 变更 | `ci: add GitHub Actions` |

---

## 🔗 相关资源

- [快速开始指南](../quick-start.md)
- [Linux 命令文档](../linux-commands/README.md)
- [完整命令参考表](../../references/commands-reference.md)
