# 微服务架构命令模块

微服务架构是一种将单一应用程序划分为一组小服务的设计方法，每个服务运行在独立进程中，通过轻量级通信机制协作。本模块涵盖服务发现、API网关、服务网格、分布式追踪、断路器、负载均衡等核心技术栈的命令行参考。

## 目录

- [服务发现 Service Discovery](#服务发现-service-discovery)
- [API 网关 API Gateway](#api-网关-api-gateway)
- [服务网格 Service Mesh](#服务网格-service-mesh)
- [分布式追踪 Distributed Tracing](#分布式追踪-distributed-tracing)
- [断路器 Circuit Breaker](#断路器-circuit-breaker)
- [负载均衡 Load Balancing](#负载均衡-load-balancing)
- [配置文件参考](#配置文件参考)

---

## 服务发现 Service Discovery

### Consul - 服务发现与配置管理

Consul 是 HashiCorp 开源的分布式服务发现与配置管理工具，支持服务注册、健康检查、Key-Value 存储、多数据中心。

#### consul agent - 启动 Consul Agent

**基础用法**:
```bash
consul agent -dev -ui -client=0.0.0.0
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 开发模式 | `consul agent -dev -ui` | 快速启动开发环境，包含 Web UI 【常用】 |
| 生产集群 | `consul agent -server -data-dir=/var/consul -bootstrap-expect=3` | 以服务器模式启动，data-dir 示例：`/var/consul`；期望节点数示例：`3` |
| 指定客户端地址 | `consul agent -dev -client=0.0.0.0` | 监听所有网络接口，客户端地址示例：`0.0.0.0` 【常用】 |
| 加入集群 | `consul join %{节点IP}%` | 节点IP示例：`192.168.1.100` 【常用】 |
| 查看成员 | `consul members` | 查看当前集群成员 |
| 健康检查 | `consul catalog services` | 查看已注册服务 |

#### consul services - 服务注册与管理

**基础用法**:
```bash
consul services register -name=%{服务名}% -address=%{地址}% -port=%{端口}%
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 注册服务 | `consul services register -name=api-gateway -address=127.0.0.1 -port=8080` | 服务名示例：`api-gateway`；地址示例：`127.0.0.1`；端口示例：`8080` 【常用】 |
| 服务健康检查 | `consul services register -name=web -address=127.0.0.1 -port=80 -check=http://localhost:80/health` | 检查类型示例：`http`；检查路径示例：`/health` |
| 注销服务 | `consul services deregister -id=%{服务ID}%` | 服务ID示例：`web-service-id` |
| 查看服务 | `consul services list` | 列出所有注册服务 【常用】 |
| 健康检查配置 | `consul services register -name=payment -address=127.0.0.1 -port=9090 -check=interval=10s,timeout=5s` | 间隔示例：`10s`；超时示例：`5s` |

#### consul kv - Key-Value 存储

**基础用法**:
```bash
consul kv put %{键}% %{值}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 存储键值 | `consul kv put config/service/retry 3` | 键示例：`config/service/retry`；值示例：`3` 【常用】 |
| 读取键值 | `consul kv get %{键}%` | 键示例：`config/service/retry` |
| 删除键值 | `consul kv delete %{键}%` | 键示例：`config/service/retry` |
| 列出键前缀 | `consul kv keys config/` | 键前缀示例：`config/` 【常用】 |
| 获取所有键 | `consul kv export config/` | 导出配置路径示例：`config/` |

---

### etcd - 分布式键值存储

etcd 是 CNCF 孵化的高可用分布式键值存储，是 Kubernetes 的核心数据存储后端。

#### etcdctl - etcd 命令行客户端

**基础用法**:
```bash
etcdctl put %{键}% %{值}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 存储键值 | `etcdctl put /service/user-api '{"host":"10.0.0.1","port":8080}'` | 键示例：`/service/user-api`；值示例：`{"host":"10.0.0.1"}` 【常用】 |
| 读取键值 | `etcdctl get %{键}%` | 键示例：`/service/user-api` 【常用】 |
| 读取键前缀 | `etcdctl get --prefix=/service/` | 前缀示例：`/service/` 【常用】 |
| 删除键 | `etcdctl del %{键}%` | 键示例：`/service/user-api` |
| 集群健康检查 | `etcdctl endpoint health` | 检查所有节点健康状态 【常用】 |
| 查看集群状态 | `etcdctl endpoint status` | 查看各节点状态和版本 |
| 快照备份 | `etcdctl snapshot save /backup/snapshot.db` | 备份路径示例：`/backup/snapshot.db` 【常用】 |
| 恢复快照 | `etcdctl snapshot restore /backup/snapshot.db --data-dir=/var/lib/etcd` | 恢复路径示例：`/var/lib/etcd` |
| 监控键变化 | `etcdctl watch %{键}%` | 键示例：`/service/user-api` 【常用】 |
| 租约管理 | `etcdctl lease grant 60` | 租约时间（秒）示例：`60` |

---

### Nacos - 阿里巴巴服务发现平台

Nacos 是阿里巴巴开源的一站式服务发现、配置管理和服务管理平台。

#### 启动 Nacos

**基础用法**:
```bash
cd %{nacos目录}% && sh startup.sh -m standalone
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 单机启动 | `sh startup.sh -m standalone` | 以单机模式启动，默认端口 `8848` 【常用】 |
| 集群模式 | `sh startup.sh -m cluster` | 以集群模式启动 |
| 指定端口 | `sh startup.sh -m standalone -p %{端口}%` | 端口示例：`8849` |
| Docker 启动 | `docker run --name nacos -d -p 8848:8848 -e MODE=standalone nacos/nacos-server` | 镜像示例：`nacos/nacos-server` 【常用】 |
| 查看日志 | `tail -f %{nacos目录}%/logs/nacos.log` | 日志路径示例：`/opt/nacos/logs/nacos.log` |

#### Nacos Open API

**基础用法**:
```bash
curl -X PUT 'http://localhost:8848/nacos/v1/ns/instance'
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 注册服务 | `curl -X POST 'http://localhost:8848/nacos/v1/ns/instance?serviceName=%{服务名}%&ip=%{IP}%&port=%{端口}%'` | 服务名示例：`user-service`；IP示例：`192.168.1.10`；端口示例：`8080` 【常用】 |
| 注销服务 | `curl -X DELETE 'http://localhost:8848/nacos/v1/ns/instance?serviceName=%{服务名}%&ip=%{IP}%&port=%{端口}%'` | 同上 |
| 查询服务 | `curl 'http://localhost:8848/nacos/v1/ns/instance/list?serviceName=%{服务名}%'` | 服务名示例：`user-service` 【常用】 |
| 发布配置 | `curl -X POST 'http://localhost:8848/nacos/v1/cs/configs?dataId=%{配置ID}%&group=%{分组}%&content=%{内容}%'` | 配置ID示例：`application.yml`；分组示例：`DEFAULT_GROUP` |
| 获取配置 | `curl 'http://localhost:8848/nacos/v1/cs/configs?dataId=%{配置ID}%&group=%{分组}%'` | 同上 【常用】 |

---

## API 网关 API Gateway

### Kong - 开源 API 网关

Kong 是高性能、可扩展的 API 网关，支持插件扩展、认证、限流等功能。

#### kong start - 启动 Kong

**基础用法**:
```bash
kong start
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动服务 | `kong start` | 使用默认配置文件启动 【常用】 |
| 指定配置 | `kong start -c /etc/kong/kong.conf` | 配置文件路径示例：`/etc/kong/kong.conf` 【常用】 |
| 停止服务 | `kong stop` | 停止 Kong 服务 |
| 重载配置 | `kong reload` | 热重载配置而不中断连接 【常用】 |
| 验证配置 | `kong check /etc/kong/kong.conf` | 配置文件路径示例：`/etc/kong/kong.conf` |
| 数据库迁移 | `kong migrations bootstrap` | 初始化数据库结构 【常用】 |
| 数据库升级 | `kong migrations up` | 升级数据库版本 |
| 查看状态 | `kong health` | 检查 Kong 健康状态 【常用】 |

#### Kong Admin API - 管理 API

**基础用法**:
```bash
curl -i -X POST http://localhost:8001/services/ --data name=%{服务名}% --data url=%{上游URL}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建服务 | `curl -i -X POST http://localhost:8001/services/ --data 'name=user-service&url=http://user-api:8080'` | 服务名示例：`user-service`；上游URL示例：`http://user-api:8080` 【常用】 |
| 创建路由 | `curl -i -X POST http://localhost:8001/routes/ --data 'name=user-route&service.name=user-service&paths[]=/api/users'` | 路由名示例：`user-route`；路径示例：`/api/users` 【常用】 |
| 启用速率限制插件 | `curl -X POST http://localhost:8001/services/%{服务ID}%/plugins --data 'name=rate-limiting&config.minute=100'` | 插件名示例：`rate-limiting`；限制示例：`100` |
| 查看服务列表 | `curl http://localhost:8001/services/` | 【常用】 |
| 查看路由列表 | `curl http://localhost:8001/routes/` | 【常用】 |
| 启用 CORS 插件 | `curl -X POST http://localhost:8001/routes/%{路由ID}%/plugins --data 'name=cors&config.origins=*'` | 允许来源示例：`*` |
| 健康检查 | `curl http://localhost:8001/status` | 查看 Kong 状态统计 【常用】 |

---

### Nginx - 反向代理网关

Nginx 是高性能 HTTP 服务器和反向代理服务器，常用作 API 网关。

#### nginx 命令

**基础用法**:
```bash
nginx
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动服务 | `nginx` | 使用默认配置启动 【常用】 |
| 指定配置 | `nginx -c /etc/nginx/nginx.conf` | 配置文件路径示例：`/etc/nginx/nginx.conf` 【常用】 |
| 测试配置 | `nginx -t -c /etc/nginx/nginx.conf` | 测试配置文件语法 【常用】 |
| 重载配置 | `nginx -s reload` | 无中断重载配置 【常用】 |
| 停止服务 | `nginx -s stop` | 快速关闭 |
| 优雅停止 | `nginx -s quit` | 等待请求处理完毕后关闭 |
| 查看版本 | `nginx -v` | 查看 Nginx 版本 |
| 查看编译参数 | `nginx -V` | 查看编译时参数和模块 |
| 发送信号 | `kill -HUP %{master进程PID}%` | 优雅重载，PID示例：`1234` 【常用】 |

#### Nginx 反向代理配置

**基础用法**:
```nginx
location /api/ {
    proxy_pass http://backend-service:8080/;
}
```

**扩展示例**:

| 场景 | 配置片段 | 说明 |
|------|----------|------|
| 基础反向代理 | `location /api/ { proxy_pass http://backend:8080/; }` | 代理到后端服务 【常用】 |
| WebSocket 支持 | `location /ws/ { proxy_pass http://ws-backend:9000/; proxy_http_version 1.1; proxy_set_header Upgrade $http_upgrade; proxy_set_header Connection "upgrade"; }` | WebSocket 代理配置 【常用】 |
| 负载均衡 upstream | `upstream backend { server 10.0.0.1:8080; server 10.0.0.2:8080; } location /api/ { proxy_pass http://backend; }` | 基础负载均衡 |
| SSL 终止 | `server { listen 443 ssl; ssl_certificate /etc/nginx/ssl/server.crt; ssl_certificate_key /etc/nginx/ssl/server.key; location / { proxy_pass http://backend:8080; } }` | HTTPS 终止配置 |
| 限流配置 | `limit_req_zone $binary_remote_addr zone=api_limit:10m rate=10r/s; location /api/ { limit_req zone=api_limit burst=20; }` | 请求速率限制 【常用】 |
| 缓存配置 | `proxy_cache_path /data/nginx/cache levels=1:2 keys_zone=api_cache:10m max_size=1g; location /api/ { proxy_cache api_cache; proxy_cache_valid 200 1h; }` | 响应缓存配置 |

---

## 服务网格 Service Mesh

### Istio - 功能强大的服务网格

Istio 是 CNCF 孵化项目，提供流量管理、安全、可观测性等企业级功能。

#### istioctl install - 安装 Istio

**基础用法**:
```bash
istioctl install --set profile=demo
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 默认安装 | `istioctl install --set profile=demo` | 使用 demo 配置安装，适合开发环境 【常用】 |
| 最小安装 | `istioctl install --set profile=minimal` | 最小组件安装，减少资源占用 |
| 远程安装 | `istioctl install --set profile=remote` | 安装远程配置文件 |
| 指定命名空间 | `istioctl install -n %{命名空间}% --set values.global.istioNamespace=%{命名空间}%` | 命名空间示例：`istio-system` 【常用】 |
| 自定义安装 | `istioctl install --set profile=default --set values.cni.enabled=true` | 启用 CNI 模式 |
| 预览安装 | `istioctl install --set profile=demo --dry-run` | 预览安装配置不实际安装 |
| 查看配置清单 | `istioctl profile dump demo` | 查看配置详情 |
| 列出可用配置 | `istioctl profile list` | 查看所有可用的安装配置 【常用】 |

#### istioctl analyze - 配置分析与诊断

**基础用法**:
```bash
istioctl analyze
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 分析当前集群 | `istioctl analyze -n %{命名空间}%` | 命名空间示例：`default` 【常用】 |
| 分析指定文件 | `istioctl analyze %{yaml文件}%` | YAML文件示例：`./virtual-service.yaml` |
| 分析所有命名空间 | `istioctl analyze --all-namespaces` | 分析集群所有命名空间 【常用】 |
| 输出 JSON 格式 | `istioctl analyze -o json` | 以 JSON 格式输出分析结果 |
| 显示详细消息 | `istioctl analyze -v` | 详细输出模式 |
| 分析特定资源 | `istioctl analyze %{资源类型}%/%{资源名}% -n %{命名空间}%` | 资源类型示例：`VirtualService`；资源名示例：`reviews` |

#### istioctl 流量管理

**基础用法**:
```bash
istioctl kube-inject -f deployment.yaml | kubectl apply -f -
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 注入 Sidecar | `istioctl kube-inject -f %{deployment文件}% \| kubectl apply -f -` | Deployment文件示例：`./deploy.yaml` 【常用】 |
| 查看 Envoy 配置 | `istioctl proxy-config cluster %{pod名}% -n %{命名空间}%` | Pod名示例：`productpage-v1-xxx`；命名空间示例：`default` 【常用】 |
| 查看路由配置 | `istioctl proxy-config route %{pod名}% -n %{命名空间}%` | 【常用】 |
| 查看端点列表 | `istioctl proxy-config endpoints %{pod名}% -n %{命名空间}%` | |
| 授权策略 | `istioctl x authz check %{pod名}% -n %{命名空间}%` | 检查授权策略 |
| 生成流量图 | `istioctl x waypoint apply --namespace %{命名空间}%` | 为命名空间生成 Waypoint Proxy |

---

### Linkerd - 轻量级服务网格

Linkerd 是 CNCF 毕业项目，以简单、安全、高性能著称。

#### linkerd install - 安装 Linkerd

**基础用法**:
```bash
linkerd install | kubectl apply -f -
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装控制面 | `linkerd install | kubectl apply -f -` | 安装 Linkerd 控制平面 【常用】 |
| 安装扩展 | `linkerd extensions install` | 安装可选扩展组件 |
| 升级安装 | `linkerd upgrade | kubectl apply -f -` | 升级现有安装 |
| 多集群安装 | `linkerd multicluster install` | 安装多集群支持 |
| 查看状态 | `linkerd check` | 检查 Linkerd 安装状态 【常用】 |
| 卸载 | `linkerd uninstall | kubectl delete -f -` | 移除 Linkerd |
| 可视化仪表板 | `linkerd dashboard` | 打开 Linkerd 仪表板 【常用】 |
| 注入 Deployment | `linkerd inject %{deployment文件}% | kubectl apply -f -` | 为 Deployment 注入 Sidecar 【常用】 |

---

## 分布式追踪 Distributed Tracing

### Jaeger - Uber 开源的分布式追踪系统

Jaeger 是 CNCF 毕业项目，提供分布式追踪和请求链路分析能力。

#### jaeger 命令行

**基础用法**:
```bash
jaeger-all-in-one --collector.zipkin.http-port=9411
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 快速启动 | `jaeger-all-in-one` | 启动 All-in-One 模式（包含 Agent、Collector、Query、UI），默认端口 `16686` 【常用】 |
| 指定存储后端 | `jaeger-all-in-one --span-storage-type=elasticsearch --es.server-urls=http://localhost:9200` | 存储类型示例：`elasticsearch`；ES地址示例：`http://localhost:9200` |
| 启用 Zipkin 兼容 | `jaeger-all-in-one --collector.zipkin.http-port=9411` | Zipkin 端口示例：`9411` 【常用】 |
| Docker 启动 | `docker run -d --name jaeger -p 6831:6831/udp -p 16686:16686 -p 14268:14268 jaegertracing/all-in-one:latest` | All-in-One 容器部署 【常用】 |
| Kubernetes 部署 | `kubectl apply -f https://jaegertracing.github.io/jaeger-operator/template.yaml` | 使用 Operator 部署 |
| 导出追踪数据 | `jaeger-agent --collector.zipkin.host-port=9411` | 对接 Zipkin 收集器 |

---

### Zipkin - Twitter 开源的分布式追踪系统

Zipkin 是分布式追踪系统，支持多种存储后端。

#### zipkin 命令行

**基础用法**:
```bash
zipkin-server
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 快速启动 | `zipkin-server` | 使用默认配置启动，默认端口 `9411` 【常用】 |
| 指定存储 | `zipkin-server --storage.elasticsearchHosts=localhost:9200` | ES 主机示例：`localhost:9200` |
| MySQL 存储 | `zipkin-server --storage.mysql=true --mysql.host=localhost --mysql.port=3306 --mysql.username=root --mysql.password=password` | 数据库连接配置 |
| Docker 启动 | `docker run -d -p 9411:9411 -p 9412:9412 openzipkin/zipkin` | Docker 容器部署 【常用】 |
| 查询追踪 API | `curl 'http://localhost:9411/api/v2/traces?serviceName=%{服务名}%&startTime=%{开始时间}%'` | 服务名示例：`order-service` |
| 查看依赖关系 | `curl 'http://localhost:9411/api/v2/dependencies?endTime=%{结束时间}%'` | 结束时间（Unix 毫秒）示例：`1640000000000` |

---

### OpenTelemetry Collector - 可观测性数据收集

OpenTelemetry 是 CNCF 孵化的可观测性标准框架，支持追踪、指标、日志的统一收集。

#### otelcol 命令行

**基础用法**:
```bash
otelcol-contrib --config=%{配置文件}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动收集器 | `otelcol-contrib --config=/etc/otelcol/config.yaml` | 配置文件路径示例：`/etc/otelcol/config.yaml` 【常用】 |
| Docker 运行 | `docker run otel/opentelemetry-collector-contrib:latest --config=/etc/otelcol-connector/config.yaml` | 容器化部署 【常用】 |
| 验证配置 | `otelcol-contrib --config=%{配置文件}% --check-config` | 验证配置文件正确性 |
| 导出追踪到 Jaeger | `otelcol-contrib --config=/etc/otelcol/jaeger-exporter.yaml` | Jaeger 导出配置 |
| 导出指标到 Prometheus | `otelcol-contrib --config=/etc/otelcol/prometheus-exporter.yaml` | Prometheus 导出配置 |
| 查看帮助 | `otelcol-contrib --help` | 查看所有可用选项 |
| gRPC 接收 | `otelcol-contrib --config=/etc/otelcol/grpc-receiver.yaml` | gRPC 接收配置示例 |

---

## 断路器 Circuit Breaker

### Resilience4j - Java 轻量级断路器库

Resilience4j 是 Java 轻量级熔断库，提供断路器、重试、限流、舱壁等模式。

#### resilience4j CLI 工具

**基础用法**:
```bash
resilience4j bulkhead execute %{命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 执行舱壁命令 | `resilience4j bulkhead execute java -jar app.jar` | 为 Java 应用执行舱壁保护 |
| 限流执行 | `resilience4j rate-limiter execute java -jar app.jar` | 限制每秒请求数 |
| 断路器状态查询 | `resilience4j circuit-breaker get-state` | 查询当前断路器状态 |
| 重试配置 | `resilience4j retry execute --max-attempts=3 java -jar app.jar` | 最大重试次数示例：`3` |
| 超时控制 | `resilience4j timelimiter execute --timeout-duration=5s java -jar app.jar` | 超时时间示例：`5s` |
| 批量熔断监控 | `resilience4j circuit-breaker list-circuits` | 列出所有配置的断路器 |
| 手动重置断路器 | `resilience4j circuit-breaker reset %{断路器名}%` | 断路器名示例：`paymentService` |

#### Spring Boot + Resilience4j 配置

**基础用法**:
在 `application.yml` 中配置断路器。

**扩展示例**:

| 场景 | 配置片段 | 说明 |
|------|----------|------|
| 断路器基础配置 | `resilience4j.circuitbreaker.configs.default.sliding-window-size=10` | 滑动窗口大小示例：`10` |
| 失败率阈值 | `resilience4j.circuitbreaker.configs.default.failure-rate-threshold=50` | 失败率阈值示例：`50%` |
| 慢调用阈值 | `resilience4j.circuitbreaker.configs.default.slow-call-duration-threshold=5s` | 慢调用阈值示例：`5s` |
| 重试配置 | `resilience4j.retry.configs.default.max-attempts=3` | 最大重试次数示例：`3` |
| 限流配置 | `resilience4j.ratelimiter.configs.default.limit-for-period=100` | 每周期限制次数示例：`100` |
| 舱壁配置 | `resilience4j.bulkhead.configs.default.max-concurrent-calls=10` | 最大并发调用数示例：`10` |

---

## 负载均衡 Load Balancing

### HAProxy - 高性能负载均衡器

HAProxy 是高性能 TCP/HTTP 负载均衡器，广泛用于高流量场景。

#### haproxy 命令

**基础用法**:
```bash
haproxy -f %{配置文件}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动 HAProxy | `haproxy -f /etc/haproxy/haproxy.cfg` | 配置文件路径示例：`/etc/haproxy/haproxy.cfg` 【常用】 |
| 前端/后端统计 | `haproxy -f /etc/haproxy/haproxy.cfg -s` | 统计页面信息刷新 |
| 停止服务 | `pkill haproxy` | 停止 HAProxy 进程 |
| 测试配置 | `haproxy -c -f /etc/haproxy/haproxy.cfg` | 检查配置文件语法 【常用】 |
| 查看版本 | `haproxy -v` | 查看 HAProxy 版本 |
| 优雅重载 | `haproxy -f /etc/haproxy/haproxy.cfg -sf %{pid}%` | 优雅重载，PID示例：`1234` 【常用】 |

#### HAProxy 配置示例

| 场景 | 配置片段 | 说明 |
|------|----------|------|
| 基础负载均衡 | `frontend http_front\\n  bind *:80\\n  default_backend web_servers\\nbackend web_servers\\n  balance roundrobin\\n  server web1 10.0.0.1:8080 check` | 轮询负载均衡 【常用】 |
| 加权最少连接 | `backend web_servers\\n  balance leastconn\\n  server web1 10.0.0.1:8080 weight 10 check\\n  server web2 10.0.0.2:8080 weight 5 check` | 加权最少连接算法 |
| 健康检查 | `server web1 10.0.0.1:8080 check inter 3s rise 2 fall 5` | 健康检查配置：间隔 `3s`；上升 `2`；下降 `5` |
| SSL 终止 | `frontend https_front\\n  bind *:443 ssl crt /etc/ssl/certs/server.pem\\n  default_backend web_servers` | HTTPS 终止 |
| 速率限制 | `frontend http_front\\n  stick-table type ip size 200k expire 30s\\n  acl too_many req.src -m reg -i too-many\\n  tcp-request connection reject if too_many` | 基于 IP 的连接限制 |
| 后端故障转移 | `backend web_servers\\n  option httpchk GET /health\\n  server web1 10.0.0.1:8080 check backup\\n  server web2 10.0.0.2:8080 check inter 3s rise 2 fall 3` | 备份服务器配置 |

---

### Traefik - 云原生反向代理与负载均衡器

Traefik 是云原生边缘路由器，支持动态服务发现和自动配置。

#### traefik 命令

**基础用法**:
```bash
traefik --configFile=%{配置文}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动 Traefik | `traefik --configFile=/etc/traefik/traefik.toml` | 配置文件路径示例：`/etc/traefik/traefik.toml` 【常用】 |
| Docker 提供商 | `traefik --api --docker` | 启用 Docker 提供商和 API |
| Kubernetes 提供商 | `traefik --kubernetes` | 启用 Kubernetes 提供商 |
| Let's Encrypt 自动 HTTPS | `traefik --acme.email=admin@example.com --acme.storage=acme.json --acme.entrypoint=https` | ACME 配置，邮箱示例：`admin@example.com` |
| 查看路由 | `traefik --api.dashboard=true` | 启用仪表板 |
| 日志级别 | `traefik --log.level=DEBUG` | 日志级别示例：`DEBUG` 【常用】 |
| Docker 标签路由 | `docker run -d -l "traefik.http.routers.web.rule=Host(\`example.com\`)" -l "traefik.http.routers.web.rule=PathPrefix(\`/api\`)" nginx` | 通过标签配置路由 |
| 查看版本 | `traefik version` | 查看 Traefik 版本 【常用】 |

#### Traefik 动态配置

| 场景 | 配置片段 | 说明 |
|------|----------|------|
| 文件提供者 | `--providers.file.filename=/etc/traefik/dynamic.yaml` | 动态配置文件路径 |
| 基础负载均衡 | `http:\\n  routers:\\n    my-router:\\n      rule: "Host(\\`example.com\\`)"\\n      service: my-service\\n  services:\\n    my-service:\\n      loadBalancer:\\n        servers:\\n          - url: "http://10.0.0.1:8080"` | 路由和服务定义 |
| 限流中间件 | `apiVersion: traefik.containo.us/v1alpha1\\nkind: Middleware\\nmetadata:\\n  name: rate-limit\\nspec:\\n  rateLimit:\\n    average: 100\\n    burst: 50` | 速率限制中间件 |
| 重试策略 | `http:\\n  services:\\n    my-service:\\n      loadBalancer:\\n        servers:\\n          - url: "http://10.0.0.1:8080"\\n        healthCheck:\\n          path: /health\\n          interval: 10s` | 健康检查配置 |

---

## 配置文件参考

### 微服务架构常见端口

| 组件 | 默认端口 | 说明 |
|------|----------|------|
| Consul UI | 8500 | Consul Web 控制台 |
| Consul Agent | 8300 | Consul 代理通信 |
| Kong Admin API | 8001 | Kong 管理接口 |
| Kong Proxy | 8000 | Kong 代理端口 |
| Nacos Server | 8848 | Nacos 控制台和 API |
| Jaeger UI | 16686 | Jaeger Web 控制台 |
| Zipkin | 9411 | Zipkin 收集器端口 |
| Linkerd Dashboard | 3000 | Linkerd 仪表板 |
| Istio Dashboard | 9080 | Istio Kiali 仪表板 |
| Traefik Dashboard | 8080 | Traefik Web UI |
| HAProxy Stats | 8404 | HAProxy 统计页面 |

### 常用环境变量

| 变量 | 说明 | 示例 |
|------|------|------|
| CONSUL_HTTP_ADDR | Consul 地址 | `http://localhost:8500` |
| ETCDCTL_API | etcd API 版本 | `3` |
| KUBECONFIG | Kubernetes 配置路径 | `~/.kube/config` |
| OTEL_EXPORTER_OTLP_ENDPOINT | OTel 收集器端点 | `http://localhost:4317` |

---

## 前置条件

- **Consul**: Go 1.18+, 下载地址: https://www.consul.io/downloads
- **etcd**: Go 1.18+, 下载地址: https://etcd.io/downloads
- **Nacos**: Java 8+, 下载地址: https://nacos.io/download
- **Kong**: Docker/Kubernetes 或 nginx 环境
- **Istio**: Kubernetes 1.19+, kubectl 已配置
- **Linkerd**: Kubernetes 1.19+, kubectl 已配置
- **Jaeger**: Go 1.18+, Docker（可选）
- **Zipkin**: Java 8+, Docker（可选）
- **OpenTelemetry Collector**: Go 1.18+, 下载地址: https://opentelemetry.io
- **HAProxy**: 2.x 或 1.9+, 安装方式: `apt install haproxy` / `yum install haproxy`
- **Traefik**: Docker 或 Kubernetes 环境
- **Resilience4j**: Java 8+, Maven/Gradle 依赖管理

## 相关模块

- [Kubernetes 命令](../Kubernetes 命令/) - K8s 环境下的微服务部署
- [Docker 命令](../Docker 命令/) - 容器化运行时
- [系统监控](../系统监控/) - 微服务监控与告警
- [网络诊断](../网络诊断/) - 服务间网络故障排查