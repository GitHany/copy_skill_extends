# 命令参数详解

本文档详细说明 `commands.json` 中各命令的参数定义规范。

## 📋 参数定义规范

每个命令的 `params` 字段包含以下信息：

| 字段 | 类型 | 说明 |
|------|------|------|
| `type` | string | 参数类型：string、path、integer、boolean、enum |
| `required` | boolean | 是否为必填参数 |
| `description` | string | 参数的详细描述 |
| `example` | any | 参数的示例值 |
| `notes` | string | 注意事项、特殊说明、常见值 |
| `default` | any | 默认值（可选） |

---

## 🔍 Linux 命令参数详解

### grep - 搜索文件内容

#### 主命令
```bash
grep [options] "%{pattern}%" %{file}%
```

#### 参数说明

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `pattern` | string | ✅ | 要搜索的文本内容，支持基础正则表达式（. * + ? []） | `error` | 包含特殊字符（空格、*、?、[]、$、^等）时必须用引号包裹；搜索字面字符串建议用固定字符串模式 `grep -F` |
| `file` | path | ✅ | 要搜索的文件路径，支持通配符和多个文件（空格分隔） | `/var/log/app.log` | 不指定时从标准输入读取；多个文件用空格分隔或使用通配符如 `*.log` `/var/log/*.log` |

#### 扩展命令参数

##### 1. 递归搜索目录
```bash
grep -r "%{pattern}%" %{directory}%
```

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `pattern` | string | ✅ | 要搜索的文本内容 | `NullPointerException` | 递归搜索时会自动忽略二进制文件，除非使用 `-a` 参数 |
| `directory` | path | ✅ | 要递归搜索的目录路径，会遍历所有子目录 | `/var/log` | 深度递归可能耗时，大目录建议配合 `--include` 或 `--exclude` 过滤文件类型 |

##### 2. 忽略大小写搜索
```bash
grep -i "%{pattern}%" %{file}%
```

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `pattern` | string | ✅ | 要搜索的文本（不区分大小写） | `error` | 会匹配 ERROR、Error、eRRor 等所有大小写组合 |
| `file` | path | ✅ | 要搜索的文件路径 | `/var/log/app.log` | - |

##### 3. 显示行号
```bash
grep -n "%{pattern}%" %{file}%
```

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `pattern` | string | ✅ | 要搜索的文本内容 | `ERROR` | - |
| `file` | path | ✅ | 要搜索的文件路径 | `/var/log/app.log` | 输出格式为 `行号:匹配内容`，如 `42:ERROR database connection failed` |

##### 4. 反向搜索（不包含的内容）
```bash
grep -v "%{pattern}%" %{file}%
```

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `pattern` | string | ✅ | 要排除的文本内容 | `DEBUG` | 输出所有不包含该模式的行，常用于过滤日志中的调试信息 |
| `file` | path | ✅ | 要搜索的文件路径 | `/var/log/app.log` | - |

##### 5. 正则表达式搜索
```bash
grep -E "%{regex}%" %{file}%
```

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `regex` | string | ✅ | 扩展正则表达式（ERE），支持 + ? \| () {} 等元字符 | `ERROR\|WARN\|FATAL` | 常用正则：`^` 行首、`$` 行尾、`.` 任意字符、`*` 零或多、`+` 一或多、`?` 零或一、`\|` 或、`[]` 字符集、`()` 分组、`{n}` 精确n次、`{n,m}` n到m次 |
| `file` | path | ✅ | 要搜索的文件路径 | `/var/log/app.log` | - |

##### 6. 统计匹配次数
```bash
grep -c "%{pattern}%" %{file}%
```

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `pattern` | string | ✅ | 要统计的文本内容 | `ERROR` | - |
| `file` | path | ✅ | 要搜索的文件路径 | `/var/log/app.log` | 只输出匹配行数（整数），不显示具体内容；多个文件时每个文件单独输出 |

##### 7. 显示匹配行前后N行
```bash
grep -A %{after}% -B %{before}% "%{pattern}%" %{file}%
```

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `after` | integer | ✅ | 匹配行之后要显示的行数 | `3` | `0` 表示不显示后续行 |
| `before` | integer | ✅ | 匹配行之前要显示的行数 | `2` | `0` 表示不显示前面行；也可用 `-C N` 同时显示前后 N 行 |
| `pattern` | string | ✅ | 要搜索的文本内容 | `ERROR` | - |
| `file` | path | ✅ | 要搜索的文件路径 | `/var/log/app.log` | 匹配行与上下文之间会用 `--` 分隔 |

##### 8. 只输出匹配的文件名
```bash
grep -l "%{pattern}%" %{directory}/*.%{extension}%
```

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `pattern` | string | ✅ | 要搜索的文本内容 | `TODO` | - |
| `directory` | path | ✅ | 要搜索的目录路径 | `./src` | - |
| `extension` | string | ✅ | 文件扩展名（不含点号），用于过滤文件类型 | `py` | 常用值：py、js、ts、java、go、md、log、txt、json 等 |

---

### find - 查找文件

#### 主命令
```bash
find %{path}% -name "%{pattern}%"
```

#### 参数说明

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `path` | path | ✅ | 搜索的起始目录路径，会递归遍历所有子目录 | `/var/log` | 常用值：`.`（当前目录）、`/`（根目录）、`~`（家目录）、`/tmp` 等；注意：`/` 根目录搜索可能耗时较长 |
| `pattern` | string | ✅ | 文件名匹配模式，支持通配符 `*`（任意字符）、`?`（单字符）、`[]`（字符集） | `*.log` | 必须用引号包裹防止 shell 展开；常用模式：`*.{py,js,txt}`、`*.conf`、`data_*.*`、`*2024*` 等 |

#### 扩展命令参数

##### 1. 按文件类型查找
```bash
find %{path}% -type f -name "*.%{ext}%"
```

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `path` | path | ✅ | 搜索的起始目录 | `/home/user/projects` | - |
| `ext` | string | ✅ | 文件扩展名（不含点号） | `py` | `-type` 值：`f`=文件、`d`=目录、`l`=符号链接、`p`=命名管道、`s`=socket、`b`=块设备、`c`=字符设备 |

##### 2. 按时间查找（最近N天）
```bash
find %{path}% -mtime -%{days}%
```

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `path` | path | ✅ | 搜索的起始目录 | `/var/log` | - |
| `days` | integer | ✅ | 天数条件，数字前符号含义：`-`=小于N天、`+`=大于N天、无=正好N天 | `7` | `mtime`=修改时间、`atime`=访问时间、`ctime`=状态变更时间；`-7`=7天内修改过、`+30`=30天前修改过 |

##### 3. 按文件大小查找
```bash
find %{path}% -size +%{size}M
```

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `path` | path | ✅ | 搜索的起始目录 | `/home/user` | - |
| `size` | integer | ✅ | 文件大小阈值 | `100` | 单位：`c`=字节、`k`=KB、`M`=MB、`G`=GB；符号：`+`=大于、`-`=小于、无=等于；如 `+100M`=大于100MB |

##### 4. 查找并删除
```bash
find %{path}% -name "%{pattern}%" -delete
```

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `path` | path | ✅ | 搜索的起始目录 | `/tmp` | - |
| `pattern` | string | ✅ | 文件名匹配模式 | `*.tmp` | ⚠️ 警告：`-delete` 会直接删除匹配的文件和空目录！建议先不加 `-delete` 预览结果确认后再执行 |

##### 5. 查找并执行命令
```bash
find %{path}% -name "%{pattern}%" -exec %{cmd}% {} \;
```

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `path` | path | ✅ | 搜索的起始目录 | `/var/log` | - |
| `pattern` | string | ✅ | 文件名匹配模式 | `*.log` | - |
| `cmd` | string | ✅ | 对每个匹配文件执行的命令，`{}` 代表当前文件路径 | `gzip` | 常用命令：`gzip`（压缩）、`rm -f`（删除）、`mv {} /backup/`（移动）、`chmod 644`（改权限）；末尾 `\;` 是必需的分隔符；也可用 `+` 代替 `\;` 一次处理多个文件 |

---

## 🐳 Docker 命令参数详解

### docker run - 运行容器

#### 主命令
```bash
docker run -d --name %{container_name}% -p %{host_port}%:%{container_port}% %{image_name}%
```

#### 参数说明

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `container_name` | string | ✅ | 容器名称，用于后续操作（stop/start/logs/exec等） | `myapp` | 命名规范：小写字母、数字、连字符；不能以连字符开头；全局唯一 |
| `host_port` | integer | ✅ | 主机端口号，外部访问容器的端口 | `8080` | 范围：1-65535；需确保主机端口未被占用；常用端口：80(HTTP)、443(HTTPS)、3306(MySQL)、5432(PostgreSQL) |
| `container_port` | integer | ✅ | 容器内部应用监听的端口 | `80` | 由镜像决定，需查看镜像文档或使用 `docker inspect` 查看；Web应用常用 80/8080/3000 |
| `image_name` | string | ✅ | Docker 镜像名称，可包含标签 | `nginx:latest` | 格式：`[registry/]name[:tag]`；如 `registry.example.com/myapp:v1.0`；省略标签默认使用 `latest` |

#### 扩展命令参数

##### 1. 运行容器并挂载卷
```bash
docker run -d --name %{name}% -v %{host_path}%:%{container_path}% %{image}%
```

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `name` | string | ✅ | 容器名称 | `myapp` | - |
| `host_path` | path | ✅ | 主机上的文件或目录路径 | `/data/app` | 路径不存在时会自动创建目录；可使用绝对路径或命名卷 |
| `container_path` | path | ✅ | 容器内的挂载目标路径 | `/app/data` | 路径不存在时会自动创建；常用路径：`/etc/nginx/conf.d`、`/var/lib/mysql`、`/app/logs` |
| `image` | string | ✅ | Docker 镜像名称 | `nginx:latest` | - |

##### 2. 运行容器并设置环境变量
```bash
docker run -d --name %{name}% -e %{var}%=%{value}% %{image}%
```

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `name` | string | ✅ | 容器名称 | `myapp` | - |
| `var` | string | ✅ | 环境变量名称 | `DB_HOST` | 命名规范：大写字母、下划线；常用：`DB_HOST`、`DB_PORT`、`DB_PASSWORD`、`REDIS_URL`、`API_KEY` |
| `value` | string | ✅ | 环境变量值 | `localhost` | 包含特殊字符时需用引号；敏感信息（密码、密钥）建议使用 `--env-file` 或 Docker Secrets |
| `image` | string | ✅ | Docker 镜像名称 | `postgres:15` | - |

##### 3. 运行容器并连接网络
```bash
docker run -d --name %{name}% --network %{network_name}% %{image}%
```

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `name` | string | ✅ | 容器名称 | `myapp` | - |
| `network_name` | string | ✅ | Docker 网络名称 | `app-network` | 网络需预先创建（`docker network create`）；同一网络内容器可通过容器名互相访问 |
| `image` | string | ✅ | Docker 镜像名称 | `nginx:latest` | - |

##### 4. 交互式运行容器
```bash
docker run -it %{image}% /bin/bash
```

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `image` | string | ✅ | Docker 镜像名称 | `ubuntu:22.04` | 常用基础镜像：`ubuntu`、`alpine`、`debian`、`python`、`node`；`-i` 保持标准输入打开，`-t` 分配伪终端 |

---

### docker build - 构建镜像

#### 主命令
```bash
docker build -t %{image_name}%:%{tag}% %{context_path}%
```

#### 参数说明

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `image_name` | string | ✅ | 构建后的镜像名称 | `myapp` | 命名规范：小写字母、数字、连字符；可包含 registry 前缀如 `registry.example.com/myapp` |
| `tag` | string | ✅ | 镜像标签，通常使用版本号或 `latest` | `v1.0` | 常用标签格式：语义化版本号（`v1.0.0`）、Git 提交 SHA（`abc123`）、环境标识（`dev`/`staging`/`prod`） |
| `context_path` | path | ✅ | Docker 构建上下文路径（包含 Dockerfile 的目录） | `.` | 构建上下文会被发送到 Docker 守护进程，避免包含大文件或无关目录（使用 `.dockerignore` 排除） |

#### 扩展命令参数

##### 1. 无缓存构建
```bash
docker build --no-cache -t %{image}%:%{tag}% %{path}%
```

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `image` | string | ✅ | 镜像名称 | `myapp` | - |
| `tag` | string | ✅ | 镜像标签 | `v1.0` | - |
| `path` | path | ✅ | 构建上下文路径 | `.` | `--no-cache` 会忽略所有缓存层，重新执行每条指令，构建时间会更长 |

##### 2. 指定 Dockerfile
```bash
docker build -f %{dockerfile}% -t %{image}%:%{tag}% %{context}%
```

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `dockerfile` | path | ✅ | Dockerfile 文件路径（相对或绝对路径） | `Dockerfile.prod` | 默认使用 `./Dockerfile`；可指定不同环境的 Dockerfile 如 `Dockerfile.dev`、`Dockerfile.prod` |
| `image` | string | ✅ | 镜像名称 | `myapp` | - |
| `tag` | string | ✅ | 镜像标签 | `prod` | - |
| `context` | path | ✅ | 构建上下文路径 | `.` | 上下文路径决定哪些文件可以被 `COPY`/`ADD` 指令访问 |

---

## 🐙 Git 命令参数详解

### git pull - 拉取并合并

#### 主命令
```bash
git pull origin %{branch}%
```

#### 参数说明

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `branch` | string | ✅ | 要拉取的远程分支名称 | `main` | 常用分支：`main`/`master`（主分支）、`develop`（开发分支）、`feature/*`（功能分支）、`release/*`（发布分支）；确保本地已配置远程仓库（`git remote add`） |

#### 扩展命令参数

##### 1. 拉取并 rebase
```bash
git pull --rebase origin %{branch}%
```

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `branch` | string | ✅ | 要拉取的远程分支名称 | `main` | `--rebase` 会将本地提交移到远程提交之后，避免产生合并提交；适合保持提交历史线性；如有冲突需逐个解决并 `git rebase --continue` |

### git reset - 回退提交

#### 主命令
```bash
git reset --hard %{revision}%
git push --force origin %{remote_branch}%
```

#### 参数说明

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `revision` | string | ✅ | 要回退到的提交引用 | `HEAD~2` | 格式：`HEAD~N`（前N次提交）、`HEAD^`（父提交）、完整SHA（`abc123def`）、分支名（`main`）；`--hard` 会丢弃工作区和暂存区的所有修改，⚠️ 不可恢复！ |
| `remote_branch` | string | ✅ | 要强制推送的远程分支 | `main` | `--force` 会覆盖远程历史，⚠️ 多人协作分支慎用！建议使用 `--force-with-lease` 更安全 |

#### 扩展命令参数

##### 1. 软回退（保留工作区）
```bash
git reset --soft HEAD~%{n}%
```

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `n` | integer | ✅ | 要回退的提交数量 | `1` | `--soft` 只移动 HEAD 指针，保留暂存区和工作区的所有修改；适合重新提交或合并多个提交 |

##### 2. 混合回退（保留文件）
```bash
git reset --mixed HEAD~%{n}%
```

| 参数 | 类型 | 必填 | 说明 | 示例 | 注意事项 |
|------|------|------|------|------|----------|
| `n` | integer | ✅ | 要回退的提交数量 | `1` | `--mixed`（默认模式）移动 HEAD 并重置暂存区，但保留工作区的修改；修改的文件会变为未暂存状态（unstaged） |

---

## 📝 参数类型说明

| 类型 | 说明 | 示例值 |
|------|------|--------|
| `string` | 字符串，文本内容 | `"error"`, `"myapp"`, `"*.log"` |
| `path` | 文件/目录路径 | `/var/log`, `./src`, `~/.bashrc` |
| `integer` | 整数，数字值 | `8080`, `7`, `100` |
| `boolean` | 布尔值，true/false | `true`, `false` |
| `enum` | 枚举值，固定选项之一 | `f`/`d`/`l`, `main`/`develop`/`feature` |

---

## 🔗 相关资源

- [完整命令参考表](../references/commands-reference.md)
- [Linux 命令文档](../linux-commands/README.md)
- [Docker 命令文档](../docker-commands/README.md)
- [Git 命令文档](../git-commands/README.md)
