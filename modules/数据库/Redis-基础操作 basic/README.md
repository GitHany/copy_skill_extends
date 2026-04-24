# Redis 基本操作

Redis 字符串操作常用命令参考。

## SET 设置键值

**命令**: `SET %{key}% %{value}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| key | string | 是 | 键名【常用】 | user:1001:name |
| value | string | 是 | 值 | hello |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 设置字符串值 | `redis-cli SET user:1001:name "张三"` | key=user:1001:name, value=张三【常用】 |
| 设置带过期时间 | `redis-cli SETEX session:abc 3600 "token_data"` | 过期时间=3600秒 |
| 设置 NX (不存在才设置) | `redis-cli SETNX lock:order "locked"` | 仅当键不存在时设置 |
| 设置 XX (存在才覆盖) | `redis-cli SET user:1001:name 新数据 XX` | 仅当键存在时覆盖 |
| 设置多个键值 | `redis-cli MSET user:1001:age 25 user:1001:city "北京"` | 批量设置多个键值 |

---

## GET 获取值

**命令**: `GET %{key}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| key | string | 是 | 键名【常用】 | user:1001:name |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 获取字符串值 | `redis-cli GET user:1001:name` | key=user:1001:name【常用】 |
| 获取多个键 | `redis-cli MGET user:1001:name user:1001:age` | 批量获取多个值 |

---

## DEL 删除键

**命令**: `DEL %{key}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| key | string | 是 | 键名【常用】 | user:1001:session |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 删除单个键 | `redis-cli DEL user:1001:session` | key=user:1001:session【常用】 |
| 删除多个键 | `redis-cli DEL user:1001:session user:1001:cache user:1001:temp` | 批量删除多个键 |

---

## EXISTS 检查键

**命令**: `EXISTS %{key}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| key | string | 是 | 键名 | user:1001:profile |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 检查单个键 | `redis-cli EXISTS user:1001:profile` | 返回1存在/0不存在 |
| 检查多个键 | `redis-cli EXISTS user:1001:profile user:1001:session user:1001:cache` | 批量检查多个键 |

---

## KEYS 查找键

**命令**: `KEYS %{pattern}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| pattern | string | 是 | 匹配模式【常用】 | user:* |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查找所有键 | `redis-cli KEYS '*'` | pattern=* 匹配所有 |
| 查找用户键 | `redis-cli KEYS 'user:*'` | pattern=user:*【常用】 |
| 查找带前缀的键 | `redis-cli KEYS 'cache:*'` | pattern=cache:* |

---

## EXPIRE 设置过期

**命令**: `EXPIRE %{key}% %{seconds}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| key | string | 是 | 键名【常用】 | session:abc |
| seconds | integer | 是 | 过期时间（秒） | 3600 |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 设置过期时间（秒） | `redis-cli EXPIRE session:abc 3600` | key=session:abc, seconds=3600【常用】 |
| 设置过期时间（分钟） | `redis-cli EXPIRE session:abc 30` | minutes=30 自动转换为秒 |

---

## TTL 查看剩余时间

**命令**: `TTL %{key}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| key | string | 是 | 键名 | user:1001:session |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看剩余生存时间 | `redis-cli TTL user:1001:session` | 返回-2不存在/-1永久/正数秒数 |

---

## PERSIST 移除过期

**命令**: `PERSIST %{key}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| key | string | 是 | 键名 | user:1001:session |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 移除过期时间 | `redis-cli PERSIST user:1001:session` | 使键永久有效 |

---

## TYPE 查看类型

**命令**: `TYPE %{key}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| key | string | 是 | 键名 | user:1001:profile |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看键类型 | `redis-cli TYPE user:1001:profile` | 返回string/list/set/zset/hash/none |

---

## RENAME 重命名键

**命令**: `RENAME %{oldkey}% %{newkey}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| oldkey | string | 是 | 原键名 | user:1001:old_name |
| newkey | string | 是 | 新键名 | user:1001:new_name |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 重命名键 | `redis-cli RENAME user:1001:old_name user:1001:new_name` | oldkey→newkey |

---

## APPEND 追加内容

**命令**: `APPEND %{key}% %{value}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| key | string | 是 | 键名 | user:1001:tags |
| value | string | 是 | 追加的值 | ,新标签 |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 追加字符串 | `redis-cli APPEND user:1001:tags ",新标签"` | 向字符串末尾追加内容 |

---

## STRLEN 获取长度

**命令**: `STRLEN %{key}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| key | string | 是 | 键名 | user:1001:bio |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 获取字符串长度 | `redis-cli STRLEN user:1001:bio` | 返回字符串值的字节长度 |

---

## INCR 自增

**命令**: `INCR %{key}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| key | string | 是 | 键名【常用】 | page:views:2024 |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 键值加 1 | `redis-cli INCR page:views:2024` | key=page:views:2024, 数值+1【常用】 |

---

## DECR 自减

**命令**: `DECR %{key}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| key | string | 是 | 键名 | stock:product001 |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 键值减 1 | `redis-cli DECR stock:product001` | 数值-1 |

---

## INCRBY 增量

**命令**: `INCRBY %{key}% %{increment}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| key | string | 是 | 键名 | user:1001:credits |
| increment | integer | 是 | 增量数值 | 100 |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 键值加指定数 | `redis-cli INCRBY user:1001:credits 100` | key + increment |

---

## DECRBY 减量

**命令**: `DECRBY %{key}% %{decrement}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| key | string | 是 | 键名 | user:1001:balance |
| decrement | integer | 是 | 减量数值 | 50 |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 键值减指定数 | `redis-cli DECRBY user:1001:balance 50` | key - decrement |

---

## SELECT 切换数据库

**命令**: `SELECT %{index}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| index | integer | 是 | 数据库编号 | 0 |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 切换到数据库 0 | `redis-cli SELECT 0` | index=0 |
| 切换到数据库 1 | `redis-cli SELECT 1` | index=1 |
| 切换到指定数据库 | `redis-cli SELECT 2` | index=2 |

---

## PING 测试连接

**命令**: `ping`

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 测试连接 | `redis-cli ping` | 返回 PONG 表示连接正常 |
| 带密码连接 | `redis-cli -a yourpassword ping` | password=yourpassword |
| 指定主机连接 | `redis-cli -h 127.0.0.1 ping` | host=127.0.0.1 |
| 指定端口连接 | `redis-cli -p 6379 ping` | port=6379 |