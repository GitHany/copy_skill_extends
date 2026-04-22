# API 与认证命令文档

API 设计与身份验证完整参考文档，涵盖 RESTful API、GraphQL、OAuth2/JWT 认证及安全配置。

## 目录

- [RESTful API](#restful-api)
- [认证机制](#认证机制)
- [GraphQL](#graphql)
- [安全配置](#安全配置)
- [实用场景示例](#实用场景示例)
- [命令速查表](#命令速查表)

---

## RESTful API

### HTTP 方法

| 方法 | 用途 | 示例场景 |
|------|------|----------|
| GET | 获取资源 | `GET /users` 获取用户列表 |
| POST | 创建资源 | `POST /users` 创建新用户 |
| PUT | 完整更新资源 | `PUT /users/123` 完整更新用户 |
| PATCH | 部分更新资源 | `PATCH /users/123` 更新单个字段 |
| DELETE | 删除资源 | `DELETE /users/123` 删除用户 |

### 常见状态码

| 状态码 | 含义 | 适用场景 |
|--------|------|----------|
| 200 OK | 请求成功 | GET/PUT/PATCH 成功 |
| 201 Created | 资源创建成功 | POST 创建新资源 |
| 204 No Content | 无返回内容 | DELETE 成功 |
| 400 Bad Request | 请求格式错误 | 参数校验失败 |
| 401 Unauthorized | 未认证 | 缺少或无效令牌 |
| 403 Forbidden | 无权限 | 已认证但无权限 |
| 404 Not Found | 资源不存在 | 查找不存在的资源 |
| 429 Too Many Requests | 请求过于频繁 | 触发限流 |
| 500 Internal Server Error | 服务器错误 | 未知服务端异常 |

### API 版本控制策略

#### URL 路径版本
```
GET /api/v1/users
GET /api/v2/users
```
最直观，浏览器可直接访问，SEO 友好。

#### Header 版本
```bash
curl -H "Accept: application/vnd.api+json; version=2" /users
```
不污染 URL，但调试困难。

#### 查询参数版本
```
GET /users?version=2
```
简单但容易被缓存忽略。

### 限流配置 (Rate Limiting)

| 策略 | 配置 | 说明 |
|------|------|------|
| 固定窗口 | `rateLimit: { windowMs: 60000, max: 100 }` | 每分钟最多 100 请求 |
| 滑动窗口 | `rateLimit: { slidingWindow: true, points: 100, duration: 60 }` | 更精确的限流 |
| 令牌桶 | `rateLimit: { tokenBucket: { points: 100, refill: 10, interval: 60 } }` | 支持突发流量 |

### CORS 配置

```javascript
// Express CORS 配置
app.use(cors({
  origin: ['https://example.com', 'https://app.example.com'],
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  exposedHeaders: ['X-Total-Count'],
  credentials: true,
  maxAge: 86400
}));
```

### Swagger / OpenAPI 文档

```yaml
# openapi.yaml
openapi: 3.0.0
info:
  title: 用户管理 API
  version: 1.0.0
paths:
  /users:
    get:
      summary: 获取用户列表
      parameters:
        - name: page
          in: query
          schema:
            type: integer
            default: 1
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/User'
```

---

## 认证机制

### JWT 命令

#### 生成 JWT
```javascript
// jsonwebtoken 库
const jwt = require('jsonwebtoken');

const token = jwt.sign(
  { userId: 123, role: 'admin' },
  process.env.JWT_SECRET,
  { expiresIn: '7d', algorithm: 'HS256' }
);
```

#### 验证 JWT
```javascript
const decoded = jwt.verify(token, process.env.JWT_SECRET, {
  algorithms: ['HS256'],
  issuer: 'my-app',
  audience: 'users'
});
```

#### 解码 JWT（不验证）
```javascript
const decoded = jwt.decode(token, { complete: true });
// 返回 { header, payload, signature }
```

#### JWT 刷新令牌
```javascript
// 访问令牌（短期）
const accessToken = jwt.sign(
  { userId, type: 'access' },
  secret,
  { expiresIn: '15m' }
);

// 刷新令牌（长期）
const refreshToken = jwt.sign(
  { userId, type: 'refresh' },
  refreshSecret,
  { expiresIn: '7d' }
);
```

### OAuth2 授权流程

#### 授权码模式
```bash
# 1. 引导用户到授权服务器
GET https://auth.example.com/authorize?
  client_id=YOUR_CLIENT_ID&
  redirect_uri=https://yourapp.com/callback&
  response_type=code&
  scope=read write&
  state=RANDOM_STATE

# 2. 交换授权码为访问令牌
POST https://auth.example.com/token
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code&
code=AUTH_CODE&
redirect_uri=https://yourapp.com/callback&
client_id=YOUR_CLIENT_ID&
client_secret=YOUR_CLIENT_SECRET

# 响应
{
  "access_token": "eyJhbG...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "dGhpcyBpcyB...",
  "scope": "read write"
}
```

#### 客户端凭证模式（服务间通信）
```bash
POST /oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials&
client_id=SERVICE_ID&
client_secret=SERVICE_SECRET&
scope=api
```

#### 刷新令牌
```bash
POST /oauth/token

grant_type=refresh_token&
refresh_token=REFRESH_TOKEN&
client_id=CLIENT_ID&
client_secret=CLIENT_SECRET
```

### Passport.js 策略

#### 本地策略（用户名密码）
```javascript
const passport = require('passport');
const LocalStrategy = require('passport-local');

passport.use(new LocalStrategy(
  { usernameField: 'email', passwordField: 'password' },
  async (email, password, done) => {
    const user = await User.findOne({ email });
    if (!user) return done(null, false);
    const match = await bcrypt.compare(password, user.passwordHash);
    if (!match) return done(null, false);
    return done(null, user);
  }
));
```

#### JWT 策略
```javascript
const JwtStrategy = require('passport-jwt');
const ExtractJwt = require('passport-jwt').ExtractJwt;

passport.use(new JwtStrategy({
  jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
  secretOrKey: process.env.JWT_SECRET,
  issuer: 'my-app',
  audience: 'users'
}, (payload, done) => {
  User.findById(payload.userId)
    .then(user => done(null, user || false))
    .catch(err => done(err, false));
}));
```

#### Google OAuth 策略
```javascript
const GoogleStrategy = require('passport-google-oauth20');

passport.use(new GoogleStrategy({
  clientID: process.env.GOOGLE_CLIENT_ID,
  clientSecret: process.env.GOOGLE_CLIENT_SECRET,
  callbackURL: '/auth/google/callback'
}, (accessToken, refreshToken, profile, done) => {
  User.findOrCreate({ googleId: profile.id }, (err, user) => done(err, user));
}));
```

### bcrypt 密码哈希

```javascript
const bcrypt = require('bcrypt');
const SALT_ROUNDS = 12;

// 哈希密码
const passwordHash = await bcrypt.hash(plainPassword, SALT_ROUNDS);

// 验证密码
const match = await bcrypt.compare(plainPassword, passwordHash);
```

### Session 管理

```javascript
// Express session 配置
const session = require('express-session');
const RedisStore = require('connect-redis');

app.use(session({
  store: new RedisStore({ client: redisClient }),
  secret: process.env.SESSION_SECRET,
  resave: false,
  saveUninitialized: false,
  cookie: {
    secure: process.env.NODE_ENV === 'production',
    httpOnly: true,
    maxAge: 24 * 60 * 60 * 1000, // 24 小时
    sameSite: 'strict'
  },
  name: 'sessionId'
}));
```

### 2FA / TOTP 设置

```javascript
const speakeasy = require('speakeasy');
const QRCode = require('qrcode');

// 生成 TOTP 密钥（注册时）
const secret = speakeasy.generateSecret({
  name: 'MyApp:user@example.com',
  issuer: 'MyApp'
});

// 生成二维码（前端显示）
const qrcodeUrl = await QRCode.toDataURL(secret.otpauth_url);

// 验证 TOTP 令牌
const verified = speakeasy.totp.verify({
  secret: user.totpSecret,
  encoding: 'base32',
  token: userProvidedCode,
  window: 1 // 允许前后各 1 个时间步长误差
});
```

---

## GraphQL

### Apollo Server 快速启动

```javascript
const { ApolloServer, gql } = require('apollo-server');

const typeDefs = gql`
  type User {
    id: ID!
    name: String!
    email: String!
  }

  type Query {
    users: [User!]!
    user(id: ID!): User
  }

  type Mutation {
    createUser(name: String!, email: String!): User!
  }
`;

const resolvers = {
  Query: {
    users: () => users,
    user: (_, { id }) => users.find(u => u.id === id)
  },
  Mutation: {
    createUser: (_, { name, email }) => {
      const user = { id: String(users.length + 1), name, email };
      users.push(user);
      return user;
    }
  }
};

const server = new ApolloServer({ typeDefs, resolvers });
server.listen().then(({ url }) => console.log(`Server at ${url}`));
```

### graphql-yoga 快速启动

```javascript
const { createServer } = require('graphql-yoga');
const { schema } = require('./schema');

const server = createServer({
  schema,
  port: 4000,
  cors: { origin: 'https://myapp.com' }
});

server.start();
```

### Schema 验证与类型定义

```graphql
enum Role {
  ADMIN
  USER
  GUEST
}

input CreateUserInput {
  name: String!
  email: String!
  role: Role = USER
}

type User {
  id: ID!
  name: String!
  email: String!
  role: Role!
  createdAt: DateTime!
}

type Query {
  user(id: ID!): User
  users(limit: Int = 10, offset: Int = 0): [User!]!
}

type Mutation {
  createUser(input: CreateUserInput!): User!
  updateUser(id: ID!, input: UpdateUserInput!): User!
  deleteUser(id: ID!): Boolean!
}
```

### Resolver 上下文与认证

```javascript
const server = new ApolloServer({
  typeDefs,
  resolvers,
  context: ({ req }) => {
    const token = req.headers.authorization?.replace('Bearer ', '');
    const user = token ? verifyToken(token) : null;
    return { user, prisma };
  }
});
```

### 查询 (Query) 示例

```graphql
# 带分页和过滤的查询
query GetUsers($limit: Int, $offset: Int, $role: Role) {
  users(limit: $limit, offset: $offset) {
    id
    name
    email
    role
  }
}

# 变量
{
  "limit": 10,
  "offset": 0,
  "role": "USER"
}
```

### 变更 (Mutation) 示例

```graphql
mutation CreateUser($input: CreateUserInput!) {
  createUser(input: $input) {
    id
    name
    email
  }
}
```

### 订阅 (Subscriptions)

```graphql
type Subscription {
  userCreated: User!
}

# 服务端
const Subscription = {
  userCreated: {
    subscribe: (_, __, { pubsub }) =>
      pubsub.asyncIterator('USER_CREATED')
  }
};

// 发布事件
pubsub.publish('USER_CREATED', { userCreated: newUser });
```

---

## 安全配置

### HTTPS / SSL 配置

```javascript
// Node.js HTTPS 服务器
const https = require('https');
const fs = require('fs');

const options = {
  key: fs.readFileSync('/path/to/private.key'),
  cert: fs.readFileSync('/path/to/certificate.crt'),
  ca: fs.readFileSync('/path/to/ca_bundle.crt'),
  minVersion: 'TLSv1.2',
  ciphers: 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384'
};

https.createServer(options, app).listen(443);
```

#### Let's Encrypt 免费证书

```bash
# 使用 certbot
sudo certbot --nginx -d api.example.com

# 或手动续期
sudo certbot renew --dry-run
```

### API Key 管理

```javascript
// 生成 API Key
const apiKey = crypto.randomBytes(32).toString('hex');
// 存储时哈希保存
const apiKeyHash = crypto.createHash('sha256').update(apiKey).digest('hex');

// 验证 API Key
const requestHash = crypto.createHash('sha256').update(requestApiKey).digest('hex');
const match = await bcrypt.compare(requestHash, storedHash);
```

### 输入验证

```javascript
const Joi = require('joi');

const schema = Joi.object({
  email: Joi.string().email().required(),
  password: Joi.string().min(8).pattern(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/).required(),
  age: Joi.number().integer().min(13).max(120),
  url: Joi.string().uri()
});

const { error, value } = schema.validate(requestBody);
if (error) return res.status(400).json({ error: error.details[0].message });
```

### CORS 安全头

```javascript
// 使用 Helmet 设置安全头
const helmet = require('helmet');

app.use(helmet());

// 自定义 CORS
app.use((req, res, next) => {
  res.setHeader('Access-Control-Allow-Origin', 'https://trusted-domain.com');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader('X-XSS-Protection', '1; mode=block');
  next();
});
```

### CSP 内容安全策略

```javascript
app.use(helmet.contentSecurityPolicy({
  directives: {
    defaultSrc: ["'self'"],
    scriptSrc: ["'self'", "'nonce-{generated}'"],
    styleSrc: ["'self'", "https://fonts.googleapis.com"],
    imgSrc: ["'self'", "data:", "https:"],
    connectSrc: ["'self'", "https://api.example.com"],
    fontSrc: ["'self'", "https://fonts.gstatic.com"],
    objectSrc: ["'none'"],
    mediaSrc: ["'self'"],
    frameSrc: ["'none'"]
  }
}));
```

---

## 实用场景示例

### 场景 1: Express + JWT + Refresh Token 认证

```javascript
const express = require('express');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const rateLimit = require('express-rate-limit');
const cors = require('cors');
const helmet = require('helmet');

const app = express();

app.use(helmet());
app.use(cors({ origin: 'https://myapp.com', credentials: true }));
app.use(express.json());

// 限流
app.use('/api/auth', rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5,
  message: '登录尝试过于频繁'
}));

// 登录
app.post('/api/auth/login', async (req, res) => {
  const { email, password } = req.body;
  const user = await User.findOne({ email });
  if (!user || !(await bcrypt.compare(password, user.passwordHash))) {
    return res.status(401).json({ error: '无效凭证' });
  }

  const accessToken = jwt.sign(
    { userId: user.id, role: user.role },
    process.env.JWT_SECRET,
    { expiresIn: '15m' }
  );

  const refreshToken = jwt.sign(
    { userId: user.id, type: 'refresh' },
    process.env.REFRESH_SECRET,
    { expiresIn: '7d' }
  );

  res.json({ accessToken, refreshToken });
});

// 刷新令牌
app.post('/api/auth/refresh', (req, res) => {
  const { refreshToken } = req.body;
  try {
    const decoded = jwt.verify(refreshToken, process.env.REFRESH_SECRET);
    const accessToken = jwt.sign(
      { userId: decoded.userId },
      process.env.JWT_SECRET,
      { expiresIn: '15m' }
    );
    res.json({ accessToken });
  } catch (e) {
    res.status(401).json({ error: '刷新令牌无效' });
  }
});

// 受保护的路由
const authenticate = (req, res, next) => {
  const token = req.headers.authorization?.replace('Bearer ', '');
  if (!token) return res.status(401).json({ error: '未认证' });
  try {
    req.user = jwt.verify(token, process.env.JWT_SECRET);
    next();
  } catch (e) {
    res.status(401).json({ error: '令牌无效' });
  }
};

app.get('/api/users', authenticate, async (req, res) => {
  const users = await User.findAll({ where: { role: 'USER' } });
  res.json(users);
});
```

### 场景 2: GraphQL + Apollo Server + JWT

```javascript
const { ApolloServer } = require('apollo-server-express');
const { makeExecutableSchema } = require('@graphql-tools/schema');
const jwt = require('jsonwebtoken');

const typeDefs = gql`
  type Query {
    me: User
    posts: [Post!]!
  }

  type Mutation {
    login(email: String!, password: String!): AuthPayload!
  }

  type User {
    id: ID!
    name: String!
    email: String!
    posts: [Post!]!
  }

  type AuthPayload {
    token: String!
    user: User!
  }
`;

const resolvers = {
  Query: {
    me: (_, __, { user }) => user,
    posts: (_, __, { user }) => user ? Post.findAll() : []
  },
  Mutation: {
    login: async (_, { email, password }) => {
      const user = await User.findOne({ where: { email } });
      if (!user || !(await bcrypt.compare(password, user.passwordHash))) {
        throw new AuthenticationError('无效凭证');
      }
      const token = jwt.sign({ userId: user.id }, process.env.JWT_SECRET, { expiresIn: '1d' });
      return { token, user };
    }
  }
};

const server = new ApolloServer({
  schema: makeExecutableSchema({ typeDefs, resolvers }),
  context: ({ req }) => {
    const token = req.headers.authorization?.replace('Bearer ', '');
    const user = token ? jwt.verify(token, process.env.JWT_SECRET) : null;
    return { user };
  }
});
```

### 场景 3: API 完整安全配置

```javascript
const express = require('express');
const helmet = require('helmet');
const cors = require('cors');
const rateLimit = require('express-rate-limit');
const hpp = require('hpp'); // HTTP Parameter Pollution 防护
const mongoSanitize = require('express-mongo-sanitize'); // NoSQL 注入防护
const xss = require('xss-clean'); // XSS 防护

const app = express();

// 安全头
app.use(helmet());

// XSS 防护
app.use(xss());

// NoSQL 注入防护
app.use(mongoSanitize());

// HTTP Parameter Pollution 防护
app.use(hpp());

// CORS
app.use(cors({
  origin: process.env.ALLOWED_ORIGINS?.split(','),
  credentials: true
}));

// 全局限流
app.use(rateLimit({
  windowMs: 60 * 1000,
  max: 100,
  standardHeaders: true,
  legacyHeaders: false
}));

// 请求体大小限制
app.use(express.json({ limit: '10kb' }));
app.use(express.urlencoded({ extended: true, limit: '10kb' }));

// API 签名验证（自定义头）
app.use((req, res, next) => {
  const signature = req.headers['x-api-signature'];
  const timestamp = req.headers['x-api-timestamp'];

  if (Date.now() - parseInt(timestamp) > 300000) { // 5 分钟内的请求
    return res.status(401).json({ error: '请求已过期' });
  }

  const expectedSig = crypto
    .createHmac('sha256', process.env.API_SECRET)
    .update(timestamp + req.method + req.path)
    .digest('hex');

  if (signature !== expectedSig) {
    return res.status(401).json({ error: '签名无效' });
  }

  next();
});
```

---

## 命令速查表

| 分类 | 操作 | 命令/函数 |
|------|------|-----------|
| JWT | 生成令牌 | `jwt.sign(payload, secret, { expiresIn })` |
| JWT | 验证令牌 | `jwt.verify(token, secret)` |
| JWT | 解码令牌 | `jwt.decode(token)` |
| bcrypt | 哈希密码 | `bcrypt.hash(password, 12)` |
| bcrypt | 验证密码 | `bcrypt.compare(password, hash)` |
| OAuth2 | 授权码换取令牌 | `POST /oauth/token` + `grant_type=authorization_code` |
| OAuth2 | 刷新令牌 | `POST /oauth/token` + `grant_type=refresh_token` |
| TOTP | 生成密钥 | `speakeasy.generateSecret({ name })` |
| TOTP | 验证验证码 | `speakeasy.totp.verify({ secret, token })` |
| Passport | 本地策略注册 | `passport.use(new LocalStrategy(...))` |
| Passport | JWT 策略注册 | `passport.use(new JwtStrategy(...))` |
| 限流 | 固定窗口 | `rateLimit({ windowMs: 60000, max: 100 })` |
| CORS | 配置跨域 | `cors({ origin, credentials, methods })` |
| 安全头 | 设置安全头 | `helmet()` |
| GraphQL | 启动 Apollo | `new ApolloServer({ typeDefs, resolvers })` |
| GraphQL | 启动 Yoga | `createServer({ schema, port })` |
| 验证 | Joi 校验 | `Joi.object({}).validate(data)` |
| HTTPS | 创建 HTTPS 服务器 | `https.createServer(options, app)` |
| API Key | 生成 | `crypto.randomBytes(32).toString('hex')` |
| 订阅 | GraphQL 订阅 | `pubsub.asyncIterator('EVENT_NAME')` |

---

## 相关资源

- [快速开始指南](../quick-start.md)
- [Docker 命令文档](../Docker 命令/README.md)
- [GitHub CLI 命令文档](../GitHub CLI 命令/README.md)
- [完整命令参考表](../../references/commands-reference.md)
