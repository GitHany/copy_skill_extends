# GitHub CLI 命令文档

GitHub CLI (gh) 完整参考文档。

## 目录

- [仓库操作](#仓库操作)
- [Issue 管理](#issue-管理)
- [Pull Request 管理](#pull-request-管理)
- [Actions](#actions)
- [GitHub API](#github-api)

---

## 仓库操作

### gh repo clone - 克隆仓库

**基础用法**:
```bash
gh repo clone %{owner}/{repo}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 克隆到指定目录 | `gh repo clone {owner}/{repo} {directory}` | **directory**: 目标目录路径, 示例: `~/projects/myrepo` |
| 指定所有者 | `gh repo clone {owner}/{repo}` | **owner**: 仓库所有者, 示例: `octocat`; **repo**: 仓库名称, 示例: `hello-world` |

### gh repo create - 创建仓库

**基础用法**:
```bash
gh repo create %{name}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建私有仓库 | `gh repo create %{name}% --private` | **name**: 仓库名称, 示例: `my-new-repo` |
| 创建公开仓库 | `gh repo create %{name}% --public` | **name**: 仓库名称, 示例: `my-new-repo` |
| 创建并推送本地代码 | `gh repo create %{name}% --push --source=.` | **name**: 仓库名称, 示例: `my-new-repo` |
| 创建并克隆 | `gh repo create %{name}% --clone` | **name**: 仓库名称, 示例: `my-new-repo` |

### gh repo fork - 派生仓库

**基础用法**:
```bash
gh repo fork %{owner}/{repo}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 派生并克隆到本地 | `gh repo fork {owner}/{repo} --clone` | **owner**: 仓库所有者, 示例: `github`; **repo**: 仓库名称, 示例: `hello-world` |
| 派生到指定组织 | `gh repo fork {owner}/{repo} --org {org}` | **org**: 目标组织名称, 示例: `my-org` |

### gh repo view - 查看仓库

**基础用法**:
```bash
gh repo view
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看指定仓库 | `gh repo view {owner}/{repo}` | **owner**: 仓库所有者, 示例: `octocat`; **repo**: 仓库名称, 示例: `hello-world` |
| 显示仓库 URL | `gh repo view --url` | 仅显示 URL |
| 显示仓库内容 | `gh repo view --files` | 查看仓库文件列表 |

### gh repo list - 列出仓库

**基础用法**:
```bash
gh repo list %{username}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 限制数量 | `gh repo list {username} --limit {number}` | **username**: GitHub 用户名, 示例: `octocat`; **number**: 返回数量上限, 示例: `10` |
| 列出组织仓库 | `gh repo list --org {org}` | **org**: 组织名称, 示例: `github` |
| 按类型筛选 | `gh repo list {username} --source` | 仅显示用户拥有的仓库 |

---

## Issue 管理

### gh issue list - 列出 Issue

**基础用法**:
```bash
gh issue list
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看指定仓库 | `gh issue list --repo {owner}/{repo}` | **owner**: 仓库所有者, 示例: `octocat`; **repo**: 仓库名称, 示例: `hello-world` |
| 按状态筛选 | `gh issue list --state {state}` | **state**: Issue 状态, 示例: `open` (可选: open/closed/all) |
| 按标签筛选 | `gh issue list --label {label}` | **label**: 标签名称, 示例: `bug` |
| 按作者筛选 | `gh issue list --author {author}` | **author**: 作者用户名, 示例: `octocat` |
| 按受理人筛选 | `gh issue list --assignee {assignee}` | **assignee**: 受理人用户名, 示例: `octocat` |
| 限制数量 | `gh issue list --limit {number}` | **number**: 返回数量上限, 示例: `20` |
| 搜索 Issue | `gh issue list --search "{query}"` | **query**: 搜索关键词, 示例: `error in login` |

### gh issue view - 查看 Issue

**基础用法**:
```bash
gh issue view %{issue_number}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看远程仓库 Issue | `gh issue view {issue_number} --repo {owner}/{repo}` | **issue_number**: Issue 编号, 示例: `123`; **owner/repo**: 其他仓库 |
| 显示评论 | `gh issue view {issue_number} --comments` | 包含评论 |
| 在浏览器打开 | `gh issue view {issue_number} --web` | 网页查看 |

### gh issue create - 创建 Issue

**基础用法**:
```bash
gh issue create --title "%{title}%" --body "%{body}%"
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建并指定标签 | `gh issue create --title "{title}" --body "{body}" --label {label}` | **【常用】title**: Issue 标题, 示例: `登录功能报错`; **label**: 标签名称, 示例: `bug` |
| 创建并指定受理人 | `gh issue create --title "{title}" --body "{body}" --assignee {assignee}` | **assignee**: 受理人用户名, 示例: `octocat` |
| 创建里程碑 | `gh issue create --title "{title}" --body "{body}" --milestone "{milestone}"` | **milestone**: 里程碑标题, 示例: `v1.0` |
| 打开编辑器 | `gh issue create` | 交互式创建 |
| 创建到指定仓库 | `gh issue create --repo {owner}/{repo} --title "{title}" --body "{body}"` | **owner/repo**: 仓库信息 |

### gh issue close - 关闭 Issue

**基础用法**:
```bash
gh issue close %{issue_number}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 关闭并说明原因 | `gh issue close {issue_number} --reason "{reason}"` | **issue_number**: Issue 编号, 示例: `123`; **reason**: 关闭原因, 示例: `completed` (可选: completed/not-planned) |
| 关闭指定仓库 Issue | `gh issue close {issue_number} --repo {owner}/{repo}` | 其他仓库 |

### gh issue reopen - 重新打开 Issue

**基础用法**:
```bash
gh issue reopen %{issue_number}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 重新打开指定仓库 Issue | `gh issue reopen {issue_number} --repo {owner}/{repo}` | **owner/repo**: 仓库信息 |

### gh issue edit - 编辑 Issue

**基础用法**:
```bash
gh issue edit %{issue_number}% --title "%{title}%" --body "%{body}%"
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 修改标题和描述 | `gh issue edit {issue_number} --title "{title}" --body "{body}"` | **issue_number**: Issue 编号, 示例: `123` |
| 修改标签 | `gh issue edit {issue_number} --label {label}` | **label**: 标签, 示例: `bug,enhancement` |
| 添加受理人 | `gh issue edit {issue_number} --add-assignee {assignee}` | **assignee**: 受理人, 示例: `octocat` |
| 修改里程碑 | `gh issue edit {issue_number} --milestone "{milestone}"` | **milestone**: 里程碑, 示例: `v1.0` |
| 编辑指定仓库 Issue | `gh issue edit {issue_number} --repo {owner}/{repo}` | 其他仓库 |

### gh issue comment - 评论 Issue

**基础用法**:
```bash
gh issue comment %{issue_number}% --body "%{body}%"
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 编辑最近评论 | `gh issue comment edit {issue_number} --body "{body}"` | **body**: 评论内容, 示例: `感谢报告，已确认此问题` |
| 删除最近评论 | `gh issue comment delete {issue_number}` | 删除评论 |
| 评论指定仓库 Issue | `gh issue comment {issue_number} --repo {owner}/{repo} --body "{body}"` | **owner/repo**: 仓库信息 |

### gh label list - 查看标签

**基础用法**:
```bash
gh label list
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看指定仓库标签 | `gh label list --repo {owner}/{repo}` | **owner/repo**: 仓库信息 |
| 限制数量 | `gh label list --limit {number}` | **number**: 返回数量上限, 示例: `50` |

---

## Pull Request 管理

### gh pr create - 创建 Pull Request

**基础用法**:
```bash
gh pr create --title "%{title}%" --body "%{body}%"
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建并指定审查者 | `gh pr create --title "{title}" --body "{body}" --reviewer {reviewer}` | **【常用】title**: PR 标题, 示例: `feat: 添加用户登录功能`; **reviewer**: 审查者, 示例: `octocat,hubot` |
| 创建并指定标签 | `gh pr create --title "{title}" --body "{body}" --label {label}` | **label**: 标签, 示例: `feature,bugfix` |
| 创建并指定受理人 | `gh pr create --title "{title}" --body "{body}" --assignee {assignee}` | **assignee**: 受理人, 示例: `octocat` |
| 创建指定目标分支 | `gh pr create --title "{title}" --body "{body}" --base {base_branch}` | **base_branch**: 目标分支, 示例: `main` |
| 创建指定源分支 | `gh pr create --title "{title}" --body "{body}" --head {head_branch}` | **head_branch**: 源分支, 示例: `feature/login` |
| 创建草稿 PR | `gh pr create --title "{title}" --body "{body}" --draft` | 草稿状态 |
| 创建并推送到远程 | `gh pr create --title "{title}" --body "{body}" --push` | 推送分支并创建 PR |
| 创建到指定仓库 | `gh pr create --repo {owner}/{repo} --title "{title}" --body "{body}"` | **owner/repo**: 仓库信息 |

### gh pr list - 列出 Pull Request

**基础用法**:
```bash
gh pr list
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看指定仓库 | `gh pr list --repo {owner}/{repo}` | **owner/repo**: 仓库信息 |
| 按状态筛选 | `gh pr list --state {state}` | **state**: PR 状态, 示例: `open` (可选: open/closed/merged/all) |
| 按标签筛选 | `gh pr list --label {label}` | **label**: 标签名称, 示例: `bug` |
| 按作者筛选 | `gh pr list --author {author}` | **author**: 作者用户名, 示例: `octocat` |
| 搜索 PR | `gh pr list --search "{query}"` | **query**: 搜索关键词, 示例: `login feature` |
| 限制数量 | `gh pr list --limit {number}` | **number**: 返回数量上限, 示例: `20` |

### gh pr view - 查看 Pull Request

**基础用法**:
```bash
gh pr view %{pr_number}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 在浏览器打开 | `gh pr view {pr_number} --web` | 网页查看 |
| 显示评论 | `gh pr view {pr_number} --comments` | 包含评论 |
| 显示变更文件 | `gh pr view {pr_number} --files` | 查看变更文件 |

### gh pr checkout - 检出 Pull Request

**基础用法**:
```bash
gh pr checkout %{pr_number}%
```

### gh pr merge - 合并 Pull Request

**基础用法**:
```bash
gh pr merge %{pr_number}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| Squash 合并 | `gh pr merge {pr_number} --squash --message "{message}"` | **【常用】pr_number**: PR 编号, 示例: `123`; **message**: Squash 提交信息, 示例: `feat: 合并登录功能` |
| Rebase 合并 | `gh pr merge {pr_number} --rebase` | Rebase 方式合并 |
| 合并并删除分支 | `gh pr merge {pr_number} --delete-branch` | 合并后删除源分支 |
| 自动合并 | `gh pr merge {pr_number} --auto` | 等待 CI 通过后自动合并 |
| 合并并添加说明 | `gh pr merge {pr_number} --body "{body}"` | **body**: 合并说明, 示例: `合并说明` |
| 允许合并冲突 | `gh pr merge {pr_number} --admin --merge` | 强制合并（需管理员权限） |

### gh pr close - 关闭 Pull Request

**基础用法**:
```bash
gh pr close %{pr_number}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 关闭并删除分支 | `gh pr close %{pr_number}% --delete-branch` | 同时删除源分支 |

### gh pr reopen - 重新打开 Pull Request

**基础用法**:
```bash
gh pr reopen %{pr_number}%
```

### gh pr edit - 编辑 Pull Request

**基础用法**:
```bash
gh pr edit %{pr_number}% --title "%{title}%" --body "%{body}%"
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 修改标题和描述 | `gh pr edit {pr_number} --title "{title}" --body "{body}"` | **title**: 新标题, 示例: `feat: 更新登录功能` |
| 修改目标分支 | `gh pr edit {pr_number} --base {base}` | **base**: 目标分支, 示例: `develop` |
| 添加标签 | `gh pr edit {pr_number} --add-label {label}` | **label**: 标签名称, 示例: `feature` |
| 移除标签 | `gh pr edit {pr_number} --remove-label {label}` | 删除标签 |
| 添加受理人 | `gh pr edit {pr_number} --add-assignee {assignee}` | **assignee**: 受理人, 示例: `octocat` |
| 移除受理人 | `gh pr edit {pr_number} --remove-assignee {assignee}` | 移除受理人 |

### gh pr add-assignee - 添加受理人

**基础用法**:
```bash
gh pr add-assignee %{pr_number}% %{assignee}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 添加多个受理人 | `gh pr add-assignee {pr_number} {user1} {user2}` | **【常用】pr_number**: PR 编号, 示例: `123`; **user1/user2**: 受理人, 示例: `octocat` |

### gh pr add-label - 添加标签

**基础用法**:
```bash
gh pr add-label %{pr_number}% %{label}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 添加多个标签 | `gh pr add-label {pr_number} {label1} {label2}` | **【常用】pr_number**: PR 编号, 示例: `123`; **label1/label2**: 标签, 示例: `bug`, `urgent` |

### gh pr review - 审查 Pull Request

**基础用法**:
```bash
gh pr review %{pr_number}% --%{action}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 批准 PR | `gh pr review {pr_number} --approve` | **【常用】pr_number**: PR 编号, 示例: `123` |
| 请求修改 | `gh pr review {pr_number} --request-changes --body "{body}"` | **body**: 审查意见, 示例: `LGTM!` |
| 仅评论 | `gh pr review {pr_number} --comment --body "{body}"` | Comment only |
| 批准并添加说明 | `gh pr review {pr_number} --approve --body "{body}"` | 带评论批准 |

### gh pr checks - 查看 CI 状态

**基础用法**:
```bash
gh pr checks %{pr_number}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 等待检查完成 | `gh pr checks {pr_number} --watch` | 持续监控 |
| 显示详细状态 | `gh pr checks {pr_number} --verbose` | **pr_number**: PR 编号, 示例: `123` |

---

## Actions

### gh run list - 列出运行记录

**基础用法**:
```bash
gh run list
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 限制数量 | `gh run list --limit {number}` | **【常用】number**: 返回数量上限, 示例: `20` |
| 按状态筛选 | `gh run list --status {status}` | **status**: 运行状态, 示例: `success` (可选: queued/in_progress/success/failure/cancelled) |
| 按分支筛选 | `gh run list --branch {branch}` | **branch**: 分支名称, 示例: `main` |
| 按工作流筛选 | `gh run list --workflow {workflow}` | **workflow**: 工作流名称, 示例: `CI` |
| 查看指定仓库 | `gh run list --repo {owner}/{repo}` | **owner/repo**: 仓库信息 |

### gh run view - 查看运行详情

**基础用法**:
```bash
gh run view %{run_id}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 显示日志 | `gh run view {run_id} --log` | **【常用】run_id**: 运行 ID, 示例: `123456789` |
| 显示作业 | `gh run view {run_id} --job` | 查看 Jobs |
| 在浏览器打开 | `gh run view {run_id} --web` | 网页查看 |
| 查看指定仓库 | `gh run view {run_id} --repo {owner}/{repo}` | **owner/repo**: 仓库信息 |

### gh run rerun - 重新运行

**基础用法**:
```bash
gh run rerun %{run_id}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 重新运行指定仓库 | `gh run rerun {run_id} --repo {owner}/{repo}` | **run_id**: 运行 ID, 示例: `123456789`; **owner/repo**: 仓库信息 |
| 重新运行失败作业 | `gh run rerun {run_id} --failed` | 重新运行失败的作业 |

### gh run cancel - 取消运行

**基础用法**:
```bash
gh run cancel %{run_id}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 取消指定仓库 | `gh run cancel {run_id} --repo {owner}/{repo}` | **run_id**: 运行 ID, 示例: `123456789` |

### gh workflow list - 列出工作流

**基础用法**:
```bash
gh workflow list
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 显示禁用状态 | `gh workflow list --all` | 包含禁用的工作流 |
| 查看指定仓库 | `gh workflow list --repo {owner}/{repo}` | **owner/repo**: 仓库信息 |

### gh workflow view - 查看工作流

**基础用法**:
```bash
gh workflow view %{workflow_id}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 在浏览器打开 | `gh workflow view {workflow_id} --web` | 网页查看 |
| 查看指定仓库 | `gh workflow view {workflow_id} --repo {owner}/{repo}` | **workflow_id**: 工作流名称/ID, 示例: `CI` |

### gh workflow run - 触发工作流

**基础用法**:
```bash
gh workflow run %{workflow_name}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 传递输入参数 | `gh workflow run {workflow_name} --field {key}={value}` | **【常用】workflow_name**: 工作流名称, 示例: `CI`; **key**: 输入参数名, 示例: `environment`; **value**: 参数值, 示例: `production` |
| 指定分支 | `gh workflow run {workflow_name} --ref {branch}` | **branch**: 分支名称, 示例: `main` |
| 运行指定仓库 | `gh workflow run {workflow_name} --repo {owner}/{repo}` | **owner/repo**: 仓库信息 |

---

## GitHub API

### gh api - 调用 REST API

**基础用法**:
```bash
gh api repos/{owner}/{repo}
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| POST 创建 Issue | `gh api repos/{owner}/{repo}/issues -X POST -f title="{title}" -f body="{body}"` | **title**: 标题, 示例: `Bug Report`; **body**: 正文, 示例: `详细描述` |
| GET 带参数 | `gh api repos/{owner}/{repo}/issues?state=open&per_page=100` | 查询参数 |
| jq 处理响应 | `gh api repos/{owner}/{repo}/issues --jq '.[] \| {number, title, state}'` | 格式化输出 |
| 设置请求头 | `gh api repos/{owner}/{repo} -H "Accept: application/vnd.github+json"` | 自定义 Header |
| GraphQL 查询 | `gh api graphql -f query='{viewer{login}}'` | GraphQL API |
| 认证信息 | `gh api user` | 查看当前用户信息 |

---

## 实用场景

### 日常 PR 工作流

```bash
# 1. 查看当前仓库 PR 列表
gh pr list

# 2. 创建新 PR
gh pr create --title "feat: add new feature" --body "Description here" --label "enhancement"

# 3. 查看 PR 详情
gh pr view 123

# 4. 检查 CI 状态
gh pr checks 123

# 5. 审查 PR (批准)
gh pr review 123 --approve --body "LGTM!"

# 6. 合并 PR (squash)
gh pr merge 123 --squash --message "feat: add new feature"

# 7. 关闭并删除分支
gh pr close 123 --delete-branch
```

### Issue 管理

```bash
# 1. 查看所有 Open 的 Issue
gh issue list --state open

# 2. 按标签筛选
gh issue list --label "bug"

# 3. 创建新 Issue
gh issue create --title "Bug: login fails" --body "Steps to reproduce..." --label "bug"

# 4. 查看 Issue 详情
gh issue view 456

# 5. 添加评论
gh issue comment 456 --body "Thanks for reporting!"

# 6. 关闭 Issue
gh issue close 456 --reason "fixed"
```

### CI 检查

```bash
# 1. 查看最近运行
gh run list --limit 10

# 2. 查看运行详情和日志
gh run view 987654

# 3. 等待检查通过
gh run list --status in_progress
gh run view 987654 --log

# 4. 重新运行失败的 workflow
gh run rerun 987654

# 5. 取消正在运行的 workflow
gh run cancel 987654
```

---

## 相关资源

- [Git 命令文档](../Git 命令/README.md)
- [Linux 命令文档](../Linux 命令/README.md)