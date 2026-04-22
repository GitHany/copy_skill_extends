# 搜索引擎与全文检索命令文档

全面覆盖 Elasticsearch、Meilisearch、Algolia、OpenSearch 等主流搜索引擎的完整命令参考。

## 目录

- [Elasticsearch 扩展](#elasticsearch-扩展)
- [Meilisearch](#meilisearch)
- [Algolia](#algolia)
- [OpenSearch](#opensearch)
- [搜索工具](#搜索工具)

---

## Elasticsearch 扩展

### Query DSL 高级查询

**基础用法**:
```bash
curl -X POST "http://localhost:9200/%{索引名}%/_search" -H "Content-Type: application/json" -d '%{查询JSON}%'
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| Multi-Match 查询 | `curl -X POST "http://localhost:9200/myindex/_search" -H "Content-Type: application/json" -d '{"query":{"multi_match":{"query":"关键词","fields":["title^2","content"]}}}'` | 【常用】索引名(示例: myindex); title^2 字段权重提升; title 字段(示例: content); Multi-Match 多字段匹配 |
| Fuzzy 模糊查询 | `curl -X POST "http://localhost:9200/myindex/_search" -H "Content-Type: application/json" -d '{"query":{"fuzzy":{"name":{"value":"张三","fuzziness":"AUTO"}}}}'` | 【常用】索引名(示例: myindex); name 字段(示例: 张三); fuzziness 模糊度(示例: AUTO 自动); 容忍拼写错误 |
| Prefix 前缀查询 | `curl -X POST "http://localhost:9200/myindex/_search" -H "Content-Type: application/json" -d '{"query":{"prefix":{"code":"PRJ"}}}'` | 【常用】索引名(示例: myindex); code 字段(示例: PRJ 前缀); 匹配以指定字符开头的词 |
| Wildcard 通配符查询 | `curl -X POST "http://localhost:9200/myindex/_search" -H "Content-Type: application/json" -d '{"query":{"wildcard":{"name":"张*"}}}'` | 【常用】索引名(示例: myindex); name 字段(示例: 张*); * 匹配任意字符; Wildcard 支持通配符 |
| Range 范围查询 | `curl -X POST "http://localhost:9200/myindex/_search" -H "Content-Type: application/json" -d '{"query":{"range":{"age":{"gte":18,"lte":60,"format":"yyyy"}}}}'` | 【常用】索引名(示例: myindex); gte 大于等于(示例: 18); lte 小于等于(示例: 60); format 日期格式(示例: yyyy) |
| Exists 存在查询 | `curl -X POST "http://localhost:9200/myindex/_search" -H "Content-Type: application/json" -d '{"query":{"exists":{"field":"email"}}}'` | 【常用】索引名(示例: myindex); email 字段(示例: email); 查询指定字段存在且非空的文档 |
| Script 脚本查询 | `curl -X POST "http://localhost:9200/myindex/_search" -H "Content-Type: application/json" -d '{"query":{"script":{"script":{"source":"doc[''price''].value > params.threshold","lang":"painless","params":{"threshold":100}}}}}'` | 【常用】索引名(示例: myindex); price 字段(示例: 100); painless 脚本; 自定义条件过滤 |
| IDS 查询 | `curl -X POST "http://localhost:9200/myindex/_search" -H "Content-Type: application/json" -d '{"query":{"ids":{"values":["1","2","3"]}}}'` | 【常用】索引名(示例: myindex); values 文档ID列表(示例: 1,2,3); 根据文档 ID 批量查询 |
| Constant Score | `curl -X POST "http://localhost:9200/myindex/_search" -H "Content-Type: application/json" -d '{"query":{"constant_score":{"filter":{"term":{"status":"active"}},"boost":1.2}}}'` | 【常用】索引名(示例: myindex); status 字段(示例: active); boost 权重(示例: 1.2); 过滤查询不评分 |

---

### _cat 索引与分片

**基础用法**:
```bash
curl -X GET "http://localhost:9200/_cat/%{资源}%?v"
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看所有索引 | `curl -X GET "http://localhost:9200/_cat/indices?v"` | 【常用】_cat/indices 查看所有索引; ?v 显示表头; health/status/index 列 |
| 查看分片详情 | `curl -X GET "http://localhost:9200/_cat/shards?v"` | 【常用】_cat/shards 查看分片; ?v 显示表头; index/shard/state 列 |
| 查看主分片 | `curl -X GET "http://localhost:9200/_cat/shards?v&h=index,shard,prirep,state,store"` | 【常用】prirep 主分片/副本分片; state 分片状态; store 存储大小 |
| 查看未分配分片 | `curl -X GET "http://localhost:9200/_cat/shards?v&h=index,shard,prirep,state,unassigned.reason"` | 【常用】unassigned.reason 未分配原因; ALLOCATED 正常; UNASSIGNED 未分配 |
| 查看索引模板 | `curl -X GET "http://localhost:9200/_cat/templates?v"` | 【常用】_cat/templates 查看模板; name/index patterns 列 |
| 查看别名 | `curl -X GET "http://localhost:9200/_cat/aliases?v"` | 【常用】_cat/aliases 查看别名; alias/index/filter/routing 列 |
| 查看字段数据 | `curl -X GET "http://localhost:9200/_cat/fielddata?v"` | 【常用】_cat/fielddata 查看字段数据; field/size 列; 内存占用情况 |
| 查看恢复进度 | `curl -X GET "http://localhost:9200/_cat/recovery?v"` | 【常用】_cat/recovery 查看恢复; index/shard/type/stage 列; 索引恢复状态 |

---

### 集群与节点高级操作

**基础用法**:
```bash
curl -X GET "http://localhost:9200/_cluster/%{操作}%"
```

**扩展开示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 节点信息 | `curl -X GET "http://localhost:9200/_cat/nodes?v&h=name,heap.current,heap.percent,heap.max"` | 【常用】heap.current 当前堆内存; heap.percent 堆内存使用率; name 节点名称 |
| 节点 Hot Threads | `curl -X GET "http://localhost:9200/_nodes/hot_threads"` | 【常用】_nodes/hot_threads 查看热点线程; identify 标识线程; 帮助定位性能瓶颈 |
| 集群设置 | `curl -X GET "http://localhost:9200/_cluster/settings?flat_settings=true"` | 【常用】flat_settings 扁平化输出; transient 临时设置; persistent 永久设置 |
| 更新集群设置 | `curl -X PUT "http://localhost:9200/_cluster/settings" -H "Content-Type: application/json" -d '{"transient":{"indices.recovery.max_bytes_per_sec":"50mb"}}'` | 【常用】transient 临时设置; indices.recovery.max_bytes_per_sec 恢复速度(示例: 50mb) |
| 节点角色信息 | `curl -X GET "http://localhost:9200/_cat/nodes?v&h=name,node.role,master"` | 【常用】node.role 节点角色(m=主节点, d=数据节点, i= ingest节点); master 是否为主节点 |
| 分片重新路由 | `curl -X POST "http://localhost:9200/_cluster/reroute" -H "Content-Type: application/json" -d '{"commands":[{"allocate_empty_primary":{"index":"myindex","shard":0,"node":"node1","accept_data_loss":true}}]}'` | 【常用】reroute 手动分片分配; allocate_empty_primary 分配空主分片; accept_data_loss 接受数据丢失 |
| 任务管理 | `curl -X GET "http://localhost:9200/_tasks?detailed=true&actions=*search"` | 【常用】_tasks 查看任务; detailed 详细视图; *search 搜索相关任务; group_by 按组分类 |
| 取消任务 | `curl -X POST "http://localhost:9200/_tasks/node1:12345/_cancel"` | 【常用】node1:12345 任务ID; _cancel 取消任务; 停止正在运行的任务 |

---

### Painless 脚本

**基础用法**:
```bash
curl -X POST "http://localhost:9200/%{索引名}%/_update/%{文档ID}%" -H "Content-Type: application/json" -d '{"script":{"source":"%{脚本内容}%","lang":"painless","params":%{参数}%}}'
```

**扩展开示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 字段自增 | `curl -X POST "http://localhost:9200/myindex/_update/1" -H "Content-Type: application/json" -d '{"script":{"source":"ctx._source.views += params.inc","lang":"painless","params":{"inc":1}}}'` | 【常用】索引名(示例: myindex); ctx._source.views 操作字段; params.inc 参数(示例: 1) |
| 条件更新 | `curl -X POST "http://localhost:9200/myindex/_update/1" -H "Content-Type: application/json" -d '{"script":{"source":"if (ctx._source.status == params.old) { ctx._source.status = params.new }","lang":"painless","params":{"old":"pending","new":"done"}}}'` | 【常用】索引名(示例: myindex); if 条件判断; old 原值(示例: pending); new 新值(示例: done) |
| 数组操作 | `curl -X POST "http://localhost:9200/myindex/_update/1" -H "Content-Type: application/json" -d '{"script":{"source":"ctx._source.tags.add(params.tag)","lang":"painless","params":{"tag":"featured"}}}'` | 【常用】索引名(示例: myindex); ctx._source.tags 数组字段; .add() 添加元素; tag 标签(示例: featured) |
| Map 对象操作 | `curl -X POST "http://localhost:9200/myindex/_update/1" -H "Content-Type: application/json" -d '{"script":{"source":"ctx._source.metadata.put(params.key, params.value)","lang":"painless","params":{"key":"priority","value":"high"}}}'` | 【常用】索引名(示例: myindex); metadata.put() 设置键值; key 键名(示例: priority); value 值(示例: high) |
| 字符串操作 | `curl -X POST "http://localhost:9200/myindex/_update/1" -H "Content-Type: application/json" -d '{"script":{"source":"ctx._source.name = ctx._source.name.toUpperCase()","lang":"painless"}}'` | 【常用】索引名(示例: myindex); .toUpperCase() 转大写; Painless 字符串内置方法 |
| 删除字段 | `curl -X POST "http://localhost:9200/myindex/_update/1" -H "Content-Type: application/json" -d '{"script":{"source":"ctx._source.remove(params.field)","lang":"painless","params":{"field":"temp_data"}}}'` | 【常用】索引名(示例: myindex); ctx._source.remove() 删除字段; field 字段名(示例: temp_data) |
| Bulk 脚本更新 | `curl -X POST "http://localhost:9200/_bulk" -H "Content-Type: application/json" --data-binary '{"update":{"_index":"myindex","_id":"1"}}\n{"script":{"source":"ctx._source.score += params.delta","lang":"painless","params":{"delta":10}}}\n'` | 【常用】_bulk 批量操作; update 更新操作; score 分数字段(示例: 10); delta 增量值 |
| Transform 数据转换 | `curl -X POST "http://localhost:9200/_reindex" -H "Content-Type: application/json" -d '{"source":{"index":"myindex"},"dest":{"index":"myindex_v2"},"script":{"source":"ctx._source.timestamp = ctx._source.created_at.getMillis()","lang":"painless"}}'` | 【常用】_reindex 数据重建; ctx._source.timestamp 目标字段; .getMillis() 转换为时间戳; created_at 源字段 |

---

### ILM 索引生命周期管理

**基础用法**:
```bash
curl -X GET "http://localhost:9200/_ilm/policy/%{策略名}%"
```

**扩展开示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看 ILM 策略 | `curl -X GET "http://localhost:9200/_ilm/policy/my_policy"` | 【常用】策略名(示例: my_policy); phases 包含 hot/warm/delete 阶段 |
| 创建 ILM 策略 | `curl -X PUT "http://localhost:9200/_ilm/policy/my_policy" -H "Content-Type: application/json" -d '{"policy":{"phases":{"hot":{"min_age":"0ms","actions":{"rollover":{"max_age":"7d","max_size":"50gb"},"set_priority":{"priority":100}}}}}}'` | 【常用】策略名(示例: my_policy); hot 热阶段(示例: 0ms); rollover 滚动(示例: 7d/50gb); set_priority 优先级(示例: 100) |
| 热阶段压缩 | `curl -X PUT "http://localhost:9200/_ilm/policy/my_policy" -H "Content-Type: application/json" -d '{"policy":{"phases":{"hot":{"actions":{"forcemerge":{"max_num_segments":1},"rollover":{"max_age":"1d"}}}}}}'` | 【常用】策略名(示例: my_policy); forcemerge 强制合并(示例: 1 段); rollover 滚动(示例: 1d) |
| 暖阶段冷却 | `curl -X PUT "http://localhost:9200/_ilm/policy/my_policy" -H "Content-Type: application/json" -d '{"policy":{"phases":{"warm":{"min_age":"30d","actions":{"shrink":{"number_of_shards":1},"allocate":{"number_of_replicas":0}}}}}}'` | 【常用】策略名(示例: my_policy); min_age 最小年龄(示例: 30d); shrink 收缩分片(示例: 1); allocate 分配副本(示例: 0) |
| 冷阶段冻结 | `curl -X PUT "http://localhost:9200/_ilm/policy/my_policy" -H "Content-Type: application/json" -d '{"policy":{"phases":{"cold":{"min_age":"60d","actions":{"freeze":{}}}}}}'` | 【常用】策略名(示例: my_policy); min_age 最小年龄(示例: 60d); freeze 冻结索引; 冻结后无法写入 |
| 删除阶段 | `curl -X PUT "http://localhost:9200/_ilm/policy/my_policy" -H "Content-Type: application/json" -d '{"policy":{"phases":{"delete":{"min_age":"90d","actions":{"delete":{}}}}}}'` | 【常用】策略名(示例: my_policy); min_age 最小年龄(示例: 90d); delete 删除操作; 自动清理旧数据 |
| 应用策略到索引 | `curl -X PUT "http://localhost:9200/myindex/_settings" -H "Content-Type: application/json" -d '{"settings":{"index.lifecycle.name":"my_policy"}}'` | 【常用】索引名(示例: myindex); index.lifecycle.name 策略名(示例: my_policy) |
| 查看索引 ILM 状态 | `curl -X GET "http://localhost:9200/myindex/_ilm/explain"` | 【常用】索引名(示例: myindex); _ilm/explain 查看生命周期状态; phase_current 当前阶段 |
| 索引模板绑定策略 | `curl -X PUT "http://localhost:9200/_index_template/my_template" -H "Content-Type: application/json" -d '{"index_patterns":["logs-*"],"template":{"settings":{"index.lifecycle.name":"my_policy"}}}}'` | 【常用】模板名(示例: my_template); index_patterns 索引模式(示例: logs-*); 自动应用策略 |

---

## Meilisearch

### Meilisearch 启动与配置

**基础用法**:
```bash
meilisearch --http-addr 127.0.0.1:7700 --master-key "%{主密钥}%"
```

**扩展开示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 默认启动 | `meilisearch` | 【常用】默认监听 127.0.0.1:7700; 无认证; 首次启动生成 master key |
| 指定端口启动 | `meilisearch --http-addr 0.0.0.0:7700 --master-key "masterKey123"` | 【常用】http-addr 监听地址(示例: 0.0.0.0:7700); master-key 主密钥(示例: masterKey123); 启用认证 |
| 指定数据目录 | `meilisearch --db-path /var/lib/meilisearch/data --http-addr 127.0.0.1:7700` | 【常用】db-path 数据目录(示例: /var/lib/meilisearch/data); http-addr 地址(示例: 127.0.0.1:7700) |
| 启用压缩 | `meilisearch --http-addr 127.0.0.1:7700 --env production --no-analytics` | 【常用】env 环境(示例: production); no-analytics 禁用分析; 生产环境推荐 |
| Docker 启动 | `docker run -d -p 7700:7700 -e MEILI_MASTER_KEY=masterKey123 -v /meili_data:/meili_data getmeili/meilisearch` | 【常用】MEILI_MASTER_KEY 环境变量; /meili_data:/meili_data 数据卷映射 |
| 查看版本 | `meilisearch --version` | 【常用】显示版本信息; meilisearch-cli --version 同效 |
| 显示帮助 | `meilisearch --help` | 【常用】显示所有可用参数; 配置项说明 |

---

### Meilisearch CLI - 索引操作

**基础用法**:
```bash
meilisearch-cli index %{操作}% --index-uid "%{索引UID}%"
```

**扩展开示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建索引 | `meilisearch-cli index create --index-uid "products" --primary-key "id"` | 【常用】index create 创建索引; index-uid 索引唯一标识(示例: products); primary-key 主键(示例: id) |
| 查看索引列表 | `meilisearch-cli index list` | 【常用】index list 查看所有索引; 显示 uid/primaryKey/documentCount |
| 查看索引信息 | `meilisearch-cli index get --index-uid "products"` | 【常用】index get 获取索引详情; index-uid 索引UID(示例: products) |
| 删除索引 | `meilisearch-cli index delete --index-uid "products"` | 【常用】index delete 删除索引; index-uid 索引UID(示例: products); 不可恢复 |
| 更新索引 | `meilisearch-cli index update --index-uid "products" --primary-key "product_id"` | 【常用】index update 更新索引配置; primary-key 新主键(示例: product_id) |
| 获取索引统计 | `meilisearch-cli index stats --index-uid "products"` | 【常用】index stats 获取统计; numberOfDocuments 文档数; is_indexing 是否索引中 |

---

### Meilisearch CLI - 文档操作

**基础用法**:
```bash
meilisearch-cli documents %{操作}% --index-uid "%{索引UID}%" --file "%{文件路径}%"
```

**扩展开示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 添加文档(JSON) | `meilisearch-cli documents add --index-uid "products" --file "/path/to/documents.json"` | 【常用】documents add 添加文档; file 文件路径(示例: /path/to/documents.json); 支持 JSON/JSONL |
| 添加文档(NDJSON) | `meilisearch-cli documents add --index-uid "products" --file "/path/to/data.ndjson" --content-type application/x-ndjson` | 【常用】content-type 内容类型(示例: application/x-ndjson); NDJSON 每行一条 JSON |
| 添加 CSV 文档 | `meilisearch-cli documents add --index-uid "products" --file "/path/to/data.csv" --content-type text/csv` | 【常用】content-type 内容类型(示例: text/csv); CSV 需包含表头行 |
| 替换所有文档 | `meilisearch-cli documents add --index-uid "products" --file "/path/to/data.json" --primary-key "id"` | 【常用】primary-key 主键(示例: id); 替换模式下添加覆盖已有文档 |
| 删除文档 | `meilisearch-cli documents delete --index-uid "products" --document-id "1"` | 【常用】documents delete 删除; document-id 文档ID(示例: 1) |
| 按条件删除 | `meilisearch-cli documents delete --index-uid "products" --filter "category = 'electronics'"` | 【常用】filter 过滤条件(示例: category = 'electronics'); 批量删除符合条件的文档 |
| 清空索引 | `meilisearch-cli documents delete-all --index-uid "products"` | 【常用】delete-all 清空所有文档; 危险操作,不可恢复 |
| 获取文档 | `meilisearch-cli documents get --index-uid "products" --document-id "1"` | 【常用】documents get 获取; document-id 文档ID(示例: 1) |

---

### Meilisearch CLI - 搜索操作

**基础用法**:
```bash
meilisearch-cli search "%{搜索词}%" --index-uid "%{索引UID}%"
```

**扩展开示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 基础搜索 | `meilisearch-cli search "手机" --index-uid "products"` | 【常用】搜索词(示例: 手机); index-uid 索引UID(示例: products); 返回匹配结果 |
| 带分页搜索 | `meilisearch-cli search "电脑" --index-uid "products" --offset 0 --limit 20` | 【常用】offset 偏移量(示例: 0); limit 每页数量(示例: 20); 分页获取结果 |
| 属性过滤搜索 | `meilisearch-cli search "电脑" --index-uid "products" --attributes-toRetrieve "name,price,category"` | 【常用】attributesToRetrieve 返回字段(示例: name,price,category); 减少返回数据量 |
| 高亮显示 | `meilisearch-cli search "手机" --index-uid "products" --attributesToHighlight "name,description"` | 【常用】attributesToHighlight 高亮字段(示例: name,description); 返回匹配处加标签 |
| 过滤条件搜索 | `meilisearch-cli search "电脑" --index-uid "products" --filter "price >= 1000 AND price <= 5000"` | 【常用】filter 过滤条件(示例: price >= 1000 AND price <= 5000); 价格区间筛选 |
| 排序搜索 | `meilisearch-cli search "电脑" --index-uid "products" --sort "price:asc"` | 【常用】sort 排序(示例: price:asc); 支持多字段排序(示例: price:asc,created_at:desc) |
| Faceted 搜索 | `meilisearch-cli search "" --index-uid "products" --facets "category,brand"` | 【常用】facets 分面统计(示例: category,brand); 聚合各分类的文档数量 |

---

### curl 操作 Meilisearch API

**基础用法**:
```bash
curl -X GET "http://localhost:7700/indexes/%{索引UID}%/search" -H "Authorization: Bearer %{API_KEY}%" -d '{"q":"%{搜索词}%"}'
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 健康检查 | `curl -X GET "http://localhost:7700/health"` | 【常用】返回 Meilisearch 健康状态; {"status":"available"} 表示正常 |
| 获取版本 | `curl -X GET "http://localhost:7700/version"` | 【常用】返回 Meilisearch 版本信息; pkgVersion/packageVersion |
| 创建索引 | `curl -X POST "http://localhost:7700/indexes" -H "Authorization: Bearer masterKey123" -H "Content-Type: application/json" -d '{"uid":"products","primaryKey":"id"}'` | 【常用】uid 索引唯一标识(示例: products); primaryKey 主键(示例: id) |
| 搜索接口 | `curl -X POST "http://localhost:7700/indexes/products/search" -H "Authorization: Bearer masterKey123" -H "Content-Type: application/json" -d '{"q":"手机","limit":20}'` | 【常用】q 查询词(示例: 手机); limit 限制条数(示例: 20); 返回 hits/estimatedTotalHits |
| 添加文档 | `curl -X POST "http://localhost:7700/indexes/products/documents" -H "Authorization: Bearer masterKey123" -H "Content-Type: application/json" -d '[{"id":1,"name":"手机","price":2999}]'` | 【常用】documents 接口添加; id 文档ID(示例: 1); name 名称(示例: 手机); price 价格(示例: 2999) |
| 获取文档 | `curl -X GET "http://localhost:7700/indexes/products/documents/1" -H "Authorization: Bearer masterKey123"` | 【常用】documents/1 获取单文档; 1 文档ID; 返回完整文档 |
| 删除文档 | `curl -X DELETE "http://localhost:7700/indexes/products/documents/1" -H "Authorization: Bearer masterKey123"` | 【常用】DELETE 删除; documents/1 删除单文档; 返回 taskUid 用于查询进度 |
| 获取任务状态 | `curl -X GET "http://localhost:7700/tasks/123" -H "Authorization: Bearer masterKey123"` | 【常用】tasks/123 任务ID(示例: 123); status 任务状态(enqueued/processing/done/failed) |

---

## Algolia

### Algolia CLI 操作

**基础用法**:
```bash
algolia %{操作}%
```

**扩展开示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 配置凭证 | `algolia configure --app-id YOUR_APP_ID --api-key YOUR_API_KEY` | 【常用】configure 配置认证; app-id 应用ID(示例: YOUR_APP_ID); api-key API密钥 |
| 列出索引 | `algolia list indices` | 【常用】list indices 列出所有索引; 显示索引名称和记录数 |
| 查看索引信息 | `algolia index show %{索引名}%` | 【常用】index show 查看索引; 索引名(示例: products); 显示配置和统计 |
| 复制索引 | `algolia index copy --from %{源索引}% --to %{目标索引}%` | 【常用】index copy 复制索引; 源索引(示例: products); 目标索引(示例: products_backup) |
| 移动索引 | `algolia index move --from %{源索引}% --to %{目标索引}%` | 【常用】index move 移动索引; 原子操作; 常用于索引重命名 |
| 删除索引 | `algolia index delete %{索引名}%` | 【常用】index delete 删除索引; 索引名(示例: products); 不可恢复 |

---

### Algolia Index 操作

**基础用法**:
```bash
algolia index %{操作}% --index %{索引名}%
```

**扩展开示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 搜索记录 | `algolia index search --index products --query "手机" --hits 20` | 【常用】index search 搜索; query 搜索词(示例: 手机); hits 返回条数(示例: 20) |
| 搜索+分页 | `algolia index search --index products --query "电脑" --page 0 --hitsPerPage 20` | 【常用】page 页码(示例: 0); hitsPerPage 每页数量(示例: 20); 分页查询 |
| 配置索引 | `algolia index configure --index products --searchableAttributes "name,description,brand"` | 【常用】configure 配置; searchableAttributes 可搜索字段(示例: name,description,brand) |
| 设置排名 | `algolia index ranking --index products --ranking "typo,geo,words,proximity,attribute,exact,custom"` | 【常用】ranking 排名规则; typo 拼写; geo 距离; custom 自定义; 按优先级排列 |
| 添加记录 | `algolia index add --index products --file /path/to/data.json` | 【常用】index add 添加; file 文件路径(示例: /path/to/data.json); 支持 JSON 数组 |
| 清空索引 | `algolia index clear --index products` | 【常用】index clear 清空; 索引名(示例: products); 删除所有记录但保留配置 |

---

### Algolia CLI 其他操作

**基础用法**:
```bash
algolia browse %{索引名}%
```

**扩展开示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 浏览记录 | `algolia browse products --page 0 --hitsPerPage 100` | 【常用】browse 浏览; page 页码(示例: 0); hitsPerPage 每页数量(示例: 100) |
| 导出索引 | `algolia export products --file /path/to/export.json` | 【常用】export 导出; file 导出文件路径(示例: /path/to/export.json) |
| 导入索引 | `algolia import products --file /path/to/data.json --batchSize 1000` | 【常用】import 导入; batchSize 批量大小(示例: 1000); 影响导入速度 |
| 查看分面 | `algolia index facets --index products --attributes "category,brand"` | 【常用】facets 分面统计; attributes 属性(示例: category,brand); 聚合各值计数 |
| 设置同义词 | `algolia index synonyms --index products --synonyms '{"手机":["移动电话","智能手机"]}'` | 【常用】synonyms 同义词; 手机 关键词(示例: 移动电话,智能手机); 扩展搜索匹配 |
| 设置拼写容忍 | `algolia index settings --index products --typoTolerance true --minWordSizeforTypos 4` | 【常用】typoTolerance 拼写容忍(示例: true); minWordSizeforTypos 最小容错词长(示例: 4) |
| 克隆设置 | `algolia index copy-settings --from products --to products_backup` | 【常用】copy-settings 克隆设置; from 源索引(示例: products); to 目标索引(示例: products_backup) |

---

## OpenSearch

### OpenSearch 启动与配置

**基础用法**:
```bash
./opensearch-node-name --install
./opensearch-node-name
```

**扩展开示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 单节点启动 | `./opensearch-2.11.0/bin/opensearch -d -p pid` | 【常用】opensearch 主程序; -d 后台运行; -p pid 文件记录进程ID |
| 指定集群名称 | `./opensearch -E cluster.name=my-cluster -E node.name=node1` | 【常用】cluster.name 集群名(示例: my-cluster); node.name 节点名(示例: node1) |
| 指定网络地址 | `./opensearch -E network.host=0.0.0.0 -E http.port=9200` | 【常用】network.host 监听地址(示例: 0.0.0.0); http.port 端口(示例: 9200) |
| Docker 启动 | `docker run -d -p 9200:9200 -p 9600:9600 -e "discovery.type=single-node" opensearchproject/opensearch` | 【常用】discovery.type=single-node 单节点模式; 9600 性能分析端口 |
| 安全模式启动 | `./opensearch -E plugins.security.enabled=true` | 【常用】plugins.security.enabled 启用安全插件; 需配置认证和 TLS |
| 查看节点信息 | `curl -X GET "https://localhost:9200/_nodes?pretty" -k -u admin:admin` | 【常用】-k 忽略 SSL 证书; -u 认证用户(示例: admin:admin); _nodes 查看节点 |

---

### OpenSearch CLI

**基础用法**:
```bash
opensearch-cli %{操作}%
```

**扩展开示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 列出索引 | `opensearch-cli index list --endpoint https://localhost:9200 --auth username:password` | 【常用】index list 列出索引; endpoint 端点(示例: https://localhost:9200); auth 认证(示例: username:password) |
| 创建索引 | `opensearch-cli index create --index-name products --body /path/to/mapping.json --endpoint https://localhost:9200 --auth username:password` | 【常用】index create 创建; index-name 索引名(示例: products); body mapping文件(示例: /path/to/mapping.json) |
| 搜索查询 | `opensearch-cli search --index-name products --query-file /path/to/query.json --endpoint https://localhost:9200 --auth username:password` | 【常用】search 搜索; query-file 查询文件(示例: /path/to/query.json); 返回 hits/aggregations |
| 文档操作 | `opensearch-cli document index --index-name products --id 1 --body /path/to/doc.json --endpoint https://localhost:9200 --auth username:password` | 【常用】document index 索引文档; id 文档ID(示例: 1); body 文档内容(示例: /path/to/doc.json) |
| 集群健康 | `opensearch-cli cluster health --endpoint https://localhost:9200 --auth username:password` | 【常用】cluster health 健康检查; status 状态(green/yellow/red); numberOfNodes 节点数 |
| 批量导入 | `opensearch-cli bulk --index-name products --file /path/to/bulk.ndjson --endpoint https://localhost:9200 --auth username:password` | 【常用】bulk 批量; file 批量文件(示例: /path/to/bulk.ndjson); NDJSON 格式 |

---

### OpenSearch 特有 API

**基础用法**:
```bash
curl -X GET "https://localhost:9200/_opensearch/%{操作}%" -u admin:admin -k
```

**扩展开示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| OpenSearch Dashboards 健康 | `curl -X GET "https://localhost:9200/_opensearch/dashboards/health" -k -u admin:admin` | 【常用】dashboards/health 仪表板健康; cluster_status 集群状态 |
| 统计信息 | `curl -X GET "https://localhost:9200/_opensearch/stats?pretty" -k -u admin:admin` | 【常用】stats 统计; indices/indexing/index 索引统计; nodes/os/jvm 节点统计 |
| SQL 查询 | `curl -X POST "https://localhost:9200/_plugins/_query/sql" -k -u admin:admin -H "Content-Type: application/json" -d '{"query":"SELECT * FROM products LIMIT 10"}'` | 【常用】_plugins/_query/sql SQL接口; query SQL语句(示例: SELECT * FROM products); 简化查询 |
| SQL 解释 | `curl -X POST "https://localhost:9200/_plugins/_query/sql/_explain" -k -u admin:admin -H "Content-Type: application/json" -d '{"query":"SELECT name FROM products WHERE price > 1000"}'` | 【常用】_explain SQL解释; query SQL语句(示例: WHERE price > 1000); 返回 OpenSearch DSL |
| _point_in_time | `curl -X POST "https://localhost:9200/products/_pit?keep_alive=1m" -k -u admin:admin` | 【常用】_pit 创建时间点; keep_alive 保留时间(示例: 1m); 用于跨索引搜索 |
| PIT 搜索 | `curl -X POST "https://localhost:9200/_search" -k -u admin:admin -H "Content-Type: application/json" -d '{"size":10,"query":{"match":{"name":"手机"}},"pit":{"id":"pit_id","keep_alive":"1m"}}'` | 【常用】pit.id 时间点ID(示例: pit_id); keep_alive 保留时间(示例: 1m); 支持分页翻页 |
| 异步搜索 | `curl -X POST "https://localhost:9200/products/_async_search?wait_for_completion_timeout=10s" -k -u admin:admin -H "Content-Type: application/json" -d '{"query":{"match_all":{}}}'` | 【常用】_async_search 异步搜索; wait_for_completion_timeout 超时(示例: 10s); 返回 search_id |

---

## 搜索工具

### curl 通用搜索 API

**基础用法**:
```bash
curl -X %{METHOD}% "%{URL}%" -H "Authorization: Bearer %{TOKEN}%" -H "Content-Type: application/json" -d '%{BODY}%'
```

**扩展开示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 通用 GET 请求 | `curl -X GET "https://api.example.com/search?q=关键词&limit=10"` | 【常用】GET 请求搜索; q 查询参数(示例: 关键词); limit 限制条数(示例: 10) |
| 带 Header 请求 | `curl -X POST "https://api.example.com/search" -H "Authorization: Bearer token123" -H "Content-Type: application/json" -d '{"query":"关键词"}'` | 【常用】Authorization 认证; Bearer token123 令牌(示例: token123); query 查询词 |
| 下载大文件 | `curl -X GET "https://api.example.com/search?q=关键词" -H "Accept: application/x-ndjson" -o results.ndjson` | 【常用】Accept 指定返回格式(示例: application/x-ndjson); -o 输出文件(示例: results.ndjson) |
| 超时设置 | `curl -X POST "https://api.example.com/search" -H "Content-Type: application/json" -d '{"q":"关键词"}' --max-time 30` | 【常用】max-time 超时(示例: 30秒); 防止请求hang住 |
| 重试机制 | `curl -X POST "https://api.example.com/search" -H "Content-Type: application/json" -d '{"q":"关键词"}' --retry 3 --retry-delay 2` | 【常用】retry 重试次数(示例: 3); retry-delay 重试间隔(示例: 2秒); 网络不稳定时使用 |
| 代理请求 | `curl -X GET "https://api.example.com/search?q=关键词" -x http://proxy.example.com:8080` | 【常用】-x 代理地址(示例: http://proxy.example.com:8080); 绕过网络限制 |
| 输出响应头 | `curl -X GET "https://api.example.com/search?q=关键词" -i` | 【常用】-i 显示响应头; 调试 API 返回的 Header 信息 |
| 静默模式 | `curl -s -X POST "https://api.example.com/search" -H "Content-Type: application/json" -d '{"q":"关键词"}'` | 【常用】-s 静默模式; 不显示进度条和错误; 适合脚本使用 |
| JSON 格式化 | `curl -s -X POST "https://api.example.com/search" -H "Content-Type: application/json" -d '{"q":"关键词"}' | jq '.'` | 【常用】jq '.' 格式化 JSON 输出; 提升可读性; 需要安装 jq |
| 提取字段 | `curl -s -X POST "https://api.example.com/search" -H "Content-Type: application/json" -d '{"q":"关键词"}' | jq '.hits.hits[]._source.name'` | 【常用】jq '.hits.hits[]._source.name' 提取字段; hits.hits 命中结果; name 字段名 |

---

### 搜索索引与数据同步

**基础用法**:
```bash
# 数据导入
curl -X POST "http://localhost:9200/_bulk" -H "Content-Type: application/json" --data-binary "@%{文件路径}%"
```

**扩展开示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| JSON 文件批量导入 | `curl -X POST "http://localhost:9200/products/_bulk" -H "Content-Type: application/json" --data-binary "@/data/products.json"` | 【常用】_bulk 批量; @ 文件引用(示例: @/data/products.json); JSON 格式按行 action+doc |
| NDJSON 文件导入 | `curl -X POST "http://localhost:9200/_bulk" -H "Content-Type: application/x-ndjson" --data-binary "@/data/records.ndjson"` | 【常用】application/x-ndjson NDJSON格式; @/data/records.ndjson 文件路径; 每行 action,下一行 doc |
| CSV 文件导入 | `cat /data/records.csv | jq -r '.[] | {index:{_index:"products",_id:.id}},.' | curl -X POST "http://localhost:9200/_bulk" -H "Content-Type: application/x-ndjson" --data-binary @-` | 【常用】jq 转换 CSV 为 NDJSON; index:{_index:"products"} 索引名(示例: products); id 字段(示例: .id) |
| 数据库同步到 ES | `sync-db --source postgresql://localhost:5432/db --target http://localhost:9200 --index products --batch 5000` | 【常用】sync-db 同步工具; source 数据库连接(示例: postgresql://localhost:5432/db); batch 批次大小(示例: 5000) |
| Logstash 数据管道 | `logstash -f /etc/logstash/pipeline.conf` | 【常用】logstash 数据管道; -f 配置文件(示例: /etc/logstash/pipeline.conf); 支持多数据源 |
| 实时数据订阅 | `curl -X POST "http://localhost:9200/products/_search?scroll=5m" -H "Content-Type: application/json" -d '{"query":{"match_all":{}}}'` | 【常用】scroll 滚动上下文(示例: 5m); scroll=5m 保持搜索上下文(示例: 5分钟) |
| Scroll 分页查询 | `curl -X GET "http://localhost:9200/_search/scroll" -H "Content-Type: application/json" -d '{"scroll":"5m","scroll_id":"DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAD4AAAA="}'` | 【常用】scroll_id 游标ID; scroll 保留时间(示例: 5m); 遍历大体量数据 |
| 索引别名切换 | `curl -X POST "http://localhost:9200/_aliases" -H "Content-Type: application/json" -d '{"actions":[{"add":{"index":"products_v2","alias":"products"}}]}'` | 【常用】_aliases 别名操作; add 添加别名; index 索引名(示例: products_v2); alias 别名(示例: products) |
| 零停机索引切换 | `curl -X POST "http://localhost:9200/_aliases" -H "Content-Type: application/json" -d '{"actions":[{"remove":{"index":"products_v1","alias":"products"}},{"add":{"index":"products_v2","alias":"products"}}]}'` | 【常用】remove 移除旧别名; add 添加新别名; products_v1 旧索引(示例: products_v1); products_v2 新索引(示例: products_v2); 原子切换 |
