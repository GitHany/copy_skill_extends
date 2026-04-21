# 网络诊断命令文档

网络诊断与故障排查完整参考文档。

## 目录

- [ping 连通性测试](#ping-连通性测试)
- [traceroute/tracert 路由追踪](#traceroutetracert-路由追踪)
- [netstat 网络连接状态](#netstat-网络连接状态)
- [nslookup/dig DNS 查询](#nslookupdig-dns-查询)
- [curl HTTP 请求](#curl-http-请求)
- [wget 文件下载](#wget-文件下载)
- [telnet 端口测试](#telnet-端口测试)
- [nc/netcat 网络瑞士军刀](#ncnetcat-网络瑞士军刀)

---

## ping 连通性测试

**基础用法**:
```bash
ping %{主机或IP}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定次数 | `ping -c 4 %{主机}%` | 只 ping 4 次 |
| 持续 ping | `ping %{主机}%` | 不停止持续 ping |
| 设置间隔 | `ping -i 2 %{主机}%` | 每 2 秒一次 |
| 大数据包 | `ping -s 1000 %{主机}%` | 发送 1000 字节数据包 |
| 详细输出 | `ping -v %{主机}%` | 显示详细统计信息 |

---

## traceroute/tracert 路由追踪

**基础用法**:
```bash
traceroute %{主机}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 最大跳数 | `traceroute -m 30 %{主机}%` | 设置最大跳数 |
| 设置超时 | `traceroute -w 5 %{主机}%` | 等待超时时间 |
| 使用 ICMP | `traceroute -I %{主机}%` | 使用 ICMP 协议 |
| Windows 追踪 | `tracert %{主机}%` | Windows 系统命令 |
| 显示 IP | `traceroute -n %{主机}%` | 不解析主机名 |

---

## netstat 网络连接状态

**基础用法**:
```bash
netstat %{选项}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看监听端口 | `netstat -tulpn` | 显示所有监听端口 【常用】 |
| 查看 TCP 连接 | `netstat -t` | 显示 TCP 连接 |
| 查看 UDP 连接 | `netstat -u` | 显示 UDP 连接 |
| 显示进程 | `netstat -tlnp` | 显示进程名和 PID |
| 统计汇总 | `netstat -s` | 显示协议统计信息 |
| 持续显示 | `netstat -c` | 每秒刷新显示 |
| 路由表 | `netstat -r` | 显示路由表 |

---

## nslookup/dig DNS 查询

**基础用法**:
```bash
nslookup %{域名}%
dig %{域名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 基本查询 | `nslookup %{域名}%` | 查询 A 记录 |
| 指定 DNS | `nslookup %{域名}% 8.8.8.8` | 使用指定 DNS 服务器 |
| 查询 MX | `nslookup -type=mx %{域名}%` | 查询邮件服务器记录 |
| 查询 TXT | `nslookup -type=txt %{域名}%` | 查询 TXT 记录 |
| 简短输出 | `dig +short %{域名}%` | 只显示结果 |
| 追踪解析 | `dig +trace %{域名}%` | 追踪完整 DNS 解析过程 |
| 查询 NS | `dig %{域名}% ns` | 查询域名服务器记录 |
| 查询 TXT | `dig %{域名}% txt` | 查询 TXT 记录 |

---

## curl HTTP 请求

**基础用法**:
```bash
curl %{URL}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 下载文件 | `curl -O %{URL}%` | 下载并保存原文件名 |
| 保存到文件 | `curl -o %{文件名}% %{URL}%` | 指定保存文件名 |
| POST 请求 | `curl -X POST -d "data=value" %{URL}%` | 提交表单数据 |
| 设置请求头 | `curl -H "Authorization: Bearer %{token}%" %{URL}%` | 添加请求头 |
| 跟随重定向 | `curl -L %{URL}%` | 自动跳转 |
| 显示响应头 | `curl -I %{URL}%` | 只显示响应头 |
| 详细信息 | `curl -v %{URL}%` | 显示完整请求过程 |
| 跳过 SSL | `curl -k %{URL}%` | 忽略证书错误 |
| 发送 JSON | `curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' %{URL}%` | JSON 请求 |

---

## wget 文件下载

**基础用法**:
```bash
wget %{URL}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定文件名 | `wget -O %{文件名}% %{URL}%` | 保存到指定名 |
| 断点续传 | `wget -c %{URL}%` | 继续下载 【常用】 |
| 后台下载 | `wget -b %{URL}%` | 后台下载 |
| 限速下载 | `wget --limit-rate=200k %{URL}%` | 限制下载速度 |
| 递归下载 | `wget -r %{URL}%` | 递归下载整个站点 |
| 认证下载 | `wget --user=%{用户}% --password=%{密码}% %{URL}%` | 带认证下载 |
| 文件列表 | `wget -i urls.txt` | 从文件读取 URL |
| 匹配下载 | `wget -A "*.pdf" %{URL}%` | 只下载匹配文件 |

---

## telnet 端口测试

**基础用法**:
```bash
telnet %{主机}% %{端口}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| HTTP 端口 | `telnet %{主机}% 80` | 测试 80 端口 |
| HTTPS 端口 | `telnet %{主机}% 443` | 测试 443 端口 |
| SMTP 端口 | `telnet %{主机}% 25` | 测试邮件发送端口 |
| SSH 端口 | `telnet %{主机}% 22` | 测试 SSH 端口 |
| MySQL 端口 | `telnet %{主机}% 3306` | 测试数据库端口 |
| Redis 端口 | `telnet %{主机}% 6379` | 测试 Redis 端口 |

---

## nc/netcat 网络瑞士军刀

**基础用法**:
```bash
nc %{主机}% %{端口}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 端口扫描 | `nc -zv %{主机}% %{端口}%` | 扫描端口是否开放 【常用】 |
| 范围扫描 | `nc -zv %{主机}% 20-30` | 扫描端口范围 |
| 接收文件 | `nc -l %{端口}% > %{文件名}%` | 监听并接收文件 |
| 发送文件 | `nc %{主机}% %{端口}% < %{文件}%` | 发送文件 |
| 聊天服务器 | `nc -l %{端口}%` | 简单聊天/调试 |
| 连接测试 | `nc %{主机}% %{端口}%` | 连接远程端口 |
| HTTP 请求 | `echo -e "GET / HTTP/1.0\r\n\r\n" \| nc %{主机}% 80` | 发送 HTTP 请求 |
| 设置超时 | `nc -w 3 %{主机}% %{端口}%` | 设置连接超时 |

---

## 实用场景示例

### 场景 1: 网站访问故障排查

```bash
# 1. 测试 DNS 解析
nslookup example.com
dig +short example.com

# 2. 测试网络连通性
ping -c 4 example.com

# 3. 追踪路由
traceroute example.com

# 4. 测试 HTTP 响应
curl -I https://example.com
curl -v https://example.com
```

### 场景 2: 端口与服务诊断

```bash
# 查看监听端口
netstat -tulpn
ss -tulpn

# 测试端口连通性
nc -zv example.com 80
telnet example.com 443

# 检查远程服务是否可达
curl http://example.com:8080
```

### 场景 3: 数据库连接测试

```bash
# MySQL 端口测试
nc -zv mysql.example.com 3306
telnet mysql.example.com 3306

# Redis 端口测试
nc -zv redis.example.com 6379
telnet redis.example.com 6379
```

### 场景 4: 文件传输

```bash
# 使用 nc 传输文件 (接收端先执行)
nc -l 1234 > received.txt

# 发送端
nc target.example.com 1234 < file.txt

# 使用 wget 下载
wget -c https://example.com/large-file.zip
```

---

## 命令速查表

| 分类 | 常用命令 |
|------|----------|
| 连通性 | `ping` |
| 路由追踪 | `traceroute`, `tracert` |
| 连接状态 | `netstat`, `ss` |
| DNS 查询 | `nslookup`, `dig` |
| HTTP 请求 | `curl` |
| 文件下载 | `wget` |
| 端口测试 | `telnet`, `nc` |
| 综合工具 | `nc` (瑞士军刀) |
