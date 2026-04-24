# Serverless 与边缘计算 文档

Serverless 与边缘计算完整命令参考，涵盖 AWS Lambda (含 SAM CLI)、Vercel、Netlify、Cloudflare Workers、Deno Deploy、Supabase Edge Functions 及 Serverless Framework 等平台。

## 目录

- [AWS Lambda](#aws-lambda)
- [AWS SAM CLI](#aws-sam-cli)
- [Serverless Framework](#serverless-framework)
- [Vercel](#vercel)
- [Netlify](#netlify)
- [Cloudflare Workers](#cloudflare-workers)
- [Deno Deploy](#deno-deploy)
- [Supabase Edge Functions](#supabase-edge-functions)

---

## AWS Lambda

### aws lambda create-function - 创建函数

**基础用法**:
```bash
aws lambda create-function --function-name %{function_name}% --runtime %{runtime}% --role %{role_arn}% --handler %{handler}% --zip-file %{zip_file}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 Node.js 函数 | `aws lambda create-function --function-name {name} --runtime nodejs18.x --role {arn} --handler index.handler --zip-file fileb://{file}` | **【常用】name**: 函数名; **arn**: IAM 角色 ARN; **file**: 打包文件 |
| 指定环境变量 | `aws lambda create-function --function-name {name} --runtime {runtime} --role {arn} --handler {handler} --environment Variables={KEY}=value --zip-file fileb://{file}` | 环境变量注入 |
| 指定 VPC 配置 | `aws lambda create-function --function-name {name} --runtime {runtime} --role {arn} --handler {handler} --vpc-config SubnetIds=[{subnet}],SecurityGroupIds=[{sg}] --zip-file fileb://{file}` | **subnet**: 子网 ID; **sg**: 安全组 ID |
| 指定超时/内存 | `aws lambda create-function --function-name {name} --runtime {runtime} --role {arn} --handler {handler} --timeout {timeout} --memory-size {memory} --zip-file fileb://{file}` | **timeout**: 超时(秒), 示例: `30`; **memory**: 内存(MB), 示例: `256` |
| 使用 ARM64 架构 | `aws lambda create-function --function-name {name} --runtime {runtime} --role {arn} --handler {handler} --architectures arm64 --zip-file fileb://{file}` | Graviton2 架构，更高性价比 |

### aws lambda invoke - 调用函数

**基础用法**:
```bash
aws lambda invoke --function-name %{function_name}% %{output_file}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 同步调用并获取日志 | `aws lambda invoke --function-name {name} --payload '{payload}' --log-type Tail {output}` | **【常用】name**: 函数名; **payload**: JSON 负载; **output**: 输出文件 |
| 异步调用 | `aws lambda invoke --function-name {name} --invocation-type Event {output}` | Event 调用不等待响应 |
| 指定版本/别名调用 | `aws lambda invoke --function-name {name} --qualifier {qualifier} {output}` | **qualifier**: 版本或别名, 示例: `prod`, `$LATEST` |
| 从文件读取 Payload | `aws lambda invoke --function-name {name} --payload file://{payload_file} {output}` | 外部文件作为请求体 |
| Dry Run 验证 | `aws lambda invoke --function-name {name} --invocation-type DryRun {output}` | 仅验证不实际执行 |

### aws lambda update-function-code - 更新函数代码

**基础用法**:
```bash
aws lambda update-function-code --function-name %{function_name}% --zip-file %{zip_file}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 通过 S3 更新 | `aws lambda update-function-code --function-name {name} --s3-bucket {bucket} --s3-key {key}` | **bucket**: S3 存储桶; **key**: 对象键 |
| 指定版本更新 | `aws lambda update-function-code --function-name {name} --s3-bucket {bucket} --s3-key {key} --s3-object-version {version}` | 指定 S3 对象版本 |
| 替换替换处理程序 | `aws lambda update-function-code --function-name {name} --zip-file fileb://{file} --handler {new_handler}` | 更改入口函数 |
| 跳过旧版本保留 | `aws lambda update-function-code --function-name {name} --zip-file fileb://{file} --revision-id {revision}` | 乐观锁防止并发更新 |

### aws lambda update-function-configuration - 更新函数配置

**基础用法**:
```bash
aws lambda update-function-configuration --function-name %{function_name}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 更新内存大小 | `aws lambda update-function-configuration --function-name {name} --memory-size {size}` | **size**: 内存 MB, 示例: `512` |
| 更新超时时间 | `aws lambda update-function-configuration --function-name {name} --timeout {seconds}` | **seconds**: 超时秒, 示例: `60` |
| 更新环境变量 | `aws lambda update-function-configuration --function-name {name} --environment Variables={ENV}=prod` | 设置或更新环境变量 |
| 更新 VPC 配置 | `aws lambda update-function-configuration --function-name {name} --vpc-config SubnetIds=[{subnet}],SecurityGroupIds=[{sg}]` | 重新配置 VPC |
| 更新并发限制 | `aws lambda update-function-configuration --function-name {name} --reserved-concurrent-executions {count}` | **count**: 保留并发数, 示例: `100` |

### aws lambda list-functions - 列出函数

**基础用法**:
```bash
aws lambda list-functions
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 筛选运行时 | `aws lambda list-functions --master-region {region}` | 查看指定区域函数 |
| 分页获取函数 | `aws lambda list-functions --max-items {max}` | **max**: 最大数量, 示例: `10` |
| 获取函数配置 | `aws lambda get-function --function-name {name}` | 查看单个函数详情 |

---

## AWS SAM CLI

### sam init - 初始化项目

**基础用法**:
```bash
sam init
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定运行时初始化 | `sam init --name {name} --runtime {runtime}` | **runtime**: 运行时, 示例: `python3.11`, `nodejs18.x`, `go1.x` |
| 无交互式初始化 | `sam init --name {name} --runtime {runtime} --app-template hello-world --no-interactive` | 自动化脚本使用 |
| 基于镜像初始化 | `sam init --name {name} --base-image {base_image}` | **base_image**: 基础镜像, 示例: `amazon/nodejs18.x-base` |
| 生成 TypeScript 项目 | `sam init --name {name} --runtime nodejs18.x --app-template hello-world-typescript` | 生成 TypeScript 模板 |
| 指定依赖管理器 | `sam init --name {name} --runtime {runtime} --package-type {type}` | **type**: 打包类型, 示例: `Zip`, `Image` |

### sam build - 构建应用

**基础用法**:
```bash
sam build
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定构建参数 | `sam build --use-container --container-env-var FILE_ENV={file}` | 使用容器构建 |
| 指定构建目录 | `sam build --build-dir {build_dir}` | **build_dir**: 构建目录, 示例: `./build` |
| 指定模板文件 | `sam build -t {template}` | **template**: 模板路径, 示例: `template.yaml` |
| 构建指定函数 | `sam build --function-identifier {function_name}` | 仅构建单个函数加速 |
| 清理后重新构建 | `sam build --clean` | 清除 .aws-sam 目录后重新构建 |

### sam deploy - 部署应用

**基础用法**:
```bash
sam deploy --guided
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 非交互式部署 | `sam deploy --no-confirm-changeset --stack-name {stack}` | **stack**: 栈名称, 示例: `my-app` |
| 指定参数部署 | `sam deploy --parameter-overrides ParameterKey=Environment,ParameterValue=prod` | 覆盖模板参数 |
| 自动确认变更集 | `sam deploy --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM` | 授予 IAM 权限 |
| 指定 S3 桶 | `sam deploy --s3-bucket {bucket} --s3-prefix {prefix}` | 指定部署包存储位置 |
| 回滚部署 | `aws cloudformation cancel-update-stack --stack-name {stack}` | 取消正在进行的更新 |

---

## Serverless Framework

### serverless config credentials - 配置凭证

**基础用法**:
```bash
serverless config credentials --provider %{provider}% --key %{key}% --secret %{secret}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 配置 AWS 凭证 | `serverless config credentials --provider aws --key {access_key} --secret {secret_key}` | **access_key/secret_key**: AWS 访问密钥 |
| 使用 Profile 配置 | `serverless config credentials --provider aws --key {key} --secret {secret} --profile {profile}` | **profile**: Profile 名称, 示例: `my-profile` |
| 配置阿里云凭证 | `serverless config credentials --provider aliyun --key {key} --secret {secret}` | 阿里云 Provider |
| 配置腾讯云凭证 | `serverless config credentials --provider tencent --key {key} --secret {secret}` | 腾讯云 Provider |

### serverless create - 创建服务

**基础用法**:
```bash
serverless create --template %{template}% --path %{path}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 AWS Node.js 项目 | `serverless create --template aws-nodejs --path {path}` | **path**: 项目目录, 示例: `./my-service` |
| 创建 AWS Python 项目 | `serverless create --template aws-python --path {path}` | Python 运行时模板 |
| 创建阿里云项目 | `serverless create --template aliyun-python --path {path}` | 阿里云函数计算模板 |
| 创建自定义模板 | `serverless create --template-url {url} --path {path}` | 从 GitHub URL 创建 |
| 指定名称创建 | `serverless create --template {template} --name {name} --path {path}` | 同时指定服务名 |

### serverless deploy - 部署服务

**基础用法**:
```bash
serverless deploy
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定阶段部署 | `serverless deploy --stage {stage}` | **stage**: 阶段名称, 示例: `prod`, `staging` |
| 指定区域部署 | `serverless deploy --region {region}` | **region**: AWS 区域, 示例: `us-east-1` |
| 指定函数部署 | `serverless deploy --function {function_name}` | 仅部署单个函数 |
| 显示变更集 | `serverless deploy --verbose` | 详细输出模式 |
| 强制部署 | `serverless deploy --force` | 跳过变更检查强制部署 |

### serverless package - 打包服务

**基础用法**:
```bash
serverless package
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定输出目录 | `serverless package --package {package_dir}` | **package_dir**: 输出目录, 示例: `./.serverless` |
| 指定阶段打包 | `serverless package --stage {stage}` | 打包指定阶段配置 |
| 指定区域打包 | `serverless package --region {region}` | 打包指定区域配置 |

### serverless invoke - 调用函数

**基础用法**:
```bash
serverless invoke --function %{function_name}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 传入 Payload 调用 | `serverless invoke --function {name} --data '{payload}'` | **payload**: JSON 格式数据 |
| 从文件读取调用 | `serverless invoke --function {name} --path {payload_file}` | **payload_file**: 请求文件, 示例: `./event.json` |
| 指定阶段调用 | `serverless invoke --function {name} --stage {stage}` | 调用指定阶段函数 |
| 查看函数日志 | `serverless logs --function {name}` | 查看函数执行日志 |

### serverless logs - 查看日志

**基础用法**:
```bash
serverless logs --function %{function_name}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 实时跟踪日志 | `serverless logs --function {name} --tail` | 持续监控日志输出 |
| 指定时间范围 | `serverless logs --function {name} --startTime {time}` | **time**: ISO8601 时间或相对时间, 示例: `1h ago` |
| 限制日志行数 | `serverless logs --function {name} --limit {lines}` | **lines**: 返回行数, 示例: `100` |

---

## Vercel

### vercel - 部署项目

**基础用法**:
```bash
vercel
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 部署到生产环境 | `vercel --prod` | 直接部署到生产环境 |
| 指定项目部署 | `vercel --scope {scope}` | **scope**: 团队/用户名, 示例: `my-team` |
| 部署并设置名称 | `vercel --name {project_name}` | 覆盖项目名称 |
| 区分环境部署 | `vercel --environment {env}` | **env**: `development`, `preview`, `production` |
| 不连接 Git 自动部署 | `vercel --yes --no-git` | 跳过 Git 集成直接部署 |
| 设置 Token 部署 | `vercel --token {token}` | CI/CD 场景使用 |

### vercel env - 环境变量管理

**基础用法**:
```bash
vercel env pull %{file}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 拉取环境变量 | `vercel env pull {file}` | **file**: 输出文件, 示例: `.env.local` |
| 添加环境变量 | `vercel env add {name}` | 交互式添加新的环境变量 |
| 列出环境变量 | `vercel env ls` | 查看所有环境变量列表 |
| 删除环境变量 | `vercel env rm {name}` | **name**: 变量名, 示例: `DATABASE_URL` |
| 拉取生产环境变量 | `vercel env pull {file} --environment production` | 指定生产环境 |

### vercel secrets - 密钥管理

**基础用法**:
```bash
vercel secrets add %{name}% %{value}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 添加密钥 | `vercel secrets add {name} {value}` | **name**: 密钥名; **value**: 密钥值 |
| 列出所有密钥 | `vercel secrets ls` | 查看所有密钥列表 |
| 重命名密钥 | `vercel secrets rename {old} {new}` | 重命名现有密钥 |
| 删除密钥 | `vercel secrets remove {name}` | 删除指定密钥 |

### vercel logs - 查看日志

**基础用法**:
```bash
vercel logs %{url}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 实时查看日志 | `vercel logs {url} --follow` | 持续监控部署日志 |
| 指定部署查看 | `vercel logs {url} --deployment-id {id}` | **id**: 部署 ID |
| 按数量限制日志 | `vercel logs {url} --limit {count}` | **count**: 日志条数, 示例: `50` |
| 查看函数日志 | `vercel logs --token {token}` | 使用 Token 查看 |

### vercel inspect - 查看部署详情

**基础用法**:
```bash
vercel inspect %{deployment_id}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看最新部署 | `vercel inspect` | 查看当前项目最新部署 |
| 查看指定部署 | `vercel inspect {deployment_id}` | **deployment_id**: 部署 ID |
| 查看 JSON 格式 | `vercel inspect {deployment_id} --json` | JSON 格式输出便于解析 |

### vercel remove - 删除部署

**基础用法**:
```bash
vercel remove %{deployment_id}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 删除指定部署 | `vercel remove {deployment_id}` | **【常用】deployment_id**: 部署 ID, 示例: `dpl_abc123` |
| 删除所有预览部署 | `vercel remove --yes --all-previews` | 清理所有非生产部署 |
| 强制删除 | `vercel remove {deployment_id} --force` | 跳过确认直接删除 |

---

## Netlify

### netlify init - 初始化站点

**基础用法**:
```bash
netlify init
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 非交互式初始化 | `netlify init --auto-init` | 自动创建并连接站点 |
| 指定站点名称 | `netlify init --name {site_name}` | **site_name**: 站点名称, 示例: `my-awesome-site` |
| 连接现有站点 | `netlify init --id {site_id}` | **site_id**: 已有站点 ID |
| 指定构建命令 | `netlify init --build-command {command}` | **command**: 构建命令, 示例: `npm run build` |
| 指定发布目录 | `netlify init --dir {dir}` | **dir**: 发布目录, 示例: `dist`, `build` |

### netlify deploy - 部署

**基础用法**:
```bash
netlify deploy
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 部署到生产环境 | `netlify deploy --prod` | 直接发布到生产环境 |
| 指定发布目录 | `netlify deploy --dir {dir}` | **dir**: 目录路径, 示例: `./public` |
| 指定构建命令 | `netlify deploy --build-command {command}` | 覆盖构建配置 |
| 创建变更集预览 | `netlify deploy --message {message}` | **message**: 部署描述 |
| 指定函数目录 | `netlify deploy --functions {func_dir}` | **func_dir**: 函数目录, 示例: `./functions` |

### netlify functions - 函数管理

**基础用法**:
```bash
netlify functions:create %{name}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建新函数 | `netlify functions:create {name}` | **name**: 函数名, 示例: `hello` |
| 列出所有函数 | `netlify functions:list` | 查看已部署函数列表 |
| 调用函数（本地） | `netlify functions:invoke {name} --port {port}` | 本地测试函数 |
| 删除函数 | `netlify functions:remove {name}` | 删除指定函数 |
| 模拟函数调用 | `netlify functions:invoke {name} --no-open` | 本地触发器测试 |
| 设置函数超时 | `netlify functions:create {name} --timeout {seconds}` | **seconds**: 超时秒数, 示例: `20` |

### netlify env - 环境变量

**基础用法**:
```bash
netlify env:list
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 列出所有环境变量 | `netlify env:list` | 查看所有环境变量 |
| 设置环境变量 | `netlify env:set {key} {value}` | **key/value**: 变量名和值 |
| 获取环境变量 | `netlify env:get {key}` | 获取单个变量值 |
| 删除环境变量 | `netlify env:unset {key}` | 删除指定变量 |
| 导入环境变量 | `netlify env:import {file}` | **file**: .env 文件路径 |

### netlify edge-functions - 边缘函数

**基础用法**:
```bash
netlify edge-functions:create %{name}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建边缘函数 | `netlify edge-functions:create {name}` | **name**: 函数名, 示例: `geo-redirect` |
| 列出边缘函数 | `netlify edge-functions:list` | 查看所有边缘函数 |
| 本地测试边缘函数 | `netlify dev --edge-functions {dir}` | **dir**: 函数目录 |
| 模拟请求测试 | `netlify edge-functions:invoke {name} --request {request}` | 本地模拟请求 |

---

## Cloudflare Workers

### wrangler init - 初始化项目

**基础用法**:
```bash
wrangler init %{name}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 初始化 Worker 项目 | `wrangler init {name}` | **name**: 项目名称, 示例: `my-worker` |
| 初始化 TypeScript 项目 | `wrangler init {name} --type {type}` | **type**: 项目类型, 示例: `webpack`, `rollup` |
| 在当前目录初始化 | `wrangler init .` | 在当前目录创建项目 |
| 指定 GitHub 模板 | `wrangler init {name} --template {template}` | 使用 GitHub 模板创建 |

### wrangler dev - 本地开发

**基础用法**:
```bash
wrangler dev
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定端口启动 | `wrangler dev --port {port}` | **port**: 端口号, 示例: `8787` |
| 指定环境变量 | `wrangler dev --env {env}` | **env**: 环境名称, 示例: `production` |
| 启用本地 KV | `wrangler dev --kv {namespace}` | **namespace**: KV 命名空间名称 |
| 启用热重载 | `wrangler dev --local` | 本地模式开发 |
| 指定 Worker 名称 | `wrangler dev --name {worker_name}` | 指定 Worker 名称 |

### wrangler deploy - 部署

**基础用法**:
```bash
wrangler deploy
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定环境部署 | `wrangler deploy --env {env}` | **env**: 环境名称, 示例: `staging` |
| 指定 Triggers | `wrangler deploy --routes "example.com/*"` | 自定义路由 |
| 不上传 secrets | `wrangler deploy --no-bundle` | 仅上传脚本不上传 secrets |
| 部署为旧版兼容 | `wrangler deploy --compatibility-date {date}` | **date**: 兼容日期, 示例: `2024-01-01` |

### wrangler kv - KV 存储

**基础用法**:
```bash
wrangler kv:namespace create %{name}%
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 KV 命名空间 | `wrangler kv:namespace create {name}` | **name**: 命名空间名称 |
| 列出所有 KV 命名空间 | `wrangler kv:namespace list` | 查看命名空间列表 |
| 写入 KV 数据 | `wrangler kv:key put {key} {value} --namespace-id {id}` | **key/value/id**: 键值和命名空间 ID |
| 读取 KV 数据 | `wrangler kv:key get {key} --namespace-id {id}` | 读取指定键值 |
| 列出所有键 | `wrangler kv:key list --namespace-id {id}` | 列出命名空间所有键 |
| 删除 KV 数据 | `wrangler kv:key delete {key} --namespace-id {id}` | 删除指定键 |

### wrangler secret - 密钥管理

**基础用法**:
```bash
wrangler secret put %{name}%
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 设置密钥 | `wrangler secret put {name}` | 交互式输入密钥值 |
| 删除密钥 | `wrangler secret delete {name}` | 删除指定密钥 |
| 列出密钥 | `wrangler secret list` | 查看所有密钥（不显示值） |

---

## Deno Deploy

### deno.json 配置与部署

**基础用法**:
```bash
deno.json 的 import_map 和 task 配置
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 初始化项目 | `echo > deno.json '{"imports":{},"tasks":{"start":"deno run --allow-net server.ts"}}'` | 创建 Deno 配置文件 |
| 部署到生产 | `deployctl deploy --project={project} ./server.ts` | **project**: 项目名称 |
| 指定入口文件 | `deployctl deploy --entry-url={url} ./server.ts` | **url**: 自定义入口 URL |
| 部署带权限 | `deployctl deploy --allow-net=:8000 --allow-read ./server.ts` | 指定权限部署 |
| 列出部署项目 | `deployctl projects list` | 查看所有部署项目 |
| 查看部署日志 | `deployctl logs --project={project}` | 查看项目运行日志 |

---

## Supabase Edge Functions

### supabase functions new - 创建函数

**基础用法**:
```bash
supabase functions new %{name}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建新函数 | `supabase functions new {name}` | **name**: 函数名, 示例: `hello-world` |
| 使用模板创建 | `supabase functions new {name} --template-url {url}` | 从模板创建 |
| 指定分析器 | `supabase functions new {name} --no-verify-jwt` | 禁用 JWT 验证 |

### supabase functions serve - 本地运行

**基础用法**:
```bash
supabase functions serve %{name}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动函数服务 | `supabase functions serve {name} --env-file ./env.json` | 加载环境变量文件 |
| 指定端口 | `supabase functions serve {name} --port {port}` | **port**: 端口号, 示例: `3000` |
| 热重载模式 | `supabase functions serve {name} --reload` | 文件变化自动重载 |

### supabase functions deploy - 部署函数

**基础用法**:
```bash
supabase functions deploy %{name}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 部署单个函数 | `supabase functions deploy {name}` | **【常用】name**: 函数名 |
| 部署所有函数 | `supabase functions deploy` | 部署项目中所有函数 |
| 指定引用密钥 | `supabase functions deploy {name} --no-verify-jwt` | 禁用 JWT 验证部署 |
| 设置环境变量 | `supabase functions deploy {name} --env-secrets FILE=./secrets.toml` | 部署时注入密钥 |

### supabase functions logs - 查看日志

**基础用法**:
```bash
supabase functions logs %{name}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看函数日志 | `supabase functions logs {name}` | **【常用】name**: 函数名 |
| 指定时间范围 | `supabase functions logs {name} --since {duration}` | **duration**: 时间范围, 示例: `1h`, `24h` |
| 实时跟踪日志 | `supabase functions logs {name} --follow` | 持续监控日志 |

---

## 实用场景

### AWS Lambda 完整生命周期

```bash
# 1. 创建函数
aws lambda create-function \
  --function-name my-function \
  --runtime nodejs18.x \
  --role arn:aws:iam::123456789012:role/lambda-ex \
  --handler index.handler \
  --zip-file fileb://function.zip

# 2. 同步调用测试
aws lambda invoke \
  --function-name my-function \
  --payload '{"name": "world"}' \
  --log-type Tail \
  output.json

# 3. 异步调用（事件驱动）
aws lambda invoke \
  --function-name my-function \
  --invocation-type Event \
  output.json

# 4. 更新函数代码
aws lambda update-function-code \
  --function-name my-function \
  --zip-file fileb://new-function.zip

# 5. 更新配置（内存/超时）
aws lambda update-function-configuration \
  --function-name my-function \
  --memory-size 512 \
  --timeout 60

# 6. 查看函数配置
aws lambda get-function-configuration --function-name my-function
```

### SAM CLI 完整开发流程

```bash
# 1. 初始化项目
sam init --name my-app --runtime nodejs18.x --app-template hello-world

# 2. 进入项目目录
cd my-app

# 3. 构建
sam build

# 4. 本地测试
sam local invoke HelloWorldFunction --event events/event.json

# 5. 引导式部署
sam deploy --guided

# 6. 查看输出
aws cloudformation describe-stacks --stack-name my-app --query 'Stacks[0].Outputs'

# 7. 更新部署
sam build && sam deploy
```

### Serverless Framework 部署到 AWS

```bash
# 1. 配置 AWS 凭证
serverless config credentials --provider aws --key AKIA... --secret xxxx

# 2. 创建服务
serverless create --template aws-nodejs --path my-service

# 3. 进入目录
cd my-service

# 4. 编辑 serverless.yml 后部署
serverless deploy --stage prod --region us-east-1

# 5. 调用测试
serverless invoke --function hello --stage prod --data '{"name": "test"}'

# 6. 查看日志
serverless logs --function hello --stage prod --tail

# 7. 单函数快速更新
serverless deploy --function hello
```

### Vercel 完整部署流程

```bash
# 1. 登录（交互式）
vercel login

# 2. 拉取环境变量
vercel env pull .env.local

# 3. 本地预览部署
vercel

# 4. 生产环境部署
vercel --prod

# 5. 查看部署详情
vercel inspect <deployment_id>

# 6. 查看日志
vercel logs <url> --tail

# 7. 添加密钥
vercel secrets add API_KEY "my-secret-value"

# 8. 删除旧部署
vercel remove <old_deployment_id>
```

### Netlify 函数开发流程

```bash
# 1. 初始化
netlify init

# 2. 创建 Serverless 函数
netlify functions:create hello

# 3. 本地测试
netlify functions:invoke hello --no-open

# 4. 部署函数
netlify deploy --prod --functions ./functions

# 5. 设置环境变量
netlify env:set DATABASE_URL "postgres://..."
netlify env:set API_KEY "xxx"

# 6. 查看函数日志
netlify functions:list
```

### Cloudflare Workers 完整流程

```bash
# 1. 初始化项目
wrangler init my-worker

# 2. 开发模式
cd my-worker
wrangler dev --port 8787

# 3. 设置密钥
wrangler secret put API_TOKEN

# 4. 部署
wrangler deploy

# 5. 测试
curl https://my-worker.workers.dev

# 6. 查看日志
wrangler logs --name my-worker

# 7. KV 存储操作
wrangler kv:namespace create MY_KV
wrangler kv:key put "key1" "value1" --namespace-id <id>
wrangler kv:key get "key1" --namespace-id <id>
```

### Supabase Edge Functions 开发流程

```bash
# 1. 登录 Supabase CLI
supabase login

# 2. 初始化本地开发
supabase init

# 3. 创建 Edge Function
supabase functions new hello-world

# 4. 本地运行测试
supabase functions serve hello-world --port 3000

# 5. 本地触发测试
curl -X POST http://localhost:3000/functions/v1/hello-world \
  -H "Content-Type: application/json" \
  -d '{"name": "World"}'

# 6. 部署到生产
supabase functions deploy hello-world

# 7. 查看日志
supabase functions logs hello-world
```

---

## 相关资源

- [AWS CLI 命令文档](../AWS CLI命令/README.md)
- [CI/CD 流水线文档](../CI_CD 流水线/README.md)
- [Docker 命令文档](../Docker 命令/README.md)
- [Kubernetes 命令文档](../Kubernetes 命令/README.md)
