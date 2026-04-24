# 安全加固命令文档

网络安全、应用安全、密钥管理、容器安全与 SSL/TLS 完整参考文档。

## 目录

- [iptables 防火墙](#iptables-防火墙规则)
- [ufw 防火墙](#ufw-防火墙管理)
- [fail2ban 入侵防御](#fail2ban-入侵防御)
- [nmap 端口扫描](#nmap-端口扫描)
- [openssl 证书](#openssl-证书生成)
- [certbot Let's Encrypt](#certbot-lets-encrypt)
- [npm/yarn audit](#npm-yarn-audit-依赖审计)
- [Snyk 安全测试](#snyk-安全测试)
- [Helmet.js 安全头](#helmetjs-安全头)
- [HashiCorp Vault](#hashicorp-vault-密钥管理)
- [AWS Secrets Manager](#aws-secrets-manager)
- [git-secrets 防止密钥泄露](#git-secrets-防止密钥泄露)
- [envchain 环境变量](#envchain-环境变量加密)
- [Docker 安全扫描](#docker-安全扫描)
- [Trivy 容器漏洞](#trivy-容器漏洞扫描)
- [Docker Bench Security](#docker-bench-security)
- [Rootless Docker](#rootless-docker)
- [mkcert 本地 HTTPS](#mkcert-本地-https)
- [SSL Labs 测试](#ssl-labs-测试)
- [Dependabot 配置](#dependabot-配置)
- [文件权限加固](#文件权限加固)
- [Linux 审计](#linux-审计)

---

## iptables 防火墙规则

**基础用法**:
```bash
iptables %{选项}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看所有规则 | `iptables -L -n -v` | 显示完整规则列表 |
| 允许 SSH | `iptables -A INPUT -p tcp --dport 22 -j ACCEPT` | 开放 22 端口 |
| 允许 HTTP/HTTPS | `iptables -A INPUT -p tcp -m multiport --dports 80,443 -j ACCEPT` | 开放 80/443 |
| 拒绝入站 | `iptables -A INPUT -j DROP` | 丢弃所有入站 |
| 允许已建立连接 | `iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT` | 放行已建立连接 |
| 删除规则 | `iptables -D INPUT %{规则号}%` | 删除指定规则 |
| 保存规则 | `iptables-save > /etc/iptables/rules.v4` | 持久化保存 |

---

## ufw 防火墙管理

**基础用法**:
```bash
ufw %{动作}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启用防火墙 | `ufw enable` | 开启防火墙 |
| 禁用防火墙 | `ufw disable` | 关闭防火墙 |
| 允许 SSH | `ufw allow ssh` | 开放 SSH 端口 |
| 允许端口 | `ufw allow %{端口}%/tcp` | 开放指定端口 |
| 拒绝端口 | `ufw deny %{端口}%/tcp` | 拒绝指定端口 |
| 查看状态 | `ufw status verbose` | 显示详细状态 |
| 允许 IP | `ufw allow from %{IP}%` | 允许指定 IP |
| 重置 | `ufw reset` | 恢复默认配置 |

---

## fail2ban 入侵防御

**基础用法**:
```bash
fail2ban-client %{动作}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动服务 | `systemctl start fail2ban` | 启动 fail2ban |
| 查看状态 | `fail2ban-client status` | 查看整体状态 |
| 查看监狱 | `fail2ban-client status sshd` | 查看 SSH 监狱 |
| 手动封禁 IP | `fail2ban-client set sshd banip 192.168.1.100` | 封禁指定 IP |
| 解除封禁 | `fail2ban-client set sshd unbanip 192.168.1.100` | 解封指定 IP |
| 重载配置 | `fail2ban-client reload` | 重载配置文件 |

---

## nmap 端口扫描

**基础用法**:
```bash
nmap %{选项}% %{目标}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 快速扫描 | `nmap 192.168.1.1` | 扫描常用端口 |
| 详细扫描 | `nmap -A target.com` | 综合扫描 (OS, 版本, 脚本) |
| 指定端口 | `nmap -p 22,80,443 target.com` | 只扫描指定端口 |
| 版本检测 | `nmap -sV target.com` | 检测服务版本 |
| 系统检测 | `nmap -O target.com` | 探测操作系统 |
| 漏洞扫描 | `nmap --script vuln target.com` | 运行漏洞脚本 |

---

## openssl 证书生成

**基础用法**:
```bash
openssl %{命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 生成 RSA 私钥 | `openssl genrsa -out key.pem 2048` | 生成 2048 位私钥 |
| 生成 CSR | `openssl req -new -key key.pem -out request.csr` | 创建证书签名请求 |
| 生成自签名证书 | `openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365` | 生成自签名证书 |
| 查看证书信息 | `openssl x509 -in cert.pem -text -noout` | 查看证书详情 |
| 验证证书 | `openssl verify cert.pem` | 验证证书链 |
| 加密文件 | `openssl enc -aes-256-cbc -salt -in file.txt -out file.enc` | AES 加密 |
| 计算哈希 | `openssl dgst -sha256 file.txt` | SHA256 哈希 |

---

## certbot Let's Encrypt

**基础用法**:
```bash
certbot %{动作}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| Nginx 申请证书 | `sudo certbot --nginx -d example.com` | 自动配置 Nginx |
| Apache 申请证书 | `sudo certbot --apache -d example.com` | 自动配置 Apache |
| 仅获取证书 | `sudo certbot certonly --webroot -w /var/www/html -d example.com` | 不修改服务器 |
| 续期所有证书 | `sudo certbot renew` | 更新即将过期的证书 |
| 测试续期 | `sudo certbot renew --dry-run` | 模拟续期操作 |
| 删除证书 | `sudo certbot delete --cert-name example.com` | 删除指定证书 |

---

## npm/yarn audit 依赖审计

**npm audit**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 审计依赖 | `npm audit` | 扫描项目漏洞 |
| 修复漏洞 | `npm audit fix` | 自动修复可修复的漏洞 |
| 强制修复 | `npm audit fix --force` | 忽略版本约束强制修复 |
| JSON 输出 | `npm audit --json` | 生成结构化报告 |
| 生产依赖 | `npm audit --production` | 仅扫描生产依赖 |

**yarn audit**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 审计依赖 | `yarn audit` | 扫描 Yarn 依赖漏洞 |
| 设置阈值 | `yarn audit --level high` | 漏洞级别阈值 |
| JSON 输出 | `yarn audit --json` | 生成结构化报告 |

---

## Snyk 安全测试

**基础用法**:
```bash
snyk %{命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 测试漏洞 | `snyk test` | 扫描项目依赖漏洞 |
| 监控依赖 | `snyk monitor` | 持续监控依赖安全 |
| 扫描容器镜像 | `snyk container test nginx:latest` | 扫描 Docker 镜像 |
| 代码安全测试 | `snyk code test` | 扫描代码安全问题 |
| 修复漏洞 | `snyk fix` | 自动修复漏洞 |

---

## Helmet.js 安全头

**基础用法**:
```bash
npm install helmet
```

**Express 集成示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 基础使用 | `app.use(helmet())` | 启用所有安全头 |
| 内容安全策略 | `app.use(helmet.contentSecurityPolicy({ directives: { defaultSrc: ["'self'"] } }))` | CSP 头 |
| 隐藏 X-Powered-By | `app.use(helmet.hidePoweredBy())` | 不暴露服务器信息 |
| 防止点击劫持 | `app.use(helmet.frameguard({ action: 'deny' }))` | X-Frame-Options |
| XSS 防护 | `app.use(helmet.xssFilter())` | X-XSS-Protection |
| HSTS 头 | `app.use(helmet.hsts({ maxAge: 31536000, includeSubDomains: true }))` | 强制 HTTPS |

---

## HashiCorp Vault 密钥管理

**基础用法**:
```bash
vault %{命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 写入密文 | `vault kv put secret/myapp/config db_password=secret123` | 存储密钥 |
| 读取密文 | `vault kv get secret/myapp/config` | 获取密钥 |
| 列出路径 | `vault kv list secret/myapp/` | 列出所有路径 |
| 删除密文 | `vault kv delete secret/myapp/config` | 删除密钥 |
| 用户密码登录 | `vault login -method=userpass username=admin` | 用户认证 |
| 查看状态 | `vault status` | 查看 Vault 状态 |

---

## AWS Secrets Manager

**基础用法**:
```bash
aws secretsmanager %{命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建密文 | `aws secretsmanager create-secret --name myapp/db-creds --secret-string '{"user":"admin","pass":"xxx"}'` | 创建密钥 |
| 获取密文 | `aws secretsmanager get-secret-value --secret-id myapp/db-creds` | 获取密钥值 |
| 列出密文 | `aws secretsmanager list-secrets` | 列出所有密钥 |
| 删除密文 | `aws secretsmanager delete-secret --secret-id myapp/db-creds` | 删除密钥 |
| 自动轮转 | `aws secretsmanager rotate-secret --secret-id myapp/db-creds` | 轮转密钥 |

---

## git-secrets 防止密钥泄露

**基础用法**:
```bash
git secrets --%{动作}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装钩子 | `git secrets --install` | 在仓库安装 pre-commit 钩子 |
| 添加禁止模式 | `git secrets --add --global --literal 'password\\s*='` | 添加密钥模式 |
| 添加 AWS 模式 | `git secrets --add-gLOBAL --allowed --regex 'AKIA[0-9A-Z]{16}'` | 允许合法 AWS Key |
| 扫描文件 | `git secrets --scan app.js` | 扫描单文件 |
| 递归扫描目录 | `git secrets --scan -r src/` | 扫描整个目录 |
| 查看配置 | `git secrets --list` | 列出所有规则 |

---

## envchain 环境变量加密

**基础用法**:
```bash
envchain %{命名空间}% %{命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 设置变量 | `envchain myapp DB_PASSWORD=secret123 node app.js` | 设置并运行 |
| 交互式设置 | `envchain --set myapp AWS_SECRET_KEY` | 安全输入敏感数据 |
| 运行命令 | `envchain myapp node -e "console.log(process.env.DB_PASSWORD)"` | 使用环境变量 |
| 列出变量 | `envchain myapp env` | 查看该命名空间的变量 |

---

## Docker 安全扫描

**docker scan**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 扫描镜像 | `docker scan nginx:latest` | 使用 Snyk 扫描 |
| JSON 输出 | `docker scan --json nginx:latest` | 结构化结果 |
| 排除基础镜像 | `docker scan --exclude-base nginx:latest` | 仅扫描自定义层 |

**trivy 容器漏洞扫描**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 扫描镜像 | `trivy image nginx:latest` | 全面漏洞扫描 |
| 扫描文件系统 | `trivy fs ./` | 扫描项目目录 |
| JSON 输出 | `trivy image --format json --output report.json nginx:latest` | 生成报告 |
| 高危漏洞 | `trivy image --severity HIGH,CRITICAL nginx:latest` | 仅显示高危漏洞 |
| 忽略已修复 | `trivy image --ignore-unfixed nginx:latest` | 跳过无补丁漏洞 |
| K8s 集群扫描 | `trivy k8s --report summary` | 扫描 Kubernetes |

**docker bench security**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 完整扫描 | `docker run -it --net host --cap-add audit_control -v /var/lib/docker:/var/lib/docker aquasec/docker-bench-security` | CIS 基线测试 |
| 特定测试 | `docker run ... aquasec/docker-bench-security -c 1` | 只运行主机配置测试 |
| JSON 输出 | `docker run ... -f json -o results.json` | 生成 JSON 报告 |

---

## Rootless Docker

**基础用法**:
```bash
curl -fsSL https://get.docker.com/rootless | sh
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装 rootless | `curl -fsSL https://get.docker.com/rootless | sh` | 非 root 用户安装 |
| 启动 daemon | `DOCKER_BUILDKIT=1 dockerd-rootless.sh &` | 启动无 root daemon |
| 设置环境 | `export DOCKER_HOST=unix:///run/user/$(id -u)/docker.sock` | 配置客户端连接 |
| 验证安装 | `docker info | grep -i rootless` | 确认无 root 运行 |

---

## mkcert 本地 HTTPS

**基础用法**:
```bash
mkcert %{命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装本地 CA | `mkcert -install` | 添加为系统信任 CA |
| 生成证书 | `mkcert localhost` | 为 localhost 生成证书 |
| 多域名证书 | `mkcert localhost 127.0.0.1 ::1` | 本地多地址证书 |
| 指定输出路径 | `mkcert -cert-file cert.pem -key-file key.pem localhost` | 自定义文件路径 |
| PFX 格式 | `mkcert -pkcs12 localhost` | 生成 Java/Windows 兼容格式 |

---

## SSL Labs 测试

**基础用法**:
```bash
curl -s 'https://www.ssllabs.com/ssltest/analyze.html?d=%{域名}%'
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 测试 SSL | `curl -s 'https://www.ssllabs.com/ssltest/analyze.html?d=example.com'` | 获取分析结果 |
| 指定端口 | `curl -s 'https://www.ssllabs.com/ssltest/analyze.html?d=example.com:8443'` | 测试非标准端口 |
| 深度测试 | `curl -s 'https://www.ssllabs.com/ssltest/analyze.html?d=example.com&all=on'` | 完整测试所有协议 |

> 建议直接在浏览器访问 https://www.ssllabs.com/ssltest/ 获取详细报告。

---

## Dependabot 配置

**.github/dependabot.yml 示例**:

```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
    labels:
      - "security"
      - "dependencies"

  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"

  - package-ecosystem: "docker"
    directory: "/"
    schedule:
      interval: "weekly"
```

---

## 文件权限加固

**chmod 文件权限**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 锁定配置文件 | `chmod 600 .env` | 仅所有者读写 |
| 可执行脚本 | `chmod 700 backup.sh` | 仅所有者可执行 |
| 公共目录 | `chmod 755 /var/www/` | 所有者读写执行，其他人读执行 |
| 移除所有权限 | `chmod 000 sensitive.file` | 完全禁用 |
| 递归目录 | `chmod -R 600 config/` | 批量设置 |
| 只读文件 | `chmod 444 readme.md` | 所有人都只读 |

**chown 文件所有者**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 设置所有者 | `chown www-data:www-data /var/www/` | 设为 Web 服务用户 |
| 递归目录 | `chown -R nginx:nginx /data/logs/` | 批量设置 |
| 仅设置用户 | `chown app: /opt/app/bin` | 继承组 |
| 系统文件安全 | `chown root:root /etc/passwd && chmod 644 /etc/passwd` | 保护系统文件 |

---

## Linux 审计

**auditd 审计守护进程**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看规则 | `auditctl -l` | 列出所有审计规则 |
| 监控文件 | `auditctl -w /etc/passwd -p rwxa` | 监控密码文件访问 |
| 监控目录 | `auditctl -w /etc/ -p rwxa -k config_change` | 监控配置目录 |
| 添加系统调用规则 | `auditctl -a always,exit -F arch=b64 -S execve` | 监控命令执行 |
| 搜索审计日志 | `ausearch -k config_change` | 查找配置变更 |
| 生成报告 | `aureport` | 生成审计摘要报告 |

---

## 实用场景示例

### 场景 1: 服务器安全加固流程

```bash
# 1. 配置防火墙 (仅开放必要端口)
ufw default deny incoming
ufw allow ssh
ufw allow http
ufw allow https
ufw enable

# 2. 安装 fail2ban 防暴力破解
apt install fail2ban
systemctl enable fail2ban

# 3. 设置文件权限
chmod 600 .env
chmod 700 backup.sh
chown -R www-data:www-data /var/www/

# 4. 安装审计
apt install auditd
auditctl -w /etc/ -p rwxa -k config_change
```

### 场景 2: Node.js 项目安全检查

```bash
# 1. 审计依赖漏洞
npm audit
yarn audit

# 2. 使用 Snyk 深度扫描
snyk test
snyk monitor

# 3. 集成 Helmet.js 安全头
npm install helmet
# 在 Express app.js 中添加 helmet()

# 4. 防止密钥提交
git secrets --install
git secrets --add --global --literal 'password\s*='
```

### 场景 3: Docker 镜像安全

```bash
# 1. 本地镜像扫描
docker scan myapp:latest

# 2. Trivy 深度扫描
trivy image --severity HIGH,CRITICAL myapp:latest

# 3. 运行 CIS 安全基线
docker run -it --net host --cap-add audit_control \
  -v /var/lib/docker:/var/lib/docker \
  aquasec/docker-bench-security

# 4. 使用 rootless 运行
curl -fsSL https://get.docker.com/rootless | sh
export DOCKER_HOST=unix:///run/user/$(id -u)/docker.sock
```

### 场景 4: SSL 证书管理

```bash
# 1. 使用 mkcert 生成本地开发证书
mkcert -install
mkcert localhost 127.0.0.1 ::1

# 2. 使用 Let's Encrypt 申请正式证书
sudo certbot --nginx -d example.com -d www.example.com

# 3. 查看证书信息
openssl x509 -in /etc/letsencrypt/live/example.com/fullchain.pem -text -noout

# 4. 自动续期
sudo certbot renew --dry-run
```

### 场景 5: 密钥管理最佳实践

```bash
# 1. 使用 Vault 管理生产密钥
vault kv put secret/myapp/database username=admin password=secret
vault kv get secret/myapp/database

# 2. 使用 AWS Secrets Manager
aws secretsmanager create-secret --name prod/db-creds \
  --secret-string '{"host":"db.example.com","port":5432}'

# 3. 使用 envchain 管理本地密钥
envchain --set myapp AWS_ACCESS_KEY_ID
envchain --set myapp AWS_SECRET_ACCESS_KEY
envchain myapp node app.js

# 4. Git 提交前检查
git secrets --scan -r .
```

---

## 命令速查表

| 分类 | 常用命令 |
|------|----------|
| 防火墙 | `iptables`, `ufw` |
| 入侵防御 | `fail2ban-client` |
| 端口扫描 | `nmap` |
| 证书 | `openssl`, `certbot`, `mkcert` |
| 依赖审计 | `npm audit`, `yarn audit` |
| 漏洞扫描 | `snyk test`, `trivy image` |
| Docker 安全 | `docker scan`, `docker bench security`, `rootless` |
| 密钥管理 | `vault`, `aws secretsmanager`, `git-secrets`, `envchain` |
| 文件权限 | `chmod`, `chown` |
| 安全审计 | `auditctl`, `ausearch`, `aureport` |
| 安全头 | `helmet` (Node.js) |
| 在线测试 | SSL Labs (浏览器) |