# CI_CD 流水线 文档

CI/CD 流水线完整命令参考，涵盖 GitHub Actions、GitLab CI、Jenkins、Terraform、Ansible、Docker 镜像管理等工具。

## 目录

- [GitHub Actions](#github-actions)
- [Terraform 基础设施即代码](#terraform-基础设施即代码)
- [Ansible 配置管理](#ansible-配置管理)
- [Docker 镜像与仓库](#docker-镜像与仓库)
- [Docker Compose 多容器编排](#docker-compose-多容器编排)
- [Jenkins 持续集成](#jenkins-持续集成)
- [GitLab CI](#gitlab-ci)

---

## GitHub Actions

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

### gh workflow run - 触发工作流

**基础用法**:
```bash
gh workflow run %{workflow_name}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定分支 | `gh workflow run {workflow_name} --ref {branch}` | **branch**: 分支名称, 示例: `main` |
| 传入输入参数 | `gh workflow run {workflow_name} --field {input}` | **input**: 参数名=值, 示例: `env=production` |
| 触发指定仓库工作流 | `gh workflow run {workflow_name} --repo {owner}/{repo}` | **owner/repo**: 仓库信息 |

### gh secret list - 列出密钥

**基础用法**:
```bash
gh secret list
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看指定仓库密钥 | `gh secret list --repo {owner}/{repo}` | **owner/repo**: 仓库信息 |

### gh secret set - 设置密钥

**基础用法**:
```bash
gh secret set %{secret_name}% --body "%{value}%"
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 从文件读取值 | `gh secret set {secret_name} --from-file {file_path}` | **file_path**: 文件路径, 示例: `./token.txt` |
| 设置环境级别密钥 | `gh secret set {secret_name} --env {env}` | **env**: 环境名称, 示例: `production` |
| 设置仓库级别密钥 | `gh secret set {secret_name} --repo {owner}/{repo}` | **owner/repo**: 仓库信息 |

### gh secret delete - 删除密钥

**基础用法**:
```bash
gh secret delete %{secret_name}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 删除指定仓库密钥 | `gh secret delete {secret_name} --repo {owner}/{repo}` | **owner/repo**: 仓库信息 |
| 删除环境级别密钥 | `gh secret delete {secret_name} --env {env}` | **env**: 环境名称, 示例: `production` |

### gh variable list - 列出变量

**基础用法**:
```bash
gh variable list
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看指定仓库变量 | `gh variable list --repo {owner}/{repo}` | **owner/repo**: 仓库信息 |

### gh variable set - 设置变量

**基础用法**:
```bash
gh variable set %{var_name}% --body "%{value}%"
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 从文件读取值 | `gh variable set {var_name} --from-file {file_path}` | **file_path**: 文件路径 |
| 设置环境级别变量 | `gh variable set {var_name} --env {env}` | **env**: 环境名称, 示例: `staging` |

### gh run rerun - 重新运行

**基础用法**:
```bash
gh run rerun %{run_id}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 重新运行指定仓库 | `gh run rerun {run_id} --repo {owner}/{repo}` | **owner/repo**: 仓库信息 |

---

## Terraform 基础设施即代码

### terraform init - 初始化

**基础用法**:
```bash
terraform init
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定插件目录 | `terraform init -plugin-dir {plugin_dir}` | **plugin_dir**: 插件目录路径, 示例: `/opt/terraform/plugins` |
| 后端配置初始化 | `terraform init -backend-config="{config}"` | **config**: 后端配置, 示例: `bucket=my-terraform-state` |
| 升级模块和 providers | `terraform init -upgrade` | 升级到最新版本 |
| 强制复制状态 | `terraform init -force-copy` | 将状态复制到新后端 |

### terraform plan - 规划变更

**基础用法**:
```bash
terraform plan
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 输出到文件 | `terraform plan -out {plan_file}` | 后续 apply 使用 |
| 目标资源 | `terraform plan -target {resource}` | **resource**: 资源地址, 示例: `aws_instance.app` |
| 变量文件 | `terraform plan -var-file {var_file}` | **var_file**: 变量文件, 示例: `prod.tfvars` |
| 销毁模式 | `terraform plan -destroy` | 预览将要销毁的资源 |

### terraform apply - 执行变更

**基础用法**:
```bash
terraform apply
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 应用指定计划文件 | `terraform apply {plan_file}` | 使用之前保存的计划 |
| 自动批准 | `terraform apply -auto-approve` | 无需交互确认 |
| 变量文件 | `terraform apply -var-file {var_file}` | **var_file**: 变量文件, 示例: `prod.tfvars` |
| 目标资源 | `terraform apply -target {resource}` | **resource**: 资源地址, 示例: `aws_instance.app` |

### terraform destroy - 销毁资源

**基础用法**:
```bash
terraform destroy
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 自动批准 | `terraform destroy -auto-approve` | 无需交互确认 |
| 目标资源 | `terraform destroy -target {resource}` | **resource**: 资源地址 |
| 变量文件 | `terraform destroy -var-file {var_file}` | **var_file**: 变量文件 |

### terraform validate - 验证配置

**基础用法**:
```bash
terraform validate
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| JSON 格式输出 | `terraform validate -json` | 便于程序解析 |

### terraform fmt - 格式化配置

**基础用法**:
```bash
terraform fmt
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 递归格式化目录 | `terraform fmt -recursive` | 格式化子目录 |
| 列出需格式化的文件 | `terraform fmt -list=true` | 仅列出不修改 |
| 检查格式（不修改） | `terraform fmt -check` | CI 中检查使用 |

### terraform show - 查看状态

**基础用法**:
```bash
terraform show
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| JSON 格式输出 | `terraform show -json` | 便于程序解析 |
| 查看指定状态文件 | `terraform show {state_file}` | **state_file**: 状态文件路径 |

### terraform output - 查看输出

**基础用法**:
```bash
terraform output
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看指定输出 | `terraform output {output_name}` | **output_name**: 输出变量名称, 示例: `instance_ip` |
| JSON 格式输出 | `terraform output -json` | 全部输出为 JSON |

### terraform state - 状态管理

**基础用法**:
```bash
terraform state %{subcommand}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 列出资源 | `terraform state list` | 列出所有资源 |
| 移动资源 | `terraform state mv {from} {to}` | 迁移资源地址 |
| 拉取远程状态 | `terraform state pull` | 查看远程状态 |
| 推送本地状态 | `terraform state push {state_file}` | 上传本地状态 |

---

## Ansible 配置管理

### ansible-playbook - 执行剧本

**基础用法**:
```bash
ansible-playbook %{playbook}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定清单文件 | `ansible-playbook {playbook} -i {inventory}` | **inventory**: 清单文件, 示例: `hosts.ini` |
| 限制主机 | `ansible-playbook {playbook} --limit {hosts}` | **hosts**: 目标主机, 示例: `webservers` |
| 执行标签任务 | `ansible-playbook {playbook} --tags {tags}` | **tags**: 任务标签, 示例: `deploy` |
| 检查模式（不执行） | `ansible-playbook {playbook} --check` | 预演模式 |
| 传递额外变量 | `ansible-playbook {playbook} -e "{key}={value}"` | 动态变量, 示例: `env=production` |
| 详细输出 | `ansible-playbook {playbook} -v` | 增加日志详细程度 |

### ansible-vault - 加密管理

**基础用法**:
```bash
ansible-vault %{action}% %{file}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建加密文件 | `ansible-vault create {file}` | 交互式创建新加密文件 |
| 加密已有文件 | `ansible-vault encrypt {file}` | 加密现有文件 |
| 解密文件 | `ansible-vault decrypt {file}` | 还原为明文 |
| 查看加密文件 | `ansible-vault view {file}` | 不解密直接查看 |
| 指定密码文件 | `ansible-vault {action} {file} --vault-password-file {password_file}` | 自动化场景 |

### ansible-galaxy - 角色管理

**基础用法**:
```bash
ansible-galaxy %{action}% %{name}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 从 Galaxy 安装 | `ansible-galaxy role install {role_name}` | **role_name**: 角色名, 示例: `geerlingguy.docker` |
| 安装 Collection | `ansible-galaxy collection install {collection_name}` | **collection_name**: 集合名, 示例: `community.general` |
| 初始化新角色 | `ansible-galaxy role init {role_name}` | 在当前目录生成角色结构 |
| 查看已安装列表 | `ansible-galaxy role list` | 列出本地已安装角色 |
| 删除角色 | `ansible-galaxy role remove {role_name}` | 从本地删除角色 |

---

## Docker 镜像与仓库

### docker login - 登录镜像仓库

**基础用法**:
```bash
docker login %{registry}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定用户名 | `docker login {registry} -u {username}` | **username**: 用户名, 示例: `admin` |
| 登录 Docker Hub | `docker login` | 默认 Docker Hub |
| 登录私有仓库 | `docker login {registry} --username {username}` | 示例: `registry.example.com` |

### docker push - 推送镜像

**基础用法**:
```bash
docker push %{image}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 推送所有标签 | `docker push {image} --all-tags` | 推送该镜像所有标签 |
| 指定仓库镜像 | `docker push {registry}/{repo}/{image}:{tag}` | 推送到私有仓库 |
| 压缩传输 | `docker push {image}` | 启用压缩减少带宽 |

### docker pull - 拉取镜像

**基础用法**:
```bash
docker pull %{image}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 拉取指定版本 | `docker pull {image}:{tag}` | **tag**: 版本标签, 示例: `latest` |
| 拉取所有标签 | `docker pull {image} --all-tags` | 拉取完整镜像集 |
| 跳过校验 | `docker pull {image} --disable-content-trust` | 跳过镜像签名校验 |

---

## Docker Compose 多容器编排

### docker-compose up - 启动服务

**基础用法**:
```bash
docker-compose up
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 后台运行 | `docker-compose up -d` | 后台守护模式 |
| 重新构建镜像 | `docker-compose up -d --build` | 强制重新构建后启动 |
| 指定 compose 文件 | `docker-compose up -f {file} -d` | **file**: 文件路径, 示例: `docker-compose.prod.yml` |
| 扩展服务实例 | `docker-compose up -d --scale {service}={num}` | **service**: 服务名, 示例: `web=3` |
| 移除孤立容器 | `docker-compose up -d --remove-orphans` | 清理不属于配置的容器 |

### docker-compose down - 停止服务

**基础用法**:
```bash
docker-compose down
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 删除数据卷 | `docker-compose down -v` | 清除持久化数据 |
| 删除镜像 | `docker-compose down --rmi {rmi_type}` | **rmi_type**: `all` 或 `local` |
| 指定 compose 文件 | `docker-compose down -f {file}` | **file**: 文件路径 |

### docker-compose build - 构建服务

**基础用法**:
```bash
docker-compose build
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 构建指定服务 | `docker-compose build {service}` | **service**: 服务名, 示例: `backend` |
| 强制重新构建 | `docker-compose build --no-cache` | 不使用缓存 |
| 并行构建 | `docker-compose build --parallel` | 加快构建速度 |
| 指定 compose 文件 | `docker-compose build -f {file}` | **file**: 文件路径 |

---

## Jenkins 持续集成

### jenkins-cli 构建任务

**基础用法**:
```bash
java -jar jenkins-cli.jar -s %{jenkins_url}% build %{job_name}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 带参数构建 | `java -jar jenkins-cli.jar -s {url} build {job} -p {param}={value}` | **param/value**: 参数化构建, 示例: `ENV=production` |
| 等待构建完成 | `java -jar jenkins-cli.jar -s {url} build {job} -s -v` | 阻塞等待并输出日志 |
| 停止构建 | `java -jar jenkins-cli.jar -s {url} stop-builds {job}` | 停止正在运行的构建 |
| 禁用任务 | `java -jar jenkins-cli.jar -s {url} disable-job {job}` | 暂停任务执行 |
| 启用任务 | `java -jar jenkins-cli.jar -s {url} enable-job {job}` | 恢复任务执行 |
| 复制任务 | `java -jar jenkins-cli.jar -s {url} copy-job {src} {dst}` | 克隆现有任务配置 |
| 删除任务 | `java -jar jenkins-cli.jar -s {url} delete-job {job}` | 永久删除任务 |

---

## GitLab CI

### gitlab-runner 注册运行器

**基础用法**:
```bash
gitlab-runner register
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 非交互式注册 | `gitlab-runner register -n --url "{url}" --registration-token "{token}" --executor "{executor}"` | 自动化脚本使用 |
| 指定 Tags | `gitlab-runner register -n --url "{url}" --registration-token "{token}" --tag-list "{tags}"` | **tags**: 标签, 示例: `docker,linux` |
| 列出已注册 runners | `gitlab-runner list` | 查看本地 runner 列表 |
| 启动 runner | `gitlab-runner run` | 以后台服务方式启动 |
| 验证 runner 配置 | `gitlab-runner verify` | 检查 runner 连通性 |
| 注销 runner | `gitlab-runner unregister --url "{url}" --token "{token}"` | 从 GitLab 移除 |

---

## 实用场景

### 完整 CI/CD 流水线发布流程

```bash
# 1. Terraform 初始化并规划
terraform init
terraform plan -out=tfplan

# 2. 查看 plan 结果后应用
terraform apply -auto-approve

# 3. 构建 Docker 镜像
docker build -t myapp:${GIT_COMMIT} .

# 4. 登录私有镜像仓库
docker login registry.example.com -u admin

# 5. 推送镜像
docker push registry.example.com/myproject/myapp:${GIT_COMMIT}

# 6. 使用 Ansible 部署
ansible-playbook deploy.yml -i inventory/prod --tags deploy

# 7. GitHub Actions 触发生产部署
gh workflow run deploy.yml -f env=production --ref main
```

### Docker Compose 全流程管理

```bash
# 1. 构建所有服务镜像
docker-compose build

# 2. 启动服务（后台）
docker-compose up -d --build

# 3. 查看运行状态
docker-compose ps

# 4. 查看日志
docker-compose logs -f

# 5. 扩展服务
docker-compose up -d --scale worker=3

# 6. 停止并清理
docker-compose down -v --rmi all
```

### GitHub Actions 密钥与环境管理

```bash
# 1. 设置生产环境密钥
gh secret set API_TOKEN --body "ghp_xxx" --env production

# 2. 设置部署区域变量
gh variable set DEPLOY_REGION --body "us-west-2" --env production

# 3. 查看所有生产环境密钥
gh secret list --env production

# 4. 触发生产部署工作流
gh workflow run deploy.yml --env production --ref main

# 5. 监控运行状态
gh run watch $(gh run list --workflow deploy.yml --limit 1 --json id --jq '.[0].id')
```

### Ansible + Terraform 基础设施即代码

```bash
# 1. 格式化检查 Terraform 文件
terraform fmt -check

# 2. 验证 Terraform 语法
terraform validate

# 3. 初始化 Terraform 后端
terraform init -backend-config="bucket=my-terraform-state"

# 4. 应用基础设施
terraform apply -auto-approve -var-file=prod.tfvars

# 5. 导出 Terraform 输出给 Ansible
export DB_HOST=$(terraform output -raw db_host)

# 6. 使用 ansible-vault 解密敏感变量
ansible-playbook site.yml -i inventory/prod --vault-password-file .vault_pass

# 7. 销毁基础设施
terraform destroy -auto-approve -var-file=prod.tfvars
```

---

## 相关资源

- [GitHub Actions 文档](../GitHubActions/README.md)
- [GitHub CLI 命令文档](../GitHub CLI 命令/README.md)
- [Docker 命令文档](../Docker 命令/README.md)
- [DockerCompose 文档](../DockerCompose/README.md)
- [Git 命令文档](../Git 命令/README.md)
