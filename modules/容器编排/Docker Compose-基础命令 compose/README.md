# Docker Compose 命令参考

Docker Compose 是 Docker 官方提供的容器编排工具，用于定义和运行多容器 Docker 应用程序。

## 目录

- [服务启停](#服务启停)
- [状态与日志](#状态与日志)
- [构建与拉取](#构建与拉取)
- [运行与执行](#运行与执行)
- [扩缩容](#扩缩容)
- [配置验证](#配置验证)

---

## 服务启停

| 场景 | 命令 | 说明 |
|------|------|------|
| 前台启动服务 | `docker-compose up` | 启动所有服务，输出日志到前台 |
| 后台启动服务 | `docker-compose up -d` | 后台运行所有服务 |
| 带项目名启动 | `docker-compose -p myproject up -d` | 指定项目名称启动 |
| 重建并启动 | `docker-compose up --build` | 强制重新构建镜像后启动 |
| 指定文件启动 | `docker-compose -f docker-prod.yml up -d` | 使用生产环境配置文件 |
| 停止并清理 | `docker-compose down` | 停止服务并移除容器 |
| 清除数据卷 | `docker-compose down -v` | 停止服务并删除数据卷 |
| 清除全部资源 | `docker-compose down -v --rmi all` | 停止服务、删除容器、数据卷、镜像 |

---

## 状态与日志

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看容器状态 | `docker-compose ps` | 显示所有容器状态 |
| 查看指定服务状态 | `docker-compose ps web` | 显示 web 服务容器状态 |
| 查看已停止容器 | `docker-compose ps -a` | 显示所有容器（包括已停止） |
| 查看服务日志 | `docker-compose logs web` | 查看 web 服务日志 |
| 实时跟踪日志 | `docker-compose logs -f web` | 实时跟踪 web 服务日志 |
| 查看最后 N 行 | `docker-compose logs --tail 100 web` | 显示最后 100 行日志 |
| 显示时间戳 | `docker-compose logs -t web` | 在日志前显示时间戳 |
| 查看最近日志 | `docker-compose logs --since 1h` | 查看最近 1 小时的日志 |

---

## 构建与拉取

| 场景 | 命令 | 说明 |
|------|------|------|
| 构建所有镜像 | `docker-compose build` | 构建配置中的所有镜像 |
| 构建指定服务 | `docker-compose build web` | 只构建 web 服务镜像 |
| 无缓存构建 | `docker-compose build --no-cache` | 强制重新构建（不使用缓存） |
| 并行构建 | `docker-compose build --parallel` | 并行构建多个服务镜像 |
| 拉取所有镜像 | `docker-compose pull` | 拉取配置中的所有镜像 |
| 拉取指定镜像 | `docker-compose pull web` | 只拉取 web 服务镜像 |
| 并行拉取 | `docker-compose pull --parallel` | 并行拉取多个镜像 |
| 忽略拉取失败 | `docker-compose pull --ignore-pull-failures` | 忽略单个镜像拉取失败 |

---

## 运行与执行

| 场景 | 命令 | 说明 |
|------|------|------|
| 运行一次性命令 | `docker-compose run web bash` | 在 web 容器中执行 bash |
| 后台运行命令 | `docker-compose run -d web python app.py` | 后台运行一次性任务 |
| 交互式终端 | `docker-compose run -it web bash` | 进入 web 容器的交互式终端 |
| 执行后删除容器 | `docker-compose run --rm web npm test` | 执行完毕后自动删除容器 |
| 覆盖入口点 | `docker-compose run --entrypoint /bin/sh web` | 覆盖默认入口点执行 |
| 进入运行中容器 | `docker-compose exec web bash` | 进入正在运行的 web 容器 |
| 交互式 exec | `docker-compose exec -it web bash` | 进入交互式终端 |
| 指定用户执行 | `docker-compose exec -u root web apt update` | 以 root 用户执行命令 |
| 指定工作目录 | `docker-compose exec -w /app web pwd` | 在指定目录执行命令 |

---

## 扩缩容

| 场景 | 命令 | 说明 |
|------|------|------|
| 扩展服务实例 | `docker-compose scale web=3` | 将 web 服务扩展到 3 个实例 |
| 缩减服务实例 | `docker-compose scale worker=1` | 将 worker 服务缩减到 1 个实例 |
| 多服务同时扩缩 | `docker-compose scale web=3 db=1` | 同时调整多个服务的实例数 |
| 启动时指定副本 | `docker-compose up -d --scale web=5` | 启动时设置 web 服务为 5 个副本 |
| 设置副本范围 | `docker-compose up -d --scale web=2-5` | 设置 web 服务副本数范围 |

---

## 配置验证

| 场景 | 命令 | 说明 |
|------|------|------|
| 验证配置文件 | `docker-compose config` | 验证并显示合并后的配置 |
| 静默验证 | `docker-compose config -q` | 只返回验证结果（0 或 1） |
| 列出所有服务 | `docker-compose config --services` | 列出配置中的所有服务名称 |
| 列出所有卷 | `docker-compose config --volumes` | 列出配置中的数据卷 |
| 转换为 JSON | `docker-compose -f docker-compose.yml convert` | 将配置转换为规范格式 |

---

## 常用组合场景

| 场景 | 命令 | 说明 |
|------|------|------|
| 完整重新部署 | `docker-compose down -v && docker-compose build && docker-compose up -d` | 清除旧环境、构建镜像、启动服务 |
| 拉取更新重启 | `docker-compose pull && docker-compose up -d` | 拉取最新镜像并重启服务 |
| 日志排查 | `docker-compose logs -f --tail=200 web` | 实时查看 web 服务最近 200 行日志 |
| 调试进入容器 | `docker-compose exec -it web /bin/sh` | 进入容器进行调试 |
| 迁移数据 | `docker-compose exec db pg_dump -U postgres > backup.sql` | 导出数据库备份 |