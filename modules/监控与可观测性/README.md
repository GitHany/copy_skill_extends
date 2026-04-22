# 监控与可观测性命令文档

全面的监控、日志、指标、追踪和告警命令参考文档。

## 目录

- [日志 (Logging)](#日志-logging)
- [指标 (Metrics)](#指标-metrics)
- [追踪 (Tracing)](#追踪-tracing)
- [告警 (Alerting)](#告警-alerting)
- [基础设施监控](#基础设施监控)
- [命令速查表](#命令速查表)

---

## 日志 (Logging)

### ELK Stack (Elasticsearch, Logstash, Kibana)

#### Elasticsearch 搜索与索引

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 搜索日志 | `curl -X GET "http://localhost:9200/logs-*/_search?q=error"` | 【常用】logs-* 多索引; q= 快速查询 |
| 条件搜索日志 | `curl -X POST "http://localhost:9200/logs-*/_search" -H "Content-Type: application/json" -d '{"query":{"match":{"message":"ERROR"}}}'` | 【常用】message 字段搜索 ERROR |
| 时间范围搜索 | `curl -X POST "http://localhost:9200/logs-*/_search" -H "Content-Type: application/json" -d '{"query":{"range":{"@timestamp":{"gte":"now-1h","lte":"now"}}},\"sort\":[{\"@timestamp\":\"desc\"}]}'` | 【常用】最近1小时日志; @timestamp 时间字段 |
| 聚合错误统计 | `curl -X POST "http://localhost:9200/logs-*/_search" -H "Content-Type: application/json" -d '{"aggs":{"error_count":{"filter":{"match":{"message":"error"}},\"aggs\":{\"by_level\":{\"terms\":{\"field\":\"level.keyword\"}}}}}'` | 【常用】按级别聚合错误 |
| 查看索引健康 | `curl -X GET "http://localhost:9200/_cluster/health?pretty"` | 【常用】集群状态; green/yellow/red |
| 查看所有索引 | `curl -X GET "http://localhost:9200/_cat/indices?v"` | 【常用】_cat 接口查看索引列表 |
| 查看节点状态 | `curl -X GET "http://localhost:9200/_cat/nodes?v"` | 【常用】查看节点 CPU/负载/Heap |

---

#### Logstash 管道管理

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 测试 Logstash 配置 | `logstash -t -f /etc/logstash/conf.d/pipeline.conf` | 【常用】-t 测试语法; -f 指定配置文件 |
| 启动 Logstash 管道 | `logstash -f /etc/logstash/conf.d/pipeline.conf --path.data /var/lib/logstash/pipeline1` | 【常用】--path.data 多管道数据目录 |
| 后台运行 Logstash | `nohup /usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/pipeline.conf &` | 【常用】后台运行并记录 PID |
| 查看 Logstash 状态 | `curl -X GET "localhost:9600/_node/stats"` | 【常用】9600 默认 API 端口; 查看管道状态和事件统计 |
| 查看 Logstash 节点信息 | `curl -X GET "localhost:9600/_node?pretty"` | 【常用】查看版本、插件、运行时信息 |
| Logstash 停止管道 | `pkill -f logstash` | 【常用】强制停止 Logstash 进程 |
| 监控 Logstash 日志 | `tail -f /var/log/logstash/logstash-plain.log` | 【常用】实时查看 Logstash 运行日志 |

---

#### Kibana Dev Tools

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| Kibana 健康检查 | `curl -X GET "http://localhost:5601/api/status"` | 【常用】查看 Kibana 运行状态 |
| 列出所有可视化 | `curl -X GET "http://localhost:5601/api/saved_objects/visualization" -H "kbn-xsrf: reporting"` | 【常用】列出保存的可视化对象 |
| 导出仪表板 | `curl -X POST "http://localhost:5601/api/saved_objects/_export?type=dashboard" -H "kbn-xsrf: reporting" -d '{"objects":[{"type":"dashboard","id":"dashboard-id"}]}' > dashboard.ndjson` | 【常用】导出仪表板为 ndjson |
| 导入仪表板 | `curl -X POST "http://localhost:5601/api/saved_objects/_import" -H "kbn-xsrf: reporting" --form file=@dashboard.ndjson` | 【常用】从 ndjson 文件导入 |
| 查看 Spaces | `curl -X GET "http://localhost:5601/api/spaces/space" -H "kbn-xsrf: reporting"` | 【常用】列出所有 Kibana Spaces |
| 创建 Space | `curl -X POST "http://localhost:5601/api/spaces/space" -H "kbn-xsrf: reporting" -H "Content-Type: application/json" -d '{"id":"prod","name":"生产环境"}'` | 【常用】id 唯一标识; name 显示名 |

---

### Loki (Grafana logging)

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| LogCLI 安装 | `go install github.com/grafana/loki/cmd/logcli@latest` | 【常用】安装 LogCLI 客户端 |
| 查询日志 | `logcli query '{app=\"nginx\"}'` | 【常用】LogQL 查询; {app=\"nginx\"} 标签过滤 |
| 查询最近日志 | `logcli query '{job=\"app\"} | json | level=\"error\"'` | 【常用】LogQL 管道过滤 JSON 字段 |
| 查询时间范围 | `logcli query '{app=\"myapp\"}' --from=2024-01-01T00:00:00Z --to=2024-01-02T00:00:00Z` | 【常用】指定时间范围 UTC |
| 实时尾部日志 | `logcli query '{app=\"myapp\"}' --tail --limit=100` | 【常用】--tail 实时; --limit 行数限制 |
| 统计日志数量 | `logcli query 'count_over_time({app=\"myapp\"}[5m])'` | 【常用】count_over_time 统计; [5m] 时间窗口 |
| 输出原始格式 | `logcli query '{app=\"myapp\"} | json' --output=raw` | 【常用】--output=raw 原始 JSON 行 |
| Loki 健康检查 | `curl -X GET "http://localhost:3100/ready"` | 【常用】3100 默认端口; ready 就绪 |
| Loki 指标端点 | `curl -X GET "http://localhost:3100/metrics"` | 【常用】Prometheus 格式运行指标 |

---

### Fluentd 命令

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 测试 Fluentd 配置 | `td-agent -c /etc/td-agent/td-agent.conf --dry-run` | 【常用】-c 配置路径; --dry-run 验证不运行 |
| 启动 Fluentd | `td-agent -c /etc/td-agent/td-agent.conf` | 【常用】td-agent 服务名; -c 指定配置 |
| 前台运行 Fluentd | `fluentd -c /etc/fluent/fluent.conf -v` | 【常用】-v verbose 详细日志 |
| Fluentd 信号重载 | `kill -HUP %{PID}%` | 【常用】SIGHUP 重载配置不中断日志 |
| 查看 Fluentd 状态 | `curl -X GET "http://localhost:24220/api/plugins"` | 【常用】24220 监控端口; 查看插件列表 |
| Fluentd 进程管理 | `systemctl status td-agent` | 【常用】systemd 管理 td-agent 服务 |
| Fluentd 日志查看 | `tail -f /var/log/td-agent/td-agent.log` | 【常用】查看 Fluentd 运行日志 |
| 停止 Fluentd | `systemctl stop td-agent` | 【常用】停止 td-agent 服务 |

---

### journalctl / rsyslog

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 实时查看日志 | `journalctl -f` | 【常用】-f follow 实时; 等价 tail -f |
| 查看最近日志 | `journalctl -n 100` | 【常用】-n 行数; 最近100行 |
| 指定服务日志 | `journalctl -u nginx.service` | 【常用】-u 指定单元; nginx.service 服务名 |
| 按优先级过滤 | `journalctl -p err` | 【常用】-p 优先级; emerg/alert/crit/err/warning/notice/info/debug |
| 时间范围查询 | `journalctl --since="2024-01-01 00:00:00" --until="2024-01-02 00:00:00"` | 【常用】--since/--until 时间范围 |
| 查看引导日志 | `journalctl -b` | 【常用】-b 当前引导; -b -1 上次引导 |
| 内核日志 | `journalctl -k` | 【常用】-k kernel 内核消息; dmesg 类似 |
| journal 磁盘使用 | `journalctl --disk-usage` | 【常用】查看日志占用的磁盘空间 |
| 压缩旧日志 | `journalctl --vacuum-time=7d` | 【常用】删除7天前的日志; --vacuum-size 限制大小 |
| rsyslog 配置文件 | `ls -la /etc/rsyslog.d/` | 【常用】查看 rsyslog 配置目录 |
| 重载 rsyslog | `systemctl reload rsyslog` | 【常用】重新加载配置不中断服务 |
| 测试 rsyslog 远程 | `logger -n %{主机}% -P %{端口}% "Test message"` | 【常用】-n 主机; -P 端口; 发送测试日志到远程 |
| 查看 rsyslog 状态 | `systemctl status rsyslog` | 【常用】查看 rsyslog 服务运行状态 |

---

## 指标 (Metrics)

### Prometheus (promtool)

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查询指标 | `curl -X POST "http://localhost:9090/api/v1/query?query=up"` | 【常用】PromQL 查询; up 目标在线状态 |
| 范围查询 | `curl -X POST "http://localhost:9090/api/v1/query_range?query=up&start=2024-01-01T00:00:00Z&end=2024-01-02T00:00:00Z&step=60s"` | 【常用】范围向量; step 步长 |
| 指标标签查询 | `curl -X POST "http://localhost:9090/api/v1/series?match[]={job=\"node\"}` | 【常用】match[] 匹配; 返回系列标签 |
| Prometheus 目标 | `curl -X GET "http://localhost:9090/api/v1/targets"` | 【常用】查看抓取目标状态 |
| Prometheus 规则验证 | `promtool check config /etc/prometheus/prometheus.yml` | 【常用】check config 验证配置文件; 规则文件同样适用 |
| 验证告警规则 | `promtool check rules /etc/prometheus/alerts.yml` | 【常用】check rules 验证告警规则语法 |
| 测试告警规则 | `promtool test rules /etc/prometheus/alerts.test.yml` | 【常用】test rules 执行单元测试 |
| Prometheus Web UI | `curl -X GET "http://localhost:9090/graph` | 【常用】Web UI 查询界面 |
| Prometheus 指标 | `curl -X GET "http://localhost:9090/metrics"` | 【常用】/metrics 端点; Prometheus 自己暴露的运行指标 |

---

### Grafana CLI

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| Grafana 健康检查 | `curl -X GET "http://localhost:3000/api/health"` | 【常用】返回 healthy/port/version |
| 列出仪表板 | `curl -X GET "http://localhost:3000/api/search?type=dashboards" -H "Authorization: Bearer %{令牌}%"` | 【常用】Authorization Bearer Token 认证 |
| 创建仪表板 | `curl -X POST "http://localhost:3000/api/dashboards/db" -H "Authorization: Bearer %{令牌}%" -H "Content-Type: application/json" -d '{"dashboard":{"title":"My Dashboard","tags":["prod"],"timezone":"browser"},"overwrite":true}'` | 【常用】overwrite 覆盖同名仪表板 |
| 发送告警通知 | `curl -X POST "http://localhost:3000/api/alerting/notifications" -H "Authorization: Bearer %{令牌}%" -H "Content-Type: application/json" -d '{"name":"webhook","type":"webhook","settings":{"url":"http://example.com/webhook"}}'` | 【常用】创建告警通知渠道 |
| 查看数据源 | `curl -X GET "http://localhost:3000/api/datasources" -H "Authorization: Bearer %{令牌}%"` | 【常用】列出所有配置的数据源 |
| 查询数据源 | `curl -X POST "http://localhost:3000/api/ds/query" -H "Authorization: Bearer %{令牌}%" -H "Content-Type: application/json" -d '{"queries":[{"refId":"A","expr":"up","datasourceId":1}],"from":"now-1h","to":"now"}'` | 【常用】直接查询已配置的数据源 |
| Grafana 配置 | `cat /etc/grafana/grafana.ini | grep -E "^\\[|admin_user|protocol"` | 【常用】查看 grafana.ini 配置; [sections] admin_user 用户; protocol 协议 |

---

### node_exporter

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动 node_exporter | `./node_exporter --web.listen-address=":9100"` | 【常用】9100 默认端口; --web.listen-address 监听地址 |
| 收集特定指标 | `./node_exporter --collector.cpu --collector.meminfo --collector.diskstats` | 【常用】--collector 选择收集器; 默认全部启用 |
| 排除特定指标 | `./node_exporter --collector.disable-defaults --collector.cpu.info --collector.meminfo` | 【常用】--collector.disable-defaults 禁用默认; 只启用指定 |
| 文本格式指标 | `curl -s http://localhost:9100/metrics | head -50` | 【常用】/metrics 端点查看暴露的指标 |
| 查看 CPU 指标 | `curl -s http://localhost:9100/metrics | grep node_cpu` | 【常用】grep 过滤; node_cpu CPU 相关指标 |
| 查看内存指标 | `curl -s http://localhost:9100/metrics | grep node_memory` | 【常用】node_memory MemAvailable/MemTotal 等 |
| 查看磁盘指标 | `curl -s http://localhost:9100/metrics | grep node_disk` | 【常用】node_disk_read_bytes/io_time 等 |
| 查看网络指标 | `curl -s http://localhost:9100/metrics | grep node_network` | 【常用】node_network_receive_bytes/transmit_bytes 等 |
| node_exporter 帮助 | `./node_exporter --help` | 【常用】查看所有可用选项和收集器 |

---

### cAdvisor

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动 cAdvisor | `docker run --rm -p 8080:8080 --volume=/:/rootfs:ro --volume=/var/run:/var/run:ro --volume=/sys:/sys:ro google/cadvisor:latest` | 【常用】8080 默认端口; --volume 挂载 cgroup 和 sys |
| 查看容器列表 | `curl -s "http://localhost:8080/api/v2.0/containers/" | jq` | 【常用】JSON API; jq 格式化输出 |
| 查看特定容器 | `curl -s "http://localhost:8080/api/v2.0/containers/%{容器ID}%" | jq` | 【常用】容器ID 可以是完整ID或短ID |
| 查看容器统计 | `curl -s "http://localhost:8080/api/v2.0/containers/%{容器ID}%/stats?maxStats=5" | jq` | 【常用】maxStats 最大统计点数 |
| 查看机器信息 | `curl -s "http://localhost:8080/api/v2.0/machine" | jq` | 【常用】返回机器规格: NUMACPU、内存等 |
| cAdvisor 指标 | `curl -s http://localhost:8080/metrics | head -30` | 【常用】Prometheus 格式指标端点 |

---

## 追踪 (Tracing)

### Jaeger

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| Jaeger All-in-One | `jaeger-all-in-one --collector.zipkin.http-port=9411` | 【常用】All-in-One 包含 collector/query/ui; zipkin 兼容端口 9411 |
| 查询 Trace | `curl -s "http://localhost:16686/api/traces?service=%{服务名}%&limit=10"` | 【常用】16686 默认 Query UI 端口; service 服务名; limit 结果数 |
| Jaeger 健康检查 | `curl -X GET "http://localhost:14268/health"` | 【常用】14268 collector 健康端点 |
| 查看 Jaeger 服务 | `curl -s "http://localhost:16686/api/services" | jq` | 【常用】列出所有已注册的服务 |
| Jaeger 采样配置 | `curl -s "http://localhost:14268/api/sampling" -H "Content-Type: application/json" -d '{"serviceName":"%{服务名}%"}'` | 【常用】查看当前服务的采样策略 |
| Jaeger span 查询 | `curl -s "http://localhost:16686/api/traces/%{traceID}%" | jq` | 【常用】traceID 追踪ID; 返回完整链路树 |
| Jaeger 依赖图 | `curl -s "http://localhost:16686/api/dependencies?endTs=%{时间戳}%" | jq` | 【常用】endTs 时间戳; 返回服务依赖拓扑 |

---

## 告警 (Alerting)

### Alertmanager

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| Alertmanager 静默 | `curl -X POST "http://localhost:9093/api/v1/silences" -H "Content-Type: application/json" -d '{"matchers":[{"name":"alertname","value":"HighMemory"}],"startsAt":"2024-01-01T00:00:00Z","endsAt":"2024-01-02T00:00:00Z","creator":"admin@example.com","comment":"Maintenance window"}'` | 【常用】matchers 标签匹配; startsAt/endsAt 生效时间 |
| 列出静默 | `curl -s "http://localhost:9093/api/v1/silences" | jq` | 【常用】返回所有当前静默规则 |
| 删除静默 | `curl -X DELETE "http://localhost:9093/api/v1/silence/%{静默ID}%"` | 【常用】静默ID 从列表获取 |
| Alertmanager 状态 | `curl -s "http://localhost:9093/api/v1/status" | jq` | 【常用】返回配置状态、集群信息和告警统计 |
| 发送测试告警 | `curl -X POST "http://localhost:9093/api/v1/alerts" -H "Content-Type: application/json" -d '[{"labels":{"alertname":"TestAlert","severity":"critical"},"annotations":{"summary":"Test alert"}}]'` | 【常用】发送模拟告警到 Alertmanager |
| Alertmanager 集群 | `amtool cluster-status --cluster.address=http://%{主机}%:9094` | 【常用】amtool 集群管理; 查看 HA 状态 |
| Alertmanager 检查配置 | `amtool check-config /etc/alertmanager/alertmanager.yml` | 【常用】amtool 验证配置文件 |

---

## 基础设施监控

### htop / top / vmstat

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 交互式进程监控 | `htop` | 【常用】htop 提供颜色界面、鼠标支持、树形视图 |
| 按内存排序 | `htop -s M` | 【常用】-s 按列排序; M 内存; C CPU; T TIME |
| 监控指定用户 | `htop -u %{用户名}%` | 【常用】-u 只显示该用户进程 |
| 监控指定进程 | `htop -p %{PID}%` | 【常用】-p 监控特定进程 ID; 多个逗号分隔 |
| 进程树视图 | `htop -t` | 【常用】-t 树形显示父子关系 |
| top 批量模式 | `top -b -n 1 | head -20` | 【常用】-b batch 模式; -n 次数; 适合脚本 |
| top 持续采样 | `top -b -d 1 -n 10 > top.log` | 【常用】每秒采样10次输出到文件 |
| top 按内存排序 | `top -o %MEM -b | head -20` | 【常用】-o 排序字段; %MEM 内存百分比 |
| vmstat 监控 | `vmstat 1 5` | 【常用】每1秒输出，共5次; 显示 r/b/si/so/bi/bo 等 |
| vmstat 详细 | `vmstat -a 1 5` | 【常用】-a 显示活跃/非活跃内存; inact/active |
| vmstat 扩展 | `vmstat -x 1 5` | 【常用】-x 显示更多内核统计; nodename 等 |

---

### iostat / sar

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| iostat 报告 | `iostat -x 1 5` | 【常用】-x 扩展统计; 每1秒输出5次 |
| iostat CPU | `iostat -c 2 3` | 【常用】-c 只显示 CPU; 每2秒3次 |
| iostat 指定设备 | `iostat -p sda 1 3` | 【常用】-p 指定设备; sda 磁盘设备名 |
| iostat 人类可读 | `iostat -h -p ALL 1 2` | 【常用】-h 人类可读; -p ALL 所有分区和设备 |
| sar 历史统计 | `sar -q 1 3` | 【常用】-q 队列长度和负载; 每1秒3次 |
| sar CPU | `sar -P ALL 1 2` | 【常用】-P ALL 每个 CPU; 查看 CPU 使用率 |
| sar 网络 | `sar -n DEV 1 2` | 【常用】-n DEV 网络设备; 查看 eth0 等流量 |
| sar 磁盘 | `sar -b 1 2` | 【常用】-b 块设备 I/O; tps_rtps/wtps 等 |
| sar 内存 | `sar -r 1 2` | 【常用】-r 内存使用; kbmemfree/kbmemused 等 |
| sar 历史数据 | `sar -f /var/log/sa/sa10 -s 00:00:00 -e 12:00:00` | 【常用】-f 读取历史文件; -s/-e 时间范围 |

---

### Netdata

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动 Netdata | `netdata -D` | 【常用】-D daemon 后台运行; 19999 默认端口 |
| Netdata 健康检查 | `curl -s "http://localhost:19999/api/v1/info" | jq` | 【常用】返回 Netdata 版本、已启用的模块等信息 |
| 收集所有指标 | `curl -s "http://localhost:19999/api/v1/allmetrics?format=json" | jq` | 【常用】allmetrics 返回所有指标; format 输出格式 |
| 查看告警状态 | `curl -s "http://localhost:19999/api/v1/alarms" | jq` | 【常用】列出所有告警规则和当前状态 |
| 手动清理缓存 | `curl -X DELETE "http://localhost:19999/api/v1/data"` | 【常用】清理 Netdata 历史数据缓存 |
| Netdata 图表数据 | `curl -s "http://localhost:19999/api/v1/data?chart=system.cpu&after=-10&before=0&points=10" | jq` | 【常用】chart 图表名; after/before 时间; points 数据点 |
| Netdata 注册表 | `curl -s "http://localhost:19999/api/v1/registry" | jq` | 【常用】查看 Netdata Cloud 注册信息 |

---

### Datadog Agent

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看 Agent 状态 | `datadog-agent status` | 【常用】返回各组件(Collector/Forwarder/APM)状态 |
| 启动 Agent | `datadog-agent start` | 【常用】启动 Datadog Agent 服务 |
| 停止 Agent | `datadog-agent stop` | 【常用】停止 Agent 服务 |
| 重载配置 | `datadog-agent config reload` | 【常用】重新加载配置无需重启 Agent |
| 发送指标 | `curl -X POST "https://api.datadoghq.com/api/v1/series" -H "Content-Type: application/json" -H "DD-API-KEY: %{API_KEY}%" -d '{"series":[{"metric":"system.load.1","points":[[%{时间戳}%, 1.5]],"type":"gauge","tags":["env:prod"]}]}'` | 【常用】直接通过 HTTP API 发送指标; API_KEY 密钥 |
| 查看 Agent 日志 | `tail -f /var/log/datadog/agent.log` | 【常用】查看 Agent 运行日志 |
| Agent 健康检查 | `datadog-agent health` | 【常用】返回 Agent 各组件健康状态 |

---

## 实用场景示例

### 场景 1: 排查服务异常 - 日志追踪

```bash
# 1. 通过 Loki 快速查找错误
logcli query '{app="myapp"} | json | level="error"' --limit=50

# 2. 通过 Jaeger 追踪慢请求
curl -s "http://localhost:16686/api/traces?service=myapp&limit=5"

# 3. 通过 Elasticsearch 搜索历史日志
curl -X POST "http://localhost:9200/logs-*/_search" -H "Content-Type: application/json" \
  -d '{"query":{"range":{"@timestamp":{"gte":"now-1h"}}},\"sort\":[{\"@timestamp\":\"desc\"}]}'
```

### 场景 2: 性能问题排查 - 系统资源

```bash
# CPU 和进程分析
htop
top -o %CPU -b -n 1 | head -15

# 内存分析
vmstat -a 1 3
free -h

# I/O 分析
iostat -x 1 5

# 历史性能数据
sar -q 1 3
sar -n DEV 1 2
```

### 场景 3: 告警链路配置

```bash
# 1. 在 Prometheus 中配置告警规则
promtool check rules /etc/prometheus/alerts.yml

# 2. Alertmanager 静默维护期间
curl -X POST "http://localhost:9093/api/v1/silences" -H "Content-Type: application/json" \
  -d '{"matchers":[{"name":"service","value":"api"}],"startsAt":"2024-01-01T00:00:00Z","endsAt":"2024-01-02T00:00:00Z","creator":"admin@example.com"}'

# 3. 查看当前告警状态
curl -s "http://localhost:9093/api/v1/alerts" | jq '.[] | select(.status=="firing")'
```

---

## 命令速查表

| 分类 | 常用命令 |
|------|----------|
| 日志收集 | `journalctl`, `rsyslog`, `fluentd`, `logcli` |
| ELK Stack | `curl ES_API`, `logstash -t`, `logcli query`, `curl Kibana/api/status` |
| 指标采集 | `node_exporter`, `cadvisor`, `promtool`, `curl /metrics` |
| 可视化 | `grafana-cli admin stats`, `curl Grafana API` |
| 追踪 | `jaeger-all-in-one`, `curl Jaeger API` |
| 告警 | `amtool silence`, `curl Alertmanager/api/v1/alerts` |
| 进程/系统 | `htop`, `vmstat`, `iostat`, `sar -q/-P/-n` |
| 云监控 | `datadog-agent status/start/stop` |
| Netdata | `netdata -D`, `curl api/v1/allmetrics` |