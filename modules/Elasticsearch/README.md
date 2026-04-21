# Elasticsearch 命令文档

Elasticsearch 完整参考文档，涵盖 REST API、索引管理、查询操作等。

## 📚 目录

- [CRUD 操作](#crud-操作)
- [索引操作](#索引操作)
- [Mapping 操作](#mapping-操作)
- [搜索查询](#搜索查询)
- [统计操作](#统计操作)
- [集群操作](#集群操作)
- [文档操作](#文档操作)

---

## CRUD 操作

### curl - Elasticsearch REST API

**基础用法**:
```bash
curl -X %{METHOD}% http://%{主机}%:%{端口}%/%{索引名}%/%{类型名}%/%{文档ID}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| GET 查询文档 | `curl -X GET "http://localhost:9200/%{索引名}%/_search"` | 【常用】索引名(示例: myindex); _search 搜索接口 |
| POST 创建文档 | `curl -X POST "http://localhost:9200/myindex/_doc/1" -H "Content-Type: application/json" -d '{"name":"张三"}'` | 【常用】POST 自动生成 _id; _doc 类型; 索引名(示例: myindex); 文档ID(示例: 1); JSON数据(示例: {"name":"张三"}) |
| PUT 创建/替换文档 | `curl -X PUT "http://localhost:9200/myindex/_doc/1?pretty" -H "Content-Type: application/json" -d '{"name":"张三","age":30}'` | 【常用】PUT 幂等操作; ?pretty 格式化输出; 索引名(示例: myindex); 文档ID(示例: 1) |
| DELETE 删除文档 | `curl -X DELETE "http://localhost:9200/myindex/_doc/1"` | 【常用】索引名(示例: myindex); 文档ID(示例: 1); 删除指定文档 |
| HEAD 检查文档存在 | `curl -I "http://localhost:9200/myindex/_doc/1"` | 【常用】索引名(示例: myindex); 文档ID(示例: 1); 返回 200 表示存在 |

---

## 索引操作

### 创建索引

**基础用法**:
```bash
curl -X PUT "http://localhost:9200/%{索引名}%"
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建索引(默认设置) | `curl -X PUT "http://localhost:9200/myindex"` | 【常用】索引名(示例: myindex); 使用默认分片数和副本数 |
| 创建索引(带配置) | `curl -X PUT "http://localhost:9200/myindex" -H "Content-Type: application/json" -d '{"settings":{"number_of_shards":3,"number_of_replicas":1}}'` | 【常用】number_of_shards 分片数(示例: 3); number_of_replicas 副本数(示例: 1) |
| 删除索引 | `curl -X DELETE "http://localhost:9200/myindex"` | 【常用】索引名(示例: myindex); 删除后不可恢复 |
| 查看所有索引 | `curl -X GET "http://localhost:9200/_cat/indices?v"` | 【常用】_cat/indices 查看索引列表; ?v 显示表头 |
| 查看单个索引 | `curl -X GET "http://localhost:9200/myindex"` | 【常用】索引名(示例: myindex); 显示索引详细信息 |
| 检查索引存在 | `curl -I "http://localhost:9200/myindex"` | 【常用】索引名(示例: myindex); HEAD 请求,返回 200/404 |
| 打开索引 | `curl -X POST "http://localhost:9200/myindex/_open"` | 【常用】索引名(示例: myindex); 重新打开已关闭的索引 |
| 关闭索引 | `curl -X POST "http://localhost:9200/myindex/_close"` | 【常用】索引名(示例: myindex); 关闭后无法写入和查询 |

---

## Mapping 操作

### 创建 Mapping

**基础用法**:
```bash
curl -X PUT "http://localhost:9200/%{索引名}%/_mapping" -H "Content-Type: application/json" -d '%{映射定义}%'
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 Mapping | `curl -X PUT "http://localhost:9200/myindex/_mapping" -H "Content-Type: application/json" -d '{"properties":{"name":{"type":"text"},"age":{"type":"integer"},"created_at":{"type":"date"}}}'` | 【常用】properties 定义字段; name 文本字段(示例: text); age 整数(示例: integer); created_at 日期(示例: date) |
| 查看 Mapping | `curl -X GET "http://localhost:9200/myindex/_mapping"` | 【常用】索引名(示例: myindex); 显示完整字段映射 |
| 查看字段 Mapping | `curl -X GET "http://localhost:9200/myindex/_mapping/field/name"` | 【常用】索引名(示例: myindex); 字段名(示例: name); 查看特定字段类型 |
| 添加字段 Mapping | `curl -X PUT "http://localhost:9200/myindex/_mapping" -H "Content-Type: application/json" -d '{"properties":{"email":{"type":"keyword"}}}'` | 【常用】索引名(示例: myindex); email 字段(示例: keyword 不分词); 只能添加,不能修改已有字段 |

---

## 搜索查询

### _search 查询

**基础用法**:
```bash
curl -X POST "http://localhost:9200/%{索引名}%/_search" -H "Content-Type: application/json" -d '%{查询JSON}%'
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查询所有文档 | `curl -X GET "http://localhost:9200/myindex/_search?q=*"` | 【常用】索引名(示例: myindex); q=* 匹配所有 |
| Match 查询 | `curl -X POST "http://localhost:9200/myindex/_search" -H "Content-Type: application/json" -d '{"query":{"match":{"name":"张三"}}}'` | 【常用】索引名(示例: myindex); name 字段(示例: 张三); 分词匹配 |
| Term 查询 | `curl -X POST "http://localhost:9200/myindex/_search" -H "Content-Type: application/json" -d '{"query":{"term":{"status":"active"}}}'` | 【常用】索引名(示例: myindex); status 字段(示例: active); 精确匹配,不分词 |
| Bool 多条件 | `curl -X POST "http://localhost:9200/myindex/_search" -H "Content-Type: application/json" -d '{"query":{"bool":{"must":[{"match":{"name":"张三"}}],"filter":[{"range":{"age":{"gte":18}}}]}}}'` | 【常用】索引名(示例: myindex); must 必须匹配; filter 过滤不评分; gte 大于等于(示例: 18) |
| 分页查询 | `curl -X POST "http://localhost:9200/myindex/_search" -H "Content-Type: application/json" -d '{"from":0,"size":10,"query":{"match_all":{}}}'` | 【常用】索引名(示例: myindex); from 起始位置(示例: 0); size 每页数量(示例: 10) |
| 排序查询 | `curl -X POST "http://localhost:9200/myindex/_search" -H "Content-Type: application/json" -d '{"sort":[{"created_at":{"order":"desc"}}],"query":{"match_all":{}}}'` | 【常用】索引名(示例: myindex); created_at 排序字段(示例: desc 降序, asc 升序) |
| 高亮显示 | `curl -X POST "http://localhost:9200/myindex/_search" -H "Content-Type: application/json" -d '{"highlight":{"fields":{"content":{}}},"query":{"match":{"content":"关键词"}}}'` | 【常用】索引名(示例: myindex); content 高亮字段(示例: 关键词); 搜索词匹配处加高亮标签 |
| 聚合查询 | `curl -X POST "http://localhost:9200/myindex/_search" -H "Content-Type: application/json" -d '{"aggs":{"status_counts":{"terms":{"field":"status"}}}}'` | 【常用】索引名(示例: myindex); status_counts 聚合名(示例: status 字段); 统计各值的文档数 |

---

## 统计操作

### _count 和 _query

**基础用法**:
```bash
curl -X POST "http://localhost:9200/%{索引名}%/_count" -H "Content-Type: application/json" -d '%{查询JSON}%'
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 统计文档数量 | `curl -X GET "http://localhost:9200/myindex/_count"` | 【常用】索引名(示例: myindex); 返回文档总数 |
| 条件统计数量 | `curl -X POST "http://localhost:9200/myindex/_count" -H "Content-Type: application/json" -d '{"query":{"match":{"status":"active"}}}'` | 【常用】索引名(示例: myindex); status 字段(示例: active); 统计满足条件的文档数 |
| _query 接口 | `curl -X POST "http://localhost:9200/myindex/_query" -H "Content-Type: application/json" -d '{"query":{"match_all":{}}}'` | 【常用】索引名(示例: myindex); 等价于 _search 但不返回 hits |
| Validate 查询 | `curl -X POST "http://localhost:9200/myindex/_validate/query" -H "Content-Type: application/json" -d '{"query":{"match":{"name":"张三"}}}'` | 【常用】索引名(示例: myindex); name 字段(示例: 张三); 验证查询语法是否正确,不执行 |

---

## 集群操作

### _cluster 健康与节点

**基础用法**:
```bash
curl -X GET "http://localhost:9200/_cluster/health"
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 集群健康状态 | `curl -X GET "http://localhost:9200/_cluster/health"` | 【常用】返回 cluster_name, status(green/yellow/red), number_of_nodes 等 |
| 集群健康(格式化) | `curl -X GET "http://localhost:9200/_cluster/health?pretty"` | 【常用】pretty 格式化 JSON 输出,更易读 |
| 指定索引健康 | `curl -X GET "http://localhost:9200/_cluster/health/myindex?pretty"` | 【常用】索引名(示例: myindex); 查看特定索引的健康状态 |
| 等待集群健康 | `curl -X GET "http://localhost:9200/_cluster/health?wait_for_status=green&timeout=30s"` | 【常用】状态(示例: green); timeout 超时时间(示例: 30s); 等待集群变为指定状态 |
| 集群状态 | `curl -X GET "http://localhost:9200/_cluster/state"` | 【常用】返回完整集群状态,包括分片分配、路由等 |
| 集群统计 | `curl -X GET "http://localhost:9200/_cluster/stats?pretty"` | 【常用】pretty 格式化; 返回集群级别的统计信息 |
| 节点列表 | `curl -X GET "http://localhost:9200/_cat/nodes?v"` | 【常用】?v 显示表头; 查看所有节点及负载情况 |
| 节点统计 | `curl -X GET "http://localhost:9200/_nodes/stats"` | 【常用】返回所有节点的详细统计信息 |
| 单个节点统计 | `curl -X GET "http://localhost:9200/_nodes/node1/stats"` | 【常用】节点ID(示例: node1); 查看特定节点统计信息 |
| 分片分配 | `curl -X GET "http://localhost:9200/_cat/shards?v"` | 【常用】?v 显示表头; 查看所有分片的分配状态 |

---

## 文档操作

### _doc 文档 CRUD

**基础用法**:
```bash
curl -X POST "http://localhost:9200/%{索引名}%/_doc/%{文档ID}%" -H "Content-Type: application/json" -d '%{文档内容}%'
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 索引文档(自动ID) | `curl -X POST "http://localhost:9200/myindex/_doc" -H "Content-Type: application/json" -d '{"name":"张三","age":30}'` | 【常用】索引名(示例: myindex); _doc 类型; 自动生成文档ID |
| 索引文档(指定ID) | `curl -X PUT "http://localhost:9200/myindex/_doc/1" -H "Content-Type: application/json" -d '{"name":"张三","age":30}'` | 【常用】索引名(示例: myindex); 文档ID(示例: 1); PUT 幂等 |
| 获取文档 | `curl -X GET "http://localhost:9200/myindex/_doc/1?pretty"` | 【常用】索引名(示例: myindex); 文档ID(示例: 1); pretty 格式化 |
| 检查文档存在 | `curl -I "http://localhost:9200/myindex/_doc/1"` | 【常用】索引名(示例: myindex); 文档ID(示例: 1); HEAD 请求 |
| 更新文档 | `curl -X POST "http://localhost:9200/myindex/_update/1" -H "Content-Type: application/json" -d '{"doc":{"name":"李四","age":25}}'` | 【常用】索引名(示例: myindex); 文档ID(示例: 1); doc 包装要更新的字段 |
| 脚本更新 | `curl -X POST "http://localhost:9200/myindex/_update/1" -H "Content-Type: application/json" -d '{"script":{"source":"ctx._source.age += params.inc","lang":"painless","params":{"inc":1}}}'` | 【常用】索引名(示例: myindex); 文档ID(示例: 1); painless 脚本; ctx._source.age 操作字段; params.inc 参数 |
| 删除文档 | `curl -X DELETE "http://localhost:9200/myindex/_doc/1"` | 【常用】索引名(示例: myindex); 文档ID(示例: 1); 删除指定文档 |
| 批量 Bulk 索引 | `curl -X POST "http://localhost:9200/_bulk" -H "Content-Type: application/json" --data-binary '{"index":{"_index":"myindex","_id":"1"}}\n{"name":"张三"}\n'` | 【常用】_bulk 批量操作; index 操作类型; _index 索引名; _id 文档ID; 换行分隔文档 |
| mget 批量读取 | `curl -X POST "http://localhost:9200/_mget" -H "Content-Type: application/json" -d '{"docs":[{"_index":"myindex","_id":"1"},{"_index":"myindex","_id":"2"}]}'` | 【常用】_mget 批量获取; _index 索引名; _id 文档ID; 一次获取多个文档 |