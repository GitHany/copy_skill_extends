# GitHubActions 文档

GitHub Actions workflow management commands.

## 目录

- [Actions 运行管理](#actions-运行管理)
- [工作流管理](#工作流管理)
- [Issue 管理](#issue-管理)
- [Pull Request 管理](#pull-request-管理)

---

## Actions 运行管理

### gh run list - 查看运行列表

**基础用法**:
```bash
gh run list
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 限制返回数量 | `gh run list --limit {number}` | **number**: 返回数量上限, 示例: `20` |
| 按状态筛选 | `gh run list --status {status}` | **status**: 运行状态, 示例: `success` (可选: queued/in_progress/success/failure/cancelled) |
| 按分支筛选 | `gh run list --branch {branch}` | **branch**: 分支名称, 示例: `main` |
| 按工作流筛选 | `gh run list --workflow {workflow}` | **workflow**: 工作流名称, 示例: `CI` |
| 监控运行状态 | `gh run list --watch` | 持续监控运行状态 |

### gh run watch - 监控运行

**基础用法**:
```bash
gh run watch %{run_id}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 监控指定仓库运行 | `gh run watch {run_id} --repo {owner}/{repo}` | **owner/repo**: 仓库信息 |
| 设置轮询间隔 | `gh run watch {run_id} --interval {seconds}` | **seconds**: 间隔秒数, 示例: `10` |

### gh run cancel - 取消运行

**基础用法**:
```bash
gh run cancel %{run_id}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 取消指定仓库运行 | `gh run cancel {run_id} --repo {owner}/{repo}` | **run_id**: 运行 ID, 示例: `123456789` |

---

## 工作流管理

### gh workflow list - 列出工作流

**基础用法**:
```bash
gh workflow list
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 显示禁用的工作流 | `gh workflow list --all` | 包含已禁用的工作流 |
| 查看指定仓库 | `gh workflow list --repo {owner}/{repo}` | **owner/repo**: 仓库信息 |

### gh workflow disable - 禁用工作流

**基础用法**:
```bash
gh workflow disable %{workflow_id}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 禁用指定仓库工作流 | `gh workflow disable {workflow_id} --repo {owner}/{repo}` | **workflow_id**: 工作流名称, 示例: `CI` |

### gh workflow enable - 启用工作流

**基础用法**:
```bash
gh workflow enable %{workflow_id}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启用指定仓库工作流 | `gh workflow enable {workflow_id} --repo {owner}/{repo}` | **workflow_id**: 工作流名称, 示例: `CI` |

---

## Issue 管理

### gh issue create - 创建 Issue

**基础用法**:
```bash
gh issue create --title "%{title}%" --body "%{body}%"
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建并指定标签 | `gh issue create --title "{title}" --body "{body}" --label {label}` | **【常用】title**: Issue 标题, 示例: `登录功能报错`; **label**: 标签名称, 示例: `bug` |
| 创建并指定受理人 | `gh issue create --title "{title}" --body "{body}" --assignee {assignee}` | **assignee**: 受理人, 示例: `octocat` |
| 创建里程碑 | `gh issue create --title "{title}" --body "{body}" --milestone "{milestone}"` | **milestone**: 里程碑标题, 示例: `v1.0` |
| 打开编辑器 | `gh issue create` | 交互式创建 |
| 创建到指定仓库 | `gh issue create --repo {owner}/{repo} --title "{title}" --body "{body}"` | **owner/repo**: 仓库信息 |

### gh issue list - 列出 Issue

**基础用法**:
```bash
gh issue list
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看指定仓库 | `gh issue list --repo {owner}/{repo}` | **owner/repo**: 仓库信息 |
| 按状态筛选 | `gh issue list --state {state}` | **state**: Issue 状态, 示例: `open` (可选: open/closed/all) |
| 按标签筛选 | `gh issue list --label {label}` | **label**: 标签名称, 示例: `bug` |
| 按作者筛选 | `gh issue list --author {author}` | **author**: 作者用户名, 示例: `octocat` |
| 按受理人筛选 | `gh issue list --assignee {assignee}` | **assignee**: 受理人用户名, 示例: `octocat` |
| 限制数量 | `gh issue list --limit {number}` | **number**: 返回数量上限, 示例: `20` |
| 搜索 Issue | `gh issue list --search "{query}"` | **query**: 搜索关键词, 示例: `error in login` |

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
| 创建并指定审查者 | `gh pr create --title "{title}" --body "{body}" --reviewer {reviewer}` | **【常用】title**: PR 标题, 示例: `feat: 添加用户登录功能`; **reviewer**: 审查者, 示例: `octocat` |
| 创建并指定标签 | `gh pr create --title "{title}" --body "{body}" --label {label}` | **label**: 标签, 示例: `feature` |
| 创建并指定受理人 | `gh pr create --title "{title}" --body "{body}" --assignee {assignee}` | **assignee**: 受理人, 示例: `octocat` |
| 创建草稿 PR | `gh pr create --title "{title}" --body "{body}" --draft` | 草稿状态 |
| 创建并推送分支 | `gh pr create --title "{title}" --body "{body}" --push` | 推送分支并创建 PR |
| 指定目标分支 | `gh pr create --title "{title}" --body "{body}" --base {base_branch}` | **base_branch**: 目标分支, 示例: `main` |
| 创建到指定仓库 | `gh pr create --repo {owner}/{repo} --title "{title}" --body "{body}"` | **owner/repo**: 仓库信息 |

### gh pr checkout - 检出 Pull Request

**基础用法**:
```bash
gh pr checkout %{pr_number}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 检出并拉取 | `gh pr checkout {pr_number} --fetch` | 检出并同步最新代码 |
| 检出指定仓库 PR | `gh pr checkout {pr_number} --repo {owner}/{repo}` | **owner/repo**: 仓库信息 |

### gh pr status - 查看 PR 状态

**基础用法**:
```bash
gh pr status
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看指定仓库 PR 状态 | `gh pr status --repo {owner}/{repo}` | **owner/repo**: 仓库信息 |
| 显示详细信息 | `gh pr status --verbose` | 显示详细状态信息 |
| 显示 JSON 格式 | `gh pr status --json {fields}` | **fields**: 输出字段, 示例: `number,title,state` |

---

## 实用场景

### CI/CD 监控工作流

```bash
# 1. 查看最近运行记录
gh run list --limit 10

# 2. 监控正在运行的 workflow
gh run watch 123456789

# 3. 按分支筛选运行
gh run list --branch main --status failure

# 4. 取消长时间运行的 workflow
gh run cancel 123456789

# 5. 查看工作流列表
gh workflow list
```

### 工作流管理

```bash
# 1. 禁用不常用的工作流
gh workflow disable nightly-build

# 2. 重新启用工作流
gh workflow enable nightly-build

# 3. 查看所有工作流（包括禁用的）
gh workflow list --all
```

### Issue 管理

```bash
# 1. 查看所有 Open 的 Issue
gh issue list --state open

# 2. 按标签筛选 Bug
gh issue list --label bug

# 3. 创建新 Issue
gh issue create --title "Bug: login fails" --body "Steps to reproduce..." --label bug

# 4. 搜索 Issue
gh issue list --search "login error"
```

### Pull Request 工作流

```bash
# 1. 创建 PR
gh pr create --title "feat: add feature" --body "Description" --label enhancement

# 2. 检出 PR 到本地
gh pr checkout 123

# 3. 查看当前分支关联的 PR
gh pr status

# 4. 指定审查者
gh pr create --title "fix: bug" --body "Fixes #123" --reviewer octocat
```

---

## 相关资源

- [GitHub CLI 命令文档](../GitHub CLI 命令/README.md)
- [Git 命令文档](../Git 命令/README.md)
