# 容器安全 (Container Security)

## 概述

容器安全模块提供全面的容器安全扫描、强化和合规管理命令，涵盖镜像扫描、运行时安全、容器加固、密钥扫描、合规检查和镜像签名等领域。

---

## 目录

1. [镜像扫描 (Image Scanning)](#1-镜像扫描-image-scanning)
2. [运行时安全 (Runtime Security)](#2-运行时安全-runtime-security)
3. [容器强化 (Container Hardening)](#3-容器强化-container-hardening)
4. [密钥扫描 (Secret Scanning)](#4-密钥扫描-secret-scanning)
5. [合规检查 (Compliance)](#5-合规检查-compliance)
6. [镜像签名 (Image Signing)](#6-镜像签名-image-signing)

---

## 1. 镜像扫描 (Image Scanning)

### 1.1 Trivy 镜像扫描

Trivy 是一个简单而全面的容器镜像漏洞扫描器。

```bash
# 扫描镜像漏洞
trivy image nginx:latest

# 按严重性级别过滤 (CRITICAL, HIGH, MEDIUM, LOW)
trivy image --severity HIGH,CRITICAL nginx:latest

# 输出到文件 (JSON格式)
trivy image -f json -o results.json nginx:latest

# 扫描并忽略未修复的漏洞
trivy image --ignore-unfixed nginx:latest

# 扫描已拉取的本地镜像
trivy image --input archive.tar

# 从 stdin 读取镜像名称
trivy image < IMAGE_ID

# 扫描超时设置
trivy image --timeout 5m nginx:latest

# 仅显示漏洞摘要
trivy image --quiet nginx:latest

# 按漏洞类型过滤 (e.g., os, library)
trivy image --vuln-type os nginx:latest

# 启用缓存扫描
trivy image --cache-dir /path/to/cache nginx:latest

# 下载漏洞数据库
trivy image --download-db-only

# 更新漏洞数据库
trivy image --update-cache nginx:latest
```

**安装方式：**
```bash
# Linux/macOS
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh

# Homebrew (macOS)
brew install trivy

# Docker
docker run --rm aquasec/trivy nginx:latest
```

### 1.2 Docker Scan (Snyk)

使用 Snyk 扫描 Docker 镜像中的漏洞。

```bash
# 扫描本地镜像
docker scan nginx:latest

# 使用 --json 输出
docker scan --json nginx:latest > result.json

# 显示详细依赖信息
docker scan --verbose nginx:latest

# 指定依赖文件 (package.json, requirements.txt等)
docker scan --file /path/to/Dockerfile nginx:latest

# 排除漏洞类型
docker scan --exclude-base nginx:latest

# 登录到 Snyk
docker scan --login

# 扫描并显示修复建议
docker scan --fixable nginx:latest

# 设置 Snyk token
export SNYK_TOKEN=your_token
docker scan nginx:latest
```

**前置条件：**
```bash
# 确保 Docker Desktop 最新版 (包含 scan 插件)
docker version

# 登录 Snyk (如果需要)
snyk auth
```

### 1.3 Clair Scanner

Clair 是一款开源的容器漏洞分析工具。

```bash
# 扫描本地镜像
clair-scanner localhost:5000/myimage:latest

# 指定 Clair 服务器地址
clair-scanner --clair https://clair.example.com localhost:5000/myimage:latest

# 输出 JSON 格式报告
clair-scanner --json-output report.json localhost:5000/myimage:latest

# 只报告严重漏洞
clair-scanner --threshold HIGH localhost:5000/myimage:latest

# 设置 HTTP 超时
clair-scanner --timeout 5m localhost:5000/myimage:latest

# 忽略已知的 CVE
clair-scanner --ignore-cve CVE-2021-1234,CVE-2021-5678 localhost:5000/myimage:latest

# 启用详细日志
clair-scanner --log-level debug localhost:5000/myimage:latest

# 使用本地 Dockerfile 分析
clair-scanner --dockerfile /path/to/Dockerfile localhost:5000/myimage:latest

# Docker 运行 Clair 本地扫描
docker run -p 6060:6060 -v /var/run/docker.sock:/var/run/docker.sock arminc/clair-scanner:latest \
  --clair http://localhost:6060 localhost:5000/myimage:latest
```

### 1.4 Anchorectl (Anchor)

Anchor 容器镜像安全评估工具。

```bash
# 扫描镜像
anchorectl scan ubuntu:latest

# 扫描并生成报告
anchorectl scan --output report.html ubuntu:latest

# 使用特定策略
anchorectl scan --policy custom-policy.json ubuntu:latest

# 扫描多个镜像
anchorectl scan ubuntu:latest nginx:latest

# 查看已扫描的结果
anchorectl results ubuntu:latest

# 列出可用策略
anchorectl policies list

# 验证镜像签名
anchorectl verify ubuntu:latest

# 导出扫描结果为 JSON
anchorectl export --format json results.json

# 设置 Anchor API 端点
anchorectl --endpoint https://anchor-api.example.com scan ubuntu:latest

# 运行交互式扫描向导
anchorectl scan --interactive
```

---

## 2. 运行时安全 (Runtime Security)

### 2.1 Falco 命令

Falco 是云原生的运行时安全工具，用于检测异常行为。

```bash
# 查看 Falco 版本
falco --version

# 启动 Falco 守护进程
falco

# 以前台模式运行 (带日志输出)
falco -c /etc/falco/falco.yaml

# 使用自定义规则文件
falco -r /path/to/custom-rules.yaml

# 输出到 JSON 格式
falco -json

# 查看实时事件 (过滤)
falco -f "thread.name=nginx"

# 告警输出到文件
falco -o output.file.enabled=true -o output.file.path=/var/log/falco/alerts.log

# 与 Kubernetes 集成
falco --k8s-audit-server.enable=true

# 启用 gRPC 输出
falco -g 0.0.0.0:5060

# 查看帮助
falco --help

# 测试规则文件语法
falco -L

# 列出所有规则
falco -L

# 运行 Falcoctl 容器运行时检测
falcoctl runtime attest --image nginx:latest

# 告警到 Syslog
falco -o output.syslog.enabled=true

# 告警到 Slack
falco -c falco-with-slack.yaml

# 告警到 Filebeat/Elasticsearch
falco -c falco-elastic.yaml

# 查看 Falco 服务状态
systemctl status falco

# 启动 Falco 服务
systemctl start falco

# 查看 Falco 日志
journalctl -u falco -f
```

**安装 Falco：**
```bash
# Ubuntu/Debian
apt-get install falco

# macOS
brew install falco

# Kubernetes 部署
helm install falco bitnami/falco -n falco --create-namespace
```

### 2.2 Sysdig 命令

Sysdig 是强大的系统级监控和故障排查工具。

```bash
# 查看版本
sysdig --version

# 实时监控所有系统调用
sysdig

# 监控容器
sysdig -c topcontainers_cpu

# 监控容器网络
sysdig -c topcontainers_net

# 保存捕获数据到文件
sysdig -w capture.scap

# 从文件读取并分析
sysdig -r capture.scap

# 监控特定容器
sysdig -pc -c topprocs_cpu container.name=myapp

# 查看容器文件读取
sysdig -c spy_files container.name=myapp

# 网络连接监控
sysdig -c topconnections

# 列出可用 chisel (Lua 脚本)
sysdig -cl

# 使用特定 chisel
sysdig -c httptop myapp

# 监控敏感文件访问
sysdig -c spy_files /etc/shadow

# 显示系统调用统计
sysdig -c scstablets

# 过滤容器事件
sysdig container.name=myapp and evt.type=execve

# 监控恶意软件行为
sysdig -c Malware

# 查看 CPU 使用最高的进程
sysdig -c topprocs_cpu

# 查看内存使用最高的进程
sysdig -c topprocs_mem

# 监控错误事件
sysdig evt.type=open and evt.res=ENOENT

# 保存为压缩文件
sysdig -z -w capture.scap.gz

# 从压缩文件分析
sysdig -z -r capture.scap.gz

# 查看 Falco 规则匹配
sysdig -c falco

# 监控 DNS 查询
sysdig -c topconns conn.sport=53

# 设置缓冲区大小
sysdig -b 8192

# 指定输出列
sysdig -p "%evt.time %evt.dir %evt.type %proc.name"

# 监控用户 sudo 使用
sysdig -c spy_sudo

# 查看 I/O 最高的文件
sysdig -c topfiles_bytes

# 监控 Kubernetes Pod
sysdig -k http://k8s-api:8080 -pc -c topprocs_cpu

# 使用过滤器语法
sysdig fd.type=file and evt.type=read

# 容器资源监控
csysdig -pc
```

### 2.3 Auditd 命令

Linux 审计守护进程，用于监控安全相关事件。

```bash
# 查看 auditd 服务状态
systemctl status auditd

# 启动 auditd 服务
systemctl start auditd

# 查看审计日志
ausearch -i

# 搜索特定用户操作
ausearch -ua root

# 搜索特定系统调用
ausearch -sc open

# 搜索文件访问
ausearch -f /etc/passwd

# 搜索失败事件
ausearch -i --success no

# 按时间范围搜索
ausearch -ts 2024-01-01 12:00:00 -te 2024-01-01 14:00:00

# 输出为 CSV 格式
ausearch -i --format csv

# 添加审计规则
auditctl -w /etc/shadow -p rwxa -k shadow_access

# 列出当前规则
auditctl -l

# 删除规则
auditctl -W /etc/shadow -k shadow_access

# 删除所有规则
auditctl -D

# 查看审计日志文件位置
auditctl -s

# 监控目录访问
auditctl -w /etc -p rwxa -k dir_etc_access

# 监控命令执行
auditctl -a always,exit -F arch=b64 -S execve -F auid>=1000

# 监控网络连接
auditctl -a always,exit -F arch=b64 -S connect -F auid>=1000

# 生成审计报告
aureport --summary

# 生成认证报告
aureport -au --summary

# 生成文件访问报告
aureport -f --summary

# 生成系统调用报告
aureport -s --summary

# 查看每日报告
aureport -t --summary

# 将审计日志导出
ausearch --format text -i > audit_log.txt

# 配置审计规则永久化
vim /etc/audit/rules.d/audit.rules

# 应用新规则
auditctl -R /etc/audit/rules.d/audit.rules

# 监控容器运行时系统调用
ausearch -sc execve | grep docker

# 查看 SELinux AVC 拒绝事件
ausearch -m AVC

# 生成合规报告
aureport -ts today -e

# 实时监控审计事件
tail -f /var/log/audit/audit.log | auditd
```

---

## 3. 容器强化 (Container Hardening)

### 3.1 Rootless Container Tools

Rootless 模式运行容器，减少特权依赖。

```bash
# 检查当前用户是否可运行 rootless 容器
docker info 2>&1 | grep "Rootless"

# 安装 rootless Docker
dockerd-rootless-setuptool.sh install

# 以 rootless 模式运行 Docker
dockerd-rootless.sh &

# 设置 DOCKER_HOST
export DOCKER_HOST=unix:///run/user/$(id -u)/docker.sock

# 验证 rootless 模式
docker info

# 限制容器资源 (cgroups v2)
docker run --rm --memory=256m nginx

# 启用 user namespace remapping
dockerd --userns-remap=default &

# 配置 /etc/subuid 和 /etc/subgid
grep $(whoami) /etc/subuid
grep $(whoami) /etc/subgid

# 创建 rootless 容器网络
dockerd-rootless.sh networking create mynet

# 使用 RootlessKit
rootlesskit --version

# 创建带有网络隔离的 rootless 容器
rootlesskit --net=slirp4netns --ipc=host --mount=/dev/full --pid=host \
  dockerd-rootless.sh

# 检查 rootless Docker 状态
systemctl --user status docker

# 查看 rootless Docker 日志
journalctl --user -u docker

# 设置 rootless Docker 自启动
loginctl enable-linger $(whoami)
```

### 3.2 Seccomp Profiles

Seccomp (Secure Computing Mode) 限制容器可用的系统调用。

```bash
# 查看当前 seccomp 状态
docker info | grep Seccomp

# 使用默认 seccomp 配置文件运行容器
docker run --security-opt seccomp=unconfined nginx

# 使用自定义 seccomp 配置
docker run --security-opt seccomp=/path/to/profile.json nginx

# 生成 seccomp 配置文件 (Docker 默认)
docker seccomp generate-unconfined > default-seccomp.json

# 使用 SCyclic 工具生成基于 Syscall 的配置
scyclic generate --only-use --output seccomp-profile.json nginx

# 查看容器使用的 seccomp 配置文件
docker inspect --format '{{.HostConfig.SecurityOpt}}' container_name

# 使用 Kubernetes seccomp
kubectl run --overrides='{"spec":{"securityContext":{"seccompProfile":{"type":"RuntimeDefault"}}}}'

# 查看已应用的 seccomp 配置
cat /var/lib/docker/seccomp/user/seccomp_profiles/*.json

# 审计容器中使用的系统调用
strace -c docker run --rm nginx ls

# 使用 bpfcc-tools 监控容器系统调用
buntrace <container_pid>

# 过滤特定系统调用
seccomp-tools allow ./profile.json

# 测试 seccomp 配置
docker run --security-opt seccomp=/path/to/test.json --rm nginx ls

# 导出默认 seccomp 配置
docker seccomp generate > default.json

# 允许特定的系统调用
{
  "names": ["read", "write", "exit"],
  "action": "SCMP_ACT_ALLOW"
}

# 拒绝所有其他系统调用
{
  "defaultAction": "SCMP_ACT_ERRNO"
}
```

### 3.3 AppArmor 命令

AppArmor 是 Linux 安全模块，用于限制程序能力。

```bash
# 检查 AppArmor 状态
aa-status

# 查看 AppArmor 进程状态
cat /sys/kernel/security/apparmor/profiles

# 列出所有配置文件
apparmor_parser -l

# 加载 AppArmor 配置文件
apparmor_parser -r /etc/apparmor.d/docker-nginx

# 卸载 AppArmor 配置文件
apparmor_parser -R /etc/apparmor.d/docker-nginx

# 创建 Docker AppArmor 配置文件
cat > /etc/apparmor.d/docker-nginx << 'EOF'
#include <tunables/global>
profile docker-nginx flags=(attach_disconnected,mediate_deleted) {
  # 允许读取 etc 文件
  /etc/** r,
  # 允许写日志目录
  /var/log/nginx/** w,
  # 拒绝网络访问
  deny network,
}
EOF

# 加载新配置文件
apparmor_parser -r /etc/apparmor.d/docker-nginx

# 运行带 AppArmor 的容器
docker run --security-opt apparmor=docker-nginx nginx

# 查看 AppArmor 日志
dmesg | grep apparmor

# 查看详细审计日志
tail -f /var/log/syslog | grep apparmor

# 创建简洁配置
aa-complain /etc/apparmor.d/docker-nginx

# 强制执行模式
aa-enforce /etc/apparmor.d/docker-nginx

# 禁用 AppArmor
systemctl stop apparmor

# 在 Kubernetes 中使用 AppArmor
kubectl annotate pod nginx-profile \
  container.apparmor.security.beta.kubernetes.io/nginx=localhost/docker-nginx

# 使用 aa-unconfined 查看未受限制的进程
aa-unconfined

# 生成 AppArmor 配置 (使用 logprof)
aa-logprof
```

### 3.4 SELinux 命令

SELinux (Security-Enhanced Linux) 强制访问控制。

```bash
# 查看当前 SELinux 状态
getenforce

# 查看详细状态
sestatus

# 临时设置为 Permissive 模式 (仅警告，不阻止)
setenforce 0

# 临时设置为 Enforcing 模式 (阻止违规)
setenforce 1

# 永久修改 SELinux 模式
vim /etc/selinux/config
# SELINUX=enforcing

# 查看 SELinux 布尔值
getsebool -a

# 启用特定布尔值
setsebool -P httpd_can_network_connect 1

# 查看文件安全上下文
ls -Z /var/www/html

# 查看进程安全上下文
ps auxZ | grep nginx

# 查看用户安全上下文
id -Z

# 修改文件安全上下文
chcon -t httpd_sys_content_t /var/www/html/index.html

# 永久修改目录安全上下文
semanage fcontext -a -t httpd_sys_content_t "/var/www/html(/.*)?"
restorecon -Rv /var/www/html

# 查看 SELinux 策略模块
semodule -l

# 启用/禁用策略模块
semodule -e nginx-module
semodule -d nginx-module

# 查看 SELinux 拒绝日志
ausearch -m avc -ts recent

# 搜索特定类型的拒绝
ausearch -m avc -c open

# 生成 SELinux 策略允许规则
audit2allow -a

# 为 Docker 容器设置 SELinux 标签
docker run --security-opt label=type:container_t nginx

# 在容器中使用共享目录
chcon -t container_file_t /shared

# 运行特权容器 (不推荐)
docker run --privileged nginx

# 使用 SELinux 标签限制容器能力
docker run --security-opt label=type:container_web_t nginx

# 查看网络端口上下文
semanage port -l | grep http

# 添加端口到上下文
semanage port -a -t http_port_t -p tcp 8888

# 列出所有 SELinux 用户
semanage user -l

# 查看文件默认上下文
matchpathcon /var/www/html
```

---

## 4. 密钥扫描 (Secret Scanning)

### 4.1 Git Secrets

在 Git 仓库中检测敏感信息泄露。

```bash
# 初始化 git-secret
git secrets --install

# 添加禁止模式 (禁止 AWS 密钥)
git secrets --add --global --literal 'AKIA[0-9A-Z]{16}'

# 添加禁止的正则表达式模式
git secrets --add --global 'aws_access_key_id\s*=\s*[A-Za-z0-9/+=]'

# 扫描当前仓库
git secrets --scan

# 扫描特定文件
git secrets --scan /path/to/file

# 递归扫描目录
git secrets --scan -r /path/to/directory

# 使用扫描器钩子
git secrets --scan --stderr

# 查看所有已注册的模式
git secrets --list

# 移除注册的模式
git secrets --remove --global --literal 'AKIA[0-9A-Z]{16}'

# 安装 git 钩子
git secrets --install -f

# 手动检查暂存的文件
git secrets --scan --staged

# 递归扫描子模块
git secrets --scan --recursive --submodules

# 扫描远程仓库 (克隆后)
git clone --recursive https://github.com/example/repo
git secrets --scan -r repo/

# 添加 AWS 官方禁止模式
git secrets --add-provider --global -- aws
git secrets --add --global 'AKIA[0-9A-Z]{16}'
git secrets --add --global '(?i)aws(.*)?['"'"']{1}.*['"'"'][0-9a-zA-Z/+=]{40}'

# 与 CI/CD 集成
git secrets --scan && echo "No secrets found"

# 使用自定义扫描器
git secrets --scan --regex 'my-secret-pattern'

# 查看扫描结果 (JSON 格式)
git secrets --scan -r --json

# 添加多个禁止模式
echo -e "pattern1\npattern2" | git secrets --add --global --regex-list
```

### 4.2 Detect Secrets

IBM 开源的敏感信息检测工具。

```bash
# 安装 detect-secrets
pip install detect-secrets

# 初始化 baseline 文件
detect-secrets scan > .secrets.baseline

# 在 CI 中扫描
detect-secrets scan --baseline .secrets.baseline .

# 添加新插件 (检测特定类型密钥)
detect-secrets scan --plugins AWSCredentialsDetector ./

# 扫描并生成报告
detect-secrets scan --output-report results.json ./

# 验证 baseline 文件
detect-secrets verify .secrets.baseline

# 更新 baseline (重新扫描并合并)
detect-secrets scan --update .secrets.baseline

# 在 pre-commit 钩子中使用
detect-secrets install --pre-commit

# 查看所有可用插件
detect-secrets scan --list-plugins

# 添加自定义正则检测
detect-secrets scan \
  --custom-plugins Path/To/Detector.py \
  ./

# 扫描特定文件类型
detect-secrets scan --string FILE ./*.py

# 审计已扫描的密钥
detect-secrets audit .secrets.baseline

# 标记已知误报
detect-secrets audit .secrets.baseline \
  --set "path/to/file:line_number" --ignore

# 生成 JSON baseline
detect-secrets scan --format json > baseline.json

# 过滤结果
detect-secrets scan --exclude-files '*.test.js' --exclude-lines 'test' .

# 扫描 git diff (检测新引入的密钥)
git diff --staged | detect-secrets scan --stdin

# 设置 baseline 版本
detect-secrets scan --baseline-version 0.13.0 . > .secrets.baseline

# 启用预热扫描 (使用缓存)
detect-secrets scan --cache .secrets.cache

# 扫描文件大小限制
detect-secrets scan --file-size-limit 10MB .

# 获取统计信息
detect-secrets scan --stats .
```

### 4.3 TruffleHog

深度扫描 Git 仓库中的敏感信息和密钥。

```bash
# 扫描当前仓库
trufflehog .

# 扫描远程 Git 仓库
trufflehog https://github.com/example/repo

# 扫描私有仓库
trufflehog git git@github.com:example/repo.git

# 扫描特定分支
trufflehog git --branch=main https://github.com/example/repo.git

# 输出为 JSON 格式
trufflehog . --json

# 保存结果到文件
trufflehog . -o results.txt

# 启用详细输出
trufflehog . -v

# 扫描多个目录
trufflehog directory ./dir1 ./dir2

# 设置结果数量限制
trufflehog . --max-results 100

# 仅扫描新提交 (从上一个版本开始)
trufflehog git --since-commit abc123 https://github.com/example/repo

# 启用熵检测
trufflehog . --entropy

# 使用自定义正则规则
trufflehog . --regex-rules-file rules.json

# 排除特定路径
trufflehog . --exclude-paths .git,node_modules,vendor

# 扫描文件系统
trufflehog filesystem /path/to/directory

# 使用预构建规则
trufflehog git https://github.com/sensitive/repo \
  --rules=/path/to/rules.yaml

# CI/CD 集成 (仅退出码)
trufflehog . --only-verified

# 设置并发数
trufflehog . --threads 4

# 扫描 S3 存储桶
trufflehog s3 --bucket my-bucket --region us-east-1

# 扫描 GitHub 组织
trufflehog github --org=my-org --token=$GH_TOKEN

# 扫描 GitHub 仓库
trufflehog github --repo=my-org/my-repo --token=$GH_TOKEN

# 扫描 GitLab
trufflehog gitlab --server-url=https://gitlab.com --token=$GITLAB_TOKEN

# 扫描 Jira
trufflehog jira --server-url=https://mycompany.atlassian.net --token=$JIRA_TOKEN

# 集成 Docker (用于 CI)
docker run --rm trufflehog/trufflehog:latest .
```

---

## 5. 合规检查 (Compliance)

### 5.1 OPA (Open Policy Agent)

策略引擎，用于策略即代码。

```bash
# 查看 OPA 版本
opa version

# 运行 OPA 服务器
opa run --server

# 运行交互式 REPL
opa run

# 评估输入数据
opa eval --data policy.rego --input input.json 'data.policy.allow'

# 测试策略
opa test --data . .

# 格式检查
opa fmt policy.rego

# 解析策略文件
opa parse policy.rego

# Bundle 打包策略
opa build --bundle policy/ -o bundle.tar.gz

# 运行 Bundle 服务器
opa run --bundle bundle.tar.gz --server

# 检查 Bundle 完整性
opa eval --bundle bundle.tar.gz 'data'

# 运行测试套件
opa test ./tests/ --verbose

# 覆盖率报告
opa test ./tests/ --coverage

# 增量评估
opa eval --data policy.rego 'data'

# 使用 JSON 输入
opa eval --data policy.rego --input input.json 'data.example.allow'

# 运行 OPA Gatekeeper 方式
opa gatekeeper

# 导出 OPA 配置
opa export --format json

# 微服务授权
opa run --server --discovery \
  --discovery.service-name=opa \
  --discovery.package=discovery

# Kubernetes 集成
kubectl apply -f policy.yaml

# 在 Docker 中运行
docker run -p 8181:8181 openpolicyagent/opa run --server

# 推送 Bundle 到远程
opa push --bundle bundle.tar.gz http://localhost:8181/v1

# 拉取 Bundle
opa run --bundle http://localhost:8181/v1/bundles/example

# 调试策略
opa eval --explain full --fail --data policy.rego 'data'

# 查看中间结果
opa eval --explain medium --data policy.rego 'data'

# 设置日志级别
opa run --log-level debug

# 启用 TLS
opa run --tls-cert-file cert.pem --tls-private-key-file key.pem

# 查看指标
curl http://localhost:8181/metrics

# 健康检查
curl http://localhost:8181/health

# Bundle 签名验证
opa verify --bundle bundle.tar.gz --signing-key private_key.pem
```

### 5.2 Conftest 命令

用于配置文件的策略测试工具。

```bash
# 查看版本
conftest --version

# 测试配置文件
conftest test deployment.yaml

# 测试多个文件
conftest test deployment.yaml config.yaml

# 指定策略目录
conftest test --policy ./policies deployment.yaml

# 使用命名空间策略
conftest test --namespace always deployment.yaml

# 输出为 JSON 格式
conftest test --output json deployment.yaml

# 输出为 JUnit XML (CI 集成)
conftest test --output junit deployment.yaml > results.xml

# 详细失败信息
conftest test -v deployment.yaml

# 使用数据文件
conftest test --data data.yaml deployment.yaml

# 测试 Helm 模板
helm template mychart | conftest -

# 测试 Terraform 计划
terraform plan -out=tfplan
conftest test tfplan -p terraform

# 在 CI 中使用 (GitHub Actions)
conftest test --fail-on-warning deployment.yaml

# 过滤测试结果
conftest test --filter 'name=deployment' deployment.yaml

# 并行测试
conftest test --parallel deployment.yaml

# 从 registry 下载策略
conftest pull instrumenta/rules/kubernetes

# 列出可用策略
conftest rules ./policies/

# 更新策略缓存
conftest update

# 使用自定义解析器
conftest test --parser yaml deployment.yaml

# 导出测试报告
conftest test --output csv deployment.yaml > report.csv

# 测试所有配置文件
find . -name "*.yaml" | xargs conftest test

# 忽略特定规则
conftest test --ignore "deny[0]" deployment.yaml

# 策略覆盖范围
conftest test --coverage deployment.yaml
```

### 5.3 Kube-bench

Kubernetes CIS Benchmark 合规检查工具。

```bash
# 查看版本
kube-bench version

# 在 master 节点运行
kube-bench run --target master

# 在 node 节点运行
kube-bench run --target node

# 在 etcd 节点运行
kube-bench run --target etcd

# 在 controlplane 运行
kube-bench run --target controlplane

# 完整检查 (所有组件)
kube-bench run

# 输出 JSON 格式
kube-bench run --json > results.json

# 输出 JUnit XML
kube-bench run --junit > results.xml

# 指定配置文件
kube-bench run --config-dir /etc/kube-bench/

# 运行特定测试
kube-bench run --focus "1.1.1"

# 跳过特定测试
kube-bench run --skip "1.1.2"

# 查看可用测试用例
kube-bench list

# 以非 root 运行
kube-bench run --skip-audit

# Kubernetes 运行 kube-bench
kubectl apply -f https://raw.githubusercontent.com/aquasecurity/kube-bench/main/job.yaml
kubectl logs -l app=kube-bench

# Helm 安装 kube-bench
helm install kube-bench aqua/kube-bench -n kube-bench --create-namespace

# 查看帮助
kube-bench --help

# 输出到文件
kube-bench run > kube-bench-results.txt 2>&1

# 仅显示失败的检查
kube-bench run --only-failed

# 设置日志级别
kube-bench run --log-level debug

# 使用自定义 benchmark 版本
kube-bench run --benchmark cis-1.5

# 查看测试摘要
kube-bench run --short

# JSON 输出美化
kube-bench run --json | jq .
```

---

## 6. 镜像签名 (Image Signing)

### 6.1 Cosign 命令

Sigstore 项目的镜像签名和验证工具。

```bash
# 查看版本
cosign version

# 生成密钥对 (云存储)
cosign generate-key-pair

# 生成对称密钥
cosign generate-key-pair --kms provider://path/to/key

# 签名镜像
cosign sign --yes docker.io/user/image:tag

# 签名并上传到 OCI registry
cosign sign --upload-distinguished-certs docker.io/user/image:tag

# 验证签名镜像
cosign verify docker.io/user/image:tag

# 验证并显示签名者
cosign verify --show-certificates docker.io/user/image:tag

# 使用公钥验证
cosign verify --key cosign.pub docker.io/user/image:tag

# 验证 Kubernetes 镜像策略
cosign verify --policy policy.json docker.io/user/image:tag

# 附加 SBOM
cosign attach sbom --sbom sbom.spdx docker.io/user/image:tag

# 附加签名证明
cosign attest --predicate predicate.json docker.io/user/image:tag

# 验证证明
cosign verify-attestation --policy policy.json docker.io/user/image:tag

# 导出证书
cosign public-key --key cosign.key > cosign.pub

# 下载镜像清单
cosign download manifest docker.io/user/image:tag

# 下载签名
cosign download signature docker.io/user/image:tag

# 删除签名
cosign delete signature docker.io/user/image:tag

# 验证时间戳 (TUF 根)
cosign verify --certificate-identity regex \
  --certificate-oidc-issuer regex \
  docker.io/user/image:tag

# 使用 Rekor 透明日志验证
cosign verify --tlog-enforce docker.io/user/image:tag

# 导入外部密钥 (Vault, PKCS11)
cosign import-key-pair --key kms://gcpkms/...

# 清理缓存
cosign clean docker.io/user/image:tag

# 列表镜像标签
cosign triangulate docker.io/user/image:tag

# Docker 集成 (skopeo)
cosign copy docker.io/user/image:v1 docker.io/user/image:v2

# 生成自定义摘要
cosign hash

# 交叉平台签名
cosign sign --payload-platforms linux/amd64,linux/arm64

# 推送和签名 Helm chart
cosign sign --y ghcr.io/user/namespace/helm-chart:v1.0.0

# 在 CI 中使用 GitHub OIDC
cosign sign --yes --oidc-provider github

# 批量签名多个镜像
for img in nginx redis postgres; do
  cosign sign --yes docker.io/user/$img:latest
done

# 吊销签名
cosign triangular docker.io/user/image:tag

# 查看签名详情
cosign describe docker.io/user/image:tag
```

### 6.2 Notary 命令

Docker Notary 镜像签名和信任管理工具。

```bash
# 查看 notary 版本
notary --version

# 初始化信任库
notary init repository

# 列出信任角色
notary list repository

# 添加签名者
notary key add repository

# 撤销密钥
notary key rotate repository

# 列出可用密钥
notary key list

# 获取远程信任库
notary delegation repository

# 添加委托角色
notary delegation add repository targets/uploader \
  --add-all

# 列出委托角色
notary delegation list repository

# 删除委托角色
notary delegation remove repository targets/uploader

# 发布更改
notary publish repository

# 验证镜像
notary verify docker.io/user/image:tag

# 查看镜像信任数据
notary lookup docker.io/user/image:tag

# 列出镜像的所有标签
notary list docker.io/user/image

# 删除镜像信任数据
notary remove docker.io/user/image:tag

# 服务器配置
notary server

# 查看信任根
notary trusted show docker.io/user/image:tag

# 管理根密钥
notary key rotate repository root

# 导入信任
notary import

# 导出信任数据
notary export

# 配置 notary 客户端
notary configure --server https://notary.example.com

# 获取委托密钥
notary delegation add repository targets/delegate \
  --alltargets --publish

# 检查信任状态
notary status repository

# 审计信任数据
notary audit docker.io/user/image:tag

# 自动化签名流程
notary script sign --repository repository \
  --key keyname --batch
```

### 6.3 Docker Trust 命令

Docker Content Trust 镜像签名集成。

```bash
# 启用 Docker Content Trust
export DOCKER_CONTENT_TRUST=1

# 禁用 Docker Content Trust
export DOCKER_CONTENT_TRUST=0

# 启用内容信任并拉取镜像
DOCKER_CONTENT_TRUST=1 docker pull nginx:latest

# 推送镜像 (自动签名)
docker push docker.io/user/image:tag

# 查看信任数据目录
ls ~/.docker/trust

# 查看私钥
ls ~/.docker/trust/private

# 查看信任密钥
ls ~/.docker/trust/tuf

# 清理信任缓存
docker trust prune

# 查看已签名的镜像
docker trust inspect docker.io/user/image:tag

# 设置 Notary 服务器
export DOCKER_CONTENT_TRUST_SERVER=https://notary.example.com:4443

# 查看信任签名
docker trust sign docker.io/user/image:tag

# 添加委托签名者
docker trust signer add --key key.pub user docker.io/user/image

# 移除签名者
docker trust signer remove user docker.io/user/image

# 查看镜像签名者
docker trust inspect --pretty docker.io/user/image:tag

# 列出签名者
docker trust signer docker.io/user/image

# 在 CI 中使用
# 设置环境变量
echo $DOCKER_CONTENT_TRUST > /dev/null

# 推送并签名
DOCKER_CONTENT_TRUST=1 docker push user/image:tag

# 验证 CI 密钥
docker trust inspect docker.io/user/image:tag

# 禁用特定镜像的信任检查
# 在 /etc/docker/daemon.json 中配置
{
  "allow-nontls-content-trust": true
}
```

---

## 快速参考表

| 分类 | 工具 | 主要用途 |
|------|------|----------|
| 镜像扫描 | `trivy` | 漏洞扫描 |
| 镜像扫描 | `docker scan` (Snyk) | Docker 漏洞检测 |
| 镜像扫描 | `clair-scanner` | 容器漏洞分析 |
| 镜像扫描 | `anchorectl` | 镜像安全评估 |
| 运行时安全 | `falco` | 异常行为检测 |
| 运行时安全 | `sysdig` | 系统监控 |
| 运行时安全 | `auditd` | 安全审计 |
| 容器强化 | `rootless` | 无特权容器 |
| 容器强化 | `seccomp` | 系统调用限制 |
| 容器强化 | `apparmor` | 程序能力限制 |
| 容器强化 | `SELinux` | 强制访问控制 |
| 密钥扫描 | `git-secrets` | Git 敏感信息检测 |
| 密钥扫描 | `detect-secrets` | 企业级密钥检测 |
| 密钥扫描 | `trufflehog` | 深度密钥扫描 |
| 合规检查 | `OPA` | 策略即代码 |
| 合规检查 | `conftest` | 配置文件测试 |
| 合规检查 | `kube-bench` | K8s 合规检查 |
| 镜像签名 | `cosign` | Sigstore 签名 |
| 镜像签名 | `notary` | Docker 信任 |
| 镜像签名 | `docker trust` | Docker 签名 |

---

## 安全最佳实践

1. **镜像扫描**：在 CI/CD 流水线中集成 Trivy 或 Snyk，扫描所有镜像后才允许部署
2. **运行时安全**：部署 Falco 或 Sysdig 监控容器行为，检测异常活动
3. **容器强化**：使用非 root 用户运行容器，启用 Seccomp/AppArmor/SELinux
4. **密钥扫描**：在 pre-commit 和 CI 中集成 git-secrets 或 detect-secrets
5. **合规检查**：使用 OPA 或 Conftest 在部署前验证配置文件
6. **镜像签名**：使用 Cosign 为所有生产镜像签名，启用 Docker Content Trust

---

## 相关模块

- [Docker 命令](../Docker 命令/README.md)
- [Kubernetes 命令](../Kubernetes 命令/README.md)
- [CI_CD 流水线](../CI_CD 流水线/README.md)