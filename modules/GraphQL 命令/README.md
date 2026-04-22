# GraphQL 命令文档

GraphQL 全栈技术完整参考文档，覆盖核心概念、服务器端、客户端、代码生成及操作工具。

## 目录

- [GraphQL Core](#graphql-core)
- [GraphQL Servers](#graphql-servers)
- [GraphQL Clients](#graphql-clients)
- [Code Generation](#code-generation)
- [GraphQL Playground](#graphql-playground)
- [Operations](#operations)

---

## GraphQL Core

### Schema 定义 — Query 类型

**基础用法**:
```graphql
type %{类型名称}% {
  %{字段1}%: %{类型1}%
  %{字段2}%: %{类型2}%
}
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 带参数的查询字段 | `user(id: ID): User` | 查询指定 ID 的用户 【常用】 |
| 数组返回类型 | `users: [User!]!` | 返回非空用户数组 【常用】 |
| 带别名的查询 | `alias: user(id: "1") { name }` | 使用别名避免字段冲突 |

### Schema 定义 — Mutation 类型

**基础用法**:
```graphql
type Mutation {
  %{mutation名称}%(%{参数}%): %{返回类型}%
}
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建数据 | `createUser(name: String!): User` | 创建新用户 【常用】 |
| 更新数据 | `updateUser(id: ID!, name: String): User` | 更新用户信息 【常用】 |
| 删除数据 | `deleteUser(id: ID!): Boolean` | 删除用户 |

### Schema 定义 — Subscription 类型

**基础用法**:
```graphql
type Subscription {
  %{subscription名称}%(%{参数}%): %{返回类型}%
}
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 监听创建事件 | `userCreated: User` | 监听新用户创建 【常用】 |
| 监听更新事件 | `userUpdated: User` | 监听用户更新 【常用】 |
| 按房间订阅 | `messageAdded(roomId: ID!): Message` | 监听特定房间消息 |

### Input 类型定义

**基础用法**:
```graphql
input %{input名称}% {
  %{字段1}%: %{类型1}%
  %{字段2}%: %{类型2}%
}
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 嵌套 Input | `input CreatePostInput { title: String!, author: AuthorInput! }` | 嵌套复杂输入类型 【常用】 |
| Mutation 中使用 | `createPost(input: CreatePostInput!): Post` | 作为 Mutation 参数 【常用】 |

### Enum 类型定义

**基础用法**:
```graphql
enum %{enum名称}% {
  %{值1}%
  %{值2}%
  %{值3}%
}
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| Enum 用作字段类型 | `status: UserStatus` | 字段类型为枚举 【常用】 |
| 常见场景 | `enum Role { ADMIN USER GUEST }` | 角色权限枚举 |

### Interface 与 Union

**基础用法**:
```graphql
interface %{interface名称}% {
  %{字段1}%: %{类型1}%
}
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 类型实现接口 | `type User implements Node { id: ID! }` | 实现 Node 接口 【常用】 |
| Union 联合类型 | `union SearchResult = User | Post` | 组合多个类型 【常用】 |
| 查询 Interface | `{ ... on User { name } ... on Post { title } }` | 内联片段查询 |

---

## GraphQL Servers

### Apollo Server 启动服务

**基础用法**:
```bash
npx apollo-server %{文件路径}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定端口启动 | `PORT=4000 npx apollo-server src/index.ts` | 监听 4000 端口 【常用】 |
| 安装 Apollo Server | `npm install @apollo/server graphql` | 安装 Apollo Server v4 |
| Apollo Server v4 启动 | `const server = new ApolloServer({ typeDefs, resolvers }); await server.start();` | 最新版本启动方式 【常用】 |

### graphql-yoga 创建服务

**基础用法**:
```bash
npm install graphql-yoga
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 Yoga 服务 | `createServer(yoga).listen(4000, () => {})` | HTTP 服务器启动 【常用】 |
| Express 集成 | `app.use('/graphql', yoga)` | 集成到 Express 【常用】 |
| 创建网关 | `npx create-gateway` | 快速创建 GraphQL 网关 |

### graphql-tools Schema 操作

**基础用法**:
```bash
npm install @graphql-tools/schema @graphql-tools/delegate @graphql-tools/wrap
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| Schema 合并 | `mergeSchemas({ schemas: [schemaA, schemaB] })` | 合并多个子 Schema 【常用】 |
| Schema 委托 | `delegateToSchema({ schema, operation: 'query', fieldName: 'user' })` | 委托到子 Schema 【常用】 |
| Schema 转换 | `transformSchema(schema, [new RenameTypes(name => `_${name}`)])` | 重命名类型 |

### Prisma GraphQL

**基础用法**:
```bash
npx prisma init
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 生成 Prisma Client | `npx prisma generate` | 生成类型安全的数据库客户端 【常用】 |
| 创建迁移 | `npx prisma migrate dev --name init_users` | 创建数据库迁移 【常用】 |
| 应用迁移 | `npx prisma migrate deploy` | 部署迁移到生产环境 【常用】 |
| Prisma Studio | `npx prisma studio` | 浏览器可视化数据库 【常用】 |

### Apollo Federation

**基础用法**:
```bash
npm install @apollo/subgraph
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 定义 Entity 主键 | `extend type User @key(fields: "id") { id: ID! @external }` | 声明联合主键 【常用】 |
| 引用远程类型 | `type Review @extends @key(fields: "id") { author: User @provides(fields: "username") }` | 跨服务引用 【常用】 |
| 网关构建 | `ApolloGateway.from(services)` | 构建超图网关 |

---

## GraphQL Clients

### Apollo Client 初始化

**基础用法**:
```bash
npm install @apollo/client graphql
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 Client 实例 | `new ApolloClient({ uri: 'http://localhost:4000/graphql', cache: new InMemoryCache() })` | 初始化客户端 【常用】 |
| useQuery Hook | `const { data, loading, error } = useQuery(GET_USERS)` | 执行查询 【常用】 |
| useMutation Hook | `const [createUser] = useMutation(CREATE_USER_MUTATION)` | 执行变更 【常用】 |
| useSubscription Hook | `const { data } = useSubscription(USER_ADDED_SUBSCRIPTION)` | 订阅实时数据 |

### urql 初始化

**基础用法**:
```bash
npm install urql graphql
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 urql Client | `createClient({ url: 'http://localhost:4000/graphql' })` | 初始化 urql 客户端 【常用】 |
| 执行查询 | `client.query(\`query { users { id name } }\`).toPromise()` | Promise 风格查询 【常用】 |
| urql React Hook | `const [result] = useQuery({ query: GET_USERS })` | React Hook 用法 |

### Fetch 发送 GraphQL 请求

**基础用法**:
```javascript
fetch('%{endpoint}%', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ query: `%{query}%`, variables: %{variables}% })
}).then(res => res.json()).then(console.log);
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 带认证头 | `headers: { 'Authorization': 'Bearer token' }` | JWT 认证 【常用】 |
| 错误处理 | `.catch(err => console.error(err.response?.data))` | 错误捕获 |
| 上传文件（multipart） | `FormData` 配合 `multipart/form-data` | 文件上传场景 |

### Axios 发送 GraphQL 请求

**基础用法**:
```javascript
import axios from 'axios';
axios.post('%{endpoint}%', {
  query: `%{query}%`,
  variables: %{variables}%
}).then(res => console.log(res.data));
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| Axios 实例配置 | `axios.create({ baseURL: 'http://localhost:4000/graphql' })` | 统一配置端点 |
| 错误处理 | `.catch(err => console.error(err.response?.data?.errors))` | GraphQL 错误捕获 |
| 请求拦截器 | `axios.interceptors.request.use(config => { config.headers.Authorization = token; return config; })` | 自动附加认证 |

---

## Code Generation

### graphql-codegen 初始化

**基础用法**:
```bash
npx graphql-codegen init
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装核心依赖 | `npm install -D @graphql-codegen/cli @graphql-codegen/typescript` | 安装代码生成器 【常用】 |
| 生成 TypeScript 类型 | `npx graphql-codegen` | 根据 Schema 生成类型 【常用】 |
| 生成 Apollo Hooks | `npm install -D @graphql-codegen/typescript-apollo-hooks` | 生成类型化 Hooks |
| 生成 urql Hooks | `npm install -D @graphql-codegen/typescript-urql` | 生成 urql 类型 |
| 监听文件变化 | `npx graphql-codegen --watch` | 开发模式自动重新生成 |

### Apollo Kotlin Codegen

**基础用法**:
```bash
./gradlew Apollo:generate%sApollo%Files
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 添加 Gradle 插件 | `plugins { id 'com.apollographql.apollo3' version '3.8.2' }` | 配置 Gradle 插件 【常用】 |
| 配置服务 | `apollo { service("service") { packageName.set("com.example.graphql") } }` | 配置生成的包名 【常用】 |
| Gradle 生成 | `./gradlew :app:generate%sApollo%Files` | 执行代码生成 |

---

## GraphQL Playground

### GraphQL Playground 启动

**基础用法**:
```bash
npx graphql-playground %{端口}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定端点 | `npx graphql-playground -e http://localhost:4000/graphql` | 启动指定端点 【常用】 |
| Express 中间件 | `app.use('/playground', playgroundMiddleware({ endpoint: '/graphql' }))` | 集成到 Express |
| Apollo Server v4 内置 | Apollo Server 4 默认启用 Apollo Sandbox（内置 IDE） |

### GraphiQL 启动

**基础用法**:
```bash
npx graphiql
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定端点 | `npx graphiql -u http://localhost:4000/graphql` | 指定 GraphQL 端点 【常用】 |
| Express 中间件 | `app.use('/graphiql', graphiqlMiddleware({ endpointURL: '/graphql' }))` | 集成到 Express 【常用】 |

### Insomnia GraphQL 请求

**基础用法**:
```bash
POST %{endpoint}%
Content-Type: application/json
{ "query": "%{query}%" }
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 导入 Schema | 在 Insomnia Schema 标签页粘贴 SDL 或导入 .graphql 文件 | 自动补全支持 |
| 环境变量 | `{{ base_url }}/graphql` | 利用环境变量动态端点 |
| Pre-request Script | 设置动态 Authorization Token | 请求前脚本 |

### Postman GraphQL 请求

**基础用法**:
```bash
POST %{endpoint}%
Content-Type: application/json
{ "query": "%{query}%" }
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| GraphQL Body 类型 | 选择 Body 类型为 'GraphQL' | Postman 内置 GraphQL 支持 【常用】 |
| Variables | 在 Variables 编辑器输入 `{"id": "1"}` | 变量注入 |
| 导入 Schema | Postman 侧边栏 Schema 按钮导入 SDL | 获得自动补全 |

---

## Operations

### GraphQL Introspection 查询

**基础用法**:
```bash
POST %{endpoint}%
Content-Type: application/json
{ "query": "{ __schema { types { name kind } } }" }
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查询所有类型 | `{ __schema { types { name kind } } }` | 列出 Schema 所有类型 【常用】 |
| 查询特定类型字段 | `{ __type(name: "User") { name fields { name type { name } } } }` | 查看类型详情 【常用】 |
| 查询所有 Query 字段 | `{ __schema { queryType { name fields { name args { name type { name } } } } } }` | 查看 Query 入口 |
| 禁用 Introspection | `introspection: false`（生产环境） | 关闭自省提升安全性 【常用】 |

### GraphQL 查询复杂度分析

**基础用法**:
```bash
npm install graphql-query-complexity
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 配置复杂度限制 | `createComplexityLimitRule(1000)` | 限制最大复杂度 1000 【常用】 |
| 字段级复杂度 | `@complexity(value: 2)` 指令 | 自定义字段复杂度 |
| 格式化错误消息 | `formatErrorMessage: (ctx) => '超过复杂度限制'` | 自定义错误提示 |

### GraphQL 速率限制

**基础用法**:
```bash
npm install graphql-rate-limit
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 全局限流 | `createRateLimitRule({ identifyContext: ctx => ctx.ip })` | 按 IP 限流 【常用】 |
| 字段级限流 | `@rateLimit(limit: 10, duration: 60)` | 单字段 60 秒最多 10 次 |
| Mutation 限流 | `@rateLimit(limit: 5, duration: 60)` | Mutation 变更操作限流 |

### DataLoader 批量加载

**基础用法**:
```bash
npm install dataloader
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 User Loader | `new DataLoader(keys => batchGetUsers(keys))` | 批量加载用户 【常用】 |
| 解决 N+1 问题 | Post.author 时使用 `userLoader.load(post.authorId)` | 避免 N+1 查询 【常用】 |
| Resolver 中集成 | `const resolvers = { Post: { author: post => userLoader.load(post.authorId) } }` | 集成到 Resolver |

### GraphQL SDL Schema 验证

**基础用法**:
```bash
node -e "const { buildSchema } = require('graphql'); buildSchema(fs.readFileSync('schema.graphql', 'utf8'));"
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 生成可执行 Schema | `makeExecutableSchema({ typeDefs })` | 从 SDL 生成可执行 Schema 【常用】 |
| 验证查询语法 | `validate(schema, parse(query))` | 验证客户端查询 【常用】 |
| SDL 打印 | `printSchema(schema)` | 将 Schema 对象转回 SDL 字符串 |

---

## 实用场景示例

### 场景 1: 搭建完整的 GraphQL 服务

```bash
# 1. 安装依赖
npm init -y
npm install @apollo/server graphql
npm install -D @graphql-codegen/cli @graphql-codegen/typescript-resolvers

# 2. 初始化 codegen
npx graphql-codegen init

# 3. 创建 Schema
```

```graphql
# schema.graphql
type Query {
  user(id: ID!): User
  users: [User!]!
}

type Mutation {
  createUser(name: String!, email: String!): User
  deleteUser(id: ID!): Boolean
}

type User {
  id: ID!
  name: String!
  email: String!
  createdAt: String!
}
```

```bash
# 4. 启动服务
node server.js

# 5. 打开 Playground
# http://localhost:4000/graphql
```

### 场景 2: Apollo Client 完整查询流程

```bash
# 1. 安装
npm install @apollo/client graphql
```

```javascript
// 2. 创建 Client
import { ApolloClient, InMemoryCache, gql } from '@apollo/client';
const client = new ApolloClient({
  uri: 'http://localhost:4000/graphql',
  cache: new InMemoryCache()
});

// 3. 执行查询
const GET_USERS = gql`query GetUsers { users { id name email } }`;
const { data } = await client.query({ query: GET_USERS });

// 4. 执行变更
const CREATE_USER = gql`mutation CreateUser($name: String!, $email: String!) {
  createUser(name: $name, email: $email) { id name }
}`;
await client.mutate({ mutation: CREATE_USER, variables: { name: 'Alice', email: 'alice@example.com' } });
```

### 场景 3: Federation 分布式超图

```bash
# 服务 A - Users
npm install @apollo/server @apollo/subgraph graphql
```

```graphql
# users subgraph
type User @key(fields: "id") {
  id: ID!
  name: String!
  email: String!
}
```

```bash
# 网关聚合
npm install @apollo/gateway
```

```javascript
import { ApolloGateway } from '@apollo/gateway';
const gateway = new ApolloGateway([
  { name: 'users', url: 'http://localhost:4001/graphql' },
  { name: 'posts', url: 'http://localhost:4002/graphql' }
]);
```

---

## 命令速查表

| 操作 | 命令 | 说明 |
|------|------|------|
| 定义 Query | `type Query { user(id: ID!): User }` | 查询入口 |
| 定义 Mutation | `type Mutation { createUser(name: String!): User }` | 变更入口 |
| 定义 Subscription | `type Subscription { userAdded: User }` | 订阅入口 |
| 启动 Apollo Server | `npx apollo-server src/index.ts` | 启动服务 |
| 启动 graphql-yoga | `createServer(yoga).listen(4000)` | 轻量级服务器 |
| Prisma 初始化 | `npx prisma init` | 初始化 Prisma |
| Apollo Client | `npm install @apollo/client graphql` | 客户端安装 |
| urql 安装 | `npm install urql graphql` | urql 安装 |
| Fetch 请求 | `fetch(url, { method: 'POST', body: JSON.stringify({ query }) })` | 原生请求 |
| codegen 初始化 | `npx graphql-codegen init` | 代码生成 |
| Apollo Kotlin | `./gradlew Apollo:generateApolloFiles` | Kotlin 代码生成 |
| GraphQL Playground | `npx graphql-playground 4000` | 图形化 IDE |
| GraphiQL | `npx graphiql` | 浏览器 IDE |
| Introspection | `{ __schema { types { name } } }` | 查询 Schema |
| DataLoader | `new DataLoader(keys => batchFn(keys))` | 批量加载 |

---

## 相关资源

- [快速开始指南](../quick-start.md)
- [Docker 命令文档](../Docker 命令/README.md)
- [前端包管理器文档](../前端包管理器/README.md)
- [完整命令参考表](../../references/commands-reference.md)
