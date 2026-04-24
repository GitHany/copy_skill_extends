#!/usr/bin/env python3
"""
重组工具 - 处理剩余未分类模块的分类重组
功能：
  1. 根据预定义的 REMAPPING 映射表，将模块重新分配到正确的分类
  2. 支持容器编排、版本控制、数据库等多个分类的映射
  3. 自动移动目录结构到新的分类下

使用方法：python scripts/fix_remaining.py
说明：
  - 包含完整的分类映射规则 (REMAPPING)
  - 包含各分类模块列表 (CATEGORY_MODULES)
  - 自动创建目标分类目录
  - 自动移动模块到新位置

import os
import shutil
import json
from pathlib import Path

MODULES_DIR = Path(r"C:\code\copy_skill_extends\modules")

# 补充分类映射
REMAPPING = {
    # 应该去容器编排的
    "Docker Build": "容器编排",
    "Docker compose version": "容器编排",
    "Docker 卷": "容器编排",
    "Docker 命令": "容器编排",
    "Docker 容器生命周期": "容器编排",
    "Docker 容器管理": "容器编排",
    "Docker 日志与监控": "容器编排",
    "Docker 系统管理": "容器编排",
    "Docker 网络": "容器编排",
    "Docker 镜像管理": "容器编排",
    "DockerCompose 高级模式": "容器编排",
    "Dockerfile 构建": "容器编排",
    
    # 应该去版本控制的
    "Git 分支": "版本控制",
    "Git 别名与配置": "版本控制",
    "Git 历史与版本": "版本控制",
    "Git 变基与合并": "版本控制",
    "Git 命令": "版本控制",
    "Git 子模块": "版本控制",
    "Git 工作区": "版本控制",
    "Git 忽略文件": "版本控制",
    "Git 暂存区管理": "版本控制",
    "Git 暂存管理": "版本控制",
    "Git 标签": "版本控制",
    "Git 补丁操作": "版本控制",
    "Git 远程": "版本控制",
    "Git工作流": "版本控制",
    
    # 应该去数据库的
    "MySQL 命令": "数据库",
    "MySQL 数据库管理": "数据库",
    "PostgreSQL 命令": "数据库",
    "PostgreSQL 数据库管理": "数据库",
    "MongoDB 命令": "数据库",
    "Redis 命令": "数据库",
    "Redis 数据结构操作": "数据库",
    "NoSQL数据库": "数据库",
    
    # 应该去云平台的
    "AWS EC2 管理": "云平台",
    "AWS IAM 身份管理": "云平台",
    "AWS S3 存储操作": "云平台",
    
    # 应该去前端的
    "Node.js 后端命令": "前端开发",
    "React 命令": "前端开发",
    "Vue.js 命令": "前端开发",
    "TypeScript 命令": "前端开发",
    
    # 应该去后端的
    "Python Web框架": "后端开发",
    "Python 虚拟环境": "后端开发",
    "Python 命令": "后端开发",
    "Java Spring Boot": "后端开发",
    
    # 其他
    "CI_CD 流水线": "CI_CD",
    "curl 命令": "API与认证",
    "Web API工具": "API与认证",
    "GraphQL 命令": "API与认证",
    "API与认证": "API与认证",
    "SSH 命令": "DevOps工具",
    "SSH远程操作": "DevOps工具",
    "Shell脚本模板": "DevOps工具",
    "Serverless与边缘计算": "DevOps工具",
    "Nginx 命令": "Web服务器",
    "Prometheus": "监控可观测性",
    "Grafana CLI": "监控可观测性",
    "AI_ML工具": "开发工具",
    "Claude Skills-regex": "开发工具",
    "Ansible": "基础设施",
    "Helm": "基础设施",
    "Jenkins CLI": "CI_CD",
}

def process_other():
    """处理其他目录下的模块"""
    other_path = MODULES_DIR / "其他"
    if not other_path.exists():
        print("其他目录不存在")
        return
    
    moved = []
    failed = []
    
    for module_dir in os.listdir(other_path):
        src = other_path / module_dir
        
        # 查找目标分类
        target_cat = None
        for key, value in REMAPPING.items():
            if key in module_dir or module_dir in key:
                target_cat = value
                break
        
        if not target_cat:
            # 尝试模糊匹配
            if "Docker" in module_dir or "kubectl" in module_dir or "K8s" in module_dir or "Kubernetes" in module_dir:
                target_cat = "容器编排"
            elif "Git" in module_dir:
                target_cat = "版本控制"
            elif "MySQL" in module_dir or "PostgreSQL" in module_dir or "Redis" in module_dir or "MongoDB" in module_dir or "SQL" in module_dir:
                target_cat = "数据库"
            elif "AWS" in module_dir or "Azure" in module_dir or "GCP" in module_dir:
                target_cat = "云平台"
            elif "Linux" in module_dir:
                target_cat = "Linux系统"
        
        if target_cat:
            dst = MODULES_DIR / target_cat / module_dir
            if dst.exists():
                shutil.rmtree(dst)
            try:
                shutil.move(str(src), str(dst))
                moved.append((module_dir, target_cat))
            except Exception as e:
                failed.append((module_dir, str(e)))
        else:
            print(f"  未找到分类: {module_dir}")
    
    return moved, failed

def main():
    print("处理剩余未分类模块...")
    moved, failed = process_other()
    
    print(f"\n移动成功: {len(moved)}")
    print(f"移动失败: {len(failed)}")
    
    # 打印最终统计
    print("\n最终分类统计:")
    total = 0
    for cat in sorted(os.listdir(MODULES_DIR)):
        if os.path.isdir(cat) and not cat.startswith('.') and cat != '其他':
            modules = len(os.listdir(cat))
            total += modules
            print(f"  {cat}: {modules}")
    
    print(f"\n总计: {total} modules")

if __name__ == "__main__":
    main()
