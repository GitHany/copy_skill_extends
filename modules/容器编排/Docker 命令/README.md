# Docker 命令文档

Docker 容器管理完整参考文档。

## 📚 目录

- [容器管理](#容器管理)
- [镜像管理](#镜像管理)
- [Docker Compose](#docker-compose)
- [网络与卷](#网络与卷)
- [调试与排查](#调试与排查)

---

## 容器管理

### docker run - 运行容器

**基础用法**:
```bash
docker run -d --name %{容器名称}% -p %{主机端口}%:%{容器端口}% %{镜像名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 挂载卷 | `docker run -d --name %{名称}% -v %{主机路径}%:%{容器路径}% %{镜像}%` | 主机路径示例：`/data/logs`；容器路径示例：`/app/logs`；镜像示例：`nginx` 【常用】 |
| 环境变量 | `docker run -d --name %{名称}% -e %{变量}%=%{值}% %{镜像}%` | 变量示例：`MYSQL_ROOT_PASSWORD`；值示例：`password123`；镜像示例：`mysql` |
| 连接网络 | `docker run -d --name %{名称}% --network %{网络名称}% %{镜像}%` | 网络名称示例：`my_network`；镜像示例：`nginx` 【常用】 |
| 交互模式 | `docker run -it %{镜像}% /bin/bash` | 镜像示例：`ubuntu` 【常用】 |
| 后台运行 | `docker run -d %{镜像}%` | 镜像示例：`nginx` 【常用】 |

### docker ps - 查看容器

**基础用法**:
```bash
docker ps
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 所有容器 | `docker ps -a` | 查看所有容器（包括已停止的） |
| 显示大小 | `docker ps -s` | 显示容器大小 |
| 仅显示ID | `docker ps -q` | 仅列出容器ID |
| 最新容器 | `docker ps -l` | 显示最近创建的容器 |

### docker stop - 停止容器

**基础用法**:
```bash
docker stop %{容器名称或ID}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动容器 | `docker start %{容器名称或ID}%` | 容器名称示例：`myapp` 【常用】 |
| 重启容器 | `docker restart %{容器名称或ID}%` | 容器名称示例：`myapp` 【常用】 |
| 强制停止 | `docker kill %{容器名称或ID}%` | 容器名称示例：`myapp` |

### docker rm - 删除容器

**基础用法**:
```bash
docker rm %{容器名称或ID}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 强制删除 | `docker rm -f %{容器名称或ID}%` | 容器名称示例：`myapp` 【常用】 |
| 删除所有停止的 | `docker container prune` | 删除所有已停止的容器 |
| 删除容器及卷 | `docker rm -v %{容器名称}%` | 容器名称示例：`myapp` |

### docker logs - 查看日志

**基础用法**:
```bash
docker logs %{容器名称或ID}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 实时跟踪 | `docker logs -f %{容器名称}%` | 容器名称示例：`myapp` 【常用】 |
| 最后N行 | `docker logs --tail %{行数}% %{容器名称}%` | 行数示例：`100`；容器名称示例：`myapp` 【常用】 |
| 指定时间后 | `docker logs --since %{时间}% %{容器名称}%` | 时间示例：`30m` 或 `2024-01-01`；容器名称示例：`myapp` |

### docker exec - 进入容器

**基础用法**:
```bash
docker exec -it %{容器名称或ID}% /bin/bash
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 执行单命令 | `docker exec %{容器名称}% %{命令}%` | 容器名称示例：`myapp`；命令示例：`ls -la` 【常用】 |
| 指定用户 | `docker exec -u %{用户名}% -it %{容器名称}% /bin/bash` | 用户名示例：`root`；容器名称示例：`myapp` 【常用】 |
| 后台执行 | `docker exec -d %{容器名称}% %{命令}%` | 容器名称示例：`myapp`；命令示例：`touch /tmp/file` |

---

## 镜像管理

### docker pull - 拉取镜像

**基础用法**:
```bash
docker pull %{镜像名称}%:%{标签}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 最新镜像 | `docker pull %{镜像名称}%` | 镜像名称示例：`nginx` 【常用】 |
| 指定仓库 | `docker pull %{仓库地址}%/%{镜像}%:%{标签}%` | 仓库地址示例：`registry.example.com`；镜像示例：`myapp`；标签示例：`latest` |

### docker images - 查看镜像

**基础用法**:
```bash
docker images
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 仅显示ID | `docker images -q` | 仅列出镜像ID |
| 中间镜像 | `docker images -a` | 显示所有中间镜像 |
| 按名称过滤 | `docker images %{镜像名称}%` | 镜像名称示例：`nginx` 【常用】 |
| 格式化显示 | `docker images --format "{{.Repository}}:{{.Tag}}"` | 自定义输出格式 |

### docker rmi - 删除镜像

**基础用法**:
```bash
docker rmi %{镜像名称或ID}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 强制删除 | `docker rmi -f %{镜像名称或ID}%` | 镜像名称示例：`nginx` |
| 删除未使用 | `docker image prune -a` | 删除所有未使用的镜像 |
| 删除悬空镜像 | `docker image prune` | 删除悬空（无名）镜像 |

### docker build - 构建镜像

**基础用法**:
```bash
docker build -t %{镜像名称}%:%{标签}% %{Dockerfile路径}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 无缓存构建 | `docker build --no-cache -t %{镜像}%:%{标签}% %{路径}%` | 镜像示例：`myapp`；标签示例：`latest`；路径示例：`.` 【常用】 |
| 指定Dockerfile | `docker build -f %{Dockerfile文件}% -t %{镜像}%:%{标签}% %{上下文}%` | Dockerfile示例：`Dockerfile.prod`；镜像示例：`myapp`；标签示例：`v1.0`；上下文示例：`.` 【常用】 |
| BuildKit构建 | `DOCKER_BUILDKIT=1 docker build -t %{镜像}%:%{标签}% %{路径}%` | 镜像示例：`myapp`；标签示例：`latest`；路径示例：`.` 【常用】 |

### docker push - 推送镜像

**基础用法**:
```bash
docker push %{镜像名称}%:%{标签}%
```

---

## Docker Compose

### docker-compose up - 启动服务

**基础用法**:
```bash
docker-compose up -d
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动并重建 | `docker-compose up -d --build` | 启动服务并重新构建镜像 【常用】 |
| 启动指定服务 | `docker-compose up -d %{服务1}% %{服务2}%` | 服务名称示例：`web` 【常用】 |
| 前台启动 | `docker-compose up` | 前台运行并显示日志 |

### docker-compose down - 停止服务

**基础用法**:
```bash
docker-compose down
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 停止并删除卷 | `docker-compose down -v` | 停止服务并删除关联的数据卷 |
| 停止并删除镜像 | `docker-compose down --rmi local` | 停止服务并删除本地镜像 |
| 停止并删除所有 | `docker-compose down -v --rmi all --remove-orphans` | 完整清理：停止服务、删除卷、删除镜像、删除孤儿服务 |

### docker-compose ps - 查看服务

**基础用法**:
```bash
docker-compose ps
```

### docker-compose logs - 查看日志

**基础用法**:
```bash
docker-compose logs -f %{服务名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 所有服务日志 | `docker-compose logs -f` | 查看所有服务日志 |
| 最后N行 | `docker-compose logs --tail=%{行数}% %{服务}%` | 行数示例：`100`；服务名称示例：`web` 【常用】 |

### docker-compose build - 构建服务

**基础用法**:
```bash
docker-compose build
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 构建指定服务 | `docker-compose build %{服务名称}%` | 服务名称示例：`web` 【常用】 |
| 无缓存构建 | `docker-compose build --no-cache` | 不使用缓存重新构建 |

---

## 网络与卷

### docker network create - 创建网络

**基础用法**:
```bash
docker network create %{网络名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看网络列表 | `docker network ls` | 列出所有Docker网络 |
| 查看网络详情 | `docker network inspect %{网络名称}%` | 网络名称示例：`my_network` 【常用】 |
| 删除网络 | `docker network rm %{网络名称}%` | 网络名称示例：`my_network` 【常用】 |
| 创建桥接网络 | `docker network create --driver bridge %{网络名称}%` | 网络名称示例：`bridge_net` |

### docker volume create - 创建卷

**基础用法**:
```bash
docker volume create %{卷名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看卷列表 | `docker volume ls` | 列出所有数据卷 |
| 查看卷详情 | `docker volume inspect %{卷名称}%` | 卷名称示例：`my_volume` 【常用】 |
| 删除未使用卷 | `docker volume prune` | 删除所有未使用的卷 |
| 删除指定卷 | `docker volume rm %{卷名称}%` | 卷名称示例：`my_volume` 【常用】 |

---

## 调试与排查

### docker inspect - 查看详情

**基础用法**:
```bash
docker inspect %{容器或镜像名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看IP地址 | `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' %{容器}%` | 容器名称示例：`myapp` 【常用】 |
| 查看挂载点 | `docker inspect -f '{{json .Mounts}}' %{容器}%` | 容器名称示例：`myapp` 【常用】 |
| 查看配置信息 | `docker inspect -f '{{json .Config}}' %{容器}%` | 容器名称示例：`myapp` |

### docker stats - 查看资源使用

**基础用法**:
```bash
docker stats
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定容器 | `docker stats %{容器名称}%` | 容器名称示例：`myapp` 【常用】 |
| 一次性查看 | `docker stats --no-stream` | 仅显示一次统计信息 |
| 格式化显示 | `docker stats --no-stream --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}"` | 自定义表格格式 |

### docker cp - 复制文件

**基础用法**:
```bash
docker cp %{源路径}% %{容器名称}%:%{目标路径}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 从主机到容器 | `docker cp %{主机路径}% %{容器名称}%:%{容器路径}%` | 主机路径示例：`/data/config.json`；容器名称示例：`myapp`；容器路径示例：`/app/config.json` 【常用】 |
| 从容器到主机 | `docker cp %{容器名称}%:%{容器路径}% %{主机路径}%` | 容器名称示例：`myapp`；容器路径示例：`/app/logs/app.log`；主机路径示例：`/data/app.log` 【常用】 |

---

## 💡 实用场景示例

### 场景 1: 部署 Web 应用

```bash
# 1. 构建镜像
docker build -t myapp:v1.0 .

# 2. 创建网络
docker network create app-network

# 3. 运行应用容器
docker run -d \
  --name myapp \
  --network app-network \
  -p 8080:80 \
  -e DB_HOST=db \
  -e DB_PASSWORD=secret \
  myapp:v1.0

# 4. 运行数据库容器
docker run -d \
  --name db \
  --network app-network \
  -v db-data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=secret \
  mysql:8.0

# 5. 查看日志
docker logs -f myapp
```

### 场景 2: Docker Compose 部署

```yaml
# docker-compose.yml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "8080:80"
    environment:
      - DB_HOST=db
      - DB_PASSWORD=secret
    depends_on:
      - db
    networks:
      - app-network

  db:
    image: mysql:8.0
    volumes:
      - db-data:/var/lib/mysql
    environment:
      - MYSQL_ROOT_PASSWORD=secret
    networks:
      - app-network

volumes:
  db-data:

networks:
  app-network:
```

```bash
# 启动服务
docker-compose up -d

# 查看状态
docker-compose ps

# 查看日志
docker-compose logs -f app

# 停止服务
docker-compose down
```

### 场景 3: 清理 Docker 资源

```bash
# 停止所有容器
docker stop $(docker ps -q)

# 删除所有容器
docker rm $(docker ps -aq)

# 删除未使用的镜像
docker image prune -a

# 删除未使用的卷
docker volume prune

# 删除未使用的网络
docker network prune

# 一键清理
docker system prune -a --volumes
```

---

## 📊 命令速查表

| 操作 | 命令 | 说明 |
|------|------|------|
| 运行容器 | `docker run` | 创建并启动容器 |
| 查看容器 | `docker ps` | 列出运行中的容器 |
| 停止容器 | `docker stop` | 停止运行中的容器 |
| 启动容器 | `docker start` | 启动已停止的容器 |
| 删除容器 | `docker rm` | 删除已停止的容器 |
| 查看日志 | `docker logs` | 查看容器日志 |
| 进入容器 | `docker exec` | 在容器中执行命令 |
| 拉取镜像 | `docker pull` | 从仓库下载镜像 |
| 构建镜像 | `docker build` | 从Dockerfile构建 |
| 删除镜像 | `docker rmi` | 删除本地镜像 |
| 查看镜像 | `docker images` | 列出本地镜像 |
| 推送镜像 | `docker push` | 推送到仓库 |
| 查看详情 | `docker inspect` | 查看详细信息 |
| 查看统计 | `docker stats` | 查看资源使用 |
| 复制文件 | `docker cp` | 主机与容器间复制 |

---

## 🔗 相关资源

- [快速开始指南](../quick-start.md)
- [Linux 命令文档](../linux-commands/README.md)
- [完整命令参考表](../../references/commands-reference.md)