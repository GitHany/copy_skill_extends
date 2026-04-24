# CDN 与缓存管理命令文档

CDN 和缓存管理完整参考文档，涵盖主流 CDN 服务、HTTP 缓存机制、反向代理缓存、浏览器缓存以及常用工具。

## 目录

- [CDN CLI 命令](#cdn-cli-命令)
- [HTTP 缓存机制](#http-缓存机制)
- [反向代理缓存](#反向代理缓存)
- [浏览器缓存](#浏览器缓存)
- [缓存诊断与工具](#缓存诊断与工具)
- [命令速查表](#命令速查表)

---

## CDN CLI 命令

### Cloudflare Wrangler CLI

#### wrangler login - 登录 Cloudflare

**基础用法**:
```bash
wrangler login
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 浏览器授权登录 | `wrangler login` | 打开浏览器进行 OAuth 授权 |
| 指定 OAuth 作用域 | `wrangler login --scopes account:read,zone:read` | 请求特定权限范围 |
| 验证登录状态 | `wrangler whoami` | 查看当前登录账户信息 |

#### wrangler deploy - 部署 Workers

**基础用法**:
```bash
wrangler deploy
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 部署到生产环境 | `wrangler deploy` | 部署当前 Worker 到 Cloudflare 边缘节点 |
| 指定环境部署 | `wrangler deploy --env staging` | 部署到 staging 环境 |
| 排除某些文件 | `wrangler deploy --exclude '*.test.js'` | 排除测试文件不上传 |
| 部署并查看日志 | `wrangler deploy && wrangler tail` | 部署后实时查看日志 【常用】 |

#### wrangler kv namespace - KV 命名空间

**基础用法**:
```bash
wrangler kv:namespace create %{命名空间名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 KV 命名空间 | `wrangler kv:namespace create "CACHE"` | 为缓存创建专用命名空间 |
| 列出所有命名空间 | `wrangler kv:namespace list` | 查看账户下所有 KV 命名空间 |
| 删除命名空间 | `wrangler kv:namespace delete --env production --binding CACHE` | 删除指定命名空间 |
| 写入缓存数据 | `wrangler kv:key put "user:1001" '{"name":"张三"}' --binding CACHE` | 写入 JSON 数据 |
| 读取缓存数据 | `wrangler kv:key get "user:1001" --binding CACHE` | 读取缓存值 |
| 批量删除键 | `wrangler kv:key delete "user:*" --binding CACHE` | 支持 glob 模式删除 |

#### wrangler pages - Pages 部署

**基础用法**:
```bash
wrangler pages deploy %{构建目录}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 部署静态站点 | `wrangler pages deploy ./dist` | 部署静态构建产物到 CDN 【常用】 |
| 指定项目名称 | `wrangler pages deploy ./dist --project-name=my-site` | 绑定到特定 Pages 项目 |
| 预览部署 | `wrangler pages deploy ./dist --branch=preview` | 部署到预览分支 |

---

### AWS CloudFront

#### aws cloudfront create-distribution - 创建分发

**基础用法**:
```bash
aws cloudfront create-distribution --distribution-config file://config.json
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 Web 分发 | `aws cloudfront create-distribution --distribution-config file://web-config.json` | 创建标准 CDN 分发 |
| 查看分发列表 | `aws cloudfront list-distributions` | 查看账户下所有 CloudFront 分发 |
| 获取分发配置 | `aws cloudfront get-distribution-config --id %{分发ID}%` | 获取指定分发的完整配置 |
| 启用/禁用分发 | `aws cloudfront update-distribution --id %{分发ID}% --if-match %{ETag}% --distribution-config file://updated.json` | 修改分发状态 |

#### aws cloudfront create-invalidation - 缓存失效

**基础用法**:
```bash
aws cloudfront create-invalidation --distribution-id %{分发ID}% --paths "/*"
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 刷新整个 CDN 缓存 | `aws cloudfront create-invalidation --distribution-id %{分发ID}% --paths "/*"` | 清除所有缓存 【常用】 |
| 刷新特定路径 | `aws cloudfront create-invalidation --distribution-id %{分发ID}% --paths "/static/*"` | 刷新静态资源目录 |
| 刷新多个路径 | `aws cloudfront create-invalidation --distribution-id %{分发ID}% --paths "/css/*" "/js/*" "/images/*"` | 批量刷新多个目录 |
| 查看失效状态 | `aws cloudfront get-invalidation --distribution-id %{分发ID}% --id %{失效ID}%` | 查看失效任务进度 |

---

### 阿里云 CDN

#### aliyun alidns - CDN 刷新

**基础用法**:
```bash
aliyun cdn DescribeCdnDomainList
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 列出所有 CDN 域名 | `aliyun cdn DescribeCdnDomainList` | 查看账号下所有加速域名 |
| 刷新 URL | `aliyun cdn PushObjectCache --ObjectPath "http://example.com/index.html"` | 主动刷新指定 URL 【常用】 |
| 刷新目录 | `aliyun cdn PushObjectCache --ObjectPath "http://example.com/static/" --ObjectType Directory` | 刷新整个目录 |
| 查询刷新状态 | `aliyun cdn DescribeRefreshTasks --TaskId %{任务ID}%` | 查看刷新任务执行结果 |
| 设置缓存规则 | `aliyun cdn SetCacheConfig --DomainName example.com --CacheType "lite" --TTLSeconds 3600` | 配置域名缓存策略 |

---

## HTTP 缓存机制

### 响应头配置

#### Cache-Control - 缓存控制

**基础用法**:
在 HTTP 响应头中设置缓存策略。

**扩展示例**:

| 场景 | 响应头 | 说明 |
|------|--------|------|
| 公开资源长期缓存 | `Cache-Control: public, max-age=31536000, immutable` | 静态资源（哈希文件名），一年缓存 【常用】 |
| 私有资源不缓存 | `Cache-Control: private, no-store` | 包含用户敏感信息的响应 |
| 重新验证 | `Cache-Control: no-cache, must-revalidate` | 每次使用前必须与服务端验证 |
| 共享缓存最大时间 | `Cache-Control: s-maxage=3600, max-age=0` | CDN 缓存 1 小时，浏览器不缓存 |
| 可缓存但需重新验证 | `Cache-Control: max-age=60, must-revalidate` | 60 秒后强制重新验证 |

#### ETag 和 Last-Modified

**基础用法**:
服务端支持条件请求以节省带宽。

**扩展示例**:

| 场景 | 请求头 | 说明 |
|------|--------|------|
| 首次请求响应 | `Last-Modified: Mon, 01 Jan 2024 00:00:00 GMT` + `ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"` | 同时提供两种校验器 |
| 条件请求（If-Modified-Since） | `If-Modified-Since: Mon, 01 Jan 2024 00:00:00 GMT` | 自指定时间后未修改则返回 304 |
| 条件请求（If-None-Match） | `If-None-Match: "33a64df551425fcc55e4d42a148795d9f25f89d4"` | 匹配 ETag 则返回 304 【常用】 |

#### Vary 头配置

**基础用法**:
基于请求头差异化缓存响应。

**扩展示例**:

| 场景 | 响应头 | 说明 |
|------|--------|------|
| 按 Accept-Encoding 缓存 | `Vary: Accept-Encoding` | gzip 和 brotli 版本分别缓存 |
| 按 Accept-Language 缓存 | `Vary: Accept-Language` | 不同语言版本分别缓存 |
| 按 User-Agent 缓存 | `Vary: User-Agent` | 桌面和移动版分别缓存 |
| 组合差异化 | `Vary: Accept-Encoding, Accept-Language` | 多个条件组合缓存 |

---

## 反向代理缓存

### Nginx 缓存配置

#### proxy_cache_path - 定义缓存区

**基础用法**:
```nginx
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m max_size=1g inactive=60m use_temp_path=off;
```

**扩展示例**:

| 场景 | 配置 | 说明 |
|------|------|------|
| 基础缓存配置 | `proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m max_size=1g inactive=60m use_temp_path=off;` | 10MB 元数据区，1GB 最大缓存，60分钟未访问删除 |
| 高流量配置 | `proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=cdn_cache:100m max_size=10g inactive=24h;` | 100MB 索引区，10GB 缓存，24小时清理 |
| SSD 优化配置 | `proxy_cache_path /mnt/ssd/nginx-cache levels=1:2 keys_zone=ssd_cache:50m loader_threshold=30000 loader_files=200 max_size=5g;` | SSD 高 IO 场景配置 |

#### proxy_cache - 启用缓存

**基础用法**:
```nginx
location / {
    proxy_cache my_cache;
    proxy_cache_valid 200 1h;
    add_header X-Cache-Status $upstream_cache_status;
}
```

**扩展示例**:

| 场景 | 配置 | 说明 |
|------|------|------|
| 基础反向代理缓存 | `proxy_cache_bypass $cookie_nocache $arg_nocache;` + `proxy_cache_valid 200 1h;` | 按参数绕过缓存 |
| 区分移动端缓存 | `proxy_cache_key "$scheme$request_method$host$uri$is_args$args";` + `proxy_cache_valid 200 1d;` | 按 URI 缓存，忽略 Query String |
| 缓存 POST 请求 | `proxy_cache_methods POST;` + `proxy_cache_valid 201 301 302 5m;` | 允许缓存 POST 响应 |
| 条件缓存 | `proxy_cache_valid 200 302 10m;` + `proxy_cache_valid 301 1h;` + `proxy_cache_valid any 5m;` | 不同状态码不同缓存时间 |

#### 缓存清理

**基础用法**:
```nginx
# 商业版 Nginx Plus 支持
proxy_cache_purge my_cache $arg_key;
```

**扩展开示例**（第三方模块 ngx_cache_purge）:

| 场景 | 配置 | 说明 |
|------|------|------|
| 安装 ngx_cache_purge | `yum install nginx-plus-module-njs` 或编译添加 `--add-module=ngx_cache_purge` | 需要第三方模块支持 |
| 缓存清理配置 | `location ~ /purge(/.*) { proxy_cache_purge my_cache $1; }` | 通过 URL 触发清理 |

---

### Varnish Cache

#### varnishd - 启动服务

**基础用法**:
```bash
varnishd -F -f /etc/varnish/default.vcl
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动 Varnish | `varnishd -F -f /etc/varnish/default.vcl` | 前台运行，加载 VCL 配置 【常用】 |
| 指定监听端口 | `varnishd -F -a :80 -f /etc/varnish/default.vcl` | 监听 80 端口 |
| 指定缓存存储 | `varnishd -F -s malloc,256m -f /etc/varnish/default.vcl` | 使用内存存储，256MB |
| 指定持久化存储 | `varnishd -F -s file,/var/lib/varnish/varnish_storage.bin,1G` | 使用文件存储，1GB |
| 多实例运行 | `varnishd -F -n varnish1 -a :8080 -f /etc/varnish/varnish1.vcl` | 启动第二个实例 |

#### varnish-cli - 管理命令

**基础用法**:
```bash
varnishadm ban.url .
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 清除所有缓存 | `varnishadm ban "req.url ~ ."` | 清除所有 URL 缓存 【常用】 |
| 清除特定路径 | `varnishadm ban "req.url ~ ^/static/"` | 清除 /static/ 目录下缓存 |
| 清除特定域名 | `varnishadm ban "req.http.host ~ example.com"` | 按域名清除缓存 |
| 查看缓存统计 | `varnishstat -1` | 查看命中率、存储使用等统计 |
| 重新加载 VCL | `varnishadm vcl.load default /etc/varnish/new.vcl && varnishadm vcl.use default` | 无需重启加载新配置 |
| 清理特定 URL | `varnishadm ban "req.url == /index.html"` | 精确匹配清除单个页面 |

#### varnishtest - 测试工具

**基础用法**:
```bash
varnishtest test.vtc
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 运行单个测试 | `varnishtest -v test.vtc` | 详细输出模式运行测试 |
| 运行目录测试 | `varnishtest tests/*.vtc` | 运行多个测试文件 |
| 指定 Varnish 版本 | `varnishtest -L -v test.vtc` | 兼容最新版本特性测试 |

---

### Redis 缓存操作

#### SET 与 GET

**基础用法**:
```bash
redis-cli SET cache:page:index '{"html":"...","timestamp":1700000000}'
redis-cli GET cache:page:index
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 设置字符串缓存 | `redis-cli SET cache:user:1001 "serialized_data"` | 普通字符串缓存 |
| 设置带过期时间 | `redis-cli SETEX cache:session:abc 3600 "session_token"` | 1小时后自动删除 【常用】 |
| 不存在才设置 | `redis-cli SETNX lock:order:123 "locked"` | 用于分布式锁 |
| 设置多个键值 | `redis-cli MSET cache:page:1 "html1" cache:page:2 "html2"` | 批量设置 |
| 读取并删除 | `redis-cli GETDEL cache:page:index` | 读取后立即删除缓存 |
| 读取并更新过期 | `redis-cli GETEX cache:page:index EX 3600` | 读取后重置过期时间 |

#### EXPIRE 和 TTL

**基础用法**:
```bash
redis-cli EXPIRE cache:page:index 3600
redis-cli TTL cache:page:index
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 设置过期时间（秒） | `redis-cli EXPIRE cache:user:1001 3600` | 1小时后失效 |
| 设置过期时间（毫秒） | `redis-cli PEXPIRE cache:page:index 60000` | 60秒后失效 |
| 查看剩余生存时间 | `redis-cli TTL cache:page:index` | 返回 -2 表示不存在，-1 表示永不过期 |
| 毫秒级 TTL | `redis-cli PTTL cache:page:index` | 毫秒精度查看剩余时间 |
| 移除过期时间 | `redis-cli PERSIST cache:page:index` | 转为永久缓存 |

#### 缓存键管理

**基础用法**:
```bash
redis-cli KEYS "cache:*"
redis-cli DEL cache:page:*
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看所有缓存键 | `redis-cli KEYS "cache:*"` | 列出所有缓存键（生产环境慎用） |
| 前缀扫描（安全） | `redis-cli SCAN 0 MATCH "cache:*" COUNT 100` | 分批扫描，避免阻塞 【常用】 |
| 删除匹配键 | `redis-cli DEL $(redis-cli KEYS "cache:page:*")` | 批量删除页面缓存 |
| 渐进式删除 | `redis-cli --scan --pattern "cache:old:*" | xargs redis-cli DEL` | 大量键时避免阻塞 |
| 查看缓存类型 | `redis-cli TYPE cache:page:index` | string / hash / list 等类型 |
| 查看键内存占用 | `redis-cli MEMORY USAGE cache:page:index` | 分析单个键的内存占用 |

---

## 浏览器缓存

### Service Worker

#### sw.js - 缓存策略

**基础用法**:
```javascript
// sw.js - 缓存策略脚本
const CACHE_NAME = 'v1-static-assets';
const ASSETS = [
  '/',
  '/index.html',
  '/static/main.js',
  '/static/main.css'
];
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 预缓存静态资源 | `self.addEventListener('install', e => { e.waitUntil(caches.open(CACHE_NAME).then(c => c.addAll(ASSETS))); });` | 安装时缓存核心资源 【常用】 |
| 网络优先策略 | `fetch(e.request).then(r => { caches.open(CACHE_NAME).then(c => c.put(e.request, r.clone())); return r; }).catch(() => caches.match(e.request));` | 优先网络，失败用缓存 |
| 缓存优先策略 | `caches.match(e.request).then(r => r || fetch(e.request));` | 优先缓存，网络作为兜底 |
| Stale-While-Revalidate | `caches.open(CACHE_NAME).then(c => { fetch(req).then(r => c.put(req, r.clone())); }); return caches.match(req);` | 即刻返回缓存，后台更新 |
| 清除旧缓存 | `self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE_NAME).map(caches.delete)))); });` | 激活时清理旧版本 【常用】 |

#### Cache API - 缓存管理

**基础用法**:
```javascript
const cache = await caches.open('my-cache');
await cache.add('/api/data.json');
const response = await cache.match('/api/data.json');
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 打开命名缓存 | `const cache = await caches.open('v1-api-cache');` | 创建或打开命名缓存 |
| 添加单个请求 | `await cache.add('/index.html');` | 自动 fetch 并缓存 |
| 添加多个请求 | `await cache.addAll(['/a.html', '/b.css', '/c.js']);` | 批量添加，全部成功才算完成 |
| 精确匹配请求 | `const response = await cache.match('/api/users');` | 精确匹配 URL |
| 正则匹配请求 | `const matches = await caches.match(request, { ignoreSearch: true });` | 忽略查询参数匹配 |
| 删除缓存项 | `await cache.delete('/old-page.html');` | 删除单个缓存条目 |
| 删除整个缓存 | `await caches.delete('v1-cache');` | 删除整个命名缓存 |
| 列出所有缓存 | `const cacheNames = await caches.keys();` | 查看所有缓存名称 |

---

### PWA 缓存策略

#### Workbox 配置

**基础用法**:
```javascript
import { registerRoute } from 'workbox-routing';
import { StaleWhileRevalidate, CacheFirst } from 'workbox-strategies';
```

**扩展示例**:

| 场景 | 配置 | 说明 |
|------|------|------|
| 静态资源缓存优先 | `registerRoute(({ request }) => request.destination === 'style', new CacheFirst({ cacheName: 'styles-cache' }));` | CSS 缓存优先策略 |
| API 网络优先 | `registerRoute(({ url }) => url.pathname.startsWith('/api/'), new NetworkFirst({ cacheName: 'api-cache', networkTimeoutSeconds: 3 }));` | API 优先网络，超时用缓存 |
| 图片缓存 | `registerRoute(({ request }) => request.destination === 'image', new CacheFirst({ cacheName: 'images-cache', expiration: { maxEntries: 60, maxAgeSeconds: 30 * 24 * 60 * 60 } }));` | 最多 60 张图，30 天过期 |
| Google Fonts 缓存 | `registerRoute(({ url }) => url.origin === 'https://fonts.googleapis.com', new StaleWhileRevalidate({ cacheName: 'google-fonts-stylesheets' }));` | 字体样式表缓存 |
| 预缓存清单 | `wb.precacheAndRoute(self.__WB_MANIFEST);` | Workbox 自动预缓存清单中的资源 |

---

## 缓存诊断与工具

### curl 头部检查

#### curl -I - 头部检查

**基础用法**:
```bash
curl -I https://example.com/index.html
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看响应头 | `curl -I https://example.com/static/app.js` | 检查 Cache-Control、ETag 等头 |
| 显示完整请求/响应 | `curl -v https://example.com/api/data` | 显示请求行、状态码、所有头 |
| 跟随重定向 | `curl -IL https://example.com/old-page` | 跟随 301/302 跳转查看最终头 |
| 自定义请求头 | `curl -I -H "If-None-Match: \"abc123\"" https://example.com/index.html` | 发送条件请求 |
| 指定浏览器 UA | `curl -I -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" https://example.com/` | 模拟浏览器请求 |
| 查看源站响应 | `curl -I -H "Host: example.com" http://127.0.0.1:8080/` | 直接请求源站跳过 CDN |

#### curl 缓存相关头

**基础用法**:
```bash
curl -sI https://example.com/index.html | grep -i cache
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看所有缓存头 | `curl -I https://example.com/index.html | grep -E "cache|etag|last-modified|vary"` | 一次性查看所有缓存相关头 |
| 验证 ETag 有效性 | `curl -I -H "If-None-Match: \"abc123\"" https://example.com/index.html` | 如果返回 304 则 ETag 有效 |
| 检查 Vary 头 | `curl -I https://example.com/ | grep -i vary` | 确认差异化缓存是否生效 |
| 比较 CDN 与源站 | `curl -sI https://cdn.example.com/index.html | grep -E "x-cache|age"` | 查看 CDN 命中情况和年龄 |

---

### Lighthouse 缓存审计

#### lighthouse --only-categories - 缓存审计

**基础用法**:
```bash
lighthouse https://example.com --only-categories=performance --output=json --output-path=./lighthouse-report.json
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 缓存性能审计 | `lighthouse https://example.com --only-categories=performance` | 生成包含缓存建议的性能报告 |
| 移动端缓存测试 | `lighthouse https://example.com --preset=mobile --only-categories=performance` | 模拟移动设备测试 |
| 生成 HTML 报告 | `lighthouse https://example.com --output=html --output-path=./cache-audit.html` | 生成可读 HTML 报告 |
| 提取缓存问题 | `lighthouse https://example.com --output=json | jq '.audits[\"uses-cacheable-resources\"].details.items[]'` | 提取不可缓存资源列表 |

---

### 缓存刷新与清除

#### 手动刷新 CDN

**基础用法**:
按云服务商使用对应 CLI 命令或管理控制台刷新。

**扩展示例**:

| 云服务商 | 命令 | 说明 |
|----------|------|------|
| Cloudflare | `wrangler purge ${ZONE}` 或控制台手动刷新 | 清除指定域名的所有缓存 |
| AWS CloudFront | `aws cloudfront create-invalidation --distribution-id %{ID}% --paths "/*"` | 创建全量失效任务 |
| 阿里云 | `aliyun cdn PushObjectCache --ObjectPath "http://example.com/*" --ObjectType Directory` | 全量目录刷新 |
| 腾讯云 | `coscli rm -r cos://bucket-1250000000/path/*` | 对象存储刷新 |

---

## 命令速查表

| 类别 | 操作 | 命令 | 说明 |
|------|------|------|------|
| Cloudflare | 登录 | `wrangler login` | OAuth 授权 |
| Cloudflare | 部署 Worker | `wrangler deploy` | 部署到边缘节点 |
| Cloudflare | KV 操作 | `wrangler kv:key put/get/delete` | 键值存储操作 |
| Cloudflare | Pages 部署 | `wrangler pages deploy ./dist` | 静态站点部署 |
| AWS | 创建分发 | `aws cloudfront create-distribution` | 创建 CDN 分发 |
| AWS | 刷新缓存 | `aws cloudfront create-invalidation --paths "/*"` | 全量缓存失效 |
| 阿里云 | 刷新缓存 | `aliyun cdn PushObjectCache --ObjectPath "http://example.com/*"` | CDN 缓存刷新 |
| Nginx | 定义缓存 | `proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m` | 配置缓存区 |
| Nginx | 启用缓存 | `proxy_cache my_cache; proxy_cache_valid 200 1h;` | 启用反向代理缓存 |
| Varnish | 启动服务 | `varnishd -F -f /etc/varnish/default.vcl` | 启动 Varnish 缓存服务器 |
| Varnish | 清除缓存 | `varnishadm ban "req.url ~ ."` | 清除所有 URL 缓存 |
| Varnish | 查看统计 | `varnishstat -1` | 查看缓存命中率统计 |
| Redis | 设置缓存 | `redis-cli SET cache:page:index EX 3600` | 设置 1 小时过期的缓存 |
| Redis | 读取缓存 | `redis-cli GET cache:page:index` | 获取缓存值 |
| Redis | 批量过期 | `redis-cli EXPIRE cache:* 7200` | 批量设置 2 小时过期 |
| Browser SW | 注册 SW | `navigator.serviceWorker.register('/sw.js')` | 注册 Service Worker |
| Browser Cache | 打开缓存 | `caches.open('v1')` | 打开/创建命名缓存 |
| Browser | 缓存请求 | `cache.add('/api/data')` | 添加请求到缓存 |
| curl | 头部检查 | `curl -I https://example.com/` | 查看缓存相关响应头 |
| curl | 条件请求 | `curl -I -H "If-None-Match: \"abc\"" https://example.com/` | 发送 ETag 条件请求 |
| Lighthouse | 缓存审计 | `lighthouse https://example.com --only-categories=performance` | 性能与缓存审计 |

---

## 实用场景

### 场景 1: 上线后刷新 CDN

```bash
# 1. 部署新版本资源
wrangler deploy

# 2. 刷新 CDN 缓存
aws cloudfront create-invalidation --distribution-id EDFDVBD6EXAMPLE --paths "/*"

# 3. 验证缓存已刷新
curl -I https://your-domain.com/static/app.v2.js | grep -E "x-cache|age"
```

### 场景 2: 配置 Nginx 反向代理缓存

```nginx
# /etc/nginx/conf.d/cache.conf
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=api_cache:10m
                 max_size=1g inactive=60m use_temp_path=off;

server {
    location /api/ {
        proxy_cache api_cache;
        proxy_cache_valid 200 10m;
        proxy_cache_valid 404 1m;
        proxy_cache_bypass $cookie_nocache $arg_nocache;
        add_header X-Cache-Status $upstream_cache_status;
    }
}
```

### 场景 3: Service Worker 完整缓存策略

```javascript
const CACHE_VERSION = 'v2';
const CACHE_NAME = `static-${CACHE_VERSION}`;
const OFFLINE_URL = '/offline.html';

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE_NAME).then(c => c.addAll([
    '/',
    '/index.html',
    '/static/main.css',
    '/static/main.js'
  ])));
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(names =>
    Promise.all(names.filter(n => n.startsWith('static-') && n !== CACHE_NAME).map(caches.delete))
  ));
  self.clients.claim();
});

self.addEventListener('fetch', e => {
  if (e.request.mode === 'navigate') {
    e.respondWith(fetch(e.request).catch(() => caches.match('/index.html')));
  } else {
    e.respondWith(caches.match(e.request).then(r => r || fetch(e.request)));
  }
});
```

### 场景 4: Redis 分布式缓存

```bash
# 设置页面缓存（1小时）
redis-cli SETEX "cache:page:index:zh" 3600 '{"html":"<!DOCTYPE html>...","t":1700000000}'

# 设置用户会话缓存（2天）
redis-cli SETEX "session:user:1001:token" 172800 "eyJhbGciOiJIUzI1NiJ9..."

# 批量清除旧缓存
redis-cli --scan --pattern "cache:page:*" | head -1000 | xargs redis-cli DEL

# 渐进式刷新（新版本发布时）
redis-cli --scan --pattern "cache:page:*" | xargs -P 4 redis-cli EXPIRE 60
```

---

## 相关资源

- [Nginx 命令文档](../Nginx命令/README.md)
- [Redis 基本操作文档](../Redis-基本操作/README.md)
- [Linux 命令文档](../Linux 命令/README.md)