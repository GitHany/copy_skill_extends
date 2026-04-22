# Kubernetes 高级操作文档

Kubernetes 高级操作完整参考文档，涵盖 Operators、安全、存储、网络、监控和故障排查。

## 目录

- [Kubernetes Operators](#kubernetes-operators)
- [Kubernetes 安全](#kubernetes-安全)
- [Kubernetes 存储](#kubernetes-存储)
- [Kubernetes 网络](#kubernetes-网络)
- [Kubernetes 监控](#kubernetes-监控)
- [Kubernetes 故障排查](#kubernetes-故障排查)

---

## Kubernetes Operators

### Operator SDK - 创建 API

**基础用法**:
```bash
operator-sdk create api --group %{组名}% --version %{版本}% --kind %{类型}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 CRD API | `operator-sdk create api --group %{组名}% --version %{版本}% --kind %{类型}% --resource --controller` | 创建自定义资源及其控制器 |
| 初始化项目 | `operator-sdk init --domain %{域名}% --repo %{仓库}%` | 初始化 Operator 项目，示例值：my.domain, github.com/myorg/project |
| 创建 Webhook | `operator-sdk create webhook --group %{组名}% --version %{版本}% --kind %{类型}%` | 为 CRD 创建 admission webhook |
| 运行本地 | `operator-sdk run --local --namespace=%{命名空间}%` | 本地运行 Operator，示例值：default |
| 生成 CRD | `operator-sdk generate kustomize manifests` | 生成 CRD kustomize 清单 |
| 构建镜像 | `operator-sdk build %{镜像}%` | 构建 Operator 镜像，示例值：myorg/my-operator:v1.0.0 |

### kubebuilder - 创建 API

**基础用法**:
```bash
kubebuilder init --domain %{域名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 API | `kubebuilder create api --group %{组名}% --version %{版本}% --kind %{类型}%` | 创建 CRD 和控制器代码 |
| 创建 Webhook | `kubebuilder create webhook --group %{组名}% --version %{版本}% --kind %{类型}%` | 创建 admission webhook |
| 创建多版本 API | `kubebuilder create api --group %{组名}% --version %{版本}% --version %{版本2}% --kind %{类型}%` | 多版本 API |

---

## Kubernetes 安全

### RBAC - 角色与权限

**基础用法**:
```bash
kubectl create role %{角色名称}% --verb=%{动作}% --resource=%{资源}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 Role | `kubectl create role %{角色名称}% --verb=get,list --resource=pods -n %{命名空间}%` | 创建命名空间级别 Role，示例值：pod-reader, default |
| 创建 ClusterRole | `kubectl create clusterrole %{角色名称}% --verb=get,list --resource=pods` | 创建集群级别 ClusterRole |
| 创建 RoleBinding | `kubectl create rolebinding %{绑定名称}% --role=%{角色名称}% --user=%{用户名}% -n %{命名空间}%` | 绑定 Role 到用户 |
| 创建 ClusterRoleBinding | `kubectl create clusterrolebinding %{绑定名称}% --clusterrole=%{ClusterRole名称}% --user=%{用户名}%` | 绑定 ClusterRole 到用户 |
| 查看 Role | `kubectl get roles -n %{命名空间}%` | 查看命名空间中的 Roles |
| 查看 RoleBinding | `kubectl get rolebindings -n %{命名空间}%` | 查看 RoleBindings |
| 查看 ClusterRole | `kubectl get clusterroles` | 查看所有 ClusterRoles |
| 授权检查 | `kubectl auth can-i %{动作}% %{资源}% --as=%{用户}%` | 检查用户权限 |

### NetworkPolicy - 网络策略

**基础用法**:
```bash
kubectl get networkpolicies -n %{命名空间}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看网络策略 | `kubectl get networkpolicies -n %{命名空间}%` | 查看命名空间的网络策略 |
| 查看策略详情 | `kubectl describe networkpolicy %{策略名称}% -n %{命名空间}%` | 查看网络策略详情 |
| 创建 ingress 策略 | `kubectl apply -f -` (YAML) | 应用 Ingress 网络策略 YAML |
| 隔离 Pod | `kubectl label pod %{Pod名称}% app=%{应用标签}% -n %{命名空间}%` | 为 Pod 打标签以便网络策略匹配 |

### PodSecurityPolicy / Pod Security Standards

**基础用法**:
```bash
kubectl label namespace %{命名空间}% pod-security.kubernetes.io/enforce=baseline
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启用基线策略 | `kubectl label namespace %{命名空间}% pod-security.kubernetes.io/enforce=baseline` | 应用基线 PSS 策略 |
| 启用受限策略 | `kubectl label namespace %{命名空间}% pod-security.kubernetes.io/enforce=restricted` | 应用受限 PSS 策略 |
| 查看命名空间标签 | `kubectl describe namespace %{命名空间}%` | 查看命名空间的 PSS 标签 |
| 检查 Pod 安全性 | `kubectl auth can-i create pod --subresource=securitycontext -n %{命名空间}%` | 检查安全上下文权限 |

### Secrets 管理

**基础用法**:
```bash
kubectl create secret generic %{密钥名称}% --from-literal=key=%{值}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 generic secret | `kubectl create secret generic %{密钥名称}% --from-literal=key=%{值}% -n %{命名空间}%` | 从字面值创建 Secret |
| 创建 tls secret | `kubectl create secret tls %{密钥名称}% --cert=%{证书文件}% --key=%{密钥文件}%` | 创建 TLS Secret |
| 查看 secret 列表 | `kubectl get secrets -n %{命名空间}%` | 查看命名空间中的 Secrets |
| 解码 secret 值 | `kubectl get secret %{密钥名称}% -o jsonpath='{.data.key}' | base64 -d` | 解码 Secret 内容 |

---

## Kubernetes 存储

### PersistentVolume 与 PersistentVolumeClaim

**基础用法**:
```bash
kubectl get pvc -n %{命名空间}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看 PVC | `kubectl get pvc -n %{命名空间}%` | 查看命名空间的 PVC |
| 查看 PV | `kubectl get pv` | 查看所有 PersistentVolumes |
| 创建 PVC | `kubectl create -f %{PVC文件}%` | 通过 YAML 创建 PVC |
| 绑定状态 | `kubectl get pvc -n %{命名空间}% -o wide` | 查看 PVC 绑定状态 |
| 删除 PV | `kubectl delete pv %{PV名称}%` | 删除 PersistentVolume |
| 查看 PV 详情 | `kubectl describe pv %{PV名称}%` | 查看 PV 详细信息 |

### StorageClass

**基础用法**:
```bash
kubectl get storageclass
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看所有 StorageClass | `kubectl get storageclass` | 列出所有存储类 |
| 查看默认存储类 | `kubectl get storageclass -o jsonpath='{.items[?(@.metadata.annotations.storageclass\.kubernetes\.io/is-default-class=="true")].metadata.name}'` | 获取默认存储类 |
| 设置默认存储类 | `kubectl patch storageclass %{存储类名称}% -p '{"metadata":{"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'` | 设为默认存储类 |
| 创建 StorageClass | `kubectl apply -f -` (YAML) | 通过 YAML 创建存储类 |
| 查看存储供应商 | `kubectl get sc %{存储类名称}% -o yaml` | 查看存储类配置详情 |

### CSI (Container Storage Interface)

**基础用法**:
```bash
kubectl get csinode
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看 CSI 驱动 | `kubectl get csidriver` | 列出集群中的 CSI 驱动 |
| 查看 CSI 卷 | `kubectl get csinodes -o wide` | 查看节点上的 CSI 驱动信息 |
| 查看存储操作 | `kubectl get volumeattachments` | 查看卷附件 |
| 创建 PVC 与 CSI | `kubectl apply -f -` (PVC YAML) | 创建使用 CSI 的 PVC |
| 检查 PVC 绑定 | `kubectl describe pvc %{PVC名称}% -n %{命名空间}%` | 检查 CSI 驱动的 PVC 绑定 |

### 动态卷管理

**基础用法**:
```bash
kubectl apply -f %{PV文件}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 PV | `kubectl apply -f %{PV文件}%` | 通过 YAML 创建 PersistentVolume |
| 查看卷状态 | `kubectl get pv -l %{标签键}=%{标签值}%` | 按标签过滤查看 PV |
| 扩展 PVC | `kubectl patch pvc %{PVC名称}% -p '{"spec":{"resources":{"requests":{"storage":"%{新大小}%"}}}}}' -n %{命名空间}%` | 在线扩展 PVC 大小 |
| 查看卷快照 | `kubectl get volumesnapshots -n %{命名空间}%` | 查看卷快照 |

---

## Kubernetes 网络

### 网络策略

**基础用法**:
```bash
kubectl get networkpolicies -n %{命名空间}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看网络策略 | `kubectl get networkpolicy -n %{命名空间}%` | 列出命名空间中的网络策略 |
| 查看策略详情 | `kubectl describe networkpolicy %{策略名称}% -n %{命名空间}%` | 查看网络策略详情 |
| 应用策略 | `kubectl apply -f %{策略文件}%` | 应用网络策略 YAML |
| 删除策略 | `kubectl delete networkpolicy %{策略名称}% -n %{命名空间}%` | 删除网络策略 |

### Ingress

**基础用法**:
```bash
kubectl get ingress -n %{命名空间}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看 Ingress | `kubectl get ingress -n %{命名空间}%` | 查看命名空间的 Ingress |
| 创建 Ingress | `kubectl apply -f %{Ingress文件}%` | 通过 YAML 创建 Ingress |
| 编辑 Ingress | `kubectl edit ingress %{Ingress名称}% -n %{命名空间}%` | 交互式编辑 Ingress |
| 查看 Ingress 类 | `kubectl get ingressclass` | 查看所有 IngressClass |
| 设置默认 IngressClass | `kubectl annotate ingressclass %{类名}% ingressclass.kubernetes.io/is-default-class="true"` | 设为默认 IngressClass |

### Service Mesh - Istio

**基础用法**:
```bash
istioctl get destinationrules -n %{命名空间}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看虚拟服务 | `kubectl get virtualservice -n %{命名空间}%` | 查看虚拟服务 |
| 查看目标规则 | `kubectl get destinationrule -n %{命名空间}%` | 查看目标规则 |
| 检查 Envoy 配置 | `istioctl proxy-config cluster %{Pod名称}% -n %{命名空间}%` | 查看 Pod 的 Envoy 集群配置 |
| 查看代理路由 | `istioctl proxy-config route %{Pod名称}% -n %{命名空间}%` | 查看 Pod 的路由配置 |
| 验证配置 | `istioctl analyze -n %{命名空间}%` | 分析 Istio 配置问题 |
| 查看 Sidecar | `kubectl get sidecar -n %{命名空间}%` | 查看 Sidecar 配置 |
| 创建网关 | `kubectl apply -f -` (Gateway YAML) | 创建 Istio Gateway |

---

## Kubernetes 监控

### 资源使用监控

**基础用法**:
```bash
kubectl top nodes
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看节点资源 | `kubectl top nodes` | 显示所有节点的 CPU 和内存使用 |
| 查看 Pod 资源 | `kubectl top pods -n %{命名空间}%` | 显示命名空间 Pod 的资源使用 |
| 按标签筛选 | `kubectl top pods -n %{命名空间}% -l %{标签键}=%{标签值}%` | 只显示特定标签的 Pod |
| 显示容器详情 | `kubectl top pods -n %{命名空间}% --containers` | 显示每个容器的资源使用 |
| 查看所有命名空间 | `kubectl top pods --all-namespaces` | 显示所有命名空间的 Pod 资源 |

### 日志与事件

**基础用法**:
```bash
kubectl get events -n %{命名空间}% --sort-by='.lastTimestamp'
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 按时间排序查看事件 | `kubectl get events -n %{命名空间}% --sort-by='.lastTimestamp'` | 最新的事件排在前面 |
| 查看所有命名空间事件 | `kubectl get events --all-namespaces --sort-by='.lastTimestamp'` | 查看集群所有事件 |
| 查看特定资源事件 | `kubectl get events --field-selector involvedObject.name=%{资源名称}% -n %{命名空间}%` | 查看特定对象的事件 |
| 限制输出条数 | `kubectl get events -n %{命名空间}% --limit=%{数量}%` | 限制显示的事件数量，示例值：50 |
| 查看 Pod 历史事件 | `kubectl get events -n %{命名空间}% --watch` | 实时监控事件变化 |

### 资源详情检查

**基础用法**:
```bash
kubectl describe %{资源类型}% %{资源名称}% -n %{命名空间}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看 Pod 详情 | `kubectl describe pod %{Pod名称}% -n %{命名空间}%` | 显示 Pod 详细配置和状态 |
| 查看 Node 详情 | `kubectl describe node %{节点名称}%` | 显示节点详细信息 |
| 查看 Service 详情 | `kubectl describe svc %{Service名称}% -n %{命名空间}%` | 显示 Service 详细配置 |
| 查看 Deployment 详情 | `kubectl describe deployment %{Deployment名称}% -n %{命名空间}%` | 显示 Deployment 详细信息 |
| 查看 PVC 详情 | `kubectl describe pvc %{PVC名称}% -n %{命名空间}%` | 显示 PVC 绑定和状态详情 |

---

## Kubernetes 故障排查

### 调试与诊断

**基础用法**:
```bash
kubectl debug %{Pod名称}% -it --image=%{镜像}% -n %{命名空间}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 使用调试镜像启动容器 | `kubectl debug %{Pod名称}% -it --image=%{镜像}% -n %{命名空间}%` | 在 Pod 中启动调试容器 |
| 复制 Pod 调试 | `kubectl debug %{Pod名称}% -it --copy-to=%{调试Pod名称}% -n %{命名空间}%` | 复制 Pod 用于调试 |
| 附加到容器 | `kubectl attach %{Pod名称}% -i -t -n %{命名空间}%` | 附加到运行中的容器 |
| 在容器中执行命令 | `kubectl exec %{Pod名称}% -n %{命名空间}% -- %{命令}%` | 执行单条命令，示例值：ls -la |
| 交互式进入容器 | `kubectl exec -it %{Pod名称}% -n %{命名空间}% -- /bin/sh` | 使用 sh 进入容器 |
| 交互式进入 bash | `kubectl exec -it %{Pod名称}% -n %{命名空间}% -- /bin/bash` | 使用 bash 进入容器（如果存在） |

### 端口转发

**基础用法**:
```bash
kubectl port-forward %{Pod名称}% %{本地端口}%:%{Pod端口}% -n %{命名空间}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 转发 Pod 端口 | `kubectl port-forward %{Pod名称}% %{本地端口}%:%{Pod端口}% -n %{命名空间}%` | 转发 Pod 端口到本地 |
| 转发 Service 端口 | `kubectl port-forward svc/%{Service名称}% %{本地端口}%:%{Service端口}% -n %{命名空间}%` | 转发 Service 端口 |
| 转发到所有地址 | `kubectl port-forward %{Pod名称}% %{本地端口}%:%{Pod端口}% --address=0.0.0.0 -n %{命名空间}%` | 允许外部访问 |
| 后台运行 | `kubectl port-forward %{Pod名称}% %{本地端口}%:%{Pod端口}% -n %{命名空间}% &` | 端口转发在后台运行 |
| 转发多个端口 | `kubectl port-forward %{Pod名称}% %{本地端口1}%:%{Pod端口1}% %{本地端口2}%:%{Pod端口2}% -n %{命名空间}%` | 同时转发多个端口 |

### 节点维护

**基础用法**:
```bash
kubectl cordon %{节点名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 标记节点不可调度 | `kubectl cordon %{节点名称}%` | 标记节点为不可调度，新 Pod 不会调度到该节点 |
| 驱逐节点上 Pod | `kubectl drain %{节点名称}% --ignore-daemonsets --delete-emptydir-data` | 驱逐节点上所有 Pod |
| 带超时驱逐 | `kubectl drain %{节点名称}% --ignore-daemonsets --delete-emptydir-data --grace-period=%{秒数}%` | 设置优雅终止超时 |
| 强制驱逐 | `kubectl drain %{节点名称}% --force` | 强制驱逐 DaemonSet Pod |
| 恢复节点调度 | `kubectl uncordon %{节点名称}%` | 恢复节点为可调度状态 |
| 查看节点状态 | `kubectl get nodes -o wide` | 查看所有节点状态和条件 |

---

## 实用场景示例

### 场景 1: 创建 Operator CRD

```bash
# 1. 初始化 Operator 项目
operator-sdk init --domain my.domain --repo github.com/myorg/my-operator

# 2. 创建 CRD API
operator-sdk create api --group apps --version v1 --kind MyOperator --resource --controller

# 3. 创建 Webhook
operator-sdk create webhook --group apps --version v1 --kind MyOperator

# 4. 生成 CRD 清单
operator-sdk generate kustomize manifests

# 5. 构建镜像
operator-sdk build myorg/my-operator:v1.0.0

# 6. 本地测试
operator-sdk run --local --namespace=default
```

### 场景 2: 配置 RBAC

```bash
# 1. 创建只读 Role
kubectl create role pod-reader --verb=get,list --resource=pods -n default

# 2. 绑定到用户
kubectl create rolebinding pod-reader-binding --role=pod-reader --user=user1 -n default

# 3. 创建集群级别 ClusterRole
kubectl create clusterrole cluster-reader --verb=get,list --resource=pods,namespaces

# 4. 绑定 ClusterRole
kubectl create clusterrolebinding cluster-reader-binding --clusterrole=cluster-reader --user=user1

# 5. 检查权限
kubectl auth can-i get pods --as=user1
kubectl auth can-i delete pods --as=user1
```

### 场景 3: 存储配置

```bash
# 1. 创建 StorageClass (NFS 示例)
kubectl apply -f nfs-storageclass.yaml

# 2. 创建 PVC
kubectl apply -f pvc.yaml -n myapp

# 3. 查看 PVC 状态
kubectl get pvc -n myapp

# 4. 扩展 PVC
kubectl patch pvc my-pvc -p '{"spec":{"resources":{"requests":{"storage":"20Gi"}}}}' -n myapp

# 5. 查看 PV
kubectl get pv
```

### 场景 4: 网络策略

```bash
# 1. 隔离命名空间
kubectl label namespace myns pod-security.kubernetes.io/enforce=baseline

# 2. 创建默认拒绝策略
kubectl apply -f deny-all.yaml -n myns

# 3. 创建允许 DNS 策略
kubectl apply -f allow-dns.yaml -n myns

# 4. 查看网络策略
kubectl get networkpolicy -n myns

# 5. 查看策略详情
kubectl describe networkpolicy -n myns
```

### 场景 5: Istio 配置

```bash
# 1. 查看虚拟服务
kubectl get virtualservice -n myns

# 2. 创建目标规则
kubectl apply -f destinationrule.yaml -n myns

# 3. 配置流量管理
kubectl apply -f virtualservice.yaml -n myns

# 4. 检查 Envoy 配置
istioctl proxy-config cluster myapp-pod -n myns

# 5. 分析配置
istioctl analyze -n myns
```

### 场景 6: 节点维护

```bash
# 1. 标记节点不可调度
kubectl cordon node-1

# 2. 查看节点上的 Pod
kubectl get pods -o wide | grep node-1

# 3. 驱逐 Pod（带优雅终止）
kubectl drain node-1 --ignore-daemonsets --delete-emptydir-data --grace-period=300

# 4. 执行维护操作...

# 5. 完成后恢复节点
kubectl uncordon node-1
```

### 场景 7: 调试故障 Pod

```bash
# 1. 查看 Pod 状态
kubectl get pods -n myns

# 2. 查看事件
kubectl get events -n myns --sort-by='.lastTimestamp'

# 3. 查看 Pod 详情
kubectl describe pod myapp-abc123 -n myns

# 4. 查看日志
kubectl logs myapp-abc123 -n myns --tail=100

# 5. 进入容器排查
kubectl exec -it myapp-abc123 -n myns -- /bin/bash

# 6. 端口转发进行测试
kubectl port-forward myapp-abc123 8080:8080 -n myns

# 7. 调试模式启动
kubectl debug myapp-abc123 -it --image=busybox -n myns
```

---

## 命令速查表

| 操作 | 命令 | 说明 |
|------|------|------|
| 创建 Operator API | `operator-sdk create api` | 创建 Operator CRD 和控制器 |
| 初始化 Operator | `operator-sdk init` | 初始化 Operator 项目 |
| 创建 kubebuilder API | `kubebuilder create api` | 创建 CRD 代码 |
| 创建 Role | `kubectl create role` | 创建命名空间级别角色 |
| 创建 ClusterRole | `kubectl create clusterrole` | 创建集群级别角色 |
| 创建 RoleBinding | `kubectl create rolebinding` | 绑定 Role 到用户 |
| 检查权限 | `kubectl auth can-i` | 检查用户权限 |
| 查看网络策略 | `kubectl get networkpolicy` | 查看网络隔离策略 |
| 查看 StorageClass | `kubectl get storageclass` | 查看存储类 |
| 查看 PVC | `kubectl get pvc` | 查看持久卷声明 |
| 查看 CSI 驱动 | `kubectl get csidriver` | 查看 CSI 驱动 |
| 查看 Ingress | `kubectl get ingress` | 查看入口规则 |
| 查看 Istio 虚拟服务 | `kubectl get virtualservice` | 查看服务网格配置 |
| 查看资源使用 | `kubectl top` | 查看 CPU/内存使用 |
| 查看事件 | `kubectl get events` | 查看集群事件 |
| 调试 Pod | `kubectl debug` | 启动调试容器 |
| 端口转发 | `kubectl port-forward` | 转发端口到本地 |
| 节点不可调度 | `kubectl cordon` | 标记节点不可调度 |
| 驱逐 Pod | `kubectl drain` | 安全驱逐节点 Pod |
| 恢复调度 | `kubectl uncordon` | 恢复节点可调度 |
| 解码 Secret | base64 -d | 解码 Secret 值 |
| 创建 TLS Secret | `kubectl create secret tls` | 创建 TLS 证书 Secret |

---

## 相关资源

- [Kubernetes 命令文档](../Kubernetes 命令/README.md)
- [Docker 命令文档](../Docker 命令/README.md)
- [Linux 命令文档](../Linux 命令/README.md)