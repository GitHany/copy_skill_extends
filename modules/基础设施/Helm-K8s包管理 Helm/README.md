# Helm

## 简介
Helm 是 Kubernetes 的包管理器，用于定义、安装和升级 Kubernetes 应用。通过 Chart 模板化 Kubernetes 资源清单，实现应用的一键部署和版本管理。

## 安装
```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

## 快速开始

- `helm repo add bitnami https://charts.bitnami.com/bitnami` - 添加 Chart 仓库
- `helm install myapp bitnami/nginx` - 安装 Chart
- `helm list` - 列出已安装的 Release
- `helm upgrade myapp bitnami/nginx` - 升级 Release
- `helm uninstall myapp` - 卸载 Release

## 命令索引
| 命令 | 描述 |
|------|------|
| helm install 安装 Chart | 安装 Helm Chart 到 Kubernetes 集群 |
| helm upgrade 升级 Release | 升级已安装的 Helm Release |
| helm uninstall 卸载 Release | 卸载 Release 及其所有资源 |
| helm list 列出 Release | 列出已安装的 Helm Release |
| helm repo 管理仓库 | 添加、更新和删除 Helm Chart 仓库 |
| helm rollback 回滚 Release | 将 Release 回滚到之前的版本 |
| helm template 渲染模板 | 在本地渲染 Chart 模板 |
| helm lint 检查 Chart | 检查 Chart 的语法和最佳实践 |
| helm package 打包 Chart | 将 Chart 打包为归档文件 |
| helm history 查看历史 | 查看 Release 的修订历史 |
| helm status 查看状态 | 查看已安装 Release 的状态 |
| helm create 创建 Chart | 创建新的 Chart 脚手架 |
| helm search 搜索 Chart | 搜索可用的 Chart |
| helm get values 获取值 | 获取 Release 的配置值 |
| helm dependency 依赖管理 | 管理 Chart 的依赖关系 |

## 进阶用法
- 使用 `--atomic` 标志实现自动回滚的升级
- 通过 `-f values.yaml` 自定义配置
- 使用 `helm template` 预览生成的 YAML 再部署
