# Nginx 命令文档

Nginx 服务器管理完整参考文档。

## 目录

- [配置管理](#配置管理)
- [信号控制](#信号控制)
- [日志查看](#日志查看)
- [实用场景](#实用场景)

---

## 配置管理

### nginx -t - 配置测试

**基础用法**:
```bash
nginx -t
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定配置文件测试 | `nginx -t -c %{配置文件路径}%` | 配置文件示例：`/etc/nginx/nginx.conf` |
| 测试并设置全局指令 | `nginx -t -g %{全局指令}%` | 全局指令示例：`daemon off;` |

### nginx -T - 配置验证

**基础用法**:
```bash
nginx -T
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看完整配置并搜索 | `nginx -T | grep %{关键字}%` | 关键字示例：`server_name` |
| 保存配置到文件 | `nginx -T > %{输出文件}% 2>&1` | 输出文件示例：`/tmp/nginx-config.txt` |

### nginx -c - 指定配置

**基础用法**:
```bash
nginx -c %{配置文件路径}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 使用指定配置启动 | `nginx -c %{配置文件路径}%` | 配置文件示例：`/etc/nginx/nginx.conf` 【常用】 |
| 测试配置后启动 | `nginx -t && nginx -c %{配置文件路径}%` | 配置文件示例：`/etc/nginx/nginx.conf` 【常用】 |

---

## 信号控制

### nginx -s - 信号控制

**基础用法**:
```bash
nginx -s %{信号}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 重载配置 | `nginx -s reload` | 优雅重载Nginx配置，不中断连接 【常用】 |
| 停止服务 | `nginx -s stop` | 强制停止Nginx服务 |
| 优雅退出 | `nginx -s quit` | 等待所有请求处理完毕后关闭 【常用】 |
| 重新打开日志 | `nginx -s reopen` | 用于日志轮转后重新打开日志文件 |

---

## 日志查看

### tail -f - 查看日志

**基础用法**:
```bash
tail -f %{日志文件}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看访问日志 | `tail -f %{日志目录}%/access.log` | 日志目录示例：`/var/log/nginx` 【常用】 |
| 查看错误日志 | `tail -f %{日志目录}%/error.log` | 日志目录示例：`/var/log/nginx` 【常用】 |
| 查看最后N行 | `tail -n %{行数}% %{日志文件}%` | 行数示例：`100`；日志文件示例：`/var/log/nginx/access.log` 【常用】 |
| 同时查看多日志 | `tail -f %{日志目录}%/access.log %{日志目录}%/error.log` | 日志目录示例：`/var/log/nginx` |

---

## 实用场景

### 场景 1: 部署后验证配置

```bash
# 1. 修改配置后测试
nginx -t

# 2. 查看详细测试输出
nginx -t -c /etc/nginx/nginx.conf

# 3. 确认测试成功后重载
nginx -s reload
```

### 场景 2: 日志排查问题

```bash
# 1. 实时查看访问日志
tail -f /var/log/nginx/access.log

# 2. 实时查看错误日志
tail -f /var/log/nginx/error.log

# 3. 查看最近100行错误
tail -n 100 /var/log/nginx/error.log

# 4. 搜索特定IP的访问记录
tail -f /var/log/nginx/access.log | grep %{IP地址}%
```

### 场景 3: 配置文件验证

```bash
# 1. 查看完整配置（包括默认服务器）
nginx -T

# 2. 搜索特定配置项
nginx -T | grep server_name

# 3. 保存配置用于审计
nginx -T > /tmp/nginx-config.txt 2>&1
```

### 场景 4: 启动和停止

```bash
# 1. 使用默认配置启动
nginx

# 2. 使用指定配置启动
nginx -c /etc/nginx/nginx.conf

# 3. 测试配置后启动
nginx -t && nginx -c /etc/nginx/nginx.conf

# 4. 优雅停止（等待请求处理完）
nginx -s quit

# 5. 强制停止
nginx -s stop
```

---

## 命令速查表

| 操作 | 命令 | 说明 |
|------|------|------|
| 测试配置 | `nginx -t` | 测试Nginx配置文件语法 |
| 验证并转储配置 | `nginx -T` | 显示完整配置用于验证 |
| 指定配置启动 | `nginx -c %{path}%` | 使用指定配置文件启动 |
| 重载配置 | `nginx -s reload` | 优雅重载配置 |
| 停止服务 | `nginx -s stop` | 强制停止服务 |
| 优雅退出 | `nginx -s quit` | 等待请求完成后停止 |
| 查看访问日志 | `tail -f access.log` | 实时查看访问日志 |
| 查看错误日志 | `tail -f error.log` | 实时查看错误日志 |

---

## 相关资源

- [快速开始指南](../quick-start.md)
- [Linux 命令文档](../linux-commands/README.md)
- [完整命令参考表](../../references/commands-reference.md)