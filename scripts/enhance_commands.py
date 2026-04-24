# -*- coding: utf-8 -*-
"""
增强工具 - 批量完善所有模块的 commands.json（标准版）
功能：
  1. 按照 commands_standard.json 的标准自动增强内容
  2. 包含完整的参数增强知识库
  3. 批量应用标准规范到所有模块

使用方法：python scripts/enhance_commands.py
说明：
  - 预定义常见参数的详细描述、示例和备注
  - 参考 commands_standard.json 标准进行增强
  - 自动补充缺失的参数信息

import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

# 参数增强知识库 - 常见参数的详细说明
PARAM_KNOWLEDGE = {
    # 通用参数
    "目录": {
        "description": "目标目录的路径，可以是绝对路径（如 /var/log）或相对路径（如 ./logs）。用于指定命令操作的目标位置",
        "example": "/var/log/nginx",
        "notes": "可选。默认为当前目录。建议使用绝对路径避免歧义，相对路径基于当前工作目录解析"
    },
    "文件": {
        "description": "目标文件的路径，包含文件名和扩展名。用于指定命令操作的具体文件",
        "example": "/etc/nginx/nginx.conf",
        "notes": "可选。必须包含完整的文件名和扩展名。建议先确认文件存在性和读写权限"
    },
    "路径": {
        "description": "文件系统路径，可以是文件或目录的绝对路径或相对路径。用于定位命令操作的目标",
        "example": "/usr/local/bin",
        "notes": "可选。支持绝对路径和相对路径。包含空格的路径需用引号包裹"
    },
    "主机": {
        "description": "远程服务器的主机名或 IP 地址。用于指定网络连接的目标主机",
        "example": "192.168.1.100",
        "notes": "可选。默认 127.0.0.1(localhost)。支持 IPv4、IPv6 和域名"
    },
    "端口": {
        "description": "网络服务端口号，范围 1-65535。用于指定服务监听或连接的端口",
        "example": "8080",
        "notes": "可选。默认视服务而定。1-1023 为系统端口需 root 权限，1024-65535 为用户端口"
    },
    "用户名": {
        "description": "用于身份验证的用户标识名称。不同系统中可能有不同的命名规则限制",
        "example": "admin",
        "notes": "必填。通常只能包含字母、数字、下划线和连字符，长度限制视系统而定"
    },
    "密码": {
        "description": "用于身份验证的机密字符串。应包含大小写字母、数字和特殊字符以增强安全性",
        "example": "MyP@ssw0rd!2024",
        "notes": "必填。建议使用强密码（12位以上，包含多种字符类型）。避免在命令行中明文传输密码"
    },
    "URL": {
        "description": "统一资源定位符，用于指定网络资源的地址。支持 HTTP、HTTPS、Git 等协议",
        "example": "https://github.com/user/repo.git",
        "notes": "必填。必须包含协议头（如 https://）。私有仓库可能需要认证信息"
    },
    "仓库URL": {
        "description": "代码仓库的网络地址，支持 HTTPS、SSH、Git 等协议。用于克隆或推送代码",
        "example": "https://github.com/user/repo.git",
        "notes": "必填。HTTPS 需要用户名密码，SSH 需要配置密钥。建议使用 SSH 协议进行频繁操作"
    },

    # Docker 参数
    "容器名称": {
        "description": "Docker 容器的唯一标识名称，用于后续管理操作（启动、停止、删除等）。只能包含字母、数字、下划线、连字符和点",
        "example": "myapp-web",
        "notes": "必填。同一主机上名称不能重复。建议使用 应用名-组件 格式，如 nginx-proxy、redis-cache"
    },
    "镜像名称": {
        "description": "Docker 镜像的名称，可包含命名空间、仓库名和标签。用于创建容器的基础模板",
        "example": "nginx:1.24-alpine",
        "notes": "必填。格式：[仓库/]镜像名[:标签]。建议使用具体版本标签，避免使用 latest 导致版本不可控"
    },
    "镜像": {
        "description": "Docker 镜像的名称，可包含命名空间、仓库名和标签。用于创建容器或执行操作",
        "example": "nginx:1.24-alpine",
        "notes": "必填。格式：[仓库/]镜像名[:标签]。本地不存在时会自动从仓库拉取"
    },
    "主机端口": {
        "description": "宿主机上暴露的端口号，外部请求通过此端口访问容器服务。将宿主机网络端口映射到容器内部",
        "example": "8080",
        "notes": "必填。范围 1-65535，小于 1024 需 root 权限。确保端口未被其他服务占用"
    },
    "容器端口": {
        "description": "容器内部应用实际监听的端口号。容器内应用绑定此端口提供服务",
        "example": "80",
        "notes": "必填。需与容器内应用实际监听端口一致。常见：Nginx 80、MySQL 3306、Redis 6379"
    },
    "主机路径": {
        "description": "宿主机上要挂载到容器的目录或文件绝对路径。用于实现容器数据的持久化存储",
        "example": "/data/nginx/logs",
        "notes": "必填。路径必须在宿主机上存在。建议使用绝对路径，避免相对路径解析歧义"
    },
    "容器路径": {
        "description": "容器内部的挂载目标路径，即容器内应用实际读写数据的位置",
        "example": "/var/log/nginx",
        "notes": "必填。需根据容器内应用的配置文件确认正确路径"
    },
    "网络名称": {
        "description": "Docker 网络的标识名称，用于容器间的网络通信和隔离。可以是 bridge、host、none 或自定义网络",
        "example": "myapp_network",
        "notes": "必填。自定义网络需先通过 docker network create 创建。同一网络的容器可通过名称互相访问"
    },
    "环境变量": {
        "description": "传递给容器内部应用的配置参数，以键值对形式设置。用于配置应用行为而无需修改镜像",
        "example": "MYSQL_ROOT_PASSWORD",
        "notes": "必填。变量名通常为大写字母和下划线。敏感信息建议使用 Docker Secrets 或挂载文件"
    },
    "变量值": {
        "description": "环境变量的具体取值，用于配置容器内应用的运行参数",
        "example": "mysecretpassword123",
        "notes": "必填。包含空格或特殊字符的值建议用引号包裹。敏感信息避免直接暴露在命令行"
    },
    "卷名": {
        "description": "Docker 数据卷的名称，用于持久化存储容器数据。与挂载目录不同，卷由 Docker 管理",
        "example": "mysql_data",
        "notes": "必填。卷不存在时会自动创建。使用 docker volume ls 查看已有卷，docker volume create 预创建"
    },

    # Git 参数
    "分支名": {
        "description": "Git 分支的名称标识，用于并行开发和版本管理。分支名应简洁描述功能或版本",
        "example": "feature/user-auth",
        "notes": "必填。只能包含字母、数字、下划线、连字符、点和斜杠。常用前缀：feature/、bugfix/、release/、hotfix/"
    },
    "提交信息": {
        "description": "描述代码变更内容的简短说明，用于版本历史记录和代码审查。应清晰说明做了什么和为什么",
        "example": "feat: add user authentication with JWT tokens",
        "notes": "必填。建议使用语义化提交规范：feat(新功能)、fix(修复)、docs(文档)、refactor(重构)。50字以内"
    },
    "标签名": {
        "description": "Git 标签的名称，用于标记特定的提交点（通常是版本发布）。标签分为轻量标签和附注标签",
        "example": "v1.2.0",
        "notes": "必填。建议使用语义化版本号格式：v主版本.次版本.修订号。如 v1.2.0、v2.0.0-beta.1"
    },
    "远程名": {
        "description": "远程仓库的本地别名，用于简化远程仓库的引用。默认远程仓库名为 origin",
        "example": "origin",
        "notes": "可选。默认为 origin。可通过 git remote -v 查看已配置的远程仓库"
    },

    # K8s 参数
    "命名空间": {
        "description": "Kubernetes 中的逻辑隔离区域，用于将集群资源划分为多个虚拟集群。不同命名空间的资源相互隔离",
        "example": "production",
        "notes": "可选。默认 default。常用：default、kube-system、kube-public。生产环境建议按环境划分命名空间"
    },
    "Pod名称": {
        "description": "Kubernetes Pod 的唯一标识名称，由控制器（如 Deployment）自动或手动指定",
        "example": "nginx-deployment-7c4c7b5d9-x2v4p",
        "notes": "必填。可通过 kubectl get pods 查看。支持使用部分名称匹配，也可使用标签选择器"
    },
    "资源类型": {
        "description": "Kubernetes 资源对象的类型，用于指定要操作的集群资源类别",
        "example": "deployments",
        "notes": "必填。常用：pods、deployments、services、configmaps、secrets、ingress、nodes、jobs、cronjobs"
    },
    "Deployment名称": {
        "description": "Kubernetes Deployment 控制器的名称，用于管理 Pod 的副本数和滚动更新",
        "example": "nginx-deployment",
        "notes": "必填。Deployment 负责维护指定数量的 Pod 副本，支持滚动更新和回滚"
    },
    "Service名称": {
        "description": "Kubernetes Service 的名称，用于为一组 Pod 提供稳定的网络访问端点",
        "example": "nginx-service",
        "notes": "必填。Service 通过标签选择器将流量路由到匹配的 Pod，提供负载均衡"
    },
    "副本数": {
        "description": "Pod 的期望运行实例数量，Deployment 会自动调整实际运行的 Pod 数量以匹配此值",
        "example": "3",
        "notes": "必填。必须为正整数。建议生产环境至少 2 个副本以保证高可用，开发环境可 1 个"
    },
    "配置文件": {
        "description": "Kubernetes 资源定义文件的路径，通常为 YAML 或 JSON 格式。包含资源的完整配置声明",
        "example": "/k8s/deployment.yaml",
        "notes": "必填。支持 YAML 和 JSON 格式。建议将配置文件纳入版本控制，使用 kubectl apply 进行声明式管理"
    },

    # 数据库参数
    "数据库名": {
        "description": "数据库实例的名称标识，用于区分同一数据库服务器上的不同数据库",
        "example": "myapp_production",
        "notes": "必填。命名通常只能包含字母、数字、下划线。创建后可通过 SHOW DATABASES 查看"
    },
    "表名": {
        "description": "关系型数据库中的表名称，用于组织和存储特定类型的数据记录",
        "example": "users",
        "notes": "必填。建议使用复数名词命名表名，如 users、orders、products。避免使用 SQL 保留字"
    },
    "列名": {
        "description": "数据库表中的字段名称，用于标识和访问特定的数据列",
        "example": "email",
        "notes": "必填。建议使用小写字母和下划线命名（snake_case），如 created_at、updated_at"
    },
    "查询条件": {
        "description": "用于筛选数据的条件表达式，支持比较运算符、逻辑运算符和模式匹配",
        "example": "age > 18 AND status = 'active'",
        "notes": "可选。支持 =、!=、>、<、>=、<=、LIKE、IN、BETWEEN 等运算符。字符串值需用引号包裹"
    },
    "key": {
        "description": "Redis 键名，用于唯一标识存储的数据。键是二进制安全的字符串",
        "example": "user:1001:profile",
        "notes": "必填。建议使用命名空间前缀组织键名，如 user:、session:、cache:。避免使用过长的键名"
    },
    "value": {
        "description": "Redis 键对应的存储值，可以是字符串、数字或二进制数据。最大可存储 512MB",
        "example": "{\"name\":\"张三\",\"age\":25}",
        "notes": "必填。字符串值包含空格需用引号包裹。复杂对象建议序列化为 JSON 存储"
    },
    "秒数": {
        "description": "以秒为单位的时间数值，用于设置键的过期时间或等待超时时间",
        "example": "3600",
        "notes": "必填。1 小时=3600 秒，1 天=86400 秒，7 天=604800 秒。过期后键会自动删除"
    },

    # 包管理参数
    "包名": {
        "description": "软件包的名称标识，用于在包仓库中查找和安装特定的软件包",
        "example": "requests",
        "notes": "必填。名称区分大小写（视包管理器而定）。可通过搜索命令确认包名和可用版本"
    },
    "版本号": {
        "description": "软件包的具体版本标识，遵循语义化版本规范（主版本.次版本.修订号）",
        "example": "2.28.0",
        "notes": "必填。格式：主版本.次版本.修订号。不指定版本通常安装最新版，可能导致兼容性问题"
    },

    # 文件系统参数
    "选项": {
        "description": "命令的附加选项标志，用于修改命令的默认行为。多个选项可以组合使用",
        "example": "-la",
        "notes": "可选。常见选项：-l(长格式)、-a(显示隐藏文件)、-h(人类可读)、-r(递归)、-f(强制)"
    },
    "来源": {
        "description": "源文件或目录的路径，指定要复制、移动或传输的数据来源位置",
        "example": "/var/log/app.log",
        "notes": "必填。必须存在且有读取权限。支持通配符 * 和 ? 进行批量匹配"
    },
    "目标": {
        "description": "目标文件或目录的路径，指定数据复制、移动后的存放位置",
        "example": "/backup/logs/",
        "notes": "必填。目录不存在时部分命令会自动创建，文件存在时可能会被覆盖"
    },
}

# 描述增强模板
DESCRIPTION_TEMPLATES = {
    "ls": "列出指定目录的内容，显示文件和子目录的详细信息。支持多种排序方式和过滤选项，是日常文件系统浏览和管理的基础命令。常用于查看目录结构、检查文件权限和大小、定位特定文件",
    "cd": "切换当前工作目录到指定路径。支持绝对路径和相对路径，以及特殊目录引用（如上级目录、用户主目录）。是命令行导航的基础操作，所有相对路径的文件操作都依赖于当前目录",
    "pwd": "显示当前工作目录的完整绝对路径。在脚本中常用于确认执行位置，或在复杂的目录导航后确认当前所在位置",
    "cp": "复制文件或目录从一个位置到另一个位置。支持递归复制目录、保留文件属性、显示进度等选项。是文件备份和分发的常用命令",
    "mv": "移动或重命名文件和目录。在同一文件系统内移动效率高（仅修改元数据），跨文件系统移动会实际复制数据。也可用于批量重命名",
    "rm": "删除文件或目录。删除操作通常不可恢复，使用时需谨慎。支持递归删除目录、强制删除、交互确认等选项",
    "mkdir": "创建新的目录。支持创建多级嵌套目录（自动创建父目录）和设置权限模式。是项目初始化和目录结构组织的基础命令",
    "cat": "连接并显示文件内容。常用于查看小文件内容、合并多个文件、创建简单文件。对于大文件建议使用 less 或 more",
    "grep": "在文件或输入中搜索匹配指定模式的行。支持正则表达式、忽略大小写、递归搜索、显示上下文等。是文本分析和日志排查的核心工具",
    "find": "在目录层次结构中搜索文件和目录。支持按名称、类型、大小、修改时间、权限等多种条件筛选。是文件定位和批量操作的基础",
    "chmod": "修改文件或目录的访问权限。通过数字模式（如 755）或符号模式（如 u+x）控制读、写、执行权限。是系统安全和访问控制的基础",
    "chown": "修改文件或目录的所有者和所属组。用于调整文件归属，解决权限问题，或在服务账户间转移文件所有权",
    "ps": "显示当前系统运行的进程信息。支持多种输出格式和筛选条件，是系统监控和进程管理的基础命令",
    "kill": "向指定进程发送信号，用于终止或控制进程运行。默认发送 TERM 信号请求终止，可指定其他信号实现不同控制",
    "tar": "创建和解压归档文件，支持多种压缩格式（gzip、bzip2、xz）。是文件打包备份和分发的标准工具",
    "ssh": "通过安全 shell 协议连接到远程服务器。提供加密的远程登录和命令执行，是服务器远程管理的主要方式",
    "scp": "通过 SSH 协议安全地复制文件到远程服务器或从远程服务器复制文件。支持递归复制目录和保留文件属性",
    "curl": "强大的命令行 HTTP 客户端，支持多种协议（HTTP、HTTPS、FTP 等）。用于 API 测试、文件下载、数据传输，支持自定义请求头、方法和数据",
    "wget": "非交互式网络下载工具，支持 HTTP、HTTPS、FTP 协议。支持断点续传、递归下载、后台下载，适合批量下载和脚本中使用",
    "docker run": "创建并启动一个新容器。这是最常用的 Docker 命令，用于基于指定镜像创建可运行的容器实例。支持端口映射、环境变量、数据卷挂载、网络连接等多种配置选项",
    "docker ps": "列出 Docker 容器的状态信息。可查看运行中或所有容器（含已停止）的 ID、镜像、创建时间、状态、端口映射等关键信息",
    "docker build": "根据 Dockerfile 构建 Docker 镜像。支持指定标签、构建参数、目标阶段等，是自定义镜像创建的核心命令",
    "docker exec": "在运行中的容器内执行命令。支持交互模式和后台执行，是容器调试和管理的常用方式",
    "docker logs": "获取容器的标准输出和标准错误日志。支持实时跟踪、时间范围、行数限制等选项，是容器问题排查的主要手段",
    "docker pull": "从镜像仓库拉取指定镜像到本地。支持指定标签和摘要，是获取和更新镜像的标准方式",
    "docker push": "将本地构建的镜像推送到远程仓库。需要先登录仓库并正确标记镜像，是镜像分发的核心操作",
    "docker network": "管理 Docker 网络，包括创建、删除、查看网络和连接容器。支持 bridge、host、overlay 等多种网络驱动",
    "docker volume": "管理 Docker 数据卷，提供持久化存储解决方案。卷由 Docker 管理，独立于容器生命周期，适合数据持久化",
    "docker-compose up": "根据 docker-compose.yml 文件构建、创建并启动所有服务。支持后台运行、强制重建、指定服务等选项，是本地多容器应用开发的核心命令",
    "docker-compose down": "停止并移除 docker-compose 管理的所有容器、网络和卷。支持移除卷和镜像，是清理开发环境的标准方式",
    "git clone": "将远程 Git 仓库完整复制到本地，包括所有分支、标签和提交历史。是参与项目开发的第一步，支持浅克隆、指定分支等选项",
    "git init": "在当前目录初始化一个新的 Git 仓库，创建 .git 目录和默认配置。是新项目版本控制的起点，也可用于将现有项目纳入版本控制",
    "git status": "显示工作区相对于暂存区和最新提交的状态。可查看修改、新增、删除的文件，以及分支信息和上游差异",
    "git add": "将工作区的文件修改添加到暂存区，准备提交。支持添加单个文件、批量匹配或交互式选择，是提交前的必要步骤",
    "git commit": "将暂存区的更改保存为新的提交，创建项目历史的新节点。每次提交应包含清晰的消息说明变更内容",
    "git push": "将本地分支的提交推送到远程仓库。是分享代码和协作开发的核心操作，支持指定远程和分支",
    "git pull": "从远程仓库获取最新更改并合并到当前分支。相当于 git fetch + git merge，是同步团队代码的常用命令",
    "git branch": "列出、创建或删除分支。分支是 Git 并行开发的核心机制，支持轻量级创建和切换",
    "git checkout": "切换分支或恢复工作区文件。支持创建并切换新分支、回滚文件到指定版本、分离 HEAD 等操作",
    "git merge": "将一个分支的更改合并到当前分支。支持快进合并和三方合并，是解决分支并行开发集成的标准方式",
    "git rebase": "将当前分支的提交在目标分支基础上重新应用。产生更线性的历史，但会改写提交哈希，需谨慎在共享分支使用",
    "git log": "查看提交历史记录。支持多种格式、筛选条件、图形化显示，是了解项目演进和定位变更的主要方式",
    "git diff": "显示工作区、暂存区或提交之间的差异。支持多种比较模式，是代码审查和变更确认的重要工具",
    "git stash": "临时保存工作区的未提交更改，清空工作区以便执行其他操作。支持保存、查看、恢复和删除暂存",
    "git tag": "创建、列出或删除标签。标签用于标记重要的提交点（如版本发布），分为轻量标签和附注标签",
    "git remote": "管理远程仓库配置。支持添加、删除、修改远程仓库地址，是配置代码同步目标的核心命令",
    "git fetch": "从远程仓库下载最新的分支和提交信息，但不自动合并。是安全地获取远程更新的方式",
    "kubectl get": "查看 Kubernetes 集群中的资源对象。支持多种资源类型、输出格式、标签筛选和全命名空间查询",
    "kubectl describe": "显示资源的详细信息和事件。比 get 提供更丰富的状态、条件和最近事件，是问题排查的常用命令",
    "kubectl create": "根据配置文件或命令行参数创建资源。支持从 YAML/JSON 文件创建，是声明式资源管理的基础",
    "kubectl apply": "根据配置文件应用资源的期望状态。支持创建和更新，是生产环境管理 Kubernetes 资源的推荐方式",
    "kubectl delete": "删除指定的资源对象。支持按名称、标签、配置文件删除，是资源清理和重新部署的常用操作",
    "kubectl logs": "获取 Pod 中容器的日志输出。支持实时跟踪、多容器选择、时间范围，是应用问题排查的主要手段",
    "kubectl exec": "在 Pod 的容器中执行命令。支持交互式 shell 访问，是容器内调试和管理的常用方式",
    "kubectl port-forward": "将本地端口映射到 Pod 端口，用于本地访问集群中的服务。是开发和调试阶段访问集群服务的便捷方式",
    "kubectl scale": "调整 Deployment、ReplicaSet 等资源的副本数量。支持手动扩缩容，是应对负载变化的基础操作",
    "kubectl rollout": "管理 Deployment 的滚动更新。支持查看状态、暂停、恢复和回滚，是应用发布管理的核心命令",
    "kubectl config": "管理 kubectl 的配置文件（kubeconfig）。支持切换上下文、设置集群和用户信息，是多集群管理的基础",
    "pip install": "从 PyPI 或其他仓库安装 Python 包。支持指定版本、从 requirements 文件批量安装、升级等操作",
    "pip uninstall": "卸载已安装的 Python 包。支持自动确认和从 requirements 文件批量卸载",
    "pip list": "列出当前环境中已安装的 Python 包及其版本。支持显示可更新的包和格式化输出",
    "pip freeze": "以 requirements 格式输出已安装的包列表。常用于生成项目的依赖锁定文件",
    "npm install": "安装 Node.js 项目的依赖包。支持本地安装、全局安装、开发依赖、精确版本锁定等",
    "npm run": "执行 package.json 中 scripts 定义的命令。是运行项目脚本（如构建、测试、启动）的标准方式",
    "npm publish": "将当前包发布到 npm 仓库。需要先登录并确保版本号更新，是分享 Node.js 模块的核心操作",
    "npm update": "更新项目的依赖包到最新版本。支持指定包名、全局更新和深度检查",
    "redis-cli": "Redis 命令行客户端，用于连接 Redis 服务器并执行各种数据操作。支持交互模式和批量命令执行",
    "redis set": "设置键值对到 Redis 数据库。支持设置过期时间、条件设置（NX/XX）等选项，是最基础的数据存储操作",
    "redis get": "获取指定键对应的值。如果键不存在返回 nil，是最常用的数据读取操作",
    "redis del": "删除一个或多个键。支持批量删除和按模式删除，是数据清理的主要方式",
    "redis expire": "为已存在的键设置过期时间（秒）。过期后键自动删除，是实现缓存和临时数据的核心机制",
    "mysql": "MySQL 命令行客户端，用于连接数据库服务器并执行 SQL 语句。支持交互式和批处理模式",
    "mysqldump": "MySQL 数据库备份工具，将数据库或表导出为 SQL 脚本。支持完整备份、增量备份和特定表备份",
    "mysqladmin": "MySQL 管理工具，用于执行管理操作如创建数据库、查看状态、关闭服务器等",
    "psql": "PostgreSQL 命令行客户端，支持交互式查询、脚本执行和元数据查看。是 PostgreSQL 管理的主要工具",
    "pg_dump": "PostgreSQL 数据库备份工具，支持多种导出格式（SQL、自定义、目录、tar）。是数据迁移和备份的标准工具",
    "nginx": "Nginx Web 服务器和反向代理。支持启动、停止、重载配置、测试配置等操作",
    "nginx config": "管理 Nginx 配置文件。支持语法测试、重载配置、查看完整配置，是 Nginx 运维的核心操作",
    "systemctl": "systemd 系统和服务管理器。用于控制 systemd 系统和服务管理器，支持启动、停止、重启、查看状态等",
    "journalctl": "查看 systemd 日志。支持按服务、时间、优先级筛选，是 Linux 系统日志分析的主要工具",
    "ssh-keygen": "生成、管理和转换 SSH 认证密钥对。支持多种密钥类型和位数，是安全远程访问的基础",
    "curl api": "使用 curl 调用 REST API。支持各种 HTTP 方法、请求头、请求体和认证，是 API 测试和集成的常用方式",
    "tar compress": "创建压缩归档文件。支持 gzip、bzip2、xz 等多种压缩算法，是文件打包和备份的标准工具",
    "tar extract": "解压归档文件。支持自动检测压缩格式和指定解压目录，是软件分发和数据恢复的基础",
    "chmod permission": "修改文件和目录的访问权限。通过数字或符号模式控制用户、组和其他人的读、写、执行权限",
    "chown owner": "修改文件和目录的所有者和所属组。用于调整文件归属和解决权限问题",
    "find search": "在目录树中搜索文件。支持按名称、类型、大小、时间、权限等多种条件组合筛选",
    "grep search": "文本搜索工具，使用正则表达式匹配行。支持递归搜索、上下文显示、多模式匹配，是日志分析的核心",
    "sed edit": "流编辑器，用于对文本进行过滤和转换。支持替换、删除、插入等操作，常用于脚本中的文本处理",
    "awk process": "文本处理工具，按列处理结构化文本。支持数学运算、条件判断、格式化输出，是数据处理的强大工具",
    "sort lines": "对文本行进行排序。支持按字典序、数值、月份等多种方式排序，以及去重和反向排序",
    "uniq filter": "过滤相邻的重复行。通常与 sort 配合使用进行全局去重统计，支持计数和显示唯一行",
    "wc count": "统计文件的行数、字数和字节数。是文本文件基本信息查看的快捷工具",
    "head tail": "查看文件的开头或结尾部分。支持指定行数或字节数，常用于查看日志文件的最新内容",
    "less more": "分页查看大文件内容。支持前后翻页、搜索、跳转，是查看大日志文件的首选工具",
    "vim edit": "强大的文本编辑器。支持多种模式、语法高亮、宏录制、插件扩展，是程序员最常用的编辑器之一",
    "nano edit": "简单易用的文本编辑器。界面底部显示快捷键，适合新手和简单编辑任务",
    "cat view": "显示文件内容。支持合并多个文件、添加行号、显示特殊字符，适合查看小文件",
    "echo print": "输出文本到标准输出或文件。支持转义字符、变量展开和重定向，是脚本中最基础的输出命令",
    "printf format": "格式化输出文本。支持 C 语言风格的格式说明符，提供更精确的输出控制",
    "read input": "从标准输入读取用户输入。支持提示信息、超时、静默模式，是交互式脚本的基础",
    "source execute": "在当前 shell 环境中执行脚本。使脚本中的变量和函数在当前环境生效，区别于直接执行脚本",
    "export variable": "设置环境变量并导出到子进程。是配置系统环境和应用参数的主要方式",
    "alias shortcut": "创建命令别名。用于简化长命令或设置默认选项，提高命令行效率",
    "history commands": "显示命令历史记录。支持搜索、执行历史命令和清除历史，是命令行效率提升的工具",
    "crontab schedule": "管理定时任务。支持按分钟、小时、日、月、星期设置周期性执行的任务",
    "at schedule": "安排一次性任务在指定时间执行。支持绝对时间和相对时间，适合延迟执行和定时任务",
    "nohup background": "使命令忽略挂起信号并在后台运行。配合 & 使用，确保用户退出后命令继续执行",
    "bg fg jobs": "管理后台作业。支持将作业切换到后台/前台执行，查看当前会话的所有作业状态",
    "trap signal": "捕获和处理信号。用于在脚本中优雅地处理中断、终止等信号，执行清理操作",
    "wait process": "等待后台进程完成。支持等待特定进程或所有进程，并获取退出状态",
    "sleep pause": "暂停执行指定时间。支持秒、分钟、小时、天等单位，用于脚本中的延时和定时",
    "date time": "显示或设置系统日期和时间。支持多种格式输出和日期计算，是时间处理的基础命令",
    "cal calendar": "显示日历。支持指定月份和年份，以及显示全年日历",
    "uptime system": "显示系统运行时间和负载。包括当前时间、运行时长、登录用户数和系统平均负载",
    "who users": "显示当前登录的用户信息。包括用户名、终端、登录时间和来源地址",
    "w activity": "显示当前登录用户及其正在执行的操作。比 who 提供更详细的活动信息",
    "last login": "显示用户最近登录记录。从 wtmp 日志文件中读取，支持按用户和终端筛选",
    "df disk": "显示文件系统的磁盘空间使用情况。包括总容量、已用、可用和使用百分比",
    "du usage": "显示目录或文件的磁盘使用量。支持汇总和 human-readable 格式，是查找大文件的工具",
    "free memory": "显示系统内存使用情况。包括物理内存和交换空间的总量、已用、空闲和缓存",
    "top processes": "实时显示系统进程和资源使用情况。支持交互式排序和操作，是系统监控的主要工具",
    "htop processes": "增强版 top，提供彩色界面和更多交互功能。支持鼠标操作和进程树显示",
    "vmstat system": "报告虚拟内存统计信息。包括进程、内存、分页、块 IO、陷阱和 CPU 活动",
    "iostat io": "报告 CPU 和 IO 统计信息。用于分析磁盘 IO 性能和瓶颈",
    "netstat network": "显示网络连接、路由表、接口统计等信息。是网络诊断和监控的经典工具",
    "ss sockets": "查看套接字统计信息。比 netstat 更快更强大，是查看网络连接的首选工具",
    "lsof files": "列出打开的文件。在 Linux 中一切皆文件，此命令可查看进程打开的网络连接、设备等",
    "ping network": "测试与目标主机的网络连通性。发送 ICMP 回显请求并等待响应，测量延迟和丢包率",
    "traceroute path": "显示数据包到目标主机的路由路径。用于网络故障定位和路径分析",
    "nslookup dns": "查询 DNS 记录。支持查询 A、MX、NS、TXT 等各种 DNS 记录类型",
    "dig dns": "强大的 DNS 查询工具。提供详细的 DNS 响应信息，是 DNS 调试的标准工具",
    "curl download": "下载文件或数据。支持断点续传、限速、跟随重定向，是命令行下载的常用工具",
    "wget download": "非交互式下载工具。支持递归下载、后台下载、镜像网站，适合批量下载任务",
    "scp transfer": "安全复制文件到远程主机。基于 SSH 协议加密传输，支持递归复制和限速",
    "rsync sync": "高效文件同步工具。支持增量传输、压缩、删除目标多余文件，是备份和镜像的首选",
    "sftp transfer": "安全文件传输协议客户端。提供交互式文件传输会话，支持上传、下载和目录操作",
    "ftp transfer": "文件传输协议客户端。用于与 FTP 服务器交互，支持上传、下载和目录管理",
    "telnet connect": "测试与远程主机的端口连接。常用于诊断服务是否可访问，明文传输不安全",
    "nc netcat": "网络瑞士军刀。支持端口扫描、监听、数据传输，是网络调试的万能工具",
    "ip address": "显示和管理网络接口及地址。替代 ifconfig，支持 IP 地址、路由、邻居表管理",
    "ip route": "显示和管理路由表。支持添加、删除、修改路由条目，是网络配置的核心命令",
    "ip link": "显示和管理网络接口。支持启用/禁用接口、修改 MTU 等链路层操作",
    "ifconfig interface": "配置网络接口（传统工具）。显示和设置 IP 地址、掩码、广播等接口参数",
    "route table": "显示和管理 IP 路由表（传统工具）。查看和修改内核路由表条目",
    "hostname name": "显示或设置系统主机名。主机名用于网络标识和日志记录",
    "iptables firewall": "配置 IPv4 包过滤规则。支持表、链、规则的增删改查，是 Linux 防火墙的核心",
    "ufw firewall": "简化的防火墙管理工具。提供易于使用的接口来管理 iptables 规则",
    "firewall-cmd firewall": "firewalld 的动态防火墙管理工具。支持区域、服务和富规则配置",
    "openssl crypto": "密码学工具包。支持证书生成、加密解密、SSL/TLS 测试等安全操作",
    "ssh connect": "安全远程登录。提供加密的终端会话，是 Linux 服务器远程管理的主要方式",
    "ssh-copy-id auth": "将 SSH 公钥复制到远程服务器。实现免密码登录，简化远程管理",
    "tmux terminal": "终端复用器。支持多个会话、窗口和面板，保持会话在断开连接后继续运行",
    "screen terminal": "终端复用器（传统工具）。支持会话保持和多窗口，是远程长时间任务的工具",
    "tree directory": "以树状结构显示目录内容。直观展示目录层次，支持限制深度和过滤",
    "locate search": "快速查找文件。基于预建的数据库，比 find 更快但可能不包含最新文件",
    "updatedb index": "更新 locate 的数据库。通常由定时任务自动执行，也可手动更新",
    "watch repeat": "定期执行命令并全屏显示输出。用于实时监控命令输出变化",
    "xargs execute": "从标准输入构建并执行命令。将输入转换为命令参数，支持批量处理",
    "tee output": "同时输出到标准输出和文件。用于查看输出同时保存到文件，支持追加模式",
    "script record": "记录终端会话到文件。捕获所有输入输出，用于文档记录和审计",
    "tty terminal": "显示当前终端设备文件名。用于脚本中识别当前终端",
    "stty settings": "显示和修改终端行设置。控制回显、行缓冲、特殊字符等终端行为",
    "clear screen": "清除终端屏幕。将光标移动到左上角，不清除滚动缓冲区",
    "reset terminal": "重置终端状态。恢复终端到初始状态，解决终端显示异常问题",
    "exit logout": "退出当前 shell 会话。可指定退出状态码，是脚本结束的标准方式",
    "logout session": "退出登录 shell。与 exit 类似，但仅在登录 shell 中有效",
    "su switch": "切换用户身份。不指定用户则切换到 root，需要目标用户的密码",
    "sudo elevate": "以超级用户权限执行命令。需要当前用户在 sudoers 列表中，支持配置免密码",
    "passwd password": "修改用户密码。支持设置密码过期策略和锁定账户",
    "useradd create": "创建新用户账户。支持设置主目录、shell、用户组等属性",
    "usermod modify": "修改用户账户属性。支持更改用户名、主目录、用户组、shell 等",
    "userdel delete": "删除用户账户。可选择是否删除用户主目录和邮件池",
    "groupadd create": "创建新用户组。用于组织用户和设置组权限",
    "groupmod modify": "修改用户组属性。支持更改组名和 GID",
    "groupdel delete": "删除用户组。不能删除用户的主组",
    "chpasswd batch": "批量更新用户密码。从标准输入读取用户名:密码格式数据",
    "id identity": "显示用户和组的 ID 信息。包括 UID、GID 和所属组列表",
    "groups membership": "显示用户所属的组。不指定用户则显示当前用户的组",
    "whoami current": "显示当前用户名。是获取当前身份的最简单方式",
    "logname login": "显示登录用户名。与 whoami 不同，显示最初登录的用户",
    "users loggedin": "显示当前登录的用户名列表。简单列出所有登录用户",
    "write message": "向其他用户终端发送消息。用于用户间即时通信",
    "wall broadcast": "向所有登录用户广播消息。用于系统通知和紧急公告",
    "mesg control": "控制其他用户是否可向你发送消息。启用或禁用 write 消息接收",
    "uname system": "显示系统信息。包括内核名称、主机名、内核版本、机器硬件名等",
    "hostnamectl system": "查看和修改主机名及相关设置。支持静态、瞬态和灵活主机名",
    "lsb_release distro": "显示 Linux 发行版信息。包括 ID、描述、发布号和代号",
    "cat proc": "查看 /proc 文件系统中的系统信息。/proc 是虚拟文件系统，提供内核和进程信息",
    "sysctl kernel": "运行时查看和修改内核参数。支持临时修改和永久配置",
    "dmesg boot": "查看内核环形缓冲区消息。包括启动信息和硬件检测日志",
    "lspci hardware": "列出所有 PCI 设备。用于查看显卡、网卡等硬件信息",
    "lsusb hardware": "列出所有 USB 设备。用于查看连接的 USB 设备和其属性",
    "lsblk block": "列出块设备信息。显示硬盘、分区、挂载点等存储设备层次",
    "fdisk partition": "分区表管理工具。支持查看、创建、删除、修改分区，需小心使用",
    "parted partition": "高级分区工具。支持 GPT 和 MBR，可调整分区大小",
    "mkfs filesystem": "创建文件系统。在分区上格式化指定类型的文件系统",
    "fsck check": "检查和修复文件系统。应在卸载的文件系统上运行，可能修复错误",
    "mount attach": "挂载文件系统到目录。将存储设备或远程文件系统连接到目录树",
    "umount detach": "卸载文件系统。断开存储设备与目录树的连接，需确保无进程使用",
    "df space": "显示文件系统磁盘空间使用。包括总容量、已用、可用和使用百分比",
    "du size": "显示目录或文件的磁盘使用量。支持汇总和 human-readable 格式",
    "sync flush": "将缓存数据写入磁盘。确保所有挂起的磁盘写入完成，防止数据丢失",
    "swapon swap": "启用交换空间。将交换分区或文件添加到系统的虚拟内存",
    "swapoff swap": "禁用交换空间。从系统中移除交换分区或文件",
    "mkswap create": "创建交换空间。在分区或文件上设置交换区域签名",
    "dd copy": "底层数据复制和转换。支持按块复制、格式转换，功能强大但需谨慎",
    "fallocate create": "快速创建预分配的文件。比 dd 更快创建大文件，用于测试和交换文件",
    "truncate resize": "缩小或扩展文件大小。支持指定大小和参考文件",
    "stat info": "显示文件或文件系统的详细状态。包括大小、权限、时间戳等元数据",
    "touch create": "创建空文件或更新文件时间戳。是创建标记文件和更新修改时间的常用命令",
    "ln link": "创建文件链接。支持硬链接（同一文件系统）和符号链接（跨文件系统）",
    "readlink resolve": "解析符号链接的目标路径。显示符号链接指向的实际文件",
    "realpath resolve": "显示文件的绝对路径。解析所有符号链接和相对路径",
    "dirname path": "提取路径中的目录部分。从完整路径中分离出父目录",
    "basename path": "提取路径中的文件名部分。从完整路径中分离出文件名称",
    "mktemp create": "创建临时文件或目录。生成唯一的临时名称，支持指定模板和目录",
    "tempfile create": "创建临时文件（传统工具）。生成唯一名称的临时文件",
    "install copy": "复制文件并设置权限。类似 cp 但支持设置所有者、组和权限",
    "cpio archive": "创建和提取归档文件。支持多种格式，常与 find 配合使用",
    "ar archive": "创建、修改和提取归档文件。主要用于静态库（.a 文件）管理",
    "gzip compress": "使用 Lempel-Ziv 算法压缩文件。压缩率高，是 Linux 标准的压缩工具",
    "gunzip decompress": "解压 gzip 压缩的文件。恢复原始文件并删除 .gz 文件",
    "bzip2 compress": "使用 Burrows-Wheeler 算法压缩文件。通常比 gzip 压缩率更高但速度较慢",
    "bunzip2 decompress": "解压 bzip2 压缩的文件。恢复原始文件并删除 .bz2 文件",
    "xz compress": "使用 LZMA 算法压缩文件。提供极高的压缩率，适合大文件",
    "unxz decompress": "解压 xz 压缩的文件。恢复原始文件并删除 .xz 文件",
    "zip archive": "创建 zip 格式的压缩归档。跨平台兼容性好，适合 Windows 交换",
    "unzip extract": "解压 zip 格式的归档文件。支持列出内容、选择性提取和测试",
    "rar archive": "创建 rar 格式的压缩归档。专有格式，压缩率高",
    "unrar extract": "解压 rar 格式的归档文件。支持列出内容和选择性提取",
    "7z archive": "7-Zip 压缩工具。支持多种格式，提供高压缩率",
    "compress legacy": "使用 LZW 算法压缩文件（传统 Unix 工具）。生成 .Z 文件",
    "uncompress legacy": "解压 .Z 格式的压缩文件。传统的 Unix 解压工具",
    "lzma compress": "使用 LZMA 算法压缩文件。xz 格式的前身",
    "lzop compress": "快速压缩工具。注重压缩速度而非压缩率",
    "zstd compress": "Facebook 开发的高速压缩工具。提供优秀的压缩速度和比率平衡",
    "pigz parallel": "并行的 gzip 实现。利用多核 CPU 加速压缩",
    "pbzip2 parallel": "并行的 bzip2 实现。利用多核 CPU 加速压缩",
    "pxz parallel": "并行的 xz 实现。利用多核 CPU 加速压缩",
    "split divide": "将大文件分割成小块。便于存储和传输到有限制的环境中",
    "csplit context": "按上下文分割文件。根据模式匹配分割文件，适合结构化文本",
    "paste merge": "合并文件的行。支持并行合并和指定分隔符",
    "join relate": "根据共同字段连接两个文件的行。类似 SQL 的 JOIN 操作",
    "comm compare": "比较两个已排序文件的行。显示仅文件1、仅文件2和共有的行",
    "diff compare": "比较文件差异。显示行级别的差异，支持多种输出格式",
    "patch apply": "应用 diff 生成的补丁文件。将差异应用到原始文件",
    "sdiff sidebyside": "并排比较两个文件。直观显示两个文件的差异",
    "vimdiff compare": "使用 Vim 进行可视化差异比较。在分屏中显示文件差异并支持合并",
    "cmp binary": "逐字节比较两个文件。用于二进制文件比较，显示第一个差异位置",
    "sum checksum": "计算文件的校验和。传统工具，使用简单算法",
    "cksum checksum": "计算文件的 CRC 校验和。提供 CRC32 和字节数",
    "md5sum hash": "计算 MD5 哈希值。广泛用于文件完整性校验，但不适合安全用途",
    "sha1sum hash": "计算 SHA-1 哈希值。比 MD5 更安全，但已被证明有碰撞风险",
    "sha256sum hash": "计算 SHA-256 哈希值。目前推荐的安全哈希算法，适合加密用途",
    "sha512sum hash": "计算 SHA-512 哈希值。提供最高级别的安全哈希",
    "b2sum hash": "计算 BLAKE2 哈希值。现代快速安全哈希算法",
    "base64 encode": "Base64 编码和解码。用于二进制数据的文本表示",
    "uuencode encode": "uuencode 编码（传统工具）。用于二进制数据的邮件传输",
    "uudecode decode": "uuencode 解码。恢复 uuencode 编码的数据",
    "hexdump binary": "以十六进制显示文件内容。用于查看二进制文件",
    "od dump": "以指定格式显示文件内容。支持八进制、十六进制、字符等多种格式",
    "strings text": "从二进制文件中提取可打印字符串。用于查看二进制文件中的文本",
    "file type": "识别文件类型。通过文件头和魔法数字判断文件格式",
    "stat format": "以指定格式显示文件状态。支持自定义输出格式字符串",
    "chattr attributes": "修改 Linux 文件系统扩展属性。支持设置不可修改等高级属性",
    "lsattr attributes": "显示 Linux 文件系统扩展属性。查看文件的特殊属性设置",
    "getfacl acl": "获取文件的访问控制列表。显示超出传统权限的细粒度访问控制",
    "setfacl acl": "设置文件的访问控制列表。配置细粒度的文件访问权限",
    "attr extended": "管理文件扩展属性。支持用户定义的文件元数据",
    "getfattr extended": "获取文件扩展属性。显示用户定义的文件元数据",
    "setfattr extended": "设置文件扩展属性。添加用户定义的文件元数据",
    "rename batch": "批量重命名文件。支持复杂的重命名规则和模式",
    "shred secure": "安全删除文件。多次覆盖文件内容，防止数据恢复",
    "wipe secure": "安全擦除文件。彻底删除文件使其难以恢复",
    "scrub secure": "数据清理工具。按照特定模式覆盖数据",
    "mkfifo pipe": "创建命名管道（FIFO）。用于不相关进程间的通信",
    "mknod device": "创建特殊文件。用于创建设备文件或命名管道",
    "mountpoint check": "检查目录是否是挂载点。用于脚本中的挂载验证",
    "findmnt list": "列出已挂载的文件系统。以树状结构显示挂载信息",
    "blkid identify": "识别块设备属性。显示 UUID、文件系统类型等信息",
    "e2label label": "查看或设置 ext2/3/4 文件系统标签。用于标识文件系统",
    "tune2fs tune": "调整 ext2/3/4 文件系统参数。修改文件系统的可调参数",
    "resize2fs resize": "调整 ext2/3/4 文件系统大小。通常先调整分区再调整文件系统",
    "xfs_growfs resize": "扩展 XFS 文件系统。XFS 支持在线扩展但不支持收缩",
    "btrfs filesystem": "管理 Btrfs 文件系统。支持高级功能如快照和子卷",
    "zfs filesystem": "管理 ZFS 文件系统。支持高级功能如快照、压缩和重复数据删除",
    "pvcreate prepare": "初始化物理卷。为 LVM 准备物理存储设备",
    "vgcreate create": "创建卷组。将物理卷组合成存储池",
    "lvcreate create": "创建逻辑卷。从卷组中分配逻辑存储",
    "lvextend extend": "扩展逻辑卷大小。增加逻辑卷的可用空间",
    "lvreduce reduce": "缩小逻辑卷大小。减少逻辑卷的可用空间",
    "lvremove remove": "删除逻辑卷。释放逻辑卷占用的空间",
    "lvdisplay display": "显示逻辑卷信息。查看逻辑卷的详细属性",
    "vgextend extend": "扩展卷组。向卷组添加新的物理卷",
    "vgreduce reduce": "缩小卷组。从卷组中移除物理卷",
    "vgremove remove": "删除卷组。释放卷组及其逻辑卷",
    "vgdisplay display": "显示卷组信息。查看卷组的详细属性",
    "pvs summary": "显示物理卷摘要。简要列出所有物理卷",
    "vgs summary": "显示卷组摘要。简要列出所有卷组",
    "lvs summary": "显示逻辑卷摘要。简要列出所有逻辑卷",
    "dmsetup device": "管理设备映射。底层 LVM 和加密设备管理",
    "cryptsetup encrypt": "管理加密卷。创建和打开 LUKS 加密设备",
    "losetup loop": "设置和控制循环设备。将文件作为块设备使用",
    "kpartx partitions": "为设备分区创建设备映射。用于循环设备分区访问",
    "partprobe notify": "通知内核分区表变更。在不重启的情况下重新读取分区表",
    "blockdev control": "控制块设备。设置和查询块设备参数",
    "hdparm disk": "获取和设置 SATA/IDE 设备参数。用于硬盘性能调优",
    "sdparm disk": "获取和设置 SCSI/SATA 设备参数。SCSI 设备的 hdparm 替代",
    "smartctl health": "查看硬盘 SMART 健康信息。监控硬盘健康状态和预测故障",
    "badblocks check": "检查坏块。扫描存储设备的坏扇区",
    "hdparm secure": "执行安全擦除。使用硬盘内置功能安全删除数据",
    "nvme cli": "管理 NVMe 设备。现代 SSD 的管理工具",
    "sg_scan scsi": "扫描 SCSI 设备。检测新连接的 SCSI/SATA 设备",
    "sg_inq inquiry": "查询 SCSI 设备信息。获取 SCSI 设备的详细信息",
    "lsscsi list": "列出 SCSI/SATA 设备。显示所有 SCSI 和 SATA 存储设备",
    "sas2ircu raid": "管理 SAS RAID 控制器。LSI SAS 控制器的配置工具",
    "MegaCli raid": "管理 LSI MegaRAID 控制器。企业级 RAID 管理工具",
    "ssacli raid": "管理 HPE Smart Array 控制器。HPE 服务器的 RAID 管理",
    "hpacucli raid": "管理 HPE Smart Array 控制器（旧版）。HPE 服务器的传统 RAID 管理",
    "storcli raid": "管理 Broadcom RAID 控制器。现代 RAID 管理工具",
    "sas3ircu raid": "管理 SAS3 RAID 控制器。新一代 SAS 控制器配置",
    "ipmitool bmc": "管理 IPMI 设备。远程服务器硬件管理接口",
    "dmidecode hardware": "从 DMI 解码硬件信息。显示 BIOS、系统、主板、处理器等信息",
    "smbios hardware": "显示 SMBIOS 信息。系统管理 BIOS 信息查看",
    "lshw hardware": "列出硬件配置。详细的硬件信息收集工具",
    "inxi info": "系统信息脚本。以结构化格式显示系统硬件和软件信息",
    "hardinfo benchmark": "系统信息和基准测试。图形化的硬件信息和性能测试",
    "sysbench benchmark": "模块化基准测试。测试 CPU、内存、IO、线程和数据库性能",
    "phoronix benchmark": "全面的基准测试套件。自动化测试和结果比较",
    "stress test": "系统压力测试。对系统进行 CPU、内存、IO 压力测试",
    "stress-ng test": "高级系统压力测试。stress 的增强版，更多测试选项",
    "fio benchmark": "灵活的 IO 测试器。全面的存储性能测试工具",
    "ioping latency": "测量 IO 延迟。类似于 ping 但用于存储 IO",
    "bonnie benchmark": "文件系统性能测试。经典的文件系统基准测试",
    "iozone benchmark": "文件系统基准测试。全面的文件系统性能测试",
    "lmbench benchmark": "系统性能测试套件。测量各种系统调用和操作的性能",
    "perf analyze": "Linux 性能分析工具。内核自带的性能分析框架",
    "gprof profile": "GNU 性能分析器。编译时插入的性能分析",
    "valgrind debug": "内存调试和性能分析。检测内存泄漏和错误",
    "strace trace": "跟踪系统调用。显示进程的系统调用和信号",
    "ltrace trace": "跟踪库调用。显示进程的动态库调用",
    "ptrace debug": "进程跟踪接口。调试器使用的底层进程跟踪",
    "gdb debug": "GNU 调试器。强大的程序调试工具",
    "lldb debug": "LLVM 调试器。现代的调试器替代 gdb",
    "objdump binary": "显示目标文件信息。反汇编和查看二进制文件",
    "readelf binary": "显示 ELF 文件信息。详细的 ELF 格式分析",
    "nm symbols": "列出目标文件的符号。显示函数和变量符号表",
    "strip symbols": "去除目标文件的符号。减小文件大小和保护代码",
    "ar archive": "创建、修改和提取归档。静态库管理工具",
    "ranlib index": "生成归档的索引。加速静态库的链接",
    "ld linker": "GNU 链接器。将目标文件链接成可执行文件",
    "ldd dependencies": "显示共享库依赖。列出可执行文件依赖的动态库",
    "ldconfig cache": "更新共享库缓存。配置动态链接器运行时库搜索路径",
    "pkg-config query": "查询已安装库的信息。获取编译和链接参数",
    "make build": "GNU 构建工具。根据 Makefile 自动化构建过程",
    "cmake build": "跨平台构建系统。生成平台相关的构建文件",
    "meson build": "现代构建系统。快速和用户友好的构建工具",
    "ninja build": "快速构建系统。注重速度的构建工具",
    "autoconf configure": "生成配置脚本。自动检测系统特性",
    "automake makefile": "生成 Makefile.in。根据 configure.ac 生成模板",
    "libtool library": "通用库支持脚本。简化跨平台库创建",
    "configure prepare": "配置源码编译。检测系统特性并生成 Makefile",
    "checkinstall package": "从源码创建包。编译安装并创建可卸载的包",
    "dpkg-deb package": "Debian 包工具。创建和解压 .deb 包",
    "rpm package": "RPM 包管理器。创建、查询、验证 RPM 包",
    "alien convert": "转换包格式。在不同 Linux 包格式间转换",
    "fpm package": "高效的包构建工具。支持多种包格式",
    "rpmbuild build": "构建 RPM 包。从 spec 文件创建 RPM 包",
    "mock build": "干净的 RPM 构建环境。在 chroot 中构建包",
    "pbuilder build": "Debian 包构建环境。干净的构建 chroot",
    "sbuild build": "Debian 包构建工具。支持多种构建环境",
    "lintian check": "Debian 包检查。检查包是否符合 Debian 政策",
    "rpmlint check": "RPM 包检查。检查 RPM 包的常见错误",
    "piuparts test": "Debian 包安装测试。测试包的安装、升级、删除",
    "autopkgtest test": "Debian 自动包测试。包的自动测试框架",
    "debuild build": "构建 Debian 包。自动化的 Debian 包构建",
    "debsign sign": "签名 Debian 包。对 Debian 包进行数字签名",
    "dput upload": "上传 Debian 包。将包上传到仓库",
    "dupload upload": "上传 Debian 包（旧版）。传统的包上传工具",
    "reprepro manage": "Debian 仓库管理。管理本地 Debian 包仓库",
    "aptly manage": "Debian 仓库管理。现代 Debian 包仓库管理",
    "createrepo create": "创建 YUM 仓库。生成 RPM 仓库元数据",
    "yumdownloader download": "从 YUM 仓库下载 RPM。不安装只下载包",
    "repoquery query": "查询 YUM 仓库。查询包信息和依赖关系",
    "yum-builddep dependencies": "安装构建依赖。安装 RPM 包的构建依赖",
    "mockchain chain": "批量构建 RPM。连续构建多个相互依赖的包",
    "module-build-service build": "Fedora 模块构建。构建 Fedora 模块化包",
    "fedpkg package": "Fedora 包工具。Fedora 包的构建和提交",
    "obs build": "Open Build Service。跨发行版的包构建服务",
    "osc build": "Open Build Service 客户端。与 OBS 交互的命令行工具",
    "build compare": "比较构建结果。验证构建的可重复性",
    "diffoscope compare": "深度比较文件。递归比较文件和目录",
    "disorderfs fuzz": "非确定性文件系统。测试构建的可重复性",
    "strip-nondeterminism clean": "去除构建中的非确定性。使构建结果可重复",
    "dh_make template": "创建 Debian 包模板。生成 Debian 包的初始文件",
    "debmake template": "创建 Debian 包模板。debmake 的模板生成",
    "git-buildpackage build": "从 Git 构建 Debian 包。整合 Git 和 Debian 包构建",
    "gbp build": "git-buildpackage 缩写。构建 Debian 包的快捷方式",
    "pbuilder create": "创建 pbuilder 环境。初始化 Debian 构建 chroot",
    "pbuilder update": "更新 pbuilder 环境。更新构建 chroot 的基础系统",
    "cowbuilder build": "Copy-on-write 构建。使用 COW 加速 pbuilder",
    "sbuild create": "创建 sbuild 环境。初始化 sbuild 构建环境",
    "schroot manage": "管理 chroot 环境。安全的 chroot 管理工具",
    "systemd-nspawn container": "轻量级容器。systemd 提供的容器工具",
    "machinectl machine": "管理 systemd 容器和 VM。systemd 的机器管理工具",
    "systemd-run service": "运行临时服务。在临时 scope 或 service 中运行命令",
    "systemctl service": "控制 systemd 服务。启动、停止、启用、查看服务状态",
    "journalctl logs": "查看 systemd 日志。查询和管理 systemd 日志",
    "loginctl session": "控制 systemd 登录。管理用户会话和座位",
    "timedatectl time": "控制系统时间和日期。设置时区、时间、NTP",
    "localectl locale": "控制系统本地化设置。设置语言和键盘布局",
    "hostnamectl hostname": "控制主机名。设置静态、瞬态和灵活主机名",
    "networkctl network": "控制 systemd-networkd。管理网络接口配置",
    "resolvectl dns": "控制 systemd-resolved。管理 DNS 解析配置",
    "systemd-analyze boot": "分析启动时间。显示启动过程各阶段耗时",
    "systemd-cgtop monitor": "监控控制组。显示 cgroup 资源使用 top",
    "systemd-cgls list": "列出控制组。显示 cgroup 层次结构",
    "busctl dbus": "控制 D-Bus。检查和操作 D-Bus 总线",
    "systemd-ask-password prompt": "请求密码。安全地请求用户输入密码",
    "systemd-tty-ask-password-agent agent": "密码代理。在 TTY 上处理密码请求",
    "systemd-inhibit inhibit": "阻止系统操作。延迟关机、睡眠等操作",
    "systemd-detect-virt detect": "检测虚拟化。识别运行环境的虚拟化类型",
    "systemd-delta config": "显示配置差异。显示覆盖和修改的配置",
    "systemd-escape escape": "转义字符串。为 systemd 单元名转义字符串",
    "systemd-path paths": "显示系统路径。显示各种系统目录路径",
    "systemd-resolve resolve": "解析 DNS。使用 systemd-resolved 解析域名",
    "systemd-mount mount": "挂载文件系统。使用 systemd 管理挂载",
    "systemd-umount unmount": "卸载文件系统。使用 systemd 管理卸载",
    "systemd-nspawn container": "运行容器。使用 systemd-nspawn 运行容器",
    "systemd-machine-id-setup machineid": "设置机器 ID。初始化 /etc/machine-id",
    "systemd-firstboot initial": "初始化系统。首次启动系统配置",
    "systemd-hwdb hardware": "管理硬件数据库。更新 udev 硬件数据库",
    "udevadm device": "管理 udev 设备。udev 管理工具",
    "systemd-sysusers users": "创建系统用户。根据配置创建系统用户",
    "systemd-tmpfiles tmpfiles": "管理临时文件。创建和清理临时文件",
    "systemd-networkd-wait-online wait": "等待网络就绪。等待网络连接建立",
    "systemd-notify notify": "通知 systemd。向 systemd 发送状态通知",
    "systemd-cat log": "记录到日志。将输出记录到 systemd 日志",
    "systemd-stdio-bridge bridge": "D-Bus 桥接。stdio 到 D-Bus 的桥接",
    "systemd-journal-gatewayd gateway": "日志网关。提供 HTTP 日志访问接口",
    "systemd-journal-remote remote": "远程日志。接收远程 systemd 日志",
    "systemd-journal-upload upload": "上传日志。上传日志到远程服务器",
    "systemd-importd import": "导入容器和 VM。导入系统镜像服务",
    "systemd-machined machine": "机器管理服务。注册和管理机器",
    "systemd-portabled portable": "便携服务管理。管理便携系统服务",
    "systemd-hostnamed hostname": "主机名服务。动态主机名管理服务",
    "systemd-localed locale": "本地化服务。动态本地化设置服务",
    "systemd-timedated time": "时间服务。动态时间日期设置服务",
    "systemd-logind login": "登录管理。用户登录和会话管理",
    "systemd-networkd network": "网络管理。系统网络配置管理",
    "systemd-resolved dns": "DNS 解析。系统 DNS 解析服务",
    "systemd-timesyncd ntp": "时间同步。NTP 客户端服务",
    "systemd-udevd device": "设备管理。内核设备事件管理",
    "systemd-update-done update": "更新标记。标记系统更新完成",
    "systemd-vconsole-setup console": "虚拟控制台设置。配置虚拟控制台",
    "systemd-backlight backlight": "背光控制。管理设备背光",
    "systemd-rfkill rfkill": "RF 开关管理。管理射频设备开关",
    "systemd-growfs growfs": "自动扩展文件系统。启动时扩展根文件系统",
    "systemd-makefs makefs": "自动创建文件系统。启动时创建文件系统",
    "systemd-pstore pstore": "持久存储。管理平台持久存储",
    "systemd-bootchart bootchart": "启动图表。生成启动过程图表",
    "systemd-veritysetup verity": "完整性验证。设置 verity 完整性验证",
    "systemd-volatile-root volatile": "易失根目录。管理易失性根文件系统",
    "systemd-modules-load modules": "加载内核模块。根据配置加载模块",
    "systemd-random-seed random": "随机种子。保存和恢复随机种子",
    "systemd-remount-fs remount": "重新挂载文件系统。重新挂载根和启动文件系统",
    "systemd-socket-proxyd proxy": "套接字代理。套接字激活的代理",
    "systemd-sulogin-shell shell": "单用户 shell。系统维护模式 shell",
    "systemd-sysctl sysctl": "应用内核参数。启动时应用 sysctl 配置",
    "systemd-update-utmp utmp": "更新登录记录。维护 utmp/wtmp 登录记录",
    "systemd-user-sessions sessions": "用户会话控制。控制用户会话可用性",
    "systemd-ac-power power": "电源检测。检测交流电源状态",
    "systemd-activate socket": "套接字激活。测试套接字激活",
    "systemd-bus-proxy proxy": "D-Bus 代理。VFS D-Bus 代理",
    "systemd-coredump coredump": "核心转储。处理程序崩溃核心转储",
    "systemd-fsck fsck": "文件系统检查。启动时检查文件系统",
    "systemd-hibernate hibernate": "休眠。系统休眠恢复",
    "systemd-homed home": "用户主目录。可移动用户主目录管理",
    "systemd-oomd oom": "内存耗尽。用户空间 OOM 杀手",
    "systemd-repart partition": "分区。自动分区管理",
    "systemd-stub stub": "EFI stub。统一内核镜像 EFI stub",
    "systemd-sysext extension": "系统扩展。不可变系统的扩展",
    "systemd-xdg-autostart autostart": "自动启动。XDG 自动启动支持"
    }
}


def enhance_param(param_name, param_data):
    """增强参数定义"""
    if not isinstance(param_data, dict):
        param_data = {}

    # 如果已经有详细描述（超过20字），保留原值
    existing_desc = param_data.get('description', '')
    if len(existing_desc) >= 20 and ' ' in existing_desc:
        # 已有足够详细的描述，只确保 notes 不为空
        if not param_data.get('notes'):
            param_data['notes'] = get_default_notes(param_name, param_data)
        return param_data

    # 从知识库查找
    knowledge = PARAM_KNOWLEDGE.get(param_name)
    if knowledge:
        param_data['description'] = knowledge['description']
        if not param_data.get('example') or param_data.get('example') == param_name:
            param_data['example'] = knowledge['example']
        param_data['notes'] = knowledge['notes']
    else:
        # 通用增强
        if not param_data.get('description') or len(param_data.get('description', '')) < 10:
            param_data['description'] = f"{param_name}参数，用于指定命令操作的目标或配置"
        if not param_data.get('example') or param_data.get('example') == param_name:
            param_data['example'] = get_default_example(param_name)
        if not param_data.get('notes'):
            param_data['notes'] = get_default_notes(param_name, param_data)

    return param_data


def get_default_example(param_name):
    """获取默认示例值"""
    examples = {
        "目录": "/var/log",
        "文件": "/etc/config.yaml",
        "路径": "/usr/local/bin",
        "主机": "192.168.1.