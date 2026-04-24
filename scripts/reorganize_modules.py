#!/usr/bin/env python3
"""
重组工具 - 模块重组脚本 v2 - 二级结构分类
功能：
  1. 将模块重组为二级结构（分类/模块）
  2. 修改 module 字段为完整路径格式（分类/模块名）
  3. 创建中英结合的命名规范
  4. 批量移动和重组目录结构

使用方法：python scripts/reorganize_modules.py
说明：
  - 包含完整的二级分类结构定义 (CATEGORY_STRUCTURE)
  - 支持容器编排、版本控制、数据库、云平台等多个分类
  - 自动创建分类目录
  - 自动移动模块到正确的分类下
  - 警告：此操作会修改目录结构，执行前请备份

import os
import shutil
import json
from pathlib import Path

MODULES_DIR = Path(r"C:\code\copy_skill_extends\modules")

# 定义二级分类结构 (分类 -> 模块列表)
CATEGORY_STRUCTURE = {
    "容器编排": [
        # Docker 子模块
        "Docker attach", "Docker buildx", "Docker commit", "Docker compose version",
        "Docker cp", "Docker create", "Docker create network", "Docker diff",
        "Docker events", "Docker exec", "Docker export", "Docker history",
        "Docker images", "Docker info", "Docker Inspect", "Docker kill",
        "Docker login", "Docker Network", "Docker pause", "Docker prune",
        "Docker ps", "Docker pull", "Docker push", "Docker rename",
        "Docker restart", "Docker rm", "Docker rmi", "Docker save",
        "Docker Service", "Docker start", "Docker stop", "Docker Swarm",
        "Docker unpause", "Docker update", "Docker version", "Docker Volume",
        "Docker wait", "Docker卷", "Docker命令", "Docker容器生命周期",
        "Docker容器管理", "Docker日志与监控", "Docker系统管理", "Docker网络",
        "Docker镜像管理", "DockerCompose", "DockerCompose高级模式",
        "Dockerfile构建",
        # Kubernetes
        "kubectl annotate", "kubectl api-resources", "kubectl api-versions",
        "kubectl apply", "kubectl auth", "kubectl cluster-info", "kubectl config",
        "kubectl convert", "kubectl cordon", "kubectl cp", "kubectl create",
        "kubectl delete", "kubectl describe", "kubectl drain", "kubectl edit",
        "kubectl exec", "kubectl explain", "kubectl expose", "kubectl get",
        "kubectl label", "kubectl logs", "kubectl patch", "kubectl port-forward",
        "kubectl proxy", "kubectl Rollout", "kubectl run", "kubectl scale",
        "kubectl Scaling", "kubectl top", "kubectl uncordon", "kubectl version",
        "kubectl wait", "kubectl调试", "kubectl插件", "kubectl标签与注解",
        "kubectl资源创建", "kubectl资源编辑",
        "Kubernetes ConfigMap与Secret", "Kubernetes Deployment", "Kubernetes Ingress",
        "Kubernetes Pod管理", "Kubernetes Service", "Kubernetes命令",
        "Kubernetes集群管理", "Kubernetes高级操作"
    ],
    "版本控制": [
        "Git add", "Git Archive", "Git Bisect", "Git branch", "Git checkout",
        "Git Cherry-pick", "Git clone", "Git commit", "Git config", "Git diff",
        "Git fetch", "Git grep", "Git init", "Git log", "Git merge", "Git mv",
        "Git pull", "Git push", "Git rebase", "Git Reflog", "Git remote",
        "Git reset", "Git Revert", "Git rm", "Git show", "Git stash show",
        "Git status", "Git tag", "Git分支", "Git别名与配置", "Git历史与版本",
        "Git变基与合并", "Git命令", "Git子模块", "Git工作区", "Git忽略文件",
        "Git暂存区管理", "Git暂存管理", "Git标签", "Git补丁操作", "Git远程",
        "GitHub Actions", "GitHub CLI命令", "GitHub CLI高级操作", "GitHubActions",
        "Git工作流", "GitLab CLI", "Mercurial命令", "SVN命令", "Perforce命令"
    ],
    "Linux系统": [
        "Linux alias", "Linux awk", "Linux cat", "Linux cd", "Linux chmod",
        "Linux chown", "Linux cron", "Linux curl", "Linux date", "Linux du",
        "Linux env", "Linux export", "Linux fdisk", "Linux find", "Linux grep",
        "Linux gzip", "Linux head", "Linux history", "Linux hostname", "Linux id",
        "Linux iptables", "Linux journalctl", "Linux ln", "Linux locate",
        "Linux lsblk", "Linux lsof", "Linux mount", "Linux netstat", "Linux nohup",
        "Linux pwd", "Linux rsync", "Linux scp", "Linux screen", "Linux sed",
        "Linux sort", "Linux ss", "Linux ssh-keygen", "Linux stat", "Linux strace",
        "Linux systemctl", "Linux tail", "Linux tar", "Linux tmux", "Linux touch",
        "Linux tree", "Linux ulimit", "Linux uname", "Linux uniq", "Linux unzip",
        "Linux uptime", "Linux watch", "Linux wc", "Linux wget", "Linux which",
        "Linux whoami", "Linux xargs", "Linux压缩解压", "Linux命令", "Linux文件操作",
        "Linux文本处理", "Linux权限管理", "Linux用户管理", "Linux磁盘管理",
        "Linux管道与重定向", "Linux系统监控", "Linux系统管理", "Linux网络诊断",
        "Linux网络配置", "Linux进程管理"
    ],
    "前端开发": [
        "Node.js npm Scripts", "Node.js后端命令", "npm命令", "npm脚本与包管理",
        "Yarn", "pnpm", "Bun", "React命令", "Vue.js命令", "Vite", "Webpack",
        "Tailwind CSS", "TypeScript命令"
    ],
    "后端开发": [
        "Python pip", "Python Web框架", "Python虚拟环境", "Python命令",
        "Java Spring Boot", "Go命令", "Rust Cargo"
    ],
    "数据库": [
        "MySQL mysql", "MySQL命令", "MySQL数据库管理",
        "PostgreSQL psql", "PostgreSQL命令", "PostgreSQL数据库管理",
        "MongoDB命令", "Redis命令", "Redis数据机构操作",
        "Redis-列表操作", "Redis-哈希操作", "Redis-基本操作", "Redis-有序集合",
        "Redis-服务器命令", "Redis-键管理", "Redis-集合操作",
        "Elasticsearch", "ORM框架"
    ],
    "云平台": [
        "AWS CLI命令", "AWS CloudFormation", "AWS EC2管理", "AWS IAM身份管理",
        "AWS Lambda", "AWS S3", "AWS S3 sync", "AWS s3 mb", "AWS S3存储操作",
        "AWS ec2 describe", "Azure CLI", "GCP CLI"
    ],
    "基础设施": [
        "Ansible", "Terraform", "Helm"
    ],
    "CI_CD": [
        "Jenkins CLI", "CI_CD流水线"
    ],
    "监控可观测性": [
        "Prometheus", "Grafana CLI"
    ],
    "API与认证": [
        "curl命令", "Web API工具", "GraphQL命令", "API与认证"
    ],
    "开发工具": [
        "AI_ML工具", "Claude Skills-ccg", "Claude Skills-ecc",
        "Claude Skills-oh-my-claude", "Claude Skills-openspec",
        "Claude Skills-providers", "Claude Skills-regex",
        "Claude Skills-superpowers", "Claude Skills-ultrawork"
    ],
    "DevOps工具": [
        "SSH命令", "SSH远程操作", "Shell脚本模板", "Serverless与边缘计算"
    ],
    "Web服务器": [
        "Nginx命令", "Nginx命令"
    ],
    "安全": [
        "安全加固", "容器安全"
    ],
    "测试框架": [
        "测试框架"
    ],
    "移动开发": [
        "移动开发"
    ],
    "微服务架构": [
        "微服务架构"
    ],
    "CDN缓存": [
        "CDN与缓存"
    ],
    "搜索引擎": [
        "搜索引擎"
    ],
    "消息队列": [
        "消息队列"
    ],
    "负载均衡": [
        "负载均衡"
    ],
    "配置管理": [
        "配置管理"
    ],
    "编辑器命令": [
        "编辑器命令"
    ],
    "网络诊断": [
        "网络诊断"
    ],
    "系统监控": [
        "系统监控"
    ]
}

# 中文命名映射
NAME_MAPPING = {
    # Docker
    "Docker attach": "Docker-容器挂载 attach",
    "Docker buildx": "Docker-多架构构建 buildx",
    "Docker commit": "Docker-提交容器 commit",
    "Docker compose version": "Docker Compose-版本查询 version",
    "Docker cp": "Docker-复制文件 cp",
    "Docker create": "Docker-创建容器 create",
    "Docker create network": "Docker-创建网络 create network",
    "Docker diff": "Docker-容器差异 diff",
    "Docker events": "Docker-实时事件 events",
    "Docker exec": "Docker-执行命令 exec",
    "Docker export": "Docker-导出容器 export",
    "Docker history": "Docker-镜像历史 history",
    "Docker images": "Docker-镜像列表 images",
    "Docker info": "Docker-系统信息 info",
    "Docker Inspect": "Docker-检查容器 Inspect",
    "Docker kill": "Docker-终止容器 kill",
    "Docker login": "Docker-登录仓库 login",
    "Docker Network": "Docker-网络管理 Network",
    "Docker pause": "Docker-暂停容器 pause",
    "Docker prune": "Docker-清理资源 prune",
    "Docker ps": "Docker-进程列表 ps",
    "Docker pull": "Docker-拉取镜像 pull",
    "Docker push": "Docker-推送镜像 push",
    "Docker rename": "Docker-重命名 rename",
    "Docker restart": "Docker-重启容器 restart",
    "Docker rm": "Docker-删除容器 rm",
    "Docker rmi": "Docker-删除镜像 rmi",
    "Docker save": "Docker-保存镜像 save",
    "Docker Service": "Docker-服务管理 Service",
    "Docker start": "Docker-启动容器 start",
    "Docker stop": "Docker-停止容器 stop",
    "Docker Swarm": "Docker-集群模式 Swarm",
    "Docker unpause": "Docker-恢复容器 unpause",
    "Docker update": "Docker-更新配置 update",
    "Docker version": "Docker-版本信息 version",
    "Docker Volume": "Docker-卷管理 Volume",
    "Docker wait": "Docker-等待容器 wait",
    "Docker卷": "Docker-卷管理 volume",
    "Docker命令": "Docker-命令概览 commands",
    "Docker容器生命周期": "Docker-生命周期 lifecycle",
    "Docker容器管理": "Docker-容器管理 containers",
    "Docker日志与监控": "Docker-日志监控 logs",
    "Docker系统管理": "Docker-系统管理 system",
    "Docker网络": "Docker-网络配置 network",
    "Docker镜像管理": "Docker-镜像管理 images",
    "DockerCompose": "Docker Compose-基础命令 compose",
    "DockerCompose高级模式": "Docker Compose-高级模式 advanced",
    "Dockerfile构建": "Dockerfile-构建镜像 build",
    
    # kubectl
    "kubectl annotate": "kubectl-资源注解 annotate",
    "kubectl api-resources": "kubectl-API资源 api-resources",
    "kubectl api-versions": "kubectl-API版本 api-versions",
    "kubectl apply": "kubectl-应用配置 apply",
    "kubectl auth": "kubectl-认证授权 auth",
    "kubectl cluster-info": "kubectl-集群信息 cluster-info",
    "kubectl config": "kubectl-配置管理 config",
    "kubectl convert": "kubectl-格式转换 convert",
    "kubectl cordon": "kubectl-停止调度 cordon",
    "kubectl cp": "kubectl-复制文件 cp",
    "kubectl create": "kubectl-创建资源 create",
    "kubectl delete": "kubectl-删除资源 delete",
    "kubectl describe": "kubectl-描述资源 describe",
    "kubectl drain": "kubectl-排空节点 drain",
    "kubectl edit": "kubectl-编辑资源 edit",
    "kubectl exec": "kubectl-执行命令 exec",
    "kubectl explain": "kubectl-解释资源 explain",
    "kubectl expose": "kubectl-暴露服务 expose",
    "kubectl get": "kubectl-获取资源 get",
    "kubectl label": "kubectl-管理标签 label",
    "kubectl logs": "kubectl-查看日志 logs",
    "kubectl patch": "kubectl-修补资源 patch",
    "kubectl port-forward": "kubectl-端口转发 port-forward",
    "kubectl proxy": "kubectl-代理服务 proxy",
    "kubectl Rollout": "kubectl-滚动更新 rollout",
    "kubectl run": "kubectl-运行Pod run",
    "kubectl scale": "kubectl-扩缩容 scale",
    "kubectl Scaling": "kubectl-扩缩容 scaling",
    "kubectl top": "kubectl-资源监控 top",
    "kubectl uncordon": "kubectl-恢复调度 uncordon",
    "kubectl version": "kubectl-版本信息 version",
    "kubectl wait": "kubectl-等待条件 wait",
    "kubectl调试": "kubectl-调试 debug",
    "kubectl插件": "kubectl-插件管理 plugins",
    "kubectl标签与注解": "kubectl-标签注解 labels",
    "kubectl资源创建": "kubectl-资源创建 create",
    "kubectl资源编辑": "kubectl-资源编辑 edit",
    
    # Kubernetes
    "Kubernetes ConfigMap与Secret": "K8s-配置管理 ConfigMap",
    "Kubernetes Deployment": "K8s-部署管理 Deployment",
    "Kubernetes Ingress": "K8s-入口路由 Ingress",
    "Kubernetes Pod管理": "K8s-Pod管理 Pod",
    "Kubernetes Service": "K8s-服务管理 Service",
    "Kubernetes命令": "K8s-命令概览 commands",
    "Kubernetes集群管理": "K8s-集群管理 cluster",
    "Kubernetes高级操作": "K8s-高级操作 advanced",
    
    # Git
    "Git add": "Git-暂存文件 add",
    "Git Archive": "Git-归档文件 Archive",
    "Git Bisect": "Git-二分查找 Bisect",
    "Git branch": "Git-分支管理 branch",
    "Git checkout": "Git-切换分支 checkout",
    "Git Cherry-pick": "Git-拣选提交 Cherry-pick",
    "Git clone": "Git-克隆仓库 clone",
    "Git commit": "Git-提交变更 commit",
    "Git config": "Git-配置管理 config",
    "Git diff": "Git-差异对比 diff",
    "Git fetch": "Git-获取更新 fetch",
    "Git grep": "Git-代码搜索 grep",
    "Git init": "Git-初始化仓库 init",
    "Git log": "Git-查看日志 log",
    "Git merge": "Git-合并分支 merge",
    "Git mv": "Git-移动文件 mv",
    "Git pull": "Git-拉取更新 pull",
    "Git push": "Git-推送更新 push",
    "Git rebase": "Git-变基操作 rebase",
    "Git Reflog": "Git-引用日志 Reflog",
    "Git remote": "Git-远程管理 remote",
    "Git reset": "Git-重置提交 reset",
    "Git Revert": "Git-撤销提交 Revert",
    "Git rm": "Git-删除文件 rm",
    "Git show": "Git-显示提交 show",
    "Git stash show": "Git-贮藏查看 stash",
    "Git status": "Git-状态查看 status",
    "Git tag": "Git-标签管理 tag",
    "Git分支": "Git-分支操作 branches",
    "Git别名与配置": "Git-别名配置 aliases",
    "Git历史与版本": "Git-历史版本 history",
    "Git变基与合并": "Git-变基合并 rebasing",
    "Git命令": "Git-命令总览 commands",
    "Git子模块": "Git-子模块操作 submodules",
    "Git工作区": "Git-工作区操作 workspace",
    "Git忽略文件": "Git-忽略配置 gitignore",
    "Git暂存区管理": "Git-暂存区管理 staging",
    "Git暂存管理": "Git-暂存操作 stash",
    "Git标签": "Git-标签操作 tags",
    "Git补丁操作": "Git-补丁操作 patches",
    "Git远程": "Git-远程操作 remote",
    
    # GitHub
    "GitHub Actions": "GitHub-动作执行 Actions",
    "GitHub CLI命令": "GitHub CLI-命令概览 CLI",
    "GitHub CLI高级操作": "GitHub CLI-高级操作 advanced",
    "GitHubActions": "GitHub-工作流 Actions",
    "Git工作流": "GitHub-工作流 workflow",
    "GitLab CLI": "GitLab-CLI工具 CLI",
    "Mercurial命令": "Hg-版本控制 Mercurial",
    "SVN命令": "SVN-版本控制 Subversion",
    "Perforce命令": "Perforce-版本控制 Perforce",
    
    # Linux
    "Linux alias": "Linux-命令别名 alias",
    "Linux awk": "Linux-文本处理 awk",
    "Linux cat": "Linux-查看文件 cat",
    "Linux cd": "Linux-切换目录 cd",
    "Linux chmod": "Linux-权限管理 chmod",
    "Linux chown": "Linux-所有者管理 chown",
    "Linux cron": "Linux-定时任务 cron",
    "Linux curl": "Linux-HTTP请求 curl",
    "Linux date": "Linux-日期时间 date",
    "Linux du": "Linux-磁盘使用 du",
    "Linux env": "Linux-环境变量 env",
    "Linux export": "Linux-导出变量 export",
    "Linux fdisk": "Linux-磁盘分区 fdisk",
    "Linux find": "Linux-文件搜索 find",
    "Linux grep": "Linux-文本搜索 grep",
    "Linux gzip": "Linux-压缩解压 gzip",
    "Linux head": "Linux-查看头部 head",
    "Linux history": "Linux-命令历史 history",
    "Linux hostname": "Linux-主机名 hostname",
    "Linux id": "Linux-用户ID id",
    "Linux iptables": "Linux-防火墙 iptables",
    "Linux journalctl": "Linux-系统日志 journalctl",
    "Linux ln": "Linux-创建链接 ln",
    "Linux locate": "Linux-快速搜索 locate",
    "Linux lsblk": "Linux-块设备 lsblk",
    "Linux lsof": "Linux-进程文件 lsof",
    "Linux mount": "Linux-挂载设备 mount",
    "Linux netstat": "Linux-网络状态 netstat",
    "Linux nohup": "Linux-后台运行 nohup",
    "Linux pwd": "Linux-当前目录 pwd",
    "Linux rsync": "Linux-同步文件 rsync",
    "Linux scp": "Linux-安全复制 scp",
    "Linux screen": "Linux-终端会话 screen",
    "Linux sed": "Linux-流编辑器 sed",
    "Linux sort": "Linux-排序内容 sort",
    "Linux ss": "Linux-网络连接 ss",
    "Linux ssh-keygen": "Linux-SSH密钥 ssh-keygen",
    "Linux stat": "Linux-文件状态 stat",
    "Linux strace": "Linux-系统跟踪 strace",
    "Linux systemctl": "Linux-系统服务 systemctl",
    "Linux tail": "Linux-查看尾部 tail",
    "Linux tar": "Linux-归档打包 tar",
    "Linux tmux": "Linux-终端复用 tmux",
    "Linux touch": "Linux-创建文件 touch",
    "Linux tree": "Linux-目录树形 tree",
    "Linux ulimit": "Linux-资源限制 ulimit",
    "Linux uname": "Linux-系统信息 uname",
    "Linux uniq": "Linux-去重处理 uniq",
    "Linux unzip": "Linux-解压文件 unzip",
    "Linux uptime": "Linux-运行时间 uptime",
    "Linux watch": "Linux-监控命令 watch",
    "Linux wc": "Linux-字数统计 wc",
    "Linux wget": "Linux-下载文件 wget",
    "Linux which": "Linux-查找命令 which",
    "Linux whoami": "Linux-当前用户 whoami",
    "Linux xargs": "Linux-参数构建 xargs",
    "Linux压缩解压": "Linux-压缩解压 archive",
    "Linux命令": "Linux-命令总览 commands",
    "Linux文件操作": "Linux-文件操作 files",
    "Linux文本处理": "Linux-文本处理 text",
    "Linux权限管理": "Linux-权限控制 permissions",
    "Linux用户管理": "Linux-用户管理 users",
    "Linux磁盘管理": "Linux-磁盘管理 disks",
    "Linux管道与重定向": "Linux-管道重定向 pipes",
    "Linux系统监控": "Linux-系统监控 monitoring",
    "Linux系统管理": "Linux-系统管理 system",
    "Linux网络诊断": "Linux-网络诊断 network",
    "Linux网络配置": "Linux-网络配置 network",
    "Linux进程管理": "Linux-进程管理 processes",
    
    # 前端
    "Node.js npm Scripts": "Node.js-npm脚本 npm",
    "Node.js后端命令": "Node.js-后端开发 backend",
    "npm命令": "npm-包管理 npm",
    "npm脚本与包管理": "npm-脚本管理 scripts",
    "Yarn": "Yarn-包管理器 Yarn",
    "pnpm": "pnpm-包管理器 pnpm",
    "Bun": "Bun-包管理器 Bun",
    "React命令": "React-框架命令 React",
    "Vue.js命令": "Vue-框架命令 Vue",
    "Vite": "Vite-构建工具 Vite",
    "Webpack": "Webpack-打包工具 Webpack",
    "Tailwind CSS": "Tailwind-CSS框架 Tailwind",
    "TypeScript命令": "TypeScript-类型语言 TS",
    
    # 后端
    "Python pip": "Python-pip管理 pip",
    "Python Web框架": "Python-Web框架 Web",
    "Python虚拟环境": "Python-虚拟环境 venv",
    "Python命令": "Python-命令总览 Python",
    "Java Spring Boot": "Java-Spring框架 Spring",
    "Go命令": "Go-编程语言 Go",
    "Rust Cargo": "Rust-包管理 Cargo",
    
    # 数据库
    "MySQL mysql": "MySQL-客户端 mysql",
    "MySQL命令": "MySQL-命令总览 MySQL",
    "MySQL数据库管理": "MySQL-数据库管理 database",
    "PostgreSQL psql": "PostgreSQL-客户端 psql",
    "PostgreSQL命令": "PostgreSQL-命令总览 PostgreSQL",
    "PostgreSQL数据库管理": "PostgreSQL-数据库管理 database",
    "MongoDB命令": "MongoDB-NoSQL数据库 MongoDB",
    "Redis命令": "Redis-缓存数据库 Redis",
    "Redis数据机构操作": "Redis-数据结构 data",
    "Redis-列表操作": "Redis-列表操作 list",
    "Redis-哈希操作": "Redis-哈希操作 hash",
    "Redis-基本操作": "Redis-基础操作 basic",
    "Redis-有序集合": "Redis-有序集合 sorted",
    "Redis-服务器命令": "Redis-服务器管理 server",
    "Redis-键管理": "Redis-键操作 keys",
    "Redis-集合操作": "Redis-集合操作 set",
    "Elasticsearch": "ES-搜索引擎 Elasticsearch",
    "ORM框架": "ORM-框架总览 ORM",
    
    # 云平台
    "AWS CLI命令": "AWS-CLI工具 AWS",
    "AWS CloudFormation": "AWS-基础设施即代码 CF",
    "AWS EC2管理": "AWS-云主机管理 EC2",
    "AWS IAM身份管理": "AWS-身份管理 IAM",
    "AWS Lambda": "AWS-函数计算 Lambda",
    "AWS S3": "AWS-对象存储 S3",
    "AWS S3 sync": "AWS-S3同步 sync",
    "AWS s3 mb": "AWS-创建桶 mb",
    "AWS S3存储操作": "AWS-存储操作 storage",
    "AWS ec2 describe": "AWS-查询EC2 describe",
    "Azure CLI": "Azure-CLI工具 Azure",
    "GCP CLI": "GCP-CLI工具 GCP",
    
    # 其他
    "Ansible": "Ansible-自动化运维 Ansible",
    "Terraform": "Terraform-基础设施代码 Terraform",
    "Helm": "Helm-K8s包管理 Helm",
    "Jenkins CLI": "Jenkins-CI/CD工具 Jenkins",
    "CI_CD流水线": "CI_CD-流水线 pipeline",
    "Prometheus": "Prometheus-监控系统 Prometheus",
    "Grafana CLI": "Grafana-可视化 Grafana",
    "curl命令": "curl-HTTP工具 curl",
    "Web API工具": "Web API-REST工具 API",
    "GraphQL命令": "GraphQL-查询语言 GraphQL",
    "API与认证": "API-认证授权 auth",
    "AI_ML工具": "AI_ML-人工智能工具 AI",
    "Claude Skills-ccg": "Claude-Skills技能 ccg",
    "Claude Skills-ecc": "Claude-Skills技能 ecc",
    "Claude Skills-oh-my-claude": "Claude-OM Claude",
    "Claude Skills-openspec": "Claude-OpenSpec openspec",
    "Claude Skills-providers": "Claude-Providers providers",
    "Claude Skills-regex": "Claude-正则表达式 regex",
    "Claude Skills-superpowers": "Claude-Superpowers super",
    "Claude Skills-ultrawork": "Claude-Ultrawork ultra",
    "SSH命令": "SSH-远程连接 SSH",
    "SSH远程操作": "SSH-远程操作 remote",
    "Shell脚本模板": "Shell-脚本模板 scripts",
    "Serverless与边缘计算": "Serverless-无服务器 serverless",
    "Nginx命令": "Nginx-Web服务器 Nginx",
    "安全加固": "安全-安全加固 security",
    "容器安全": "容器-安全加固 container",
    "测试框架": "测试-框架总览 testing",
    "移动开发": "移动-开发工具 mobile",
    "微服务架构": "微服务-架构模式 microservices",
    "CDN与缓存": "CDN-内容分发 cdn",
    "搜索引擎": "搜索-搜索引擎 search",
    "消息队列": "消息队列-队列工具 mq",
    "负载均衡": "负载均衡-分发策略 lb",
    "配置管理": "配置-管理工具 config",
    "编辑器命令": "编辑器-VSCode等 editor",
    "网络诊断": "网络-诊断工具 network",
    "系统监控": "系统-监控工具 monitoring"
}

def get_module_dirs():
    """获取所有模块目录"""
    return [d for d in os.listdir(MODULES_DIR) 
            if os.path.isdir(os.path.join(MODULES_DIR, d)) 
            and not d.startswith('.')]

def find_category(module_name):
    """查找模块应属于的分类"""
    for category, modules in CATEGORY_STRUCTURE.items():
        if module_name in modules:
            return category
    return "其他"

def get_new_name(module_name):
    """获取新的中英结合名称"""
    if module_name in NAME_MAPPING:
        return NAME_MAPPING[module_name]
    return module_name

def create_directories():
    """创建分类目录"""
    created = []
    for category in CATEGORY_STRUCTURE.keys():
        cat_path = MODULES_DIR / category
        if not cat_path.exists():
            cat_path.mkdir(exist_ok=True)
            created.append(category)
    
    # 创建"其他"目录
    other_path = MODULES_DIR / "其他"
    if not other_path.exists():
        other_path.mkdir(exist_ok=True)
        created.append("其他")
    
    return created

def move_and_rename_modules():
    """移动并重命名模块"""
    moved = []
    failed = []
    
    for module_dir in get_module_dirs():
        src = MODULES_DIR / module_dir
        
        # 跳过已分类的目录
        if module_dir in CATEGORY_STRUCTURE or module_dir == "其他":
            continue
        
        category = find_category(module_dir)
        new_name = get_new_name(module_dir)
        dst = MODULES_DIR / category / new_name
        
        if dst.exists():
            # 如果目标已存在，删除旧的
            shutil.rmtree(dst)
        
        try:
            shutil.move(str(src), str(dst))
            moved.append((module_dir, category, new_name))
        except Exception as e:
            failed.append((module_dir, str(e)))
    
    return moved, failed

def update_commands_json(filepath, new_module_path, category):
    """更新 commands.json"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 更新 module 字段为完整路径
        data['module'] = new_module_path
        
        # 更新 dirPath
        for cmd in data.get('commands', []):
            if 'dirPath' in cmd:
                cmd['dirPath'] = f"/{category}/"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        return True
    except Exception as e:
        print(f"    JSON update error: {e}")
        return False

def process_moved_modules():
    """处理移动后的模块"""
    updated = 0
    for category in os.listdir(MODULES_DIR):
        cat_path = MODULES_DIR / category
        if not os.path.isdir(cat_path):
            continue
        
        for module_dir in os.listdir(cat_path):
            json_path = cat_path / module_dir / "commands.json"
            if json_path.exists():
                new_module_path = f"{category}/{module_dir}"
                if update_commands_json(json_path, new_module_path, category):
                    updated += 1
    
    return updated

def print_new_structure():
    """打印新的目录结构"""
    print("\n" + "=" * 80)
    print("新的目录结构")
    print("=" * 80)
    
    total_modules = 0
    for category in sorted(os.listdir(MODULES_DIR)):
        cat_path = MODULES_DIR / category
        if not os.path.isdir(cat_path):
            continue
        
        modules = [d for d in os.listdir(cat_path) if os.path.isdir(cat_path / d)]
        total_modules += len(modules)
        print(f"\n{category}/ ({len(modules)} modules)")
        for mod in sorted(modules)[:8]:
            print(f"  ├── {mod}")
        if len(modules) > 8:
            print(f"  └── ... and {len(modules) - 8} more")
    
    print(f"\n总计: {total_modules} modules")
    print("=" * 80)

def main():
    print("=" * 80)
    print("模块重组脚本 v2")
    print("=" * 80)
    
    # 1. 创建目录
    print("\n[1/4] 创建分类目录...")
    created = create_directories()
    print(f"  创建了 {len(created)} 个分类目录")
    
    # 2. 移动并重命名
    print("\n[2/4] 移动并重命名模块...")
    moved, failed = move_and_rename_modules()
    print(f"  成功移动: {len(moved)} 个模块")
    if failed:
        print(f"  失败: {len(failed)} 个")
        for mod, err in failed[:5]:
            print(f"    - {mod}: {err}")
    
    # 3. 更新 JSON
    print("\n[3/4] 更新 commands.json...")
    updated = process_moved_modules()
    print(f"  更新了 {updated} 个 JSON 文件")
    
    # 4. 打印新结构
    print("\n[4/4] 生成新目录结构...")
    print_new_structure()
    
    print("\n完成!")

if __name__ == "__main__":
    main()
