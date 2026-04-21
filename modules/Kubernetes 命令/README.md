# Kubernetes 命令文档

Kubernetes 容器编排完整参考文档。

## 📚 目录

- [Pod 管理](#pod-管理)
- [Deployment 与扩缩容](#deployment-与扩缩容)
- [Service 与网络](#service-与网络)
- [调试与排查](#调试与排查)
- [命名空间](#命名空间)
- [上下文与配置](#上下文与配置)
- [扩展示例](#扩展示例)
- [实用场景](#实用场景)

---

## Pod 管理

### kubectl get pods - 查看 Pods

**基础用法**:
```bash
kubectl get pods
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定命名空间 | `kubectl get pods -n %{命名空间}%` | 【常用】-n 指定命名空间，示例值：default |
| 查看所有命名空间 | `kubectl get pods --all-namespaces` | 查看所有命名空间下的 Pods |
| 显示详细信息 | `kubectl get pods -o wide` | -o wide 显示更多信息（节点、IP 等） |
| 显示标签 | `kubectl get pods --show-labels` | --show-labels 显示每个 Pod 的标签 |
| Watch 模式 | `kubectl get pods -w` | -w 实时跟踪 Pod 状态变化 |
| 过滤标签 | `kubectl get pods -l %{标签键}=%{标签值}%` | -l 按标签过滤，示例值：app=nginx |

### kubectl describe pod - 查看 Pod 详情

**基础用法**:
```bash
kubectl describe pod %{Pod名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定命名空间 | `kubectl describe pod %{Pod名称}% -n %{命名空间}%` | 【常用】-n 指定命名空间，示例值：myapp-abc123, default |
| 查看所有 Pods | `kubectl describe pods` | 查看所有 Pod 的详细信息 |

### kubectl logs - 查看 Pod 日志

**基础用法**:
```bash
kubectl logs %{Pod名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 实时跟踪日志 | `kubectl logs -f %{Pod名称}%` | 【常用】-f 实时跟踪日志输出 |
| 显示最后 N 行 | `kubectl logs --tail %{行数}% %{Pod名称}%` | 【常用】--tail 显示最后 N 行，示例值：100 |
| 指定命名空间 | `kubectl logs %{Pod名称}% -n %{命名空间}%` | 【常用】-n 指定命名空间，示例值：default |
| 查看上一个容器实例 | `kubectl logs --previous %{Pod名称}%` | --previous 查看上一个容器实例的日志 |
| 指定容器 | `kubectl logs %{Pod名称}% -c %{容器名称}%` | -c 指定容器（多容器 Pod），示例值：main |
| 显示时间戳 | `kubectl logs --timestamps %{Pod名称}%` | --timestamps 显示每行日志的时间戳 |

### kubectl exec - 进入容器

**基础用法**:
```bash
kubectl exec -it %{Pod名称}% -- /bin/bash
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定命名空间 | `kubectl exec -it %{Pod名称}% -n %{命名空间}% -- /bin/bash` | 【常用】-n 指定命名空间，示例值：myapp-abc123, default |
| 执行单条命令 | `kubectl exec %{Pod名称}% -- %{命令}%` | 【常用】执行单条命令，示例值：ls -la |
| 指定容器 | `kubectl exec -it %{Pod名称}% -c %{容器名称}% -- /bin/bash` | -c 指定容器（多容器 Pod），示例值：main |
| 使用 sh | `kubectl exec -it %{Pod名称}% -- sh` | 使用 sh 代替 bash（部分容器无 bash） |

### kubectl apply - 应用配置文件

**基础用法**:
```bash
kubectl apply -f %{文件名或URL}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 通过 stdin 输入 | `kubectl apply -f -` | - 从 stdin 读取 YAML 配置 |
| 应用目录所有文件 | `kubectl apply -f %{目录路径}%/` | 应用目录下所有 YAML 文件，示例值：./k8s |
| 显示差异 | `kubectl apply -f %{文件名}% --dry-run=server` | 【常用】--dry-run=server 预览服务器端差异，示例值：./deployment.yaml |
| 记录变更 | `kubectl apply -f %{文件名}% --record` | 【常用】--record 记录本次变更，示例值：./deployment.yaml |

### kubectl delete - 删除资源

**基础用法**:
```bash
kubectl delete -f %{文件名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 删除 Pod | `kubectl delete pod %{Pod名称}%` | 【常用】删除指定 Pod，示例值：myapp-abc123 |
| 删除 Deployment | `kubectl delete deployment %{Deployment名称}%` | 删除 Deployment 及其管理的 Pods，示例值：nginx-deployment |
| 指定命名空间 | `kubectl delete -f %{文件名}% -n %{命名空间}%` | -n 指定命名空间，示例值：default |
| 强制删除 | `kubectl delete pod %{Pod名称}% --grace-period=0 --force` | 【常用】强制立即删除 Pod，示例值：myapp-abc123 |
| 删除所有资源 | `kubectl delete all --all` | 删除命名空间下所有资源 |

### kubectl port-forward - 端口转发

**基础用法**:
```bash
kubectl port-forward %{Pod名称}% %{本地端口}%:%{Pod端口}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定命名空间 | `kubectl port-forward %{Pod名称}% %{本地端口}%:%{Pod端口}% -n %{命名空间}%` | 【常用】-n 指定命名空间，示例值：myapp-abc123, 8080:80, default |
| 转发到 Service | `kubectl port-forward svc/%{Service名称}% %{本地端口}%:%{Service端口}%` | 【常用】转发 Service 端口，示例值：nginx-service, 8080:80 |
| 后台运行 | `kubectl port-forward %{Pod名称}% %{本地端口}%:%{Pod端口}% &` | & 使端口转发在后台运行 |

---

## Deployment 与扩缩容

### kubectl scale - 扩缩容 Deployment

**基础用法**:
```bash
kubectl scale deployment %{Deployment名称}% --replicas=%{副本数}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定命名空间 | `kubectl scale deployment %{Deployment名称}% --replicas=%{副本数}% -n %{命名空间}%` | 【常用】-n 指定命名空间，示例值：nginx-deployment, 3, default |
| 扩缩容多个 | `kubectl scale --replicas=%{副本数}% deployment/%{Deployment名称}%` | --replicas 指定副本数量，示例值：3 |

### kubectl rollout status - 查看滚动更新状态

**基础用法**:
```bash
kubectl rollout status deployment/%{Deployment名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定命名空间 | `kubectl rollout status deployment/%{Deployment名称}% -n %{命名空间}%` | 【常用】-n 指定命名空间，示例值：nginx-deployment, default |
| 查看历史 | `kubectl rollout history deployment/%{Deployment名称}%` | 【常用】查看版本历史，示例值：nginx-deployment |

### kubectl rollout undo - 回滚 Deployment

**基础用法**:
```bash
kubectl rollout undo deployment/%{Deployment名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 回滚到指定版本 | `kubectl rollout undo deployment/%{Deployment名称}% --to-revision=%{版本号}%` | 【常用】--to-revision 回滚到指定版本，示例值：nginx-deployment, 2 |
| 指定命名空间 | `kubectl rollout undo deployment/%{Deployment名称}% -n %{命名空间}%` | -n 指定命名空间，示例值：nginx-deployment, default |

### kubectl set image - 更新镜像

**基础用法**:
```bash
kubectl set image deployment/%{Deployment名称}% %{容器名称}%=%{镜像名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定命名空间 | `kubectl set image deployment/%{Deployment名称}% %{容器名称}%=%{镜像名称}% -n %{命名空间}%` | 【常用】更新容器镜像，示例值：nginx-deployment, nginx, nginx, default |
| 使用最新标签 | `kubectl set image deployment/%{Deployment名称}% %{容器名称}%=%{镜像名称}%:latest` | 【常用】:latest 使用最新镜像标签 |

---

## Service 与网络

### kubectl get services - 查看 Services

**基础用法**:
```bash
kubectl get services
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定命名空间 | `kubectl get services -n %{命名空间}%` | -n 指定命名空间，示例值：default |
| 显示标签 | `kubectl get services --show-labels` | --show-labels 显示每个 Service 的标签 |

### kubectl get ingress - 查看 Ingress

**基础用法**:
```bash
kubectl get ingress
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定命名空间 | `kubectl get ingress -n %{命名空间}%` | -n 指定命名空间，示例值：default |
| 显示详细信息 | `kubectl get ingress -o wide` | -o wide 显示更多信息（主机、地址等） |

### kubectl get configmaps - 查看 ConfigMaps

**基础用法**:
```bash
kubectl get configmaps
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定命名空间 | `kubectl get configmaps -n %{命名空间}%` | -n 指定命名空间，示例值：default |

### kubectl get secrets - 查看 Secrets

**基础用法**:
```bash
kubectl get secrets
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定命名空间 | `kubectl get secrets -n %{命名空间}%` | -n 指定命名空间，示例值：default |

---

## 调试与排查

### kubectl get events - 查看事件

**基础用法**:
```bash
kubectl get events
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 按时间排序 | `kubectl get events --sort-by='.lastTimestamp'` | --sort-by 按时间排序，最新的在前 |
| 指定命名空间 | `kubectl get events -n %{命名空间}%` | -n 指定命名空间，示例值：default |
| 查看所有命名空间 | `kubectl get events --all-namespaces` | --all-namespaces 查看所有命名空间的事件 |
| 限制显示数量 | `kubectl get events --limit=%{数量}%` | --limit 限制显示数量，示例值：50 |

### kubectl top pod - 查看资源使用

**基础用法**:
```bash
kubectl top pod
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定命名空间 | `kubectl top pod -n %{命名空间}%` | -n 指定命名空间，示例值：default |
| 查看所有命名空间 | `kubectl top pod --all-namespaces` | --all-namespaces 查看所有命名空间的资源使用 |
| 显示标签 | `kubectl top pod --show-labels` | --show-labels 显示标签列 |
| 指定 Pod | `kubectl top pod %{Pod名称}%` | 查看单个 Pod 的资源使用，示例值：myapp-abc123 |

### kubectl top node - 查看节点资源

**基础用法**:
```bash
kubectl top node
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定节点 | `kubectl top node %{节点名称}%` | 查看指定节点的资源使用，示例值：node-1 |
| 显示标签 | `kubectl top node --show-labels` | --show-labels 显示标签列 |

### kubectl cluster-info - 查看集群信息

**基础用法**:
```bash
kubectl cluster-info
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 导出集群信息 | `kubectl cluster-info dump` | dump 导出集群信息用于排查问题 |
| 转储详细信息 | `kubectl cluster-info dump --output-directory=%{输出目录}%` | --output-directory 指定输出目录，示例值：/tmp/cluster-dump |

### kubectl api-resources - 查看 API 资源

**基础用法**:
```bash
kubectl api-resources
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 显示详细名称 | `kubectl api-resources -o wide` | -o wide 显示资源完整名称和别名 |
| 按名称搜索 | `kubectl api-resources --namespaced=true` | --namespaced=true 只显示命名空间级别资源 |
| 查看缩写 | `kubectl api-resources --verbs=get,list` | --verbs 筛选支持特定操作的资源 |

### kubectl explain - 查看资源定义

**基础用法**:
```bash
kubectl explain %{资源类型}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 递归查看字段 | `kubectl explain %{资源类型}%.spec` | 递归查看资源的所有子字段定义 |
| 查看特定字段 | `kubectl explain %{资源类型}%.spec.%{字段路径}%` | 查看指定字段的详细定义，示例值：pod, containers |

### kubectl cp - 复制文件

**基础用法**:
```bash
kubectl cp %{命名空间}/%{Pod名称}%:%{源路径}% %{目标路径}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 复制到容器 | `kubectl cp %{本地路径}% %{命名空间}/%{Pod名称}%:%{目标路径}%` | 【常用】从本地复制到容器，示例值：./config.conf, default, myapp-abc123, /etc/nginx/conf.d |
| 指定容器 | `kubectl cp %{命名空间}/%{Pod名称}%:%{源路径}% %{目标路径}% -c %{容器名称}%` | -c 指定容器，示例值：default, myapp-abc123, /etc/nginx/nginx.conf, ./nginx.conf, main |

---

## 命名空间

### kubectl get ns - 查看命名空间

**基础用法**:
```bash
kubectl get ns
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看命名空间详情 | `kubectl describe ns %{命名空间名称}%` | 查看命名空间的详细信息和资源配额，示例值：my-namespace |

### kubectl create ns - 创建命名空间

**基础用法**:
```bash
kubectl create ns %{命名空间名称}%
```

---

## 上下文与配置

### kubectl config get-contexts - 查看上下文

**基础用法**:
```bash
kubectl config get-contexts
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 显示当前上下文 | `kubectl config current-context` | 显示当前使用的集群上下文 |

### kubectl config use-context - 切换上下文

**基础用法**:
```bash
kubectl config use-context %{上下文名称}%
```

### kubectl config view - 查看配置

**基础用法**:
```bash
kubectl config view
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 显示隐藏值 | `kubectl config view --raw` | --raw 显示完整配置（含敏感信息） |

### kubectl set-context - 设置命名空间

**基础用法**:
```bash
kubectl config set-context --current --namespace=%{命名空间}%
```

---

## 扩展示例

### kubectl get all - 查看所有资源

**基础用法**:
```bash
kubectl get all
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定命名空间 | `kubectl get all -n %{命名空间}%` | -n 指定命名空间，查看所有资源类型，示例值：default |

### kubectl edit - 编辑资源

**基础用法**:
```bash
kubectl edit %{资源类型}% %{资源名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定命名空间 | `kubectl edit %{资源类型}% %{资源名称}% -n %{命名空间}%` | 交互式编辑资源，示例值：deployment, nginx-deployment, default |

### kubectl label - 添加标签

**基础用法**:
```bash
kubectl label %{资源类型}% %{资源名称}% %{标签键}=%{标签值}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 覆盖已有标签 | `kubectl label %{资源类型}% %{资源名称}% %{标签键}=%{标签值}% --overwrite` | --overwrite 覆盖已存在的标签 |
| 指定命名空间 | `kubectl label %{资源类型}% %{资源名称}% %{标签键}=%{标签值}% -n %{命名空间}%` | -n 指定命名空间，示例值：app=nginx, default |

---

## 💡 实用场景示例

### 场景 1: Pod 调试

```bash
# 1. 查看 Pod 状态
kubectl get pods -n %{命名空间}%

# 2. 查看 Pod 详细信息
kubectl describe pod %{Pod名称}% -n %{命名空间}%

# 3. 查看日志（实时跟踪）
kubectl logs -f %{Pod名称}% -n %{命名空间}%

# 4. 进入容器排查
kubectl exec -it %{Pod名称}% -n %{命名空间}% -- /bin/bash

# 5. 查看事件（按时间排序）
kubectl get events -n %{命名空间}% --sort-by='.lastTimestamp'

# 6. 检查资源使用
kubectl top pod -n %{命名空间}%
```

### 场景 2: Deployment 更新

```bash
# 1. 更新镜像版本
kubectl set image deployment/%{Deployment名称}% %{容器名称}%=%{镜像名称}%:v2.0

# 2. 监控滚动更新状态
kubectl rollout status deployment/%{Deployment名称}% -n %{命名空间}%

# 3. 查看滚动历史
kubectl rollout history deployment/%{Deployment名称}% -n %{命名空间}%

# 4. 如果更新失败，回滚到上一版本
kubectl rollout undo deployment/%{Deployment名称}% -n %{命名空间}%

# 5. 或者回滚到指定版本
kubectl rollout undo deployment/%{Deployment名称}% --to-revision=%{版本号}% -n %{命名空间}%
```

### 场景 3: 集群排查

```bash
# 1. 查看集群信息
kubectl cluster-info

# 2. 查看所有命名空间的 Pods
kubectl get pods --all-namespaces

# 3. 查看事件（按时间排序）
kubectl get events --all-namespaces --sort-by='.lastTimestamp'

# 4. 查看节点资源使用
kubectl top node

# 5. 查看特定节点
kubectl top node %{节点名称}%

# 6. 查看 API 资源
kubectl api-resources

# 7. 查看资源定义
kubectl explain pod

# 8. 导出集群信息用于排查
kubectl cluster-info dump --output-directory=/tmp/cluster-dump
```

### 场景 4: 扩缩容

```bash
# 1. 扩容到 3 个副本
kubectl scale deployment %{Deployment名称}% --replicas=3 -n %{命名空间}%

# 2. 缩容到 1 个副本
kubectl scale deployment %{Deployment名称}% --replicas=1 -n %{命名空间}%

# 3. 检查 Deployment 状态
kubectl get deployments -n %{命名空间}%

# 4. 查看 ReplicaSet
kubectl get rs -n %{命名空间}%
```

### 场景 5: 端口转发调试

```bash
# 1. 将 Pod 端口转发到本地
kubectl port-forward %{Pod名称}% 8080:80 -n %{命名空间}%

# 2. 将 Service 端口转发到本地
kubectl port-forward svc/%{Service名称}% 8080:80 -n %{命名空间}%

# 3. 后台运行端口转发
kubectl port-forward %{Pod名称}% 8080:80 -n %{命名空间}% &
```

### 场景 6: 配置管理

```bash
# 1. 查看 ConfigMaps
kubectl get configmaps -n %{命名空间}%

# 2. 查看特定 ConfigMap
kubectl describe configmap %{ConfigMap名称}% -n %{命名空间}%

# 3. 查看 Secrets
kubectl get secrets -n %{命名空间}%

# 4. 创建命名空间
kubectl create ns %{命名空间名称}%

# 5. 设置默认命名空间
kubectl config set-context --current --namespace=%{命名空间}%
```

---

## 📊 命令速查表

| 操作 | 命令 | 说明 |
|------|------|------|
| 查看 Pods | `kubectl get pods` | 列出 Pods（常用） |
| 查看 Deployments | `kubectl get deployments` | 列出 Deployments（常用） |
| 查看 Services | `kubectl get services` | 列出 Services（常用） |
| 查看 Pod 详情 | `kubectl describe pod` | 查看详细信息（常用） |
| 查看日志 | `kubectl logs` | 查看 Pod 日志（常用） |
| 进入容器 | `kubectl exec` | 在容器中执行命令（常用） |
| 应用配置 | `kubectl apply` | 应用 YAML 配置（常用） |
| 删除资源 | `kubectl delete` | 删除资源（常用） |
| 端口转发 | `kubectl port-forward` | 端口转发（常用） |
| 扩缩容 | `kubectl scale` | 扩缩容 Deployment（常用） |
| 滚动更新状态 | `kubectl rollout status` | 查看滚动更新（常用） |
| 回滚 | `kubectl rollout undo` | 回滚到上一版本（常用） |
| 更新镜像 | `kubectl set image` | 更新容器镜像（常用） |
| 查看事件 | `kubectl get events` | 查看集群事件（高频） |
| 资源使用 | `kubectl top pod` | 查看 Pod 资源使用（高频） |
| 节点资源 | `kubectl top node` | 查看节点资源（高频） |
| 集群信息 | `kubectl cluster-info` | 查看集群信息 |
| API 资源 | `kubectl api-resources` | 查看支持的资源 |
| 资源定义 | `kubectl explain` | 查看字段定义（高频） |
| 查看命名空间 | `kubectl get ns` | 列出命名空间 |
| 创建命名空间 | `kubectl create ns` | 创建命名空间 |
| 查看上下文 | `kubectl config get-contexts` | 查看所有上下文 |
| 切换上下文 | `kubectl config use-context` | 切换上下文 |
| 查看配置 | `kubectl config view` | 查看 kubeconfig |
| 复制文件 | `kubectl cp` | 在容器间复制文件 |

---

## 🔗 相关资源

- [快速开始指南](../quick-start.md)
- [Linux 命令文档](../linux-commands/README.md)
- [Docker 命令文档](../Docker 命令/README.md)
- [完整命令参考表](../../references/commands-reference.md)