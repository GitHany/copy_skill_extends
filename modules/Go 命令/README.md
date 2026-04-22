# Go 命令文档

Go 语言开发完整参考文档，涵盖核心命令、Web 框架、数据库、微服务等常用操作。

## 目录

- [Go 核心命令](#go-核心命令)
- [Go 工具链](#go-工具链)
- [Web 框架](#web-框架)
- [数据库操作](#数据库操作)
- [微服务与 RPC](#微服务与-rpc)
- [实用工具库](#实用工具库)
- [Docker 部署](#docker-部署)
- [命令速查表](#命令速查表)

---

## Go 核心命令

### go mod init - 初始化模块

**基础用法**:
```bash
go mod init %{模块名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 初始化主模块 | `go mod init github.com/user/project` | 初始化为 GitHub 模块 |
| 初始化本地模块 | `go mod init mymodule` | 初始化本地模块名称 |
| 初始化带版本 | `go mod init %{模块名}% %{版本}%` | 指定模块版本 |

### go mod tidy - 整理依赖

**基础用法**:
```bash
go mod tidy
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 整理依赖 | `go mod tidy` | 添加缺失依赖，移除未使用依赖 【常用】 |
| 下载模块到缓存 | `go mod download` | 下载所有依赖到本地缓存 【常用】 |
| 查看依赖关系 | `go mod why %{包名}%` | 查看为什么需要某个依赖 |
| 图形化依赖 | `go mod graph` | 输出依赖关系图 |

### go build - 编译程序

**基础用法**:
```bash
go build %{文件或包}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 编译为可执行文件 | `go build -o %{输出名称}% %{主文件}%` | 输出名称示例：`myapp`；主文件示例：`main.go` 【常用】 |
| 编译所有包 | `go build ./...` | 编译当前目录及所有子包 【常用】 |
| 交叉编译 Linux | `GOOS=linux GOARCH=amd64 go build -o app` | 编译 Linux amd64 可执行文件 【常用】 |
| 交叉编译 Windows | `GOOS=windows GOARCH=amd64 go build -o app.exe` | 编译 Windows 可执行文件 |
| 编译为库 | `go build` | 编译为 .a 库文件 |
| 显示详细编译 | `go build -x %{文件}%` | 显示编译过程详细信息 |

### go run - 运行程序

**基础用法**:
```bash
go run %{文件}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 运行主程序 | `go run main.go` | 运行主程序文件 【常用】 |
| 带参数运行 | `go run %{文件}% %{参数}%` | 运行并传递命令行参数 |
| 编译并运行 | `go run .` | 编译并运行当前目录主程序 |

### go install - 安装程序

**基础用法**:
```bash
go install %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装可执行文件 | `go install github.com/user/tool@latest` | 安装最新版本工具 【常用】 |
| 安装指定版本 | `go install %{包名}%@%{版本}%` | 包名示例：`golang.org/x/tools/...`；版本示例：`v1.20.0` |
| 列出已安装 | `go install list` | 列出所有已安装的可执行文件 |

### go get - 获取依赖

**基础用法**:
```bash
go get %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 获取最新版本 | `go get github.com/gin-gonic/gin` | 获取最新版本的包 【常用】 |
| 获取指定版本 | `go get github.com/gin-gonic/gin@v1.9.0` | 获取指定版本 【常用】 |
| 更新到最新 | `go get -u %{包名}%` | 更新包到最新版本 |
| 获取所有依赖 | `go get ./...` | 获取所有本地依赖 |

### go version 和 go env - 版本与环境

**基础用法**:
```bash
go version
go env %{变量名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看 Go 版本 | `go version` | 显示当前 Go 版本 【常用】 |
| 查看 GOPATH | `go env GOPATH` | 显示 GOPATH 路径 |
| 查看 GOMODCACHE | `go env GOMODCACHE` | 显示模块缓存路径 【常用】 |
| 查看所有环境 | `go env` | 显示所有 Go 环境变量 |
| 设置代理 | `go env -w GOPROXY=https://goproxy.cn,direct` | 设置 Go 模块代理 【常用】 |

---

## Go 工具链

### gofmt - 代码格式化

**基础用法**:
```bash
gofmt %{文件}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 格式化文件 | `gofmt -w main.go` | 格式化并写入文件 【常用】 |
| 格式化目录 | `gofmt -w ./...` | 格式化所有 Go 文件 |
| 显示差异 | `gofmt -d main.go` | 显示格式化前后的差异 |
| 简化代码 | `gofmt -s -w %{文件}%` | 启用简化模式 【常用】 |
| 输出到 stdout | `gofmt %{文件}%` | 输出格式化结果到终端 |

### goimports - 智能导入

**基础用法**:
```bash
goimports -w %{文件}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 格式化并更新导入 | `goimports -w main.go` | 自动添加/移除 import 【常用】 |
| 格式化目录 | `goimports -w ./...` | 格式化整个项目 |
| 设置本地导入前缀 | `goimports -local "%{路径}%" -w %{文件}%` | 本地包使用本地前缀 【常用】 |

### go vet - 代码检查

**基础用法**:
```bash
go vet %{包或文件}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 检查当前包 | `go vet ./...` | 检查当前目录及所有子包 【常用】 |
| 启用所有检查 | `go vet -all %{文件}%` | 启用所有检查项 |
| 显示详细错误 | `go vet -v %{文件}%` | 显示详细检查信息 |
| 与 golint 结合 | `go vet && golint %{包}%` | 组合使用多种检查工具 |

### golint - 代码风格检查

**基础用法**:
```bash
golint %{包}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 检查包 | `golint ./...` | 检查所有包 【常用】 |
| 检查单个文件 | `golint %{文件}%` | 检查指定文件 |
| 设置最小注释长度 | `golint -min_confidence=%{浮点数}% %{包}%` | 最小置信度示例：`0.8` |

### gocyclo - 圈复杂度分析

**基础用法**:
```bash
gocyclo %{文件或函数}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 分析文件 | `gocyclo -over=%{阈值}% %{文件}%` | 阈值示例：`15`；显示超过阈值的函数 【常用】 |
| 分析所有包 | `gocyclo -over=%{阈值}% ./...` | 分析整个项目的圈复杂度 |
| 显示前 N 个复杂函数 | `gocyclo -top=%{数量}% ./...` | 数量示例：`20`；显示最复杂的函数 |
| 输出 JSON 格式 | `gocyclo -json %{文件}%` | 以 JSON 格式输出结果 |

### go test - 测试

**基础用法**:
```bash
go test %{包}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 运行所有测试 | `go test ./...` | 运行所有测试 【常用】 |
| 详细输出 | `go test -v ./...` | 显示详细测试输出 【常用】 |
| 覆盖率报告 | `go test -cover ./...` | 显示测试覆盖率 【常用】 |
| 覆盖率文件 | `go test -coverprofile=%{文件}% ./...` | 输出覆盖率到文件 【常用】 |
| 运行指定测试 | `go test -v -run %{正则}% %{包}%` | 正则示例：`TestFoo`；运行匹配测试 |
| 基准测试 | `go test -bench=. -benchmem %{包}%` | 运行基准测试并显示内存 【常用】 |
| 超时设置 | `go test -timeout %{时间}% %{包}%` | 时间示例：`30s`；设置测试超时 |
| 并行测试 | `go test -parallel %{数量}% %{包}%` | 数量示例：`4`；并行执行测试 【常用】 |
| 跳过长期测试 | `go test -short %{包}%` | 跳过耗时较长的测试 |

---

## Web 框架

### Gin 框架

**基础用法**:
```go
r := gin.Default()
// 或
r := gin.New()
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 创建默认引擎 | `r := gin.Default()` | 带日志和恢复中间件的引擎 【常用】 |
| 创建基础引擎 | `r := gin.New()` | 无中间件的基础引擎 【常用】 |
| GET 请求 | `r.GET("%{路径}%", %{处理函数}%)` | 路径示例：`/hello`；处理函数示例：`func(c *gin.Context){}` 【常用】 |
| POST 请求 | `r.POST("%{路径}%", %{处理函数}%)` | 路径示例：`/user`；处理函数示例：`func(c *gin.Context){}` 【常用】 |
| 路由组 | `r.Group("%{前缀}%")` | 前缀示例：`/api`；分组管理路由 【常用】 |
| 运行服务器 | `r.Run("%{地址}%")` | 地址示例：`:8080`；启动 HTTP 服务器 【常用】 |
| 中间件 | `r.Use(%{中间件}%)` | 中间件示例：`gin.Logger()`，`gin.Recovery()` |
| 参数绑定 | `c.ShouldBindJSON(&%{结构体}%)` | 绑定 JSON 请求体 【常用】 |

### Echo 框架

**基础用法**:
```go
e := echo.New()
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 创建实例 | `e := echo.New()` | 创建新的 Echo 实例 【常用】 |
| GET 请求 | `e.GET("%{路径}%", %{处理函数}%)` | 路径示例：`/hello`；处理函数示例：`func(c echo.Context) error {}` 【常用】 |
| POST 请求 | `e.POST("%{路径}%", %{处理函数}%)` | 路径示例：`/user` 【常用】 |
| 启动服务器 | `e.Start("%{地址}%")` | 地址示例：`:8080`；启动服务器 【常用】 |
| 中间件 | `e.Use(%{中间件}%)` | 中间件示例：`echo.Logger()`，`echo.Recover()` 【常用】 |
| 路由组 | `g := e.Group("%{前缀}%")` | 前缀示例：`/api`；分组路由 【常用】 |
| 绑定 JSON | `c.Bind(&%{结构体}%)` | 绑定请求体 【常用】 |

### Fiber 框架

**基础用法**:
```go
app := fiber.New()
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 创建应用 | `app := fiber.New(%{配置}%)` | 配置示例：`fiber.Config{AppName: "MyApp"}` 【常用】 |
| GET 请求 | `app.Get("%{路径}%", %{处理函数}%)` | 路径示例：`/hello`；处理函数示例：`func(c *fiber.Ctx) error {}` 【常用】 |
| POST 请求 | `app.Post("%{路径}%", %{处理函数}%)` | 路径示例：`/user` 【常用】 |
| 启动服务器 | `app.Listen("%{地址}%")` | 地址示例：`:8080` 【常用】 |
| 中间件 | `app.Use(%{中间件}%)` | 中间件示例：`fiber.Logger()`，`fiber.Recover()` |
| 路由组 | `g := app.Group("%{前缀}%")` | 前缀示例：`/api`；路由分组 【常用】 |

### Chi 路由器

**基础用法**:
```go
r := chi.NewRouter()
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 创建路由器 | `r := chi.NewRouter()` | 创建新的 Chi 路由器 【常用】 |
| GET 请求 | `r.Get("%{路径}%", %{处理函数}%)` | 路径示例：`/hello`；处理函数示例：`func(w http.ResponseWriter, r *http.Request) {}` 【常用】 |
| 路由组 | `r.Route("%{前缀}%", func(r chi.Router) {})` | 前缀示例：`/api`；路由分组 【常用】 |
| 中间件 | `r.Use(%{中间件}%)` | 中间件示例：`chi.URLFormat`，`logging` |
| 参数路由 | `r.Get("/users/{id}", %{处理函数}%)` | URL 参数示例：`id` 【常用】 |
| 通配符路由 | `r.Get("/static/{file:*}", %{处理函数}%)` | 通配符匹配 【常用】 |

---

## 数据库操作

### database/sql

**基础用法**:
```go
db, err := sql.Open("%{驱动}%", "%{数据源}%")
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 打开 MySQL 连接 | `sql.Open("mysql", "user:password@tcp(localhost:3306)/dbname")` | 打开 MySQL 连接 【常用】 |
| 打开 PostgreSQL 连接 | `sql.Open("postgres", "postgres://user:pass@localhost:5432/dbname")` | 打开 PostgreSQL 连接 【常用】 |
| 执行查询 | `db.Query("%{SQL}%", %{参数}%)` | SQL 示例：`SELECT * FROM users WHERE id=?` 【常用】 |
| 执行更新 | `db.Exec("%{SQL}%", %{参数}%)` | SQL 示例：`INSERT INTO users (name) VALUES (?)` 【常用】 |
| 预处理语句 | `db.Prepare("%{SQL}%")` | SQL 示例：`SELECT * FROM users WHERE id=?` 【常用】 |
| 开启事务 | `db.Begin()` | 开始事务 【常用】 |
| Ping 连接 | `db.Ping()` | 测试数据库连接 【常用】 |
| 设置最大连接数 | `db.SetMaxOpenConns(%{数量}%)` | 数量示例：`25`；设置最大打开连接数 【常用】 |
| 设置最大空闲连接 | `db.SetMaxIdleConns(%{数量}%)` | 数量示例：`5`；设置最大空闲连接数 |

### GORM

**基础用法**:
```go
db, err := gorm.Open(%{驱动}%, %{数据源}%)
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 连接 MySQL | `gorm.Open(mysql.Open("%{DSN}%"), &gorm.Config{})` | DSN 示例：`user:pass@tcp(localhost:3306)/db` 【常用】 |
| 连接 PostgreSQL | `gorm.Open(postgres.Open("%{DSN}%"), &gorm.Config{})` | DSN 示例：`host=localhost user=gorm password=gorm dbname=gorm port=9920 sslmode=disable` 【常用】 |
| 自动迁移 | `db.AutoMigrate(&%{模型}{})` | 模型示例：`&User{}`，`&Order{}` 【常用】 |
| 创建记录 | `db.Create(&%{记录}%)` | 记录示例：`&User{Name: "John"}` 【常用】 |
| 查询记录 | `db.First(&%{结果}%, %{条件}%)` | 条件示例：`&user, 1` 或 `&user, "name=John"` 【常用】 |
| 更新记录 | `db.Save(&%{记录}%)` | 保存或更新记录 【常用】 |
| 删除记录 | `db.Delete(&%{记录}%)` | 删除记录 【常用】 |
| 链式查询 | `db.Where("name = ?", "%{名称}%").First(&%{结果}%)` | 名称示例：`John`；链式条件查询 【常用】 |
| 预加载 | `db.Preload("%{关联}%).Find(&%{结果}%)` | 关联示例：`Orders`；预加载关联数据 【常用】 |

### go-sql-driver/mysql

**基础用法**:
```go
import _ "github.com/go-sql-driver/mysql"
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 注册驱动 | `import _ "github.com/go-sql-driver/mysql"` | 注册 MySQL 驱动 【常用】 |
| DSN 格式 | `user:password@tcp(localhost:3306)/dbname?charset=utf8mb4` | MySQL 连接字符串 【常用】 |
| 设置连接参数 | `user:pass@tcp(localhost:3306)/db?timeout=30s&readTimeout=30s` | 设置超时时间 |
| 字符集设置 | `user:pass@tcp(localhost:3306)/db?charset=utf8mb4&parseTime=true` | UTF8MB4 编码并解析时间 |

### pgx (PostgreSQL)

**基础用法**:
```go
conn, err := pgx.Connect(context.Background(), "%{连接字符串}%")
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 连接 PostgreSQL | `pgx.Connect(ctx, "postgres://user:pass@localhost:5432/db")` | 建立连接 【常用】 |
| 连接池配置 | `pgxpool.New(ctx, "postgres://user:pass@localhost:5432/db")` | 创建连接池 【常用】 |
| 执行查询 | `conn.Query(ctx, "%{SQL}%", %{参数}%)` | SQL 示例：`SELECT * FROM users WHERE id=$1` 【常用】 |
| 批量复制 | `conn.CopyFrom(ctx, "%{表名}%", %{列名}%, pgx.CopyFromRows(%{行}%))` | 批量插入数据 【常用】 |

---

## 微服务与 RPC

### protoc - Protocol Buffer 编译

**基础用法**:
```bash
protoc --%{语言}%_out=%{输出路径}% %{proto文件}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 编译 Go 代码 | `protoc --go_out=. --go-grpc_out=. %{proto文件}%` | 生成 Go 代码 【常用】 |
| 生成 gRPC 代码 | `protoc --go-grpc_out=. --go_out=. %{proto文件}%` | 同时生成 gRPC 代码 【常用】 |
| 指定导入路径 | `protoc --go_out=. --go-grpc_out=. -I%{导入路径}% %{proto文件}%` | 导入路径示例：`./proto` |
| 编译所有 proto | `protoc --go_out=. --go-grpc_out=. ./proto/*.proto` | 编译目录下所有 proto 文件 |
| 生成 gRPC 反射 | `protoc --go_out=plugins=grpc:. %{proto文件}%` | 生成支持反射的代码 |
| 生成 JSON 编码 | `protoc --go_out=. --go-grpc_out=. --grpc-gateway_out=. %{proto文件}%` | 生成 gRPC-Gateway 代码 【常用】 |

### gRPC 服务

**基础用法**:
```go
lis, _ := net.Listen("tcp", "%{地址}%")
grpcServer := grpc.NewServer()
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 创建 gRPC 服务器 | `grpcServer := grpc.NewServer()` | 创建新的 gRPC 服务器 【常用】 |
| 注册服务 | `pb.Register%{服务名}%Server(grpcServer, %{实现}%)` | 服务名示例：`UserService`；实现示例：`&server{}` 【常用】 |
| 启用反射 | `reflection.Register(grpcServer)` | 启用 gRPC 反射 【常用】 |
| 启动服务器 | `grpcServer.Serve(%{监听器}%)` | 启动服务监听 【常用】 |
| 连接 gRPC 服务 | `conn, err := grpc.Dial("%{地址}%", grpc.WithInsecure())` | 地址示例：`localhost:50051` 【常用】 |
| 创建 gRPC 客户端 | `client := pb.New%{服务名}%Client(conn)` | 服务名示例：`UserServiceClient` 【常用】 |

### Docker 多阶段构建 Go

**基础用法**:
```dockerfile
FROM golang:1.21 AS builder
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 多阶段构建 | `FROM golang:1.21 AS builder` | 第一阶段：构建环境 【常用】 |
| 编译 Go 程序 | `RUN CGO_ENABLED=0 GOOS=linux go build -o app %{主文件}%` | 静态编译 Go 程序 【常用】 |
| 最终镜像 | `FROM alpine:latest` | 第二阶段：运行镜像 |
| 复制二进制 | `COPY --from=builder /app /app` | 从构建阶段复制产物 |
| 设置入口点 | `ENTRYPOINT ["/app"]` | 设置容器入口点 【常用】 |
| 使用 scratch 镜像 | `FROM scratch` | 最小化运行镜像 【常用】 |
| 复制 CA 证书 | `COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/` | 复制证书到 scratch 镜像 |

---

## 实用工具库

### Cobra CLI 框架

**基础用法**:
```go
rootCmd := &cobra.Command{
  Use:   "%{命令名}%",
  Short: "%{简短描述}%",
  Run: func(cmd *cobra.Command, args []string) {},
}
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 创建根命令 | `cobra.OnInitialize()` | 初始化配置 【常用】 |
| 添加子命令 | `rootCmd.AddCommand(%{子命令}%)` | 添加子命令 【常用】 |
| 执行命令 | `rootCmd.Execute()` | 执行命令 【常用】 |
| 添加 Flags | `cmd.Flags().StringVar(&%{变量}%, "%{名称}%", "%{默认值}%", "%{描述}%")` | 绑定字符串参数 【常用】 |
| 添加持久 Flags | `cmd.PersistentFlags().StringVar(&%{变量}%, "%{名称}%", "%{默认值}%", "%{描述}%")` | 全局持久参数 【常用】 |
| 添加必填参数 | `cmd.MarkFlagRequired("%{名称}%")` | 标记参数为必填 【常用】 |

### Viper 配置管理

**基础用法**:
```go
viper.SetConfigName("%{配置文件名}%")
viper.AddConfigPath("%{搜索路径}%")
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 读取 JSON 配置 | `viper.SetConfigType("json")` | 设置配置文件类型 【常用】 |
| 设置默认值 | `viper.SetDefault("%{键}%", "%{值}%")` | 设置配置默认值 【常用】 |
| 读取环境变量 | `viper.AutomaticEnv()` | 自动读取环境变量 【常用】 |
| 读取环境变量绑定 | `viper.BindEnv("%{键}%", "%{环境变量}%")` | 绑定环境变量到配置键 【常用】 |
| 读取配置值 | `viper.GetString("%{键}%")` | 读取字符串值 【常用】 |
| 读取 Int 值 | `viper.GetInt("%{键}%")` | 读取整数值 |
| 解码到结构体 | `viper.Unmarshal(&%{结构体}%)` | 解码配置到结构体 【常用】 |
| 监听配置变化 | `viper.WatchConfig()` | 监听配置文件变化 【常用】 |

### Zap 日志库

**基础用法**:
```go
logger, _ := zap.NewProduction()
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 创建生产日志 | `zap.NewProduction()` | 生产环境高性能日志 【常用】 |
| 创建开发日志 | `zap.NewDevelopment()` | 开发环境友好日志 【常用】 |
| 创建基础日志 | `zap.NewExample()` | 演示用日志 |
| 带文件名日志 | `zap.NewProduction(zap.AddCaller())` | 添加调用者信息 【常用】 |
| 结构化日志 | `logger.Info("%{消息}%", zap.String("%{键}%", "%{值}%"))` | 键示例：`user`；值示例：`john` 【常用】 |
| 错误日志 | `logger.Error("%{消息}%", zap.Error(%{错误}%))` | 记录错误日志 【常用】 |
| 同步日志 | `defer logger.Sync()` | 确保日志写入 【常用】 |
| 采样日志 | `zap.NewProduction(zap.WrapCore(zap.NewSampler(core, time.Second, 1, 2)))` | 日志采样 |

### golang-migrate

**基础用法**:
```bash
migrate -path %{路径}% -database %{数据库URL}% up
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建迁移文件 | `migrate create -ext sql -dir %{路径}% -seq %{迁移名}%` | 路径示例：`./migrations`；迁移名示例：`add_users_table` 【常用】 |
| 执行迁移 | `migrate -path %{路径}% -database "%{URL}%" up` | 执行所有迁移 【常用】 |
| 回滚迁移 | `migrate -path %{路径}% -database "%{URL}%" down %{数量}%` | 数量示例：`1`；回滚迁移 【常用】 |
| 查看状态 | `migrate -path %{路径}% -database "%{URL}%" version` | 查看当前迁移版本 |
| 强制版本 | `migrate -path %{路径}% -database "%{URL}%" force %{版本}%` | 强制设置版本 |
| 下一步迁移 | `migrate -path %{路径}% -database "%{URL}%" goto %{版本}%` | 跳转到指定版本 |

---

## Docker 部署

### Go 应用 Dockerfile 示例

```dockerfile
# 构建阶段
FROM golang:1.21-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o app .

# 运行阶段
FROM alpine:latest
WORKDIR /root/
COPY --from=builder /app/app .
COPY --from=builder /app/config ./config
RUN apk --no-cache add ca-certificates
ENTRYPOINT ["./app"]
```

### 构建和运行

```bash
# 构建镜像
docker build -t myapp:latest .

# 运行容器
docker run -d -p 8080:8080 --name myapp myapp:latest

# 查看日志
docker logs -f myapp
```

---

## 命令速查表

| 操作 | 命令 | 说明 |
|------|------|------|
| 初始化模块 | `go mod init` | 创建 go.mod 文件 |
| 整理依赖 | `go mod tidy` | 整理 go.mod 和 go.sum |
| 编译程序 | `go build` | 编译 Go 程序 |
| 运行程序 | `go run` | 运行 Go 程序 |
| 安装工具 | `go install` | 安装可执行程序 |
| 运行测试 | `go test` | 运行单元测试 |
| 代码格式化 | `gofmt` | 格式化 Go 代码 |
| 代码检查 | `go vet` | 检查代码问题 |
| 编译 proto | `protoc` | 编译 Protocol Buffer |
| 依赖下载 | `go mod download` | 下载模块依赖 |
| 交叉编译 | `GOOS=linux GOARCH=amd64 go build` | 编译不同平台 |
| 查看环境 | `go env` | 显示 Go 环境变量 |

---

## 相关资源

- [快速开始指南](../quick-start.md)
- [Docker 命令文档](../Docker 命令/README.md)
- [Linux 命令文档](../Linux 命令/README.md)
- [完整命令参考表](../../references/commands-reference.md)
