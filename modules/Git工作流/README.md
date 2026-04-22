# Git 工作流与分支策略

Git 高级工作流、分支策略和 Git Hooks 完整参考文档。

## 目录

- [Git 分支管理](#git-分支管理)
- [Git Flow 工作流](#git-flow-工作流)
- [GitHub Flow 工作流](#github-flow-工作流)
- [Trunk-based Development](#trunk-based-development)
- [Git Hooks](#git-hooks)
- [Husky Git Hooks](#husky-git-hooks)
- [高级 Git 操作](#高级-git-操作)
- [Git 清理与维护](#git-清理与维护)

---

## Git 分支管理

### git branch - 分支操作

**基础用法**:
```bash
git branch %{分支名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看所有分支 | `git branch -a` | 包括本地和远程分支 |
| 重命名当前分支 | `git branch -m %{新分支名}%` | 新分支名: 新分支名称 (例: feature/new) |
| 重命名指定分支 | `git branch -m %{旧分支名}% %{新分支名}%` | 旧/新分支名: 原名 (例: old-name)，新名 (例: new-name) |
| 安全删除分支 | `git branch -d %{分支名}%` | 分支名: 分支名称 (例: feature-old)，只删除已合并分支 |
| 强制删除分支 | `git branch -D %{分支名}%` | 分支名: 分支名称 (例: feature-abandon)，强制删除 |
| 删除已合并分支 | `git branch --merged \| grep -v "main" \| xargs -r git branch -d` | 清理已合并到 main 的分支 |

### git checkout / git switch - 切换分支

**基础用法**:
```bash
git checkout %{分支名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建并切换 | `git checkout -b %{新分支名}%` | 新分支名: 新分支名称 (例: feature/new) |
| 使用 switch 创建并切换 | `git switch -c %{新分支名}%` | 新分支名: 新分支名称 (例: feature/login) |
| 切换到上一个分支 | `git checkout -` | 快速切换到上一分支 |
| 强制切换覆盖修改 | `git switch --discard-changes %{分支名}%` | 分支名: 分支名称 (例: main) |

### git merge - 合并分支

**基础用法**:
```bash
git merge %{分支名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 禁止快进合并 | `git merge --no-ff %{分支名}%` | 分支名: 分支名称 (例: feature/login)，保留分支历史 |
| no-ff 并指定提交信息 | `git merge --no-ff %{分支名}% -m "%{提交信息}%"` | 提交信息: 提交说明 (例: Merge feature) |
| squash 合并 | `git merge --squash %{分支名}%` | 分支名: 分支名称 (例: feature/login)，压缩所有提交 |
| 中止合并 | `git merge --abort` | 取消合并，回退到合并前状态 |
| 继续合并 | `git merge --continue` | 解决冲突后继续合并 |

### git rebase - 变基

**基础用法**:
```bash
git rebase %{分支名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 交互式变基 | `git rebase -i HEAD~%{数量}%` | 数量: 提交数量 (例: 3)，压缩、修改、删除提交 |
| 压缩最近 N 个提交 | `git rebase -i HEAD~%{数量}%` | 编辑器中改为 squash |
| 修改提交信息 | `git rebase -i HEAD~%{数量}%` | 编辑器中改为 reword |
| 删除某个提交 | `git rebase -i HEAD~%{数量}%` | 编辑器中删除对应行 |
| 中止变基 | `git rebase --abort` | 取消操作 |
| 继续变基 | `git rebase --continue` | 解决冲突后继续 |

---

## Git Flow 工作流

Git Flow 是一种成熟的分支管理模型，适用于有计划发布周期的项目。

### 分支类型

| 分支 | 用途 | 命名规则 |
|------|------|----------|
| main/master | 正式发布版本 | - |
| develop | 开发主分支 | - |
| feature/* | 功能分支 | feature/功能名 (例: feature/user-auth) |
| release/* | 发布分支 | release/版本号 (例: release/1.0.0) |
| hotfix/* | 热修复分支 | hotfix/问题描述 (例: hotfix/login-error) |

### 初始化 Git Flow

```bash
# 安装 git-flow (Linux/macOS)
apt-get install git-flow   # Debian/Ubuntu
brew install git-flow     # macOS

# Windows 通过 Scoop 或 Choco
scoop install git-flow

# 初始化
git flow init
```

### 功能开发流程

```bash
# 1. 开始功能分支
git flow feature start user-auth

# 2. 开发并提交
git add .
git commit -m "feat: add user authentication"

# 3. 发布功能分支
git flow feature publish user-auth

# 4. 完成功能并合并到 develop
git flow feature finish user-auth

# 5. 或指定分支完成
git flow feature finish -r user-auth   # 删除远程分支
```

### 发布流程

```bash
# 1. 从 develop 创建发布分支
git flow release start 1.0.0

# 2. 进行发布前最后修复
git commit -m "fix: release prep"

# 3. 完成发布
git flow release finish 1.0.0

# 4. 推送所有变更
git flow release finish -p 1.0.0
```

### 热修复流程

```bash
# 1. 从 main 创建热修复分支
git flow hotfix start login-error

# 2. 修复并提交
git add .
git commit -m "fix: resolve login error"

# 3. 完成热修复
git flow hotfix finish login-error

# 4. 推送到远程
git flow hotfix finish -p login-error

# 5. 打标签
git tag -a v1.0.1 -m "Hotfix for login error"
git push origin v1.0.1
```

---

## GitHub Flow 工作流

GitHub Flow 是一种轻量级分支策略，适合持续部署的项目。

### 核心规则

1. main 分支始终可部署
2. 所有变更在特性分支进行
3. 通过 Pull Request 合并
4. 合并后立即部署

### 工作流程

```bash
# 1. 从 main 创建特性分支
git checkout -b feature/add-login

# 2. 开发并提交
git add .
git commit -m "feat: add login functionality"

# 3. 推送分支
git push -u origin feature/add-login

# 4. 在 GitHub 创建 Pull Request

# 5. Code Review 后合并
# 6. 删除特性分支
git branch -d feature/add-login
```

### 修复分支

```bash
# 创建修复分支
git checkout -b fix/login-bug

# 修复并推送
git commit -m "fix: resolve login bug"
git push -u origin fix/login-bug
```

---

## Trunk-based Development

Trunk-based Development (TBD) 是一种高频集成的开发策略，所有开发者共享单一主线分支。

### 核心原则

- main/trunk 是唯一长期分支
- 特性开关控制功能发布
- 分支生命周期极短 (通常不超过 2 天)
- 频繁集成和部署

### 工作流程

```bash
# 1. 确保在 main 分支
git checkout main
git pull origin main

# 2. 创建短期特性分支
git checkout -b feature/user-auth

# 3. 频繁变基到 main
git rebase origin/main

# 4. 完成后合并
git checkout main
git merge --no-ff feature/user-auth
git push origin main

# 5. 删除特性分支
git branch -d feature/user-auth
```

### 团队协作

```bash
# 拉取最新代码
git fetch origin
git rebase origin/main

# 解决冲突后继续
git add %{冲突文件}%
git rebase --continue
```

---

## Git Hooks

Git Hooks 是在特定 Git 操作前后自动执行的脚本。

### 可用 Hooks

| Hook 名称 | 触发时机 | 用途 |
|-----------|----------|------|
| pre-commit | 提交前 | 运行测试、格式化代码 |
| prepare-commit-msg | 提交信息编辑前 | 修改提交信息模板 |
| commit-msg | 提交信息完成后 | 验证提交信息格式 |
| post-commit | 提交完成后 | 发送通知 |
| pre-push | 推送前 | 运行集成测试 |
| pre-rebase | 变基前 | 检查分支状态 |
| post-checkout | checkout 后 | 设置开发环境 |
| post-merge | 合并后 | 恢复文件权限 |

### 创建 pre-commit Hook

```bash
# 创建 pre-commit 脚本
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/sh
echo "Running pre-commit checks..."

# 运行 lint
npm run lint
if [ $? -ne 0 ]; then
  echo "Lint failed!"
  exit 1
fi

# 运行测试
npm run test
if [ $? -ne 0 ]; then
  echo "Tests failed!"
  exit 1
fi

echo "All checks passed!"
exit 0
EOF

chmod +x .git/hooks/pre-commit
```

### 创建 post-commit Hook

```bash
cat > .git/hooks/post-commit << 'EOF'
#!/bin/sh
echo "Commit completed: $(git log -1 --oneline)"
EOF

chmod +x .git/hooks/post-commit
```

### 管理 Hooks 路径

```bash
# 设置自定义 Hooks 目录
git config core.hooksPath ./hooks

# 验证设置
git config core.hooksPath

# 禁用所有 Hooks
git commit --no-verify -m "Skip hooks"
```

---

## Husky Git Hooks

Husky 是现代 Git Hooks 管理工具，与 npm 项目无缝集成。

### 安装与初始化

```bash
# 安装 Husky
npm install -D husky

# 初始化
npx husky install

# 自动启用 prepare 脚本
npm pkg set scripts.prepare="husky install"
```

### 添加 Hooks

```bash
# 添加 pre-commit
npx husky add .husky/pre-commit "npm run lint"
npx husky add .husky/pre-commit "npm run test"

# 添加 commit-msg
npx husky add .husky/commit-msg "npx commitlint --edit"

# 添加 pre-push
npx husky add .husky/pre-push "npm run build"
```

### 常见配置

**commitlint 配置 (.commitlintrc.json)**:
```json
{
  "extends": ["@commitlint/config-conventional"],
  "rules": {
    "type-enum": [2, "always", ["feat", "fix", "docs", "style", "refactor", "test", "chore"]]
  }
}
```

**lint-staged 配置 (.lintstagedrc)**:
```json
{
  "*.{js,jsx,ts,tsx}": ["eslint --fix", "prettier --write"],
  "*.{css,scss}": ["stylelint --fix", "prettier --write"],
  "*.md": ["prettier --write"]
}
```

### 卸载 Husky

```bash
npm uninstall husky
rm -rf .husky
```

---

## 高级 Git 操作

### git stash - 暂存变更

**基础用法**:
```bash
git stash
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看暂存列表 | `git stash list` | 显示所有暂存 |
| 应用并删除最近暂存 | `git stash pop` | 应用最近暂存并删除 |
| 应用但保留暂存 | `git stash apply` | 应用最近暂存保留 |
| 应用指定暂存 | `git stash apply stash@{0}` | 应用 stash@{0} |
| 创建带名称暂存 | `git stash push -m "%{暂存消息}%"` | 暂存消息: 暂存说明 (例: 临时保存登录功能) |
| 暂存未跟踪文件 | `git stash -u` | 包含未跟踪文件 |
| 查看暂存内容 | `git stash show -p` | 显示差异 |
| 删除指定暂存 | `git stash drop stash@{0}` | 删除 stash@{0} |
| 清空所有暂存 | `git stash clear` | 全部删除 |

### git cherry-pick - 拣选提交

**基础用法**:
```bash
git cherry-pick %{提交SHA}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 拣选不自动提交 | `git cherry-pick --no-commit %{提交SHA}%` | 提交SHA: 提交哈希值 (例: a1b2c3d)，手动提交 |
| 拣选多个提交 | `git cherry-pick %{提交1}% %{提交2}%` | 提交1: 第一个哈希 (例: a1b2c3d)；提交2: 第二个哈希 (例: e4f5g6h) |
| 拣选范围 | `git cherry-pick %{起始SHA}%..%{结束SHA}%` | 起始SHA: 起始哈希 (例: a1b2c3d)；结束SHA: 结束哈希 (例: e4f5g6h) |
| 继续拣选 | `git cherry-pick --continue` | 解决冲突后继续 |
| 中止拣选 | `git cherry-pick --abort` | 取消操作 |

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
git bisect good v1.0.0

# 4. 测试并标记
git bisect good  # 或 git bisect bad

# 5. 重复测试直到找到问题提交

# 6. 自动二分查找
git bisect start HEAD v1.0.0
git bisect run npm test

# 7. 找到问题提交后结束
git bisect reset
```

### git reflog - 引用日志

**基础用法**:
```bash
git reflog
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 显示最近 N 条 | `git reflog -n %{数量}%` | 数量: 显示条数 (例: 20) |
| 恢复误删分支 | `git reflog \| grep feature/login` | 查找分支引用 |
| | `git branch feature/login HEAD@{5}` | 恢复到指定状态 |
| 恢复误重置 | `git reflog \| head -20` | 查找操作记录 |
| | `git reset --hard HEAD@{3}` | 恢复到指定状态 |
| 显示分支日志 | `git reflog show %{分支名}%` | 分支名: 分支名称 (例: main) |

---

## Git 清理与维护

### git remote prune - 修剪远程分支引用

```bash
# 预览将要删除的分支引用
git remote prune origin --dry-run

# 修剪已删除的远程分支引用
git remote prune origin

# fetch 并 prune
git fetch --prune origin
```

### git gc - 垃圾回收

```bash
# 基本垃圾回收
git gc

# 立即清理
git gc --prune=now

# Aggressive 压缩 (更彻底但更慢)
git gc --aggressive

# 自动压缩 (根据仓库状态)
git gc --auto

# 显示详细统计
git gc --verbose
```

### git prune - 修剪悬空对象

```bash
# 预览修剪操作
git prune --dry-run

# 显示详细输出
git prune --verbose

# 修剪过期对象
git prune --expire 2.weeks.ago

# 完整清理 (通常由 git gc 调用)
git prune && git gc --prune=now
```

---

## 实用场景示例

### 场景 1: Git Flow 完整功能开发

```bash
# 1. 开始功能
git flow feature start user-auth

# 2. 开发
git add .
git commit -m "feat: add user authentication"

# 3. 发布
git flow feature publish user-auth

# 4. 在 GitHub 创建 PR

# 5. 合并后完成功能
git flow feature finish user-auth

# 6. 推送到远程
git push origin develop
```

### 场景 2: 紧急热修复

```bash
# 1. 创建热修复分支
git flow hotfix start login-error

# 2. 修复问题
git add .
git commit -m "fix: resolve login error"

# 3. 完成热修复
git flow hotfix finish login-error

# 4. 推送标签
git push origin v1.0.1 --tags
```

### 场景 3: 使用 Husky 自动化检查

```bash
# 1. 安装
npm install -D husky @commitlint/cli @commitlint/config-conventional

# 2. 初始化
npx husky install
npm pkg set scripts.prepare="husky install"

# 3. 配置 commitlint
echo 'module.exports = { extends: ["@commitlint/config-conventional"] };' > .commitlintrc.js

# 4. 添加 commit-msg hook
npx husky add .husky/commit-msg "npx commitlint --edit"

# 5. 添加 pre-commit hook
npx husky add .husky/pre-commit "npm run lint && npm run test"
```

### 场景 4: 恢复误操作

```bash
# 1. 查看操作历史
git reflog -n 20

# 2. 恢复分支
git branch feature/login HEAD@{5}

# 3. 恢复重置
git reset --hard HEAD@{3}

# 4. 恢复误删除的提交
git checkout -b recovery HEAD@{7}
```

### 场景 5: 分支对比与同步

```bash
# 查看分支差异
git log main..develop --oneline

# 查看两分支差异的文件
git log --name-only main..feature/login

# 同步主分支
git fetch origin
git rebase origin/main

# 强制覆盖远程
git push --force-with-lease origin feature/login
```

---

## 分支策略对比

| 策略 | 适用场景 | 优点 | 缺点 |
|------|----------|------|------|
| Git Flow | 计划发布周期 | 结构清晰，适合大型项目 | 流程较重 |
| GitHub Flow | 持续部署 | 简单快速 | 不适合多版本并行 |
| Trunk-based | 高频迭代 | 集成频繁，减少冲突 | 需要特性开关支持 |
| Forking | 开源协作 | 安全隔离 | 操作复杂 |

---

## 相关资源

- [Git 命令文档](../Git 命令/README.md)
- [GitHub CLI 命令文档](../GitHub CLI 命令/README.md)
- [GitHub Actions 文档](../GitHubActions/README.md)
