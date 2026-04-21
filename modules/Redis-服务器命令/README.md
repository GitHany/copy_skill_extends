# Redis 服务器命令

Redis 服务器管理常用命令参考。

## redis-cli 连接

**命令**: `redis-cli -h %{主机}% -p %{端口}% -a %{密码}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| 主机 | string | 否 | Redis 主机地址（默认 127.0.0.1） | 127.0.0.1 |
| 端口 | number | 否 | Redis 端口（默认 6379） | 6379 |
| 密码 | string | 否 | Redis 密码（无密码可省略 -a） | yourpassword |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 本地默认连接 | `redis-cli` | 连接到本地6379端口 |
| 指定主机连接 | `redis-cli -h 127.0.0.1` | host=127.0.0.1 |
| 指定端口连接 | `redis-cli -p 6379` | port=6379 |
| 带密码连接 | `redis-cli -a yourpassword` | password=yourpassword |
| 选择数据库 | `redis-cli -n 0` | 数据库号=0【常用】 |

---

## SELECT 选择数据库

**命令**: `SELECT %{数据库号}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| 数据库号 | number | 是 | 数据库编号【常用】 | 0 |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 切换到数据库 0 | `redis-cli SELECT 0` | 数据库号=0【常用】 |
| 切换到数据库 1 | `redis-cli SELECT 1` | 数据库号=1 |

---

## DBSIZE 数据库大小

**命令**: `DBSIZE`

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 获取当前数据库键数量 | `redis-cli DBSIZE` | 返回当前数据库的键数量 |

---

## FLUSHDB 清空数据库

**命令**: `FLUSHDB`

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 清空当前数据库 | `redis-cli FLUSHDB` | 清空当前数据库的所有键 |

---

## FLUSHALL 清空所有数据库

**命令**: `FLUSHALL`

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 清空所有数据库 | `redis-cli FLUSHALL` | 清空所有数据库的所有键【常用】 |

---

## SAVE 保存数据

**命令**: `SAVE`

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 同步保存数据 | `redis-cli SAVE` | 同步保存数据到磁盘（阻塞） |

---

## BGSAVE 后台保存

**命令**: `BGSAVE`

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 后台异步保存 | `redis-cli BGSAVE` | 后台异步保存数据到磁盘 |

---

## LASTSAVE 最后保存时间

**命令**: `LASTSAVE`

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 获取最后保存时间 | `redis-cli LASTSAVE` | 返回最后一次成功保存到磁盘的Unix时间戳 |

---

## INFO 服务器信息

**命令**: `INFO %{sections}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| sections | string | 否 | 信息板块（可选：server, clients, memory, persistence, replication, cpu, stats, keyspace） | memory |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 获取完整服务器信息 | `redis-cli INFO` | 返回所有服务器详细信息 |
| 获取内存信息 | `redis-cli INFO memory` | sections=memory【常用】 |
| 获取客户端信息 | `redis-cli INFO clients` | sections=clients |
| 获取持久化信息 | `redis-cli INFO persistence` | sections=persistence |
| 获取复制信息 | `redis-cli INFO replication` | sections=replication |
| 获取CPU信息 | `redis-cli INFO cpu` | sections=cpu |

---

## CONFIG GET 获取配置

**命令**: `CONFIG GET %{参数名}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| 参数名 | string | 是 | 配置参数名 | maxmemory |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 获取所有配置 | `redis-cli CONFIG GET *` | 返回所有配置参数 |
| 获取maxmemory配置 | `redis-cli CONFIG GET maxmemory` | 参数名=maxmemory |
| 获取databases配置 | `redis-cli CONFIG GET databases` | 参数名=databases |
| 获取appendonly配置 | `redis-cli CONFIG GET appendonly` | 参数名=appendonly |

---

## CONFIG SET 设置配置

**命令**: `CONFIG SET %{参数名}% %{参数值}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| 参数名 | string | 是 | 配置参数名 | maxmemory |
| 参数值 | string | 是 | 配置参数值 | 256mb |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 设置maxmemory | `redis-cli CONFIG SET maxmemory 256mb` | 参数名=maxmemory, 参数值=256mb |
| 设置loglevel | `redis-cli CONFIG SET loglevel notice` | 参数名=loglevel, 参数值=notice（debug/verbose/notice/warning） |

---

## SHUTDOWN 关闭服务器

**命令**: `SHUTDOWN %{选项}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| 选项 | string | 否 | 关闭选项（SAVE/NOSAVE） | SAVE |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安全关闭Redis | `redis-cli SHUTDOWN` | 安全关闭服务器 |
| 关闭并保存数据 | `redis-cli SHUTDOWN SAVE` | 关闭前先保存数据 |
| 关闭不保存数据 | `redis-cli SHUTDOWN NOSAVE` | 关闭不保存数据 |

---

## PING 测试连接

**命令**: `PING`

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 测试连接 | `redis-cli PING` | 返回 PONG 表示连接正常【常用】 |

---

## ECHO 打印消息

**命令**: `ECHO %{消息}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| 消息 | string | 是 | 要打印的消息 | hello |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 打印消息 | `redis-cli ECHO "hello"` | 消息=hello，返回相同内容 |

---

## TIME 服务器时间

**命令**: `TIME`

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 获取服务器时间 | `redis-cli TIME` | 返回Unix时间戳和微秒数 |