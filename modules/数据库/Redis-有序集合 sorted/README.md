# Redis 有序集合

Redis 有序集合操作常用命令参考。

## ZADD 添加有序集合

**命令**: `ZADD %{键名}% %{分数}% %{成员}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| 键名 | string | 是 | 有序集合键名【常用】 | leaderboard |
| 分数 | number | 是 | 成员分数 | 100 |
| 成员 | string | 是 | 成员名 | alice |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 添加单个成员 | `redis-cli ZADD leaderboard 100 "alice"` | 键名=leaderboard, 分数=100, 成员=alice【常用】 |
| 批量添加 | `redis-cli ZADD leaderboard 100 "alice" 90 "bob"` | 一次添加多个成员 |
| 带选项添加 | `redis-cli ZADD leaderboard XX CH INCR 100 "alice"` | XX=仅更新存在的，CH=返回变更数，INCR=增量更新 |

---

## ZRANGE 查询有序集合

**命令**: `ZRANGE %{键名}% %{起始索引}% %{结束索引}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| 键名 | string | 是 | 有序集合键名【常用】 | leaderboard |
| 起始索引 | number | 是 | 起始索引位置 | 0 |
| 结束索引 | number | 是 | 结束索引位置（-1表示最后） | -1 |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 按索引范围查询 | `redis-cli ZRANGE leaderboard 0 -1` | 获取所有成员【常用】 |
| 带分数返回 | `redis-cli ZRANGE leaderboard 0 -1 WITHSCORES` | 同时返回成员的分数 |
| 带lex返回 | `redis-cli ZRANGE leaderboard [a (z BYLEX` | 按字典序范围查询 |

---

## ZREVRANGE 逆序查询

**命令**: `ZREVRANGE %{键名}% %{起始索引}% %{结束索引}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| 键名 | string | 是 | 有序集合键名 | leaderboard |
| 起始索引 | number | 是 | 起始索引位置 | 0 |
| 结束索引 | number | 是 | 结束索引位置 | -1 |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 逆序查询 | `redis-cli ZREVRANGE leaderboard 0 -1` | 分数从高到低返回 |
| 带分数逆序返回 | `redis-cli ZREVRANGE leaderboard 0 -1 WITHSCORES` | 同时返回分数 |

---

## ZRANK 获取排名

**命令**: `ZRANK %{键名}% %{成员}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| 键名 | string | 是 | 有序集合键名【常用】 | leaderboard |
| 成员 | string | 是 | 成员名 | alice |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 获取排名 | `redis-cli ZRANK leaderboard "alice"` | 返回成员排名（从小到大，0为最低分）【常用】 |
| 带分数获取排名 | `redis-cli ZRANK leaderboard "alice" WITHSCORE` | 同时返回分数 |

---

## ZREVRANK 逆序排名

**命令**: `ZREVRANK %{键名}% %{成员}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| 键名 | string | 是 | 有序集合键名 | leaderboard |
| 成员 | string | 是 | 成员名 | alice |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 获取逆序排名 | `redis-cli ZREVRANK leaderboard "alice"` | 返回成员逆排名（从大到小，0为最高分） |
| 带分数逆序排名 | `redis-cli ZREVRANK leaderboard "alice" WITHSCORE` | 同时返回分数 |

---

## ZSCORE 获取分数

**命令**: `ZSCORE %{键名}% %{成员}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| 键名 | string | 是 | 有序集合键名【常用】 | leaderboard |
| 成员 | string | 是 | 成员名 | alice |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 获取成员分数 | `redis-cli ZSCORE leaderboard "alice"` | 返回成员的分数【常用】 |

---

## ZCARD 获取成员数

**命令**: `ZCARD %{键名}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| 键名 | string | 是 | 有序集合键名 | leaderboard |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 获取成员数量 | `redis-cli ZCARD leaderboard` | 返回有序集合的成员数 |

---

## ZCOUNT 统计分数范围成员

**命令**: `ZCOUNT %{键名}% %{最小分数}% %{最大分数}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| 键名 | string | 是 | 有序集合键名 | leaderboard |
| 最小分数 | number | 是 | 最小分数（闭区间） | 80 |
| 最大分数 | number | 是 | 最大分数（闭区间） | 100 |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 闭区间统计 | `redis-cli ZCOUNT leaderboard 80 100` | 统计分数在80-100之间的成员数 |

---

## ZRANGEBYSCORE 按分数范围查询

**命令**: `ZRANGEBYSCORE %{键名}% %{最小分数}% %{最大分数}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| 键名 | string | 是 | 有序集合键名 | leaderboard |
| 最小分数 | number | 是 | 最小分数 | 0 |
| 最大分数 | number | 是 | 最大分数 | 100 |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 按分数范围查询 | `redis-cli ZRANGEBYSCORE leaderboard 0 100` | 获取分数在0-100之间的成员 |
| 带偏移量和限制 | `redis-cli ZRANGEBYSCORE leaderboard 0 100 LIMIT 0 10` | 偏移0，返回10个 |
| 带分数返回 | `redis-cli ZRANGEBYSCORE leaderboard 0 100 WITHSCORES` | 同时返回分数 |

---

## ZREM 删除成员

**命令**: `ZREM %{键名}% %{成员}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| 键名 | string | 是 | 有序集合键名 | leaderboard |
| 成员 | string | 是 | 成员名 | alice |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 删除单个成员 | `redis-cli ZREM leaderboard "alice"` | 从有序集合中删除成员 |
| 批量删除 | `redis-cli ZREM leaderboard "alice" "bob"` | 一次删除多个成员 |

---

## ZINCRBY 增加分数

**命令**: `ZINCRBY %{键名}% %{增量}% %{成员}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| 键名 | string | 是 | 有序集合键名 | leaderboard |
| 增量 | number | 是 | 分数增量 | 10 |
| 成员 | string | 是 | 成员名 | alice |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 增加成员分数 | `redis-cli ZINCRBY leaderboard 10 "alice"` | alice的分数+10 |
| 减少分数 | `redis-cli ZINCRBY leaderboard -10 "alice"` | 使用负数减少分数 |

---

## ZUNIONSTORE 并集存储

**命令**: `ZUNIONSTORE %{目标键名}% %{键数量}% %{键1}% %{键2}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| 目标键名 | string | 是 | 目标键名 | combined_leaderboard |
| 键数量 | number | 是 | 参与并集的键数量 | 2 |
| 键1 | string | 是 | 第一个源键 | leaderboard1 |
| 键2 | string | 是 | 第二个源键 | leaderboard2 |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 计算并集 | `redis-cli ZUNIONSTORE combined_leaderboard 2 leaderboard1 leaderboard2` | 计算多个有序集合的并集 |
| 带权重并集 | `redis-cli ZUNIONSTORE combined_leaderboard 2 leaderboard1 leaderboard2 WEIGHTS 1 2` | 权重1和2 |
| 带聚合方式 | `redis-cli ZUNIONSTORE combined_leaderboard 2 leaderboard1 leaderboard2 AGGREGATE SUM` | SUM/MIN/MAX |

---

## ZINTERSTORE 交集存储

**命令**: `ZINTERSTORE %{目标键名}% %{键数量}% %{键1}% %{键2}%`

**参数说明**:
| 参数 | 类型 | 必填 | 说明 | 示例 |
|------|------|------|------|------|
| 目标键名 | string | 是 | 目标键名 | intersection_result |
| 键数量 | number | 是 | 参与交集的键数量 | 2 |
| 键1 | string | 是 | 第一个源键 | leaderboard1 |
| 键2 | string | 是 | 第二个源键 | leaderboard2 |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 计算交集 | `redis-cli ZINTERSTORE intersection_result 2 leaderboard1 leaderboard2` | 计算多个有序集合的交集 |
| 带权重交集 | `redis-cli ZINTERSTORE intersection_result 2 leaderboard1 leaderboard2 WEIGHTS 1 1` | 权重均为1 |
| 带聚合方式 | `redis-cli ZINTERSTORE intersection_result 2 leaderboard1 leaderboard2 AGGREGATE MIN` | 取最小分数 |