# -*- coding: utf-8 -*-
"""
增强工具 - 批量完善所有模块的 commands.json
功能：
  1. 按照标准自动增强命令描述（深度）
  2. 完善参数注释
  3. 补充示例完整性
  4. 包含完整的参数知识库 (PARAM_KNOWLEDGE)

使用方法：python scripts/enhance_all.py
说明：
  - 预定义常见参数的详细描述、示例和备注
  - 批量应用参数知识库到所有模块
  - 自动补充缺失的参数信息

import json
import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

# 参数知识库
PARAM_KNOWLEDGE = {
    "目录": {"description": "目标目录的路径，可以是绝对路径（如 /var/log）或相对路径（如 ./logs）。用于指定命令操作的目标位置", "example": "/var/log/nginx", "notes": "可选。默认为当前目录。建议使用绝对路径避免歧义，相对路径基于当前工作目录解析"},
    "文件": {"description": "目标文件的路径，包含文件名和扩展名。用于指定命令操作的具体文件", "example": "/etc/nginx/nginx.conf", "notes": "可选。必须包含完整的文件名和扩展名。建议先确认文件存在性和读写权限"},
    "路径": {"description": "文件系统路径，可以是文件或目录的绝对路径或相对路径。用于定位命令操作的目标", "example": "/usr/local/bin", "notes": "可选。支持绝对路径和相对路径。包含空格的路径需用引号包裹"},
    "主机": {"description": "远程服务器的主机名或 IP 地址。用于指定网络连接的目标主机", "example": "192.168.1.100", "notes": "可选。默认 127.0.0.1(localhost)。支持 IPv4、IPv6 和域名"},
    "端口": {"description": "网络服务端口号，范围 1-65535。用于指定服务监听或连接的端口", "example": "8080", "notes": "可选。默认视服务而定。1-1023 为系统端口需 root 权限，1024-65535 为用户端口"},
    "用户名": {"description": "用于身份验证的用户标识名称。不同系统中可能有不同的命名规则限制", "example": "admin", "notes": "必填。通常只能包含字母、数字、下划线和连字符，长度限制视系统而定"},
    "密码": {"description": "用于身份验证的机密字符串。应包含大小写字母、数字和特殊字符以增强安全性", "example": "MyP@ssw0rd!2024", "notes": "必填。建议使用强密码（12位以上，包含多种字符类型）。避免在命令行中明文传输密码"},
    "URL": {"description": "统一资源定位符，用于指定网络资源的地址。支持 HTTP、HTTPS、Git 等协议", "example": "https://github.com/user/repo.git", "notes": "必填。必须包含协议头（如 https://）。私有仓库可能需要认证信息"},
    "仓库URL": {"description": "代码仓库的网络地址，支持 HTTPS、SSH、Git 等协议。用于克隆或推送代码", "example": "https://github.com/user/repo.git", "notes": "必填。HTTPS 需要用户名密码，SSH 需要配置密钥。建议使用 SSH 协议进行频繁操作"},
    "容器名称": {"description": "Docker 容器的唯一标识名称，用于后续管理操作（启动、停止、删除等）。只能包含字母、数字、下划线、连字符和点", "example": "myapp-web", "notes": "必填。同一主机上名称不能重复。建议使用 应用名-组件 格式，如 nginx-proxy、redis-cache"},
    "镜像名称": {"description": "Docker 镜像的名称，可包含命名空间、仓库名和标签。用于创建容器的基础模板", "example": "nginx:1.24-alpine", "notes": "必填。格式：[仓库/]镜像名[:标签]。建议使用具体版本标签，避免使用 latest 导致版本不可控"},
    "镜像": {"description": "Docker 镜像的名称，可包含命名空间、仓库名和标签。用于创建容器或执行操作", "example": "nginx:1.24-alpine", "notes": "必填。格式：[仓库/]镜像名[:标签]。本地不存在时会自动从仓库拉取"},
    "主机端口": {"description": "宿主机上暴露的端口号，外部请求通过此端口访问容器服务。将宿主机网络端口映射到容器内部", "example": "8080", "notes": "必填。范围 1-65535，小于 1024 需 root 权限。确保端口未被其他服务占用"},
    "容器端口": {"description": "容器内部应用实际监听的端口号。容器内应用绑定此端口提供服务", "example": "80", "notes": "必填。需与容器内应用实际监听端口一致。常见：Nginx 80、MySQL 3306、Redis 6379"},
    "主机路径": {"description": "宿主机上要挂载到容器的目录或文件绝对路径。用于实现容器数据的持久化存储", "example": "/data/nginx/logs", "notes": "必填。路径必须在宿主机上存在。建议使用绝对路径，避免相对路径解析歧义"},
    "容器路径": {"description": "容器内部的挂载目标路径，即容器内应用实际读写数据的位置", "example": "/var/log/nginx", "notes": "必填。需根据容器内应用的配置文件确认正确路径"},
    "网络名称": {"description": "Docker 网络的标识名称，用于容器间的网络通信和隔离。可以是 bridge、host、none 或自定义网络", "example": "myapp_network", "notes": "必填。自定义网络需先通过 docker network create 创建。同一网络的容器可通过名称互相访问"},
    "环境变量": {"description": "传递给容器内部应用的配置参数，以键值对形式设置。用于配置应用行为而无需修改镜像", "example": "MYSQL_ROOT_PASSWORD", "notes": "必填。变量名通常为大写字母和下划线。敏感信息建议使用 Docker Secrets 或挂载文件"},
    "变量值": {"description": "环境变量的具体取值，用于配置容器内应用的运行参数", "example": "mysecretpassword123", "notes": "必填。包含空格或特殊字符的值建议用引号包裹。敏感信息避免直接暴露在命令行"},
    "卷名": {"description": "Docker 数据卷的名称，用于持久化存储容器数据。与挂载目录不同，卷由 Docker 管理", "example": "mysql_data", "notes": "必填。卷不存在时会自动创建。使用 docker volume ls 查看已有卷，docker volume create 预创建"},
    "分支名": {"description": "Git 分支的名称标识，用于并行开发和版本管理。分支名应简洁描述功能或版本", "example": "feature/user-auth", "notes": "必填。只能包含字母、数字、下划线、连字符、点和斜杠。常用前缀：feature/、bugfix/、release/、hotfix/"},
    "提交信息": {"description": "描述代码变更内容的简短说明，用于版本历史记录和代码审查。应清晰说明做了什么和为什么", "example": "feat: add user authentication with JWT tokens", "notes": "必填。建议使用语义化提交规范：feat(新功能)、fix(修复)、docs(文档)、refactor(重构)。50字以内"},
    "标签名": {"description": "Git 标签的名称，用于标记特定的提交点（通常是版本发布）。标签分为轻量标签和附注标签", "example": "v1.2.0", "notes": "必填。建议使用语义化版本号格式：v主版本.次版本.修订号。如 v1.2.0、v2.0.0-beta.1"},
    "远程名": {"description": "远程仓库的本地别名，用于简化远程仓库的引用。默认远程仓库名为 origin", "example": "origin", "notes": "可选。默认为 origin。可通过 git remote -v 查看已配置的远程仓库"},
    "命名空间": {"description": "Kubernetes 中的逻辑隔离区域，用于将集群资源划分为多个虚拟集群。不同命名空间的资源相互隔离", "example": "production", "notes": "可选。默认 default。常用：default、kube-system、kube-public。生产环境建议按环境划分命名空间"},
    "Pod名称": {"description": "Kubernetes Pod 的唯一标识名称，由控制器（如 Deployment）自动或手动指定", "example": "nginx-deployment-7c4c7b5d9-x2v4p", "notes": "必填。可通过 kubectl get pods 查看。支持使用部分名称匹配，也可使用标签选择器"},
    "资源类型": {"description": "Kubernetes 资源对象的类型，用于指定要操作的集群资源类别", "example": "deployments", "notes": "必填。常用：pods、deployments、services、configmaps、secrets、ingress、nodes、jobs、cronjobs"},
    "Deployment名称": {"description": "Kubernetes Deployment 控制器的名称，用于管理 Pod 的副本数和滚动更新", "example": "nginx-deployment", "notes": "必填。Deployment 负责维护指定数量的 Pod 副本，支持滚动更新和回滚"},
    "Service名称": {"description": "Kubernetes Service 的名称，用于为一组 Pod 提供稳定的网络访问端点", "example": "nginx-service", "notes": "必填。Service 通过标签选择器将流量路由到匹配的 Pod，提供负载均衡"},
    "副本数": {"description": "Pod 的期望运行实例数量，Deployment 会自动调整实际运行的 Pod 数量以匹配此值", "example": "3", "notes": "必填。必须为正整数。建议生产环境至少 2 个副本以保证高可用，开发环境可 1 个"},
    "配置文件": {"description": "Kubernetes 资源定义文件的路径，通常为 YAML 或 JSON 格式。包含资源的完整配置声明", "example": "/k8s/deployment.yaml", "notes": "必填。支持 YAML 和 JSON 格式。建议将配置文件纳入版本控制，使用 kubectl apply 进行声明式管理"},
    "数据库名": {"description": "数据库实例的名称标识，用于区分同一数据库服务器上的不同数据库", "example": "myapp_production", "notes": "必填。命名通常只能包含字母、数字、下划线。创建后可通过 SHOW DATABASES 查看"},
    "表名": {"description": "关系型数据库中的表名称，用于组织和存储特定类型的数据记录", "example": "users", "notes": "必填。建议使用复数名词命名表名，如 users、orders、products。避免使用 SQL 保留字"},
    "列名": {"description": "数据库表中的字段名称，用于标识和访问特定的数据列", "example": "email", "notes": "必填。建议使用小写字母和下划线命名（snake_case），如 created_at、updated_at"},
    "查询条件": {"description": "用于筛选数据的条件表达式，支持比较运算符、逻辑运算符和模式匹配", "example": "age > 18 AND status = 'active'", "notes": "可选。支持 =、!=、>、<、>=、<=、LIKE、IN、BETWEEN 等运算符。字符串值需用引号包裹"},
    "key": {"description": "Redis 键名，用于唯一标识存储的数据。键是二进制安全的字符串", "example": "user:1001:profile", "notes": "必填。建议使用命名空间前缀组织键名，如 user:、session:、cache:。避免使用过长的键名"},
    "value": {"description": "Redis 键对应的存储值，可以是字符串、数字或二进制数据。最大可存储 512MB", "example": "{\"name\":\"张三\",\"age\":25}", "notes": "必填。字符串值包含空格需用引号包裹。复杂对象建议序列化为 JSON 存储"},
    "秒数": {"description": "以秒为单位的时间数值，用于设置键的过期时间或等待超时时间", "example": "3600", "notes": "必填。1 小时=3600 秒，1 天=86400 秒，7 天=604800 秒。过期后键会自动删除"},
    "包名": {"description": "软件包的名称标识，用于在包仓库中查找和安装特定的软件包", "example": "requests", "notes": "必填。名称区分大小写（视包管理器而定）。可通过搜索命令确认包名和可用版本"},
    "版本号": {"description": "软件包的具体版本标识，遵循语义化版本规范（主版本.次版本.修订号）", "example": "2.28.0", "notes": "必填。格式：主版本.次版本.修订号。不指定版本通常安装最新版，可能导致兼容性问题"},
    "选项": {"description": "命令的附加选项标志，用于修改命令的默认行为。多个选项可以组合使用", "example": "-la", "notes": "可选。常见选项：-l(长格式)、-a(显示隐藏文件)、-h(人类可读)、-r(递归)、-f(强制)"},
    "来源": {"description": "源文件或目录的路径，指定要复制、移动或传输的数据来源位置", "example": "/var/log/app.log", "notes": "必填。必须存在且有读取权限。支持通配符 * 和 ? 进行批量匹配"},
    "目标": {"description": "目标文件或目录的路径，指定数据复制、移动后的存放位置", "example": "/backup/logs/", "notes": "必填。目录不存在时部分命令会自动创建，文件存在时可能会被覆盖"},
    "模式": {"description": "权限模式设置，使用数字（如 755）或符号（如 u+x）表示。控制文件或目录的读、写、执行权限", "example": "755", "notes": "必填。数字模式：所有者-组-其他，每位 0-7（4读+2写+1执行）。符号模式：u(所有者)、g(组)、o(其他)、a(所有)"},
    "所有者": {"description": "文件或目录的新所有者用户名或 UID。用于更改资源的归属用户", "example": "www-data", "notes": "必填。必须是系统中存在的用户。只有 root 或具有 CAP_CHOWN 能力的用户可修改"},
    "组": {"description": "文件或目录的新所属组名或 GID。用于更改资源的归属组", "example": "developers", "notes": "可选。默认与所有者主组相同。必须是系统中存在的组"},
    "旧名称": {"description": "文件或目录的当前名称，指定要被重命名的目标", "example": "old_name.txt", "notes": "必填。必须是存在的文件或目录路径。支持相对路径和绝对路径"},
    "新名称": {"description": "文件或目录的新名称，指定重命名后的目标名称", "example": "new_name.txt", "notes": "必填。新名称不能已存在（除非强制覆盖）。建议在同一文件系统内操作以避免数据复制"},
    "用户": {"description": "系统用户账户的名称或 UID，用于指定命令操作的目标用户身份", "example": "admin", "notes": "必填。必须是系统中存在的用户。部分命令需要 root 权限才能指定其他用户"},
    "组名": {"description": "用户组的名称或 GID，用于组织用户和设置组权限", "example": "docker", "notes": "必填。必须是系统中存在的组。创建用户时可指定主组和附加组"},
    "服务名": {"description": "系统服务的名称标识，用于控制服务的启动、停止和状态查看", "example": "nginx", "notes": "必填。服务名通常对应 systemd 单元文件（如 nginx.service）。使用 systemctl list-units 查看可用服务"},
    "进程ID": {"description": "操作系统分配给运行进程的唯一数字标识符，用于精确指定目标进程", "example": "1234", "notes": "必填。必须是正整数。使用 ps、top 或 pgrep 查找进程 ID。小心不要误杀系统关键进程"},
    "信号": {"description": "发送给进程的控制信号，用于通知进程执行特定操作（如终止、重载配置）", "example": "SIGTERM", "notes": "可选。默认 SIGTERM(15)。常用：SIGHUP(1重载)、SIGINT(2中断)、SIGKILL(9强制终止)、SIGUSR1(10用户定义)"},
    "源": {"description": "数据或文件的来源位置，指定复制、移动或同步操作的起点", "example": "/data/source/", "notes": "必填。必须存在且有适当权限。支持本地路径和远程路径（rsync、scp 等）"},
    "目的": {"description": "数据或文件的目标位置，指定复制、移动或同步操作的终点", "example": "/backup/destination/", "notes": "必填。部分命令会自动创建不存在的目录。注意检查磁盘空间和写入权限"},
    "命令": {"description": "要在目标环境（如容器、远程主机）中执行的具体命令字符串", "example": "ls -la /var/log", "notes": "必填。命令会在目标环境的 shell 中执行。包含特殊字符时建议用引号包裹"},
    "时间": {"description": "指定操作发生的时间点或时间段，格式因命令而异", "example": "2024-01-15 14:30:00", "notes": "必填。常见格式：YYYY-MM-DD HH:MM:SS、ISO 8601、相对时间（如 now、1 hour ago）"},
    "数量": {"description": "指定操作涉及的项目数量或数值大小", "example": "100", "notes": "必填。必须为正整数。视上下文可能表示条数、字节数、秒数等"},
    "大小": {"description": "指定数据或文件的大小限制，单位可以是字节、KB、MB、GB 等", "example": "10M", "notes": "必填。常用单位：B(字节)、K(KB)、M(MB)、G(GB)、T(TB)。部分命令也支持 b(512字节块)"},
    "内容": {"description": "要写入文件或作为输入的文本数据", "example": "Hello, World!", "notes": "必填。包含特殊字符时需转义或用引号包裹。支持换行符 \\n 和制表符 \\t"},
    "字符串": {"description": "要在文本中搜索或替换的字符序列", "example": "error", "notes": "必填。区分大小写（除非指定忽略大小写选项）。支持正则表达式（视命令而定）"},
    "表达式": {"description": "用于匹配、计算或转换的模式或公式，支持正则或特定语法", "example": "s/old/new/g", "notes": "必填。语法因命令而异。sed 使用 s/old/new/flags，awk 使用模式{动作}，grep 使用正则表达式"},
    "键": {"description": "配置项、映射或字典中的标识符名称", "example": "server.host", "notes": "必填。格式视具体应用而定。点号表示嵌套配置，如 database.connections.max"},
    "值": {"description": "配置项、映射或字典中的具体数据", "example": "localhost", "notes": "必填。数据类型需与键的定义匹配。字符串值建议用引号包裹"},
    "域名": {"description": "互联网域名，用于标识网络上的资源位置", "example": "example.com", "notes": "必填。必须是有效的域名格式。支持子域名，如 api.example.com"},
    "IP地址": {"description": "互联网协议地址，用于唯一标识网络中的设备", "example": "192.168.1.1", "notes": "必填。支持 IPv4（如 192.168.1.1）和 IPv6（如 ::1）格式"},
    "协议": {"description": "网络通信协议，定义数据传输的规则和格式", "example": "https", "notes": "必填。常用：http、https、ftp、sftp、ssh、tcp、udp"},
    "方法": {"description": "HTTP 请求方法，指定对资源执行的操作类型", "example": "GET", "notes": "必填。常用：GET(获取)、POST(创建)、PUT(更新)、DELETE(删除)、PATCH(部分更新)、HEAD(获取头)"},
    "头部": {"description": "HTTP 请求或响应的头部字段，传递附加的元数据信息", "example": "Content-Type: application/json", "notes": "可选。常用：Content-Type、Authorization、Accept、User-Agent。多个头部用换行或数组指定"},
    "主体": {"description": "HTTP 请求的消息体，包含要发送的实际数据", "example": "{\"name\":\"test\"}", "notes": "可选。POST、PUT、PATCH 请求通常需要。格式需与 Content-Type 头部匹配"},
    "超时": {"description": "操作的最大等待时间，超过则终止操作", "example": "30", "notes": "可选。单位通常为秒。0 表示无限等待。网络操作建议设置合理超时避免挂起"},
    "重试": {"description": "操作失败时的重试次数", "example": "3", "notes": "可选。默认通常不重试或重试 1 次。指数退避策略可减轻服务器压力"},
    "间隔": {"description": "两次操作之间的等待时间", "example": "5", "notes": "可选。单位通常为秒。轮询操作需设置合理间隔避免频繁请求"},
    "格式": {"description": "输出或输入的数据格式", "example": "json", "notes": "可选。常用：json、yaml、xml、csv、table、plain。部分命令支持自定义格式模板"},
    "编码": {"description": "字符编码方式，用于文本数据的编码和解码", "example": "utf-8", "notes": "可选。默认通常为 utf-8。常用：utf-8、gbk、latin1、ascii。处理中文需确保编码一致"},
    "语言": {"description": "自然语言或编程语言标识", "example": "zh-CN", "notes": "可选。自然语言使用 IETF 语言标签（如 zh-CN、en-US）。编程语言使用标准名称（如 python、javascript）"},
    "区域": {"description": "地理或逻辑区域标识，用于分区部署或数据存储", "example": "ap-southeast-1", "notes": "必填。云服务商通常使用区域代码，如 AWS 的 us-east-1、阿里云的 cn-hangzhou"},
}

def get_default_example(param_name):
    """获取默认示例值"""
    examples = {
        "目录": "/var/log", "文件": "/etc/config.yaml", "路径": "/usr/local/bin",
        "主机": "192.168.1.100", "端口": "8080", "用户名": "admin",
        "密码": "MyP@ssw0rd!2024", "URL": "https://github.com/user/repo.git",
        "仓库URL": "https://github.com/user/repo.git", "容器名称": "myapp-web",
        "镜像名称": "nginx:1.24-alpine", "镜像": "nginx:1.24-alpine",
        "主机端口": "8080", "容器端口": "80", "主机路径": "/data/logs",
        "容器路径": "/var/log/nginx", "网络名称": "myapp_network",
        "环境变量": "MYSQL_ROOT_PASSWORD", "变量值": "mysecretpassword123",
        "卷名": "mysql_data", "分支名": "feature/user-auth",
        "提交信息": "feat: add user authentication", "标签名": "v1.2.0",
        "远程名": "origin", "命名空间": "production",
        "Pod名称": "nginx-deployment-7c4c7b5d9-x2v4p", "资源类型": "deployments",
        "Deployment名称": "nginx-deployment", "Service名称": "nginx-service",
        "副本数": "3", "配置文件": "/k8s/deployment.yaml",
        "数据库名": "myapp_production", "表名": "users",
        "列名": "email", "查询条件": "age > 18 AND status = 'active'",
        "key": "user:1001:profile", "value": "{\"name\":\"张三\"}",
        "秒数": "3600", "包名": "requests", "版本号": "2.28.0",
        "选项": "-la", "来源": "/var/log/app.log", "目标": "/backup/logs/",
        "模式": "755", "所有者": "www-data", "组": "developers",
        "旧名称": "old_name.txt", "新名称": "new_name.txt",
        "用户": "admin", "组名": "docker", "服务名": "nginx",
        "进程ID": "1234", "信号": "SIGTERM", "源": "/data/source/",
        "目的": "/backup/destination/", "命令": "ls -la /var/log",
        "时间": "2024-01-15 14:30:00", "数量": "100", "大小": "10M",
        "内容": "Hello, World!", "字符串": "error",
        "表达式": "s/old/new/g", "键": "server.host",
        "值": "localhost", "域名": "example.com",
        "IP地址": "192.168.1.1", "协议": "https",
        "方法": "GET", "头部": "Content-Type: application/json",
        "主体": "{\"name\":\"test\"}", "超时": "30",
        "重试": "3", "间隔": "5", "格式": "json",
        "编码": "utf-8", "语言": "zh-CN",
        "区域": "ap-southeast-1",
    }
    return examples.get(param_name, f"my_{param_name.lower()}")


def enhance_param(param_name, param_data):
    """增强单个参数定义"""
    if not isinstance(param_data, dict):
        param_data = {}

    existing_desc = param_data.get('description', '')
    if len(existing_desc) >= 25 and ' ' in existing_desc:
        if not param_data.get('notes'):
            param_data['notes'] = f"{'必填' if param_data.get('required') else '可选'}。请根据实际需求填写"
        if not param_data.get('example') or param_data.get('example') == param_name:
            param_data['example'] = get_default_example(param_name)
        return param_data

    knowledge = PARAM_KNOWLEDGE.get(param_name)
    if knowledge:
        param_data['description'] = knowledge['description']
        if not param_data.get('example') or param_data.get('example') == param_name:
            param_data['example'] = knowledge['example']
        param_data['notes'] = knowledge['notes']
    else:
        if not param_data.get('description') or len(param_data.get('description', '')) < 15:
            param_data['description'] = f"{param_name}参数，用于指定命令操作的目标或配置选项"
        if not param_data.get('example') or param_data.get('example') == param_name:
            param_data['example'] = get_default_example(param_name)
        if not param_data.get('notes'):
            param_data['notes'] = f"{'必填' if param_data.get('required') else '可选'}。请根据实际需求填写"

    return param_data


def enhance_command_description(cmd_name, cmd_desc, module_name):
    """增强命令描述"""
    if len(cmd_desc) >= 30 and ' ' in cmd_desc:
        return cmd_desc

    base_desc = cmd_desc
    if not base_desc or len(base_desc) < 10:
        base_desc = f"{cmd_name} 命令"

    templates = {
        "Linux": f"{base_desc}。这是 Linux 系统管理的基础命令，广泛应用于服务器运维、自动化脚本和日常文件操作中。支持多种选项组合以适应不同场景需求",
        "Git": f"{base_desc}。这是版本控制工作流中的核心操作，用于代码的版本管理、协作开发和发布流程。正确使用此命令可以保持清晰的提交历史和高效的分支管理",
        "Docker": f"{base_desc}。这是容器化应用管理的关键命令，用于构建、运行和维护容器化工作负载。掌握此命令对于现代云原生应用的部署和运维至关重要",
        "Kubernetes": f"{base_desc}。这是 Kubernetes 集群管理的核心命令，用于操作容器编排平台中的各类资源对象。适用于应用部署、扩缩容、故障排查和集群维护场景",
        "Python": f"{base_desc}。这是 Python 生态系统中常用的开发工具命令，用于包管理、环境配置和项目构建。是 Python 开发者日常工作的基础技能",
        "Node": f"{base_desc}。这是 Node.js 开发环境中的常用命令，用于依赖管理、脚本执行和项目构建。是前端和后端 JavaScript 开发的基础工具",
        "Redis": f"{base_desc}。这是 Redis 内存数据库的核心操作命令，用于高性能数据存储和缓存管理。适用于会话存储、实时排行榜、消息队列等场景",
        "MySQL": f"{base_desc}。这是 MySQL 关系型数据库的常用管理命令，用于数据库运维、数据查询和性能优化。是 Web 应用数据持久化的基础工具",
        "PostgreSQL": f"{base_desc}。这是 PostgreSQL 高级关系型数据库的常用命令，用于数据库管理、数据操作和性能调优。以其强大的功能和扩展性著称",
        "Nginx": f"{base_desc}。这是 Nginx Web 服务器和反向代理的核心管理命令，用于网站部署、负载均衡和静态资源服务。是高并发 Web 架构的关键组件",
        "AWS": f"{base_desc}。这是 AWS 云平台的 CLI 管理命令，用于云资源的创建、配置和监控。是基础设施即代码和云自动化运维的基础工具",
        "CI_CD": f"{base_desc}。这是持续集成和持续部署流程中的关键命令，用于自动化构建、测试和发布。是现代 DevOps 实践的核心组成部分",
        "监控": f"{base_desc}。这是系统可观测性工具链中的核心命令，用于采集指标、分析日志和追踪请求。是保障系统稳定性和性能的关键手段",
        "安全": f"{base_desc}。这是系统安全加固和审计的重要命令，用于访问控制、漏洞扫描和合规检查。是保障基础设施安全的基础操作",
        "网络": f"{base_desc}。这是网络诊断和配置的核心命令，用于排查连接问题、分析流量和配置网络参数。是系统管理员必备的网络工具",
        "SSH": f"{base_desc}。这是安全远程管理的核心命令，通过加密通道连接和管理远程服务器。是 Linux 服务器运维的标准方式",
        "Shell": f"{base_desc}。这是 Shell 脚本编写和执行的常用命令，用于自动化任务和系统管理。是提升运维效率的重要技能",
        "通用": f"{base_desc}。该命令是相关技术栈中的常用操作，掌握其用法对于日常开发和运维工作非常重要。建议结合实际场景灵活运用"
    }

    module_key = "通用"
    for key in templates:
        if key in module_name:
            module_key = key
            break

    return templates[module_key]


def remove_number_prefix(text):
    """移除名称中的数字前缀，如 '1-'、'2.' 等"""
    if not isinstance(text, str):
        return text
    return re.sub(r'^\d+[-.、\s]+', '', text)


def enhance_command(cmd, module_name):
    """增强单个命令"""
    # 移除名称中的数字前缀
    if 'name' in cmd:
        cmd['name'] = remove_number_prefix(cmd['name'])

    # 增强描述
    if 'description' in cmd:
        cmd['description'] = enhance_command_description(
            cmd.get('name', ''), cmd['description'], module_name
        )
    else:
        cmd['description'] = enhance_command_description(
            cmd.get('name', ''), '', module_name
        )

    data = cmd.get('data', {})

    # 增强基础参数
    if 'params' in data and isinstance(data['params'], dict):
        for param_name, param_data in list(data['params'].items()):
            data['params'][param_name] = enhance_param(param_name, param_data)

    # 增强扩展用法
    if 'extensions' in data and isinstance(data['extensions'], list):
        for ext in data['extensions']:
            if isinstance(ext, dict):
                if 'name' in ext:
                    ext['name'] = remove_number_prefix(ext['name'])
                if 'params' in ext and isinstance(ext['params'], dict):
                    for param_name, param_data in list(ext['params'].items()):
                        ext['params'][param_name] = enhance_param(param_name, param_data)

    cmd['data'] = data
    return cmd


def process_file(file_path):
    """处理单个 commands.json 文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

    # 跳过列表格式的文件（不规范）
    if isinstance(data, list):
        print(f"Skipped (list format): {file_path}")
        return False

    module_name = data.get('module', '')

    # 增强模块描述
    if 'description' in data:
        desc = data['description']
        if len(desc) < 20:
            data['description'] = f"{module_name} 模块，提供常用的 {module_name} 相关命令和工具。适用于开发、测试和生产环境的日常操作和自动化脚本编写"

    # 增强每个命令
    if 'commands' in data:
        for cmd in data['commands']:
            enhance_command(cmd, module_name)

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Enhanced: {file_path}")
        return True
    except Exception as e:
        print(f"Error writing {file_path}: {e}")
        return False


def main():
    modules_dir = Path(__file__).parent.parent / 'modules'
    files = sorted(list(modules_dir.glob('*/commands.json')))

    success = 0
    failed = 0

    for file_path in files:
        if process_file(file_path):
            success += 1
        else:
            failed += 1

    print(f"\nDone! Success: {success}, Failed: {failed}, Total: {success + failed}")


if __name__ == '__main__':
    main()
