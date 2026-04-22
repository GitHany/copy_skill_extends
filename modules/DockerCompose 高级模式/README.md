# Docker Compose 高级模式命令参考

本文档涵盖 Docker Compose 进阶用法，包括多文件编排、网络配置、数据卷管理、多环境部署和健康检查等高级模式。

## 目录

- [多文件编排](#多文件编排)
- [网络高级配置](#网络高级配置)
- [数据卷高级配置](#数据卷高级配置)
- [多环境部署](#多环境部署)
- [健康检查配置](#健康检查配置)
- [编排与服务管理](#编排与服务管理)
- [资源清理与维护](#资源清理与维护)

---

## 多文件编排

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定单文件启动 | `docker-compose -f docker-compose.yml up -d` | 使用特定配置文件启动 |
| 合并多文件配置 | `docker-compose -f base.yml -f prod.yml up -d` | 按顺序合并配置，后者覆盖前者 |
| 合并三个配置文件 | `docker-compose -f base.yml -f app.yml -f override.yml up -d` | 多层级配置合并 |
| 指定项目名称 | `docker-compose -p myapp -f docker-prod.yml up -d` | 使用自定义项目名 |
| 查看合并后配置 | `docker-compose -f base.yml -f prod.yml config` | 验证并输出最终合并配置 |
| 输出服务列表 | `docker-compose config --services` | 列出合并配置中的所有服务 |
| 输出卷列表 | `docker-compose config --volumes` | 列出合并配置中的所有卷 |
| 指定 env 文件 | `docker-compose --env-file .env.prod config` | 使用指定的环境变量文件 |
| 跨目录引用文件 | `docker-compose -f ../common/base.yml up -d` | 引用上级目录的配置文件 |

---

## 网络高级配置

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建自定义网络 | `docker network create --driver bridge mynet` | 创建桥接网络 |
| 创建 Overlay 网络 | `docker network create --driver overlay myoverlay` | 创建 Swarm Overlay 网络 |
| 查看所有网络 | `docker network ls` | 列出所有 Docker 网络 |
| 查看网络详情 | `docker network inspect mynet` | 查看网络详细配置和连接容器 |
| 连接容器到网络 | `docker network connect mynet container_name` | 将运行中的容器连接到网络 |
| 断开容器网络 | `docker network disconnect mynet container_name` | 从网络中断开容器 |
| 删除未用网络 | `docker network prune` | 删除所有未使用的网络 |
| 删除指定网络 | `docker network rm mynet` | 删除指定网络（需先断开容器） |
| 查看容器网络 | `docker inspect container_name --format '{{json .NetworkSettings.Networks}}'` | 查看容器已连接的网络 |
| DNS 解析测试 | `docker-compose exec -it web ping db` | 测试服务间 DNS 解析 |
| 查看容器 hosts | `docker-compose exec web cat /etc/hosts` | 查看容器内部 hosts 文件 |
| 查看 DNS 服务器 | `docker-compose exec web cat /etc/resolv.conf` | 查看容器 DNS 配置 |

**docker-compose.yml 网络配置示例:**

```yaml
services:
  web:
    networks:
      front_net:
      back_net:
        aliases:
          - web.internal
  db:
    networks:
      back_net:

networks:
  front_net:
    driver: bridge
    ipam:
      config:
        - subnet: 172.28.0.0/16
  back_net:
    driver: bridge
    external: true
```

---

## 数据卷高级配置

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建命名卷 | `docker volume create mydata` | 创建命名数据卷 |
| 查看所有卷 | `docker volume ls` | 列出所有数据卷 |
| 查看卷详情 | `docker volume inspect mydata` | 查看卷的挂载点和驱动信息 |
| 删除未用卷 | `docker volume prune` | 删除所有未使用的卷 |
| 删除指定卷 | `docker volume rm mydata` | 删除指定数据卷（容器需先停止） |
| 备份卷数据 | `docker run --rm -v mydata:/data -v $(pwd):/backup alpine tar cvf /backup/volume_backup.tar -C /data .` | 备份卷数据到 tar 包 |
| 恢复卷数据 | `docker run --rm -v mydata:/data -v $(pwd):/backup alpine tar xvf /backup/volume_backup.tar -C /data` | 从备份恢复卷数据 |
| 复制卷数据 | `docker run --rm -v src_data:/src -v dest_data:/dest alpine cp -r /src/. /dest/` | 在卷之间复制数据 |
| 查看卷使用情况 | `docker volume ls -f dangling=true` | 列出未使用的卷（悬空卷） |

**docker-compose.yml 卷配置示例:**

```yaml
services:
  db:
    volumes:
      - db_data:/var/lib/postgresql/data
      - ./backup:/backup
      - /host/path:/container/path:ro

volumes:
  db_data:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: /data/db

# 绑定挂载示例
# ./backup:/backup (同步读写)
# /host/path:/container/path:ro (只读绑定)
# db_data:/var/lib/data (命名卷)
```

---

## 多环境部署

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动开发模式 | `docker-compose up -d` | 使用默认配置（读取 docker-compose.yml + docker-compose.override.yml） |
| 启动生产模式 | `docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d` | 生产环境配置覆盖默认 |
| 本地开发覆盖 | `docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d` | 开发环境特定配置 |
| 启用 profile | `docker-compose --profile frontend up -d` | 启用指定 profile 的服务 |
| 多个 profile | `docker-compose --profile frontend --profile monitoring up -d` | 同时启用多个 profile |
| 查看所有 profile | `docker-compose config --profiles` | 列出配置中的所有 profile |
| 使用 .env 文件 | `docker-compose --env-file .env up -d` | 指定环境变量文件 |
| 设置 Compose 项目名 | `docker-compose -p myproject up -d` | 设置项目名称（默认目录名） |
| 显示当前环境 | `docker-compose config | grep -E "image|environment|SECRET"` | 检查当前加载的配置 |

**docker-compose.override.yml 示例:**

```yaml
# docker-compose.override.yml (自动被 docker-compose up 读取)
services:
  web:
    environment:
      - NODE_ENV=development
    ports:
      - "3000:3000"
    volumes:
      - ./src:/app/src
```

**docker-compose.prod.yml 示例:**

```yaml
# docker-compose.prod.yml
services:
  web:
    image: myapp:production
    restart: always
    environment:
      - NODE_ENV=production
    deploy:
      replicas: 3
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
```

**profile 配置示例:**

```yaml
services:
  web:
    profiles:
      - frontend
  worker:
    profiles:
      - background
  admin:
    profiles:
      - admin
  prometheus:
    profiles:
      - monitoring
  grafana:
    profiles:
      - monitoring
    depends_on:
      - prometheus
```

---

## 健康检查配置

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看服务健康状态 | `docker-compose ps` | 显示各容器健康状态（healthy/unhealthy/starting） |
| 检查容器健康 | `docker inspect --format='{{.State.Health.Status}}' container_name` | 查看容器健康检查状态 |
| 查看健康日志 | `docker inspect --format='{{json .State.Health.Log}}' container_name` | 查看健康检查失败日志 |
| 强制重新检测 | `docker healthcheck inspect --format='{{.Test}}' container_name` | 查看健康检查命令 |
| 手动触发健康检查 | `docker exec container_name wget --spider http://localhost:8080/health` | 手动测试健康端点 |
| 查看健康配置 | `docker inspect container_name | jq '.[].Config.Healthcheck'` | 查看健康检查配置详情 |

**docker-compose.yml 健康检查配置:**

```yaml
services:
  web:
    image: myapp:latest
    healthcheck:
      test: ["CMD", "wget", "--spider", "-q", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  db:
    image: postgres:15
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
```

**健康检查参数说明:**

| 参数 | 说明 | 示例 |
|------|------|------|
| test | 检查命令（CMD / CMD-SHELL） | `["CMD", "curl", "-f", "http://localhost"]` |
| interval | 检查间隔 | `30s` |
| timeout | 超时时间 | `10s` |
| retries | 失败重试次数 | `3` |
| start_period | 启动宽限期 | `40s` |

**Liveness vs Readiness 区别:**

| 类型 | 用途 | 示例 |
|------|------|------|
| Liveness | 容器是否存活（重启判定） | `pg_isready` 检测进程 |
| Readiness | 服务是否就绪（流量调度） | `curl /ready` 检测应用 |

---

## 编排与服务管理

| 场景 | 命令 | 说明 |
|------|------|------|
| 重启所有服务 | `docker-compose restart` | 重启所有容器 |
| 重启指定服务 | `docker-compose restart web` | 只重启 web 服务 |
| 停止所有服务 | `docker-compose stop` | 优雅停止所有容器（发送 SIGTERM） |
| 强制停止服务 | `docker-compose kill` | 强制终止容器（发送 SIGKILL） |
| 删除已停止容器 | `docker-compose rm` | 移除已停止的容器 |
| 删除所有容器 | `docker-compose rm -s` | 停止后删除所有容器 |
| 强制删除（含运行中） | `docker-compose rm -fs` | 强制删除所有容器（包括运行中的） |
| 暂停服务 | `docker-compose pause web` | 暂停 web 服务（挂起进程） |
| 恢复服务 | `docker-compose unpause web` | 恢复已暂停的服务 |
| 推送镜像 | `docker-compose push` | 推送所有服务的镜像到仓库 |
| 推送指定镜像 | `docker-compose push web` | 只推送 web 服务的镜像 |
| 生命周期完整流程 | `docker-compose down -v && docker-compose build --no-cache && docker-compose up -d` | 清卷->重建->启动 |

---

## 资源清理与维护

| 场景 | 命令 | 说明 |
|------|------|------|
| 清理已停止容器 | `docker-compose rm` | 删除已停止的容器 |
| 清理未使用镜像 | `docker image prune -a` | 删除所有未使用的镜像 |
| 清理悬空卷 | `docker volume prune` | 删除未使用的卷 |
| 清理未使用网络 | `docker network prune` | 删除未使用的网络 |
| 完整清理 | `docker system prune -a --volumes` | 清理所有未使用的容器、镜像、网络、卷 |
| 查看资源占用 | `docker stats` | 查看所有容器资源使用情况 |
| 查看服务依赖 | `docker-compose ps --format "table {{.Name}}\t{{.Status}}"` | 格式化显示服务状态 |
| 强制重建服务 | `docker-compose up -d --force-recreate` | 强制重新创建容器 |
| 构建时拉取最新 | `docker-compose build --pull` | 每次构建前拉取最新基础镜像 |
| 排除构建缓存 | `docker-compose build --no-cache` | 不使用缓存进行构建 |

---

## 常用组合场景

| 场景 | 命令 | 说明 |
|------|------|------|
| 生产环境启动 | `docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d --scale web=3` | 生产配置 + 扩缩容 |
| 开发调试模式 | `docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d` | 开发覆盖配置 |
| 完整重建部署 | `docker-compose down -v && docker-compose build --no-cache && docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d` | 干净重建生产部署 |
| 日志排查完整版 | `docker-compose logs -f --tail=500 --timestamps web` | 带时间戳的实时日志 |
| 进入容器调试 | `docker-compose exec -it web /bin/sh` | 交互式 shell 调试 |
| 数据库备份 | `docker-compose exec -T db pg_dump -U postgres -d mydb > backup_$(date +%Y%m%d).sql` | 带日期的数据库备份 |
| 查看服务依赖图 | `docker-compose ps --format "{{.Name}}: {{.Status}}"` | 列出所有服务及其状态 |
| 健康检查验证 | `docker inspect --format='{{.State.Health.Status}}' $(docker-compose ps -q web)` | 检查 web 服务健康状态 |
| 网络连通性测试 | `docker-compose run --rm web ping -c 3 db` | 测试 web 到 db 的网络连通性 |