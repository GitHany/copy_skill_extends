# AWS CLI 命令文档

AWS CLI 完整参考文档，覆盖核心配置、计算、存储、数据库、网络、部署等常用场景。

## 目录

- [基础配置](#基础配置)
- [计算 (EC2)](#计算-ec2)
- [函数计算 (Lambda)](#函数计算-lambda)
- [对象存储 (S3)](#对象存储-s3)
- [关系型数据库 (RDS)](#关系型数据库-rds)
- [文档数据库 (DynamoDB)](#文档数据库-dynamodb)
- [网络与 CDN](#网络与-cdn)
- [容器服务 (ECS)](#容器服务-ecs)
- [身份与访问管理 (IAM)](#身份与访问管理-iam)
- [监控与日志 (CloudWatch)](#监控与日志-cloudwatch)
- [其他服务](#其他服务)

---

## 基础配置

### aws configure - 配置凭证

**基础用法**:
```bash
aws configure
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 配置 Access Key | `aws configure set aws_access_key_id {access_key}` | **access_key**: AWS Access Key ID, 示例: `AKIAIOSFODNN7EXAMPLE` |
| 配置默认区域 | `aws configure set region {region}` | **region**: AWS 区域, 示例: `us-east-1` |
| 配置输出格式 | `aws configure set output {format}` | **format**: 输出格式, 示例: `json` (可选: json/text/table) |
| 配置多账号 Profile | `aws configure --profile {profile}` | **profile**: Profile 名称, 示例: `my-profile` |
| 查看当前配置 | `aws configure list` | 查看所有配置项 |

### aws sts get-caller-identity - 查看身份

**基础用法**:
```bash
aws sts get-caller-identity
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 验证凭证有效性 | `aws sts get-caller-identity` | 最常用场景：确认当前凭证是否有效 |
| 使用指定 Profile | `aws sts get-caller-identity --profile {profile}` | **profile**: Profile 名称, 示例: `prod` |
| 指定区域 | `aws sts get-caller-identity --region {region}` | **region**: 区域, 示例: `us-east-1` |

### aws help - 查看帮助

**基础用法**:
```bash
aws help
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看所有服务 | `aws help` | 列出所有可用的 AWS 服务 |
| 查看服务帮助 | `aws {service} help` | **service**: 服务名称, 示例: `ec2`, `s3`, `lambda` |
| 查看命令帮助 | `aws {service} {command} help` | **command**: 服务命令, 示例: `describe-instances` |

---

## 计算 (EC2)

### aws ec2 describe-instances - 查看实例

**基础用法**:
```bash
aws ec2 describe-instances
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 按状态筛选 | `aws ec2 describe-instances --filters "Name=instance-state-name,Values={state}"` | **state**: 实例状态, 示例: `running` (可选: pending/running/stopped/terminated) |
| 按标签筛选 | `aws ec2 describe-instances --filters "Name=tag:Name,Values={tag_value}"` | **tag_value**: 标签值, 示例: `web-server` |
| 查看指定实例 | `aws ec2 describe-instances --instance-ids {instance_id}` | **instance_id**: 实例 ID, 示例: `i-0abcd1234efgh5678` |
| 指定区域 | `aws ec2 describe-instances --region {region}` | **region**: 区域, 示例: `us-east-1` |
| 查询公网 IP | `aws ec2 describe-instances --query 'Reservations[*].Instances[*].{ID:InstanceId,IP:PublicIpAddress}' --output table` | 表格形式展示实例 ID 和公网 IP |

### aws ec2 run-instances - 启动实例

**基础用法**:
```bash
aws ec2 run-instances --image-id %{ami_id}% --instance-type %{instance_type}% --count %{count}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 带密钥对启动 | `aws ec2 run-instances --image-id {ami_id} --instance-type {instance_type} --key-name {key_name}` | **【常用】ami_id**: AMI ID, 示例: `ami-0c55b159cbfafe1f0`; **instance_type**: 实例类型, 示例: `t2.micro`; **key_name**: 密钥对名称, 示例: `my-key-pair` |
| 带安全组启动 | `aws ec2 run-instances --image-id {ami_id} --instance-type {instance_type} --security-group-ids {sg_id}` | **sg_id**: 安全组 ID, 示例: `sg-0abcd1234efgh5678` |
| 带子网启动 | `aws ec2 run-instances --image-id {ami_id} --instance-type {instance_type} --subnet-id {subnet_id}` | **subnet_id**: 子网 ID, 示例: `subnet-0abcd1234efgh5678` |
| 带用户数据启动 | `aws ec2 run-instances --image-id {ami_id} --instance-type {instance_type} --user-data file://{script}` | **script**: 启动脚本路径, 示例: `userdata.sh` |
| 带标签启动 | `aws ec2 run-instances --image-id {ami_id} --instance-type {instance_type} --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value={name}}]'` | **【常用】name**: 实例名称, 示例: `web-server` |

### aws ec2 create-security-group - 创建安全组

**基础用法**:
```bash
aws ec2 create-security-group --group-name %{group_name}% --description "%{description}%"
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 在指定 VPC 创建 | `aws ec2 create-security-group --group-name {group_name} --description "{description}" --vpc-id {vpc_id}` | **【常用】group_name**: 安全组名称, 示例: `my-security-group`; **description**: 安全组描述; **vpc_id**: VPC ID, 示例: `vpc-0abcd1234efgh5678` |
| 带标签创建 | `aws ec2 create-security-group --group-name {group_name} --description "{description}" --tag-specifications 'ResourceType=security-group,Tags=[{Key=Name,Value={name}}]'` | **name**: 标签名称, 示例: `web-sg` |

### aws ec2 authorize-security-group-ingress - 添加入站规则

**基础用法**:
```bash
aws ec2 authorize-security-group-ingress --group-id %{group_id}% --protocol %{protocol}% --port %{port}% --cidr %{cidr}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 开放 SSH 访问 | `aws ec2 authorize-security-group-ingress --group-id {group_id} --protocol tcp --port 22 --cidr {cidr}` | **【常用】group_id**: 安全组 ID, 示例: `sg-0abcd1234efgh5678`; **cidr**: 来源 CIDR, 示例: `0.0.0.0/0` |
| 开放 HTTP 访问 | `aws ec2 authorize-security-group-ingress --group-id {group_id} --protocol tcp --port 80 --cidr 0.0.0.0/0` | HTTP 80 端口对所有来源开放 |
| 开放 HTTPS 访问 | `aws ec2 authorize-security-group-ingress --group-id {group_id} --protocol tcp --port 443 --cidr 0.0.0.0/0` | HTTPS 443 端口对所有来源开放 |
| 开放 MySQL 端口 | `aws ec2 authorize-security-group-ingress --group-id {group_id} --protocol tcp --port 3306 --cidr {cidr}` | **cidr**: MySQL 访问来源限制, 示例: `10.0.0.0/8` |
| 开放端口范围 | `aws ec2 authorize-security-group-ingress --group-id {group_id} --protocol tcp --port {start_port}-{end_port} --cidr 0.0.0.0/0` | **start_port/end_port**: 端口范围, 示例: `8000-9000` |
| 引用其他安全组 | `aws ec2 authorize-security-group-ingress --group-id {group_id} --protocol {protocol} --port {port} --source-group {source_sg}` | **source_sg**: 源安全组 ID, 替代 cidr 使用 |

### aws ec2 allocate-address - 分配弹性 IP

**基础用法**:
```bash
aws ec2 allocate-address
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 分配 VPC 弹性 IP | `aws ec2 allocate-address --domain vpc` | 在 VPC 中分配弹性 IP |
| 指定区域分配 | `aws ec2 allocate-address --region {region}` | **region**: 区域, 示例: `us-east-1` |

### aws ec2 associate-address - 关联弹性 IP

**基础用法**:
```bash
aws ec2 associate-address --instance-id %{instance_id}% --allocation-id %{allocation_id}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 关联并允许重绑定 | `aws ec2 associate-address --instance-id {instance_id} --allocation-id {allocation_id} --allow-reassociation` | **【常用】instance_id**: 实例 ID, 示例: `i-0abcd1234efgh5678`; **allocation_id**: 弹性 IP 分配 ID, 示例: `eipalloc-0abcd1234efgh5678` |
| 关联到网络接口 | `aws ec2 associate-address --network-interface-id {eni_id} --allocation-id {allocation_id}` | **eni_id**: 网络接口 ID, 示例: `eni-0abcd1234efgh5678` |
| 指定私有 IP 关联 | `aws ec2 associate-address --instance-id {instance_id} --allocation-id {allocation_id} --private-ip-address {private_ip}` | **private_ip**: 私有 IP, 示例: `10.0.1.100` |

---

## 函数计算 (Lambda)

### aws lambda invoke - 调用函数

**基础用法**:
```bash
aws lambda invoke --function-name %{function_name}% %{output_file}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 同步调用并获取日志 | `aws lambda invoke --function-name {function_name} --payload '{payload}' --log-type Tail {output_file}` | **【常用】function_name**: 函数名称, 示例: `my-lambda-function`; **output_file**: 输出文件, 示例: `output.json`; **payload**: JSON 格式负载, 示例: `{"key": "value"}` |
| 异步调用 | `aws lambda invoke --function-name {function_name} --invocation-type Event {output_file}` | Event 调用不等待响应 |
| 指定版本/别名调用 | `aws lambda invoke --function-name {function_name} --qualifier {qualifier} {output_file}` | **qualifier**: 版本或别名, 示例: `prod`, `$LATEST` |
| 从文件读取 Payload | `aws lambda invoke --function-name {function_name} --payload file://{payload_file} {output_file}` | **payload_file**: 负载文件路径, 示例: `input.json` |
| Dry Run 模式 | `aws lambda invoke --function-name {function_name} --invocation-type DryRun {output_file}` | 验证调用是否有效，不实际执行 |

---

## 对象存储 (S3)

### aws s3 ls - 列出存储桶

**基础用法**:
```bash
aws s3 ls
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 列出桶内容 | `aws s3 ls s3://{bucket_name}/` | **bucket_name**: 存储桶名称, 示例: `my-bucket` |
| 递归列出 | `aws s3 ls s3://{bucket_name}/ --recursive` | 递归列出所有对象 |
| 按前缀筛选 | `aws s3 ls s3://{bucket_name}/{prefix}` | **prefix**: 对象键前缀, 示例: `images/` |
| 显示统计 | `aws s3 ls s3://{bucket_name}/ --recursive --summarize` | 显示对象总数和大小 |
| 分页查询 | `aws s3api list-objects-v2 --bucket {bucket_name} --max-items {max_items}` | **max_items**: 最大返回数量, 示例: `100` |

### aws s3 mb - 创建存储桶

**基础用法**:
```bash
aws s3 mb s3://%{bucket_name}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 在指定区域创建 | `aws s3 mb s3://{bucket_name} --region {region}` | **【常用】bucket_name**: 存储桶名称, 示例: `my-unique-bucket-name`（全局唯一）; **region**: 区域, 示例: `us-east-1` |
| 设置 ACL | `aws s3 mb s3://{bucket_name} --acl {acl}` | **acl**: 访问控制, 示例: `public-read` |
| 带标签创建 | `aws s3api create-bucket --bucket {bucket_name} --tagging 'TagSet=[{Key=Environment,Value={env}}]'` | **env**: 环境标签值, 示例: `production` |

### aws s3 cp - 复制对象

**基础用法**:
```bash
aws s3 cp %{source}% s3://%{bucket_name}%/%{key}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 下载文件 | `aws s3 cp s3://{bucket_name}/{key} {local_path}` | **【常用】source**: 源路径; **bucket_name/key**: 目标路径; **local_path**: 本地路径, 示例: `./downloads/file.txt` |
| 设置 ACL | `aws s3 cp {source} s3://{bucket_name}/{key} --acl {acl}` | **acl**: 访问权限, 示例: `public-read` |
| 设置存储类型 | `aws s3 cp {source} s3://{bucket_name}/{key} --storage-class {storage_class}` | **storage_class**: 存储类型, 示例: `STANDARD_IA`, `GLACIER` |
| 递归复制目录 | `aws s3 cp {dir_path} s3://{bucket_name}/{prefix} --recursive` | **dir_path**: 目录路径, 示例: `./uploads/`; **prefix**: 目标前缀, 示例: `backup/` |
| 只复制新文件 | `aws s3 cp {source} s3://{bucket_name}/{key} --size-only` | 根据文件大小判断是否复制 |
| 排除文件 | `aws s3 cp {source} s3://{bucket_name}/{key} --exclude "{pattern}" --recursive` | **pattern**: 排除模式, 示例: `*.tmp` |

### aws s3 sync - 同步目录

**基础用法**:
```bash
aws s3 sync %{source}% s3://%{bucket_name}%/%{prefix}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 下载同步 | `aws s3 sync s3://{bucket_name}/{prefix} {local_dir}` | **local_dir**: 本地目录, 示例: `./downloads/` |
| 同步并删除多余文件 | `aws s3 sync {source} s3://{bucket_name}/{prefix} --delete` | 删除目标中有而源中没有的文件 |
| 同步并排除文件 | `aws s3 sync {source} s3://{bucket_name}/{prefix} --exclude "{pattern}"` | **pattern**: 排除模式, 示例: `*.git/*` |
| 只同步新增文件 | `aws s3 sync {source} s3://{bucket_name}/{prefix} --size-only` | 仅复制大小变化的文件 |
| 显示同步进度 | `aws s3 sync {source} s3://{bucket_name}/{prefix} --progress` | 显示实时传输进度 |

### aws s3 rm - 删除对象

**基础用法**:
```bash
aws s3 rm s3://%{bucket_name}%/%{key}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 递归删除 | `aws s3 rm s3://{bucket_name}/{prefix} --recursive` | **【常用】bucket_name**: 存储桶名称; **prefix**: 前缀, 示例: `temp/` |
| 删除空桶 | `aws s3 rb s3://{bucket_name}` | 删除空存储桶 |
| 强制删除非空桶 | `aws s3 rb s3://{bucket_name} --force` | 强制删除存储桶（包含所有对象） |
| 按大小过滤删除 | `aws s3 rm s3://{bucket_name}/{prefix} --recursive --size {size}` | **size**: 文件大小过滤, 示例: `10MB` |

### aws s3api put-object - 上传对象

**基础用法**:
```bash
aws s3api put-object --bucket %{bucket_name}% --key %{key}% --body %{file_path}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 设置内容类型 | `aws s3api put-object --bucket {bucket_name} --key {key} --body {file_path} --content-type {content_type}` | **【常用】bucket_name/key/file_path**: 存储桶/键/文件路径; **content_type**: 内容类型, 示例: `image/jpeg` |
| 设置缓存控制 | `aws s3api put-object --bucket {bucket_name} --key {key} --body {file_path} --cache-control "max-age=3600"` | 设置浏览器缓存策略 |
| 设置元数据 | `aws s3api put-object --bucket {bucket_name} --key {key} --body {file_path} --metadata '{metadata}'` | **metadata**: 元数据, 示例: `{"Author": "John"}` |
| 启用服务器加密 | `aws s3api put-object --bucket {bucket_name} --key {key} --body {file_path} --server-side-encryption AES256` | 使用 SSE-S3 加密存储 |

### aws s3api get-object - 下载对象

**基础用法**:
```bash
aws s3api get-object --bucket %{bucket_name}% --key %{key}% %{file_path}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 下载指定版本 | `aws s3api get-object --bucket {bucket_name} --key {key} --version-id {version_id} {file_path}` | **【常用】bucket_name/key/file_path**: 存储桶/键/保存路径; **version_id**: 对象版本 ID, 示例: `abc123` |
| 下载到指定文件 | `aws s3api get-object --bucket {bucket_name} --key {key} {file_path}` | 直接指定本地保存路径 |

---

## 关系型数据库 (RDS)

### aws rds describe-db-instances - 查看实例

**基础用法**:
```bash
aws rds describe-db-instances
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看指定实例 | `aws rds describe-db-instances --db-instance-identifier {db_instance_id}` | **db_instance_id**: 数据库实例标识符, 示例: `my-db-instance` |
| 按标签筛选 | `aws rds describe-db-instances --filters "Name=tag:Name,Values={tag_value}"` | **tag_value**: 标签值, 示例: `production` |
| 指定区域 | `aws rds describe-db-instances --region {region}` | **region**: 区域, 示例: `us-east-1` |
| 查询端点信息 | `aws rds describe-db-instances --query 'DBInstances[*].{ID:DBInstanceIdentifier,Endpoint:Endpoint.Address}' --output table` | 表格形式展示实例端点 |

### aws rds create-db-instance - 创建实例

**基础用法**:
```bash
aws rds create-db-instance --db-instance-identifier %{db_instance_id}% --db-instance-class %{db_instance_class}% --engine %{engine}% --allocated-storage %{allocated_storage}% --master-username %{master_username}% --master-user-password %{master_user_password}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 MySQL 实例 | `aws rds create-db-instance --db-instance-identifier {db_instance_id} --db-instance-class db.t3.micro --engine mysql --allocated-storage 20 --master-username admin --master-user-password {password}` | **【常用】db_instance_id**: 标识符, 示例: `my-database`; **password**: 密码, 示例: `MyPassword123` |
| 创建 PostgreSQL 实例 | `aws rds create-db-instance --db-instance-identifier {db_instance_id} --db-instance-class db.t3.micro --engine postgres --allocated-storage 20 --master-username postgres --master-user-password {password}` | PostgreSQL 引擎 |
| 带备份策略创建 | `aws rds create-db-instance ... --backup-retention-period 7 --preferred-backup-window "03:00-04:00"` | 保留 7 天备份，凌晨 3-4 点备份 |
| 创建多可用区实例 | `aws rds create-db-instance ... --multi-az` | 高可用多可用区部署 |
| 在指定子网组创建 | `aws rds create-db-instance ... --db-subnet-group-name {subnet_group}` | **subnet_group**: 子网组名称, 示例: `my-db-subnet-group` |

---

## 文档数据库 (DynamoDB)

### aws dynamodb list-tables - 列出表

**基础用法**:
```bash
aws dynamodb list-tables
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 限制返回数量 | `aws dynamodb list-tables --max-items {max_items}` | **max_items**: 最大返回数量, 示例: `10` |
| 分页查询 | `aws dynamodb list-tables --starting-token {token}` | **token**: 分页 Token, 示例: `abc123` |
| 指定区域 | `aws dynamodb list-tables --region {region}` | **region**: 区域, 示例: `us-east-1` |

### aws dynamodb scan - 全表扫描

**基础用法**:
```bash
aws dynamodb scan --table-name %{table_name}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 只返回部分属性 | `aws dynamodb scan --table-name {table_name} --projection-expression "{attrs}"` | **【常用】table_name**: 表名称, 示例: `Users`; **attrs**: 属性名, 示例: `user_id, name, email` |
| 按条件过滤 | `aws dynamodb scan --table-name {table_name} --filter-expression "{filter}"` | **filter**: 过滤表达式, 示例: `age > :age` |
| 限制返回数 | `aws dynamodb scan --table-name {table_name} --max-items {max_items}` | **max_items**: 最大返回数量, 示例: `100` |
| 并行扫描 | `aws dynamodb scan --table-name {table_name} --segment {segment} --total-segments {total_segments}` | **segment/total_segments**: 段编号/总段数, 示例: `0/4`（并行加速大数据表扫描） |

### aws dynamodb query - 查询项目

**基础用法**:
```bash
aws dynamodb query --table-name %{table_name}% --key-condition-expression "%{key_expr}%"
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 带参数值查询 | `aws dynamodb query --table-name {table_name} --key-condition-expression "{key_expr}" --expression-attribute-values '{values}'` | **【常用】table_name/key_expr**: 表名和主键条件, 示例: `user_id = :uid`; **values**: 表达式值, 示例: `{":uid": {"S": "user123"}}` |
| 带过滤条件 | `aws dynamodb query --table-name {table_name} --key-condition-expression "{key_expr}" --filter-expression "{filter}"` | **filter**: 过滤表达式, 示例: `#age > :min_age` |
| 只返回特定属性 | `aws dynamodb query --table-name {table_name} --key-condition-expression "{key_expr}" --projection-expression "{attrs}"` | **attrs**: 返回属性列表, 示例: `user_id, name` |
| 降序排列 | `aws dynamodb query --table-name {table_name} --key-condition-expression "{key_expr}" --scan-index-forward false` | 按倒序返回结果 |

---

## 网络与 CDN

### aws elbv2 describe-load-balancers - 查看负载均衡器

**基础用法**:
```bash
aws elbv2 describe-load-balancers
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看指定 LB | `aws elbv2 describe-load-balancers --load-balancer-arns {arn}` | **arn**: 负载均衡器 ARN, 示例: `arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/my-alb/abc123` |
| 按名称筛选 | `aws elbv2 describe-load-balancers --names {name}` | **name**: 负载均衡器名称, 示例: `my-alb` |
| 查询 DNS 名称 | `aws elbv2 describe-load-balancers --query 'LoadBalancers[*].{Name:LoadBalancerName,DNS:DNSName}' --output table` | 表格形式展示名称和 DNS |
| 查看目标组 | `aws elbv2 describe-target-groups --load-balancer-arn {arn}` | 查看 ALB 关联的目标组 |

### aws route53 list-hosted-zones - 查看托管区域

**基础用法**:
```bash
aws route53 list-hosted-zones
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 限制返回数量 | `aws route53 list-hosted-zones --max-items {max_items}` | **max_items**: 最大返回数量, 示例: `10` |
| 分页查询 | `aws route53 list-hosted-zones --marker {marker}` | **marker**: 分页标记, 示例: `abc` |
| 查看记录数统计 | `aws route53 list-hosted-zones --query 'HostedZones[*].{Name:Name,Records:ResourceRecordSetCount}' --output table` | 表格形式展示托管区和记录数 |
| 列出 DNS 记录 | `aws route53 list-resource-record-sets --hosted-zone-id {zone_id}` | **zone_id**: 托管区域 ID, 示例: `Z1234567890ABC` |

### aws cloudfront create-distribution - 创建 CDN 分发

**基础用法**:
```bash
aws cloudfront create-distribution --origin-domain-name %{origin_domain}% --default-root-object %{root_object}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 设置缓存策略 | `aws cloudfront create-distribution --origin-domain-name {origin_domain} --origin-protocol-policy {protocol}` | **【常用】origin_domain**: 源站域名, 示例: `my-bucket.s3.amazonaws.com`; **protocol**: 协议策略, 示例: `https-only` |
| 设置 SSL 证书 | `aws cloudfront create-distribution --origin-domain-name {origin_domain} --viewer-certificate {cert}` | **cert**: 证书配置, 示例: `ACMCertificateArn=arn:aws:acm:us-east-1:123:certificate/abc` |
| 设置价格分级 | `aws cloudfront create-distribution --origin-domain-name {origin_domain} --price-class {price_class}` | **price_class**: 价格分级, 示例: `PriceClass_All` (全球) / `PriceClass_200` (主要) / `PriceClass_100` (仅北美) |
| 设置备用域名 | `aws cloudfront create-distribution --origin-domain-name {origin_domain} --aliases {aliases}` | **aliases**: 备用域名, 示例: `example.com,www.example.com` |
| 列出分发 | `aws cloudfront list-distributions` | 查看所有 CDN 分发 |

---

## 容器服务 (ECS)

### aws ecs run-task - 运行任务

**基础用法**:
```bash
aws ecs run-task --cluster %{cluster}% --task-definition %{task_definition}% --launch-type %{launch_type}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定网络配置 | `aws ecs run-task --cluster {cluster} --task-definition {task_definition} --network-configuration 'awsvpcConfiguration={subnets=[{subnet}],securityGroups=[{sg_id}]}'` | **【常用】cluster**: 集群名称, 示例: `my-cluster`; **task_definition**: 任务定义, 示例: `my-task:1`; **subnet**: 子网 ID; **sg_id**: 安全组 ID |
| 覆盖任务定义 | `aws ecs run-task --cluster {cluster} --task-definition {task_definition} --overrides '{overrides}'` | **overrides**: 任务覆盖 JSON, 示例: `{"containerOverrides":[]}` |
| 指定容器命令 | `aws ecs run-task --cluster {cluster} --task-definition {task_definition} --overrides '{"containerOverrides":[{"name":"{container_name}","command":["{cmd}"]}]}'` | **container_name**: 容器名称, 示例: `web`; **cmd**: 启动命令, 示例: `python app.py` |
| 查看集群任务 | `aws ecs list-tasks --cluster {cluster}` | 列出集群中所有运行中的任务 |

### aws ecs describe-services - 查看服务

**基础用法**:
```bash
aws ecs describe-services --cluster %{cluster}% --services %{service}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看多个服务 | `aws ecs describe-services --cluster {cluster} --services {service1} {service2}` | **【常用】cluster/service**: 集群和服务名称, 示例: `my-cluster`/`my-service` |
| 查询任务数量 | `aws ecs describe-services --cluster {cluster} --services {service} --query 'services[*].{Name:serviceName,Running:sRunningTaskCount,Desired:sDesiredCount}' --output table` | 表格形式展示运行/期望任务数 |
| 查看完整任务定义 | `aws ecs describe-services --cluster {cluster} --services {service} --include TASK_DEFINITION` | 包含完整任务定义详情 |
| 列出所有服务 | `aws ecs list-services --cluster {cluster}` | 列出集群中所有服务定义 |

---

## 身份与访问管理 (IAM)

### aws iam create-user - 创建 IAM 用户

**基础用法**:
```bash
aws iam create-user --user-name %{user_name}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 带标签创建 | `aws iam create-user --user-name {user_name} --tags '[{"Key": "Department", "Value": "{dept}"}]'` | **【常用】user_name**: 用户名, 示例: `my-user`; **dept**: 部门标签, 示例: `Engineering` |
| 创建访问密钥 | `aws iam create-access-key --user-name {user_name}` | 为用户创建新的 AccessKey |
| 列出所有用户 | `aws iam list-users` | 查看所有 IAM 用户 |
| 附加管理策略 | `aws iam attach-user-policy --user-name {user_name} --policy-arn {policy_arn}` | **policy_arn**: 策略 ARN, 示例: `arn:aws:iam::aws:policy/ReadOnlyAccess` |

### aws sts assume-role - 角色扮演

**基础用法**:
```bash
aws sts assume-role --role-arn %{role_arn}% --role-session-name %{session_name}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 跨账号角色扮演 | `aws sts assume-role --role-arn {role_arn} --role-session-name {session_name} --duration-seconds {duration}` | **【常用】role_arn**: 角色 ARN, 示例: `arn:aws:iam::123456789012:role/MyRole`; **session_name**: 会话名称, 示例: `my-session`; **duration**: 持续时间, 示例: `3600` |
| 带外部 ID 角色扮演 | `aws sts assume-role --role-arn {role_arn} --role-session-name {session_name} --external-id {external_id}` | **external_id**: 外部 ID, 示例: `my-external-id`（第三方访问场景） |
| 导出临时凭证 | `export AWS_ACCESS_KEY_ID=$(aws sts assume-role --role-arn {role_arn} ... --query 'Credentials.AccessKeyId' --output text) && export AWS_SECRET_ACCESS_KEY=... && export AWS_SESSION_TOKEN=...` | 将临时凭证导出为环境变量 |
| 配置 Profile 使用角色 | `aws configure set source_profile default --profile {profile} && aws configure set role_arn {role_arn} --profile {profile}` | **profile**: Profile 名称, 示例: `prod-role`（持久化角色配置） |

---

## 监控与日志 (CloudWatch)

### aws cloudwatch put-metric-data - 上报指标

**基础用法**:
```bash
aws cloudwatch put-metric-data --namespace %{namespace}% --metric-name %{metric_name}% --value %{value}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 带单位上报 | `aws cloudwatch put-metric-data --namespace {namespace} --metric-name {metric_name} --value {value} --unit {unit}` | **【常用】namespace**: 命名空间, 示例: `MyApplication`; **metric_name/value**: 指标名/值, 示例: `RequestCount`/`100`; **unit**: 单位, 示例: `Count` |
| 带维度上报 | `aws cloudwatch put-metric-data --namespace {namespace} --metric-name {metric_name} --value {value} --dimensions {dim_name}={dim_value}` | **dim_name/dim_value**: 维度名称/值, 示例: `InstanceId`/`i-0abcd1234efgh5678` |
| 批量上报多条指标 | `aws cloudwatch put-metric-data --namespace {namespace} --metric-data '[{"MetricName":"{m1}","Value":{v1}},{"MetricName":"{m2}","Value":{v2}}]'` | **m1/v1/m2/v2**: 多指标名称和值, 示例: `CPU`/`75`/`Memory`/`60` |
| 查看指标统计 | `aws cloudwatch get-metric-statistics --namespace {namespace} --metric-name {metric_name} --start-time {start} --end-time {end} --period {period} --statistics Average` | **start/end**: ISO8601 时间; **period**: 周期（秒）, 示例: `60` |

### aws logs describe-log-groups - 查看日志组

**基础用法**:
```bash
aws logs describe-log-groups
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 按前缀筛选 | `aws logs describe-log-groups --log-group-name-prefix {prefix}` | **prefix**: 日志组名前缀, 示例: `/aws/lambda/` |
| 查询日志流 | `aws logs describe-log-streams --log-group-name {log_group}` | **log_group**: 日志组名称, 示例: `/aws/lambda/my-function` |
| 查看日志事件 | `aws logs filter-log-events --log-group-name {log_group}` | 查看日志组中的日志事件 |
| 创建日志组 | `aws logs create-log-group --log-group-name {log_group}` | 新建 CloudWatch Logs 日志组 |
| 设置保留期 | `aws logs put-retention-policy --log-group-name {log_group} --retention-in-days {days}` | **days**: 保留天数, 示例: `30` (可选: 1/3/5/7/14/30/60/90/120/150/180/365/400/545/731/1827/3653) |

---

## 其他服务

### aws efs describe-file-systems - 查看 EFS

**基础用法**:
```bash
aws efs describe-file-systems
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看指定文件系统 | `aws efs describe-file-systems --file-system-id {fs_id}` | **fs_id**: 文件系统 ID, 示例: `fs-0abcd1234efgh5678` |
| 查询挂载目标 | `aws efs describe-mount-targets --file-system-id {fs_id}` | 查看 EFS 的挂载目标 |
| 创建文件系统 | `aws efs create-file-system --creation-token {token}` | **token**: 创建令牌, 示例: `my-unique-token` |
| 挂载到 EC2 | `sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 {efs_dns}:/ {mount_point}` | **efs_dns**: EFS DNS 名称; **mount_point**: 挂载点, 示例: `/mnt/efs` |

### aws elasticache describe-cache-clusters - 查看缓存集群

**基础用法**:
```bash
aws elasticache describe-cache-clusters
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看指定集群 | `aws elasticache describe-cache-clusters --cache-cluster-id {cluster_id}` | **cluster_id**: 缓存集群 ID, 示例: `my-redis-cluster` |
| 查看 Redis 节点 | `aws elasticache describe-cache-clusters --cache-cluster-id {cluster_id} --show-cache-node-info` | 包含节点详细信息 |
| 查看复制组 | `aws elasticache describe-replication-groups --replication-group-id {rg_id}` | **rg_id**: 复制组 ID, 示例: `my-replication-group` |
| 创建 Redis 集群 | `aws elasticache create-cache-cluster --cache-cluster-id {cluster_id} --engine redis --cache-node-type {node_type} --num-cache-nodes {num_nodes}` | **node_type**: 节点类型, 示例: `cache.t3.micro`; **num_nodes**: 节点数量, 示例: `2` |

---

## 实用场景

### 快速环境验证

```bash
# 1. 验证凭证有效性
aws sts get-caller-identity

# 2. 查看当前配置
aws configure list

# 3. 切换到生产环境 Profile
export AWS_PROFILE=prod
aws sts get-caller-identity
```

### EC2 快速部署

```bash
# 1. 创建安全组
aws ec2 create-security-group --group-name web-sg --description "Web server security group" --vpc-id vpc-0abcd1234efgh5678

# 2. 开放端口
aws ec2 authorize-security-group-ingress --group-id sg-0abcd1234efgh5678 --protocol tcp --port 22 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-id sg-0abcd1234efgh5678 --protocol tcp --port 80 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-id sg-0abcd1234efgh5678 --protocol tcp --port 443 --cidr 0.0.0.0/0

# 3. 启动实例
aws ec2 run-instances --image-id ami-0c55b159cbfafe1f0 --instance-type t2.micro --key-name my-key-pair --security-group-ids sg-0abcd1234efgh5678 --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=web-server}]'

# 4. 查看实例状态
aws ec2 describe-instances --filters "Name=tag:Name,Values=web-server"
```

### S3 静态网站部署

```bash
# 1. 创建存储桶
aws s3 mb s3://my-static-website --region us-east-1

# 2. 上传网站文件
aws s3 cp ./dist/ s3://my-static-website/ --recursive --cache-control "max-age=31536000"

# 3. 同步更新文件
aws s3 sync ./dist/ s3://my-static-website/ --delete

# 4. 设置公开访问
aws s3api put-object --bucket my-static-website --key index.html --body ./dist/index.html --content-type text/html --acl public-read
```

### Lambda 函数调用

```bash
# 1. 查看函数列表
aws lambda list-functions

# 2. 同步调用函数
aws lambda invoke --function-name my-function --payload '{"name": "test"}' output.json

# 3. 异步调用函数
aws lambda invoke --function-name my-function --invocation-type Event output.json

# 4. 查看调用日志
cat output.json
```

### RDS 数据库管理

```bash
# 1. 查看数据库实例
aws rds describe-db-instances --query 'DBInstances[*].{ID:DBInstanceIdentifier,Endpoint:Endpoint.Address,Status:DBInstanceStatus}' --output table

# 2. 查看慢查询日志
aws rds download-db-log-file-portion --db-instance-identifier my-db --log-file-name error/mysql-error.log

# 3. 创建只读副本
aws rds create-db-instance-read-replica --db-instance-identifier my-db-read-replica --source-db-instance-identifier my-db
```

### IAM 跨账号访问

```bash
# 1. 扮演跨账号角色
aws sts assume-role --role-arn arn:aws:iam::123456789012:role/CrossAccountRole --role-session-name my-cross-account-session

# 2. 导出临时凭证
export AWS_ACCESS_KEY_ID=$(aws sts assume-role --role-arn arn:aws:iam::123456789012:role/CrossAccountRole --role-session-name temp --query 'Credentials.AccessKeyId' --output text)
export AWS_SECRET_ACCESS_KEY=$(aws sts assume-role --role-arn arn:aws:iam::123456789012:role/CrossAccountRole --role-session-name temp --query 'Credentials.SecretAccessKey' --output text)
export AWS_SESSION_TOKEN=$(aws sts assume-role --role-arn arn:aws:iam::123456789012:role/CrossAccountRole --role-session-name temp --query 'Credentials.SessionToken' --output text)

# 3. 验证临时凭证
aws sts get-caller-identity
```

### ECS 容器部署

```bash
# 1. 查看集群
aws ecs list-clusters

# 2. 查看服务
aws ecs describe-services --cluster my-cluster --services my-service

# 3. 更新服务（滚动部署）
aws ecs update-service --cluster my-cluster --service my-service --force-new-deployment

# 4. 运行新任务
aws ecs run-task --cluster my-cluster --task-definition my-task:2 --network-configuration 'awsvpcConfiguration={subnets=["subnet-0abcd1234efgh5678"],securityGroups=["sg-0abcd1234efgh5678"]}'
```

### CloudWatch 监控告警

```bash
# 1. 上报自定义指标
aws cloudwatch put-metric-data --namespace MyApp --metric-name RequestCount --value 100 --unit Count --dimensions InstanceId=i-0abcd1234efgh5678

# 2. 创建告警
aws cloudwatch put-metric-alarm --alarm-name HighCPU --metric-name CPUUtilization --namespace AWS/EC2 --statistic Average --period 300 --threshold 80 --comparison-operator GreaterThanThreshold --dimensions Name=InstanceId,Value=i-0abcd1234efgh5678 --evaluation-periods 2 --alarm-actions arn:aws:sns:us-east-1:123456789012:my-topic

# 3. 查看指标
aws cloudwatch get-metric-statistics --namespace AWS/EC2 --metric-name CPUUtilization --start-time 2024-01-01T00:00:00Z --end-time 2024-01-02T00:00:00Z --period 3600 --statistics Average
```

---

## 相关资源

- [Docker 命令文档](../Docker 命令/README.md)
- [Kubernetes 命令文档](../Kubernetes 命令/README.md)
- [Linux 命令文档](../Linux 命令/README.md)
