# Node.js 后端命令文档

Node.js 后端开发完整参考文档，涵盖包管理、框架操作、API开发、生产环境部署等核心场景。

## 目录

- [包管理器](#包管理器)
- [版本管理](#版本管理)
- [框架脚手架](#框架脚手架)
- [API开发](#api开发)
- [数据库连接](#数据库连接)
- [认证与安全](#认证与安全)
- [验证与中间件](#验证与中间件)
- [生产环境](#生产环境)

---

## 包管理器

### npm install - 安装依赖

**基础用法**:
```bash
npm install %{包名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装生产依赖 | `npm install %{包名}% --save` | 包名示例：`express` 【常用】 |
| 安装开发依赖 | `npm install %{包名}% --save-dev` | 包名示例：`nodemon` 【常用】 |
| 全局安装 | `npm install -g %{包名}%` | 包名示例：`pm2` 【常用】 |
| 安装特定版本 | `npm install %{包名}%@%{版本号}%` | 包名示例：`express`；版本示例：`4.18.0` 【常用】 |
| 安装所有依赖 | `npm install` | 根据 package.json 安装 【常用】 |
| 安装并保存精确版本 | `npm install %{包名}% --save-exact` | 包名示例：`lodash` |

### npm update - 更新依赖

**基础用法**:
```bash
npm update %{包名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 更新所有依赖 | `npm update` | 更新 package.json 中所有依赖 |
| 检查过时的包 | `npm outdated` | 显示可更新的包列表 【常用】 |
| 更新到最新版本 | `npm install %{包名}%@latest` | 包名示例：`typescript` 【常用】 |

### npm audit - 安全审计

**基础用法**:
```bash
npm audit
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 修复安全漏洞 | `npm audit fix` | 自动修复可修复的漏洞 【常用】 |
| 强制修复 | `npm audit fix --force` | 强制修复所有漏洞 |
| 高严重性修复 | `npm audit fix --audit-level=high` | 仅修复高严重性漏洞 |
| 生成报告 | `npm audit --json` | 输出 JSON 格式报告 |

### npm ci - 干净安装

**基础用法**:
```bash
npm ci
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 清理安装 | `npm ci --legacy-peer-deps` | 使用旧版依赖解析 【常用】 |
| 仅安装生产依赖 | `npm ci --omit=dev` | 跳过 devDependencies |
| 跳过脚本 | `npm ci --ignore-scripts` | 跳过 lifecycle scripts |

### yarn / pnpm 命令

**常用命令对照**:

| 场景 | Yarn | PNPM |
|------|------|------|
| 安装依赖 | `yarn install` | `pnpm install` 【常用】 |
| 添加依赖 | `yarn add %{包}%` | `pnpm add %{包}%` 【常用】 |
| 开发依赖 | `yarn add %{包}% -D` | `pnpm add %{包}% -D` 【常用】 |
| 删除依赖 | `yarn remove %{包}%` | `pnpm remove %{包}%` 【常用】 |
| 更新依赖 | `yarn up` | `pnpm update` 【常用】 |
| 运行脚本 | `yarn %{脚本名}%` | `pnpm %{脚本名}%` 【常用】 |

---

## 版本管理

### nvm - Node版本管理器

**基础用法**:
```bash
nvm install %{版本号}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 列出可用版本 | `nvm ls-remote` | 显示所有可用版本 |
| 安装LTS版本 | `nvm install --lts` | 安装最新 LTS 版本 【常用】 |
| 使用特定版本 | `nvm use %{版本号}%` | 版本示例：`18.16.0` 【常用】 |
| 设为默认版本 | `nvm alias default %{版本}%` | 版本示例：`18.16.0` 【常用】 |
| 查看已安装 | `nvm ls` | 列出已安装的版本 |
| 卸载版本 | `nvm uninstall %{版本号}%` | 版本示例：`16.0.0` |

### n - 轻量版本管理

**基础用法**:
```bash
n %{版本号}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装最新稳定版 | `n lts` | 安装最新 LTS 版本 |
| 安装最新版本 | `n latest` | 安装最新版 Node.js 【常用】 |
| 在当前目录使用 | `n` | 进入交互式选择版本 |

---

## 框架脚手架

### Express 脚手架

**基础用法**:
```bash
npx express-generator %{项目名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 生成带视图的项目 | `npx express-generator --view=ejs %{项目名}%` | 项目名示例：`myapp` 【常用】 |
| 指定模板引擎 | `npx express-generator --view=pug %{项目名}%` | 使用 pug 模板 【常用】 |
| 使用 TypeScript | `npx express-generator --ts %{项目名}%` | 生成 TypeScript 项目 |
| 当前目录生成 | `npx express-generator .` | 在当前目录生成项目 |

### NestJS CLI

**基础用法**:
```bash
nest new %{项目名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建新项目 | `nest new %{项目名}% --package-manager npm` | 项目名示例：`my-nest-app` 【常用】 |
| 创建资源 | `nest g resource %{名称}%` | 名称示例：`users` 【常用】 |
| 生成模块 | `nest g module %{模块名}%` | 模块名示例：`auth` |
| 生成控制器 | `nest g controller %{名称}%` | 名称示例：`users` |
| 生成服务 | `nest g service %{名称}%` | 名称示例：`users` |
| 生成守卫 | `nest g guard %{名称}%` | 名称示例：`auth` |
| 构建项目 | `nest build` | 编译 TypeScript 【常用】 |
| 启动项目 | `nest start` | 启动开发服务器 【常用】 |
| 开发模式启动 | `nest start --watch` | 热重载开发模式 【常用】 |
| 生产模式启动 | `nest start --entryFile main` | 生产环境启动 |

### Koa.js 快速创建

**基础用法**:
```bash
npx koa-generator %{项目名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 生成项目 | `npx koa-generator myapp` | 创建 Koa 项目 【常用】 |
| 指定模板 | `npx koa-generator --ejs myapp` | 使用 ejs 模板引擎 |
| 当前目录创建 | `npx koa-generator .` | 在当前目录初始化 |

---

## API开发

### REST API 快速搭建

**基础用法**:
```bash
# 初始化项目
npm init -y
npm install express
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 REST 路由 | 使用 express.Router() 创建模块化路由 | 【常用】 |
| 启动服务 | `node app.js` | 启动 Express 应用 【常用】 |
| 开发热重载 | `nodemon app.js` | 使用 nodemon 监听变化 【常用】 |
| 设置环境 | `NODE_ENV=production node app.js` | 生产环境启动 |

### Middleware 中间件配置

**常用中间件安装**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 日志中间件 | `npm install morgan --save` | HTTP 请求日志 【常用】 |
| 请求体解析 | `npm install body-parser --save` | 解析 JSON/表单数据 【常用】 |
| 压缩响应 | `npm install compression --save` | Gzip 压缩 【常用】 |
| 请求ID追踪 | `npm install uuid --save` | 生成唯一请求ID |

### 路由组织

```bash
# Express 路由结构示例
app.use('/api/users', require('./routes/users'));
app.use('/api/products', require('./routes/products'));
```

---

## 数据库连接

### PostgreSQL (pg)

**基础用法**:
```bash
npm install pg --save
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 连接池配置 | 使用 Pool 连接数据库 | 【常用】 |
| 执行查询 | `await pool.query('SELECT * FROM users')` | 异步查询 |
| 事务处理 | `await pool.query('BEGIN') ... 'COMMIT'` | 事务操作 |

### MySQL2

**基础用法**:
```bash
npm install mysql2 --save
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 连接数据库 | 使用 createPool 创建连接池 | 【常用】 |
| 预处理语句 | `connection.execute(sql, params)` | 防止 SQL 注入 【常用】 |
| 连接池选项 | `{ connectionLimit: 10, waitForConnections: true }` | 连接池配置 |

### MongoDB (mongoose)

**基础用法**:
```bash
npm install mongoose --save
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 连接MongoDB | `mongoose.connect('mongodb://localhost:27017/db')` | 连接数据库 【常用】 |
| 定义模型 | `mongoose.model('User', userSchema)` | 定义数据模型 【常用】 |
| 断开连接 | `mongoose.disconnect()` | 关闭连接 |

---

## 认证与安全

### Passport 认证

**基础用法**:
```bash
npm install passport passport-local passport-jwt --save
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 初始化Passport | `app.use(passport.initialize())` | 初始化中间件 |
| 本地策略 | 配置 LocalStrategy 进行用户名密码认证 | 【常用】 |
| JWT策略 | 配置 JwtStrategy 进行 Token 认证 | 【常用】 |
| 保护路由 | `passport.authenticate('jwt', { session: false })` | 路由保护 |

### JWT (jsonwebtoken)

**基础用法**:
```bash
npm install jsonwebtoken --save
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 生成Token | `jwt.sign(payload, secret, { expiresIn: '1h' })` | 生成 Token 【常用】 |
| 验证Token | `jwt.verify(token, secret)` | 验证 Token 【常用】 |
| 解码Token | `jwt.decode(token)` | 不验证直接解码 |

### CORS 跨域配置

**基础用法**:
```bash
npm install cors --save
```

**扩展配置**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 允许所有来源 | `app.use(cors())` | 允许所有跨域请求 【常用】 |
| 限制来源 | `cors({ origin: 'http://localhost:3000' })` | 指定允许的来源 |
| 允许凭证 | `cors({ credentials: true, origin: true })` | 允许Cookie跨域 |
| 暴露响应头 | `cors({ exposedHeaders: ['Content-Range'] })` | 暴露自定义头 |

### Helmet 安全头

**基础用法**:
```bash
npm install helmet --save
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启用所有安全头 | `app.use(helmet())` | 启用全部安全中间件 【常用】 |
| 内容安全策略 | `helmet.contentSecurityPolicy()` | 防止 XSS |
| 隐藏X-Powered-By | `helmet.hidePoweredBy()`` | 隐藏技术栈信息 |
| HSTS配置 | `helmet.hsts({ maxAge: 31536000 })` | 强制 HTTPS |

---

## 验证与中间件

### Joi 数据验证

**基础用法**:
```bash
npm install joi --save
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 定义验证 schema | `Joi.object({ name: Joi.string().required() })` | 【常用】 |
| 验证请求体 | `schema.validate(req.body)` | 验证请求数据 |
| 自定义错误消息 | `Joi.string().required().messages(...)` | 自定义提示 |

### Zod 数据验证

**基础用法**:
```bash
npm install zod --save
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 定义 schema | `z.object({ name: z.string() })` | 【常用】 |
| 验证数据 | `schema.parse(data)` | 解析并验证 |
| 类型推断 | `type User = z.infer<typeof UserSchema>`` | 从 schema 推断类型 |

### express-validator

**基础用法**:
```bash
npm install express-validator --save
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 定义验证器 | `body('email').isEmail()` | 验证邮箱格式 【常用】 |
| 自定义验证 | `body('password').custom(value => ...)` | 自定义验证逻辑 |
| 验证中间件 | `validationResult(req)` | 获取验证结果 |

---

## 生产环境

### PM2 进程管理

**基础用法**:
```bash
npm install -g pm2
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动应用 | `pm2 start app.js` | 启动 Node.js 应用 【常用】 |
| 启动并命名 | `pm2 start app.js --name %{名称}%` | 名称示例：`api-server` 【常用】 |
| 列出进程 | `pm2 list` | 查看所有进程 【常用】 |
| 查看日志 | `pm2 logs` | 查看实时日志 【常用】 |
| 实时监控 | `pm2 monit` | 实时监控 CPU/内存 |
| 重启应用 | `pm2 restart %{名称}%` | 重启指定应用 【常用】 |
| 停止应用 | `pm2 stop %{名称}%` | 停止指定应用 |
| 删除进程 | `pm2 delete %{名称}%` | 删除进程 |
| 保存进程列表 | `pm2 save` | 保存当前进程列表 |
| 开机自启 | `pm2 startup` | 配置开机自启动 |

### PM2 集群模式

**基础用法**:
```bash
pm2 start app.js -i max
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 最大核心运行 | `pm2 start app.js -i max` | 使用所有 CPU 核心 【常用】 |
| 指定实例数 | `pm2 start app.js -i 4` | 启动 4 个实例 |
| 零秒停机重载 | `pm2 reload all` | 平滑重载所有进程 |
| 查看集群状态 | `pm2 list` | 显示集群实例数 |

### PM2 配置文件

**ecosystem.config.js 示例**:
```javascript
module.exports = {
  apps: [{
    name: 'api-server',
    script: 'dist/main.js',
    instances: 'max',
    exec_mode: 'cluster',
    env: {
      NODE_ENV: 'development'
    },
    env_production: {
      NODE_ENV: 'production'
    }
  }]
};
```

### PM2 日志管理

**基础用法**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看所有日志 | `pm2 logs` | 实时查看日志 【常用】 |
| 查看错误日志 | `pm2 logs --err` | 仅显示错误日志 |
| 清理日志 | `pm2 flush` | 清空所有日志文件 |
| 日志分割 | `pm2 install pm2-logrotate` | 安装日志轮转插件 |

---

## 调试与排查

### Node.js 调试

**基础用法**:
```bash
node --inspect app.js
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 开启调试器 | `node --inspect app.js` | 启动调试服务 【常用】 |
| 断点调试 | `node --inspect-brk app.js` | 在首行断点暂停 |
| 监听调试端口 | `node --inspect=0.0.0.0:9229 app.js` | 允许远程调试 |
| Chrome DevTools | 访问 chrome://inspect 连接调试 |

### 内存泄漏检测

**基础用法**:

| 场景 | 命令 | 说明 |
|------|------|------|
| Heap 快照 | 使用 Chrome DevTools 快照分析 | 【常用】 |
| v8-profiler | `npm install v8-profiler` | 采集性能数据 |
| heapdump | `npm install heapdump` | 生成堆快照文件 |
| 定期快照 | 在代码中添加 heapdump.writeSnapshot() | 定位内存增长 |

### trace-warnings 追踪警告

**基础用法**:
```bash
node --trace-warnings app.js
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 追踪所有警告 | `node --trace-warnings app.js` | 显示所有警告堆栈 【常用】 |
| 导出追踪 | `node --trace-warnings --trace-warnings-to-file=warn.log app.js` | 输出到文件 |

### Node.js 性能分析

**基础用法**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动性能分析 | `node --prof app.js` | 生成性能日志 |
| 处理分析日志 | `node --prof-process isolate-*.log` | 解析日志输出报告 |
| 检查事件循环延迟 | `node --check-version-health` | 检测 Node 版本健康状态 |
| 堆内存使用 | `process.memoryUsage()` | 查看内存使用情况 |

---

## 实用场景示例

### 场景 1: 从零搭建 Express REST API

```bash
# 1. 初始化项目
mkdir my-api && cd my-api
npm init -y

# 2. 安装核心依赖
npm install express cors helmet dotenv
npm install --save-dev nodemon

# 3. 安装数据库和认证
npm install pg jsonwebtoken bcryptjs
npm install joi

# 4. 创建目录结构
mkdir src/routes src/middleware src/controllers src/models

# 5. 启动开发
npm install
npx nodemon src/app.js
```

### 场景 2: PM2 生产部署

```bash
# 1. 全局安装 PM2
npm install -g pm2

# 2. 创建 ecosystem 配置
cat > ecosystem.config.js << 'EOF'
module.exports = {
  apps: [{
    name: 'api',
    script: 'dist/main.js',
    instances: 'max',
    exec_mode: 'cluster',
    env: { NODE_ENV: 'production' }
  }]
};
EOF

# 3. 构建项目
npm run build

# 4. 启动服务
pm2 start ecosystem.config.js --env production

# 5. 配置开机自启
pm2 startup
pm2 save
```

### 场景 3: NestJS 项目创建与开发

```bash
# 1. 全局安装 NestJS CLI
npm i -g @nestjs/cli

# 2. 创建新项目
nest new project-api --package-manager npm

# 3. 创建资源
cd project-api
nest g resource users

# 4. 启动开发服务器
nest start --watch

# 5. 构建生产版本
nest build

# 6. 使用 PM2 部署
pm2 start dist/main.js --name api --interpreter node
```

---

## 命令速查表

| 操作 | 命令 | 说明 |
|------|------|------|
| 安装依赖 | `npm install` | 安装 package.json 中的依赖 |
| 全局安装 | `npm install -g` | 全局安装包 |
| 安全审计 | `npm audit` | 检查依赖安全漏洞 |
| 干净安装 | `npm ci` | CI 环境干净安装 |
| 版本切换 | `nvm use` | 切换 Node.js 版本 |
| 创建项目 | `nest new` | 创建 NestJS 项目 |
| 生成资源 | `nest g resource` | 生成 REST 资源 |
| PM2 启动 | `pm2 start` | 启动进程 【常用】 |
| PM2 监控 | `pm2 monit` | 实时监控 |
| PM2 集群 | `pm2 start -i max` | 集群模式启动 |
| 开启调试 | `node --inspect` | 启动调试模式 |
| 追踪警告 | `node --trace-warnings` | 追踪所有警告 |

---

## 相关资源

- [快速开始指南](../quick-start.md)
- [Linux 命令文档](../Linux 命令/README.md)
- [Docker 命令文档](../Docker 命令/README.md)
- [完整命令参考表](../../references/commands-reference.md)