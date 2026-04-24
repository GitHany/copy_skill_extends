# Web API 工具

Web API 工具模块提供 HTTP 客户端、API 测试、文档生成、协议分析和 WebSocket 通信的完整命令参考。

## 模块内容

- HTTP 客户端（curl, httpie, wget, axios/fetch）
- API 测试工具（Postman/Newman, Insomnia CLI）
- API 文档生成（swagger-cli, redoc, apidoc）
- HTTP 协议分析（httpstat, curl verbose）
- WebSocket 通信（wscat, websocat）
- GraphQL 客户端（Apollo Client, urql）

## HTTP 客户端

### curl 命令

curl 是最常用的 HTTP 客户端工具，支持各种 HTTP 操作。

- **GET 请求**：获取资源
- **POST 请求**：提交数据
- **PUT 请求**：更新资源
- **DELETE 请求**：删除资源
- **带 header 请求**：传递认证信息和自定义头
- **查看响应头**：使用 -I 只获取头部信息
- **详细输出**：使用 -v 查看完整请求响应过程

### httpie 命令

httpie 是 curl 的友好替代品，语法更直观，输出高亮。

- **http GET**：简洁的 GET 请求
- **http POST**：带 JSON 体的 POST 请求
- **下载文件**：保存响应到文件

### wget 命令

wget 适合递归下载和后台下载场景。

- **下载文件**：保存到本地
- **后台下载**：断点续传
- **镜像站点**：完整复制网站

### axios / fetch 示例

浏览器和 Node.js 环境中的 HTTP 请求方式。

- **fetch GET**：原生 fetch 发送 GET
- **fetch POST**：带 JSON 体的 POST
- **axios 实例**：创建配置化的 axios 客户端

## API 测试工具

### Newman (Postman CLI)

Newman 是 Postman Collection 的命令行运行器，支持 CI/CD 集成。

- **运行 Collection**：执行预定义的 API 测试集合
- **导出环境**：指定环境变量文件
- **生成报告**：HTML 格式的测试报告

### Insomnia CLI

Insomnia 的命令行工具，支持从配置文件运行测试。

- **导入数据**：从 .json 或 .yaml 导入 API 定义
- **运行测试**：执行 API 端点测试

### Hoppscotch CLI

Hoppscotch（开源 Postman 替代）的命令行工具。

- **发送请求**：从命令行发送 HTTP 请求
- **运行 Collection**：执行 API 集合测试

## API 文档工具

### swagger-cli

验证和打包 OpenAPI/Swagger 定义。

- **验证规范**：检查 OpenAPI 文档合法性
- **打包 Bundle**：将分散的文档合并为单文件

### redoc

将 OpenAPI 规范渲染为独立的 HTML 文档。

- **本地渲染**：生成离线 HTML 文档
- **CLI 渲染**：通过 redoc-cli 生成文档

### apidoc

从代码注释生成 API 文档。

- **生成文档**：扫描代码生成 HTML 文档
- **指定输出**：指定生成目录

## HTTP 协议分析

### httpstat

可视化 HTTP 请求各阶段耗时（DNS 解析、连接、TLS、TTFB）。

- **查看耗时**：显示每个阶段的耗时
- **自定义 cURL**：附加 curl 参数

### curl -v 详细模式

显示完整的 HTTP 请求和响应过程。

- **显示请求行**：HTTP 方法、路径、协议版本
- **显示响应头**：状态码、内容类型
- **显示详情**：DNS 查找、TLS 握手等信息

### curl -I 头部模式

只获取 HTTP 响应头，用于快速检查资源可用性。

- **检查资源**：验证资源是否存在
- **查看缓存头**：检查 Cache-Control、ETag

### 浏览器 DevTools Network

浏览器内置的网络分析工具。

- **检查请求**：查看请求头、响应头、timing
- **复制 cURL**：从 DevTools 复制完整 curl 命令

## WebSocket 通信

### wscat

Node.js 实现的 WebSocket 客户端命令行工具。

- **连接服务**：连接到 WebSocket 服务器
- **发送消息**：交互式发送文本消息
- **带 Auth 连接**：使用 Token 认证连接

### websocat

Rust 实现的 WebSocket 客户端，支持更多协议。

- **连接 ws**：连接普通 WebSocket
- **连接 wss**：连接加密 WebSocket
- **广播模式**：同时连接多个服务端

## GraphQL 客户端

### Apollo Client CLI

Apollo 生态的命令行工具。

- **生成代码**：从 Schema 生成 TypeScript 类型
- **服务端启动**：快速启动 Apollo Server

### urql

轻量级 GraphQL 客户端的命令行用法。

- **初始化**：创建 urql Client 实例
- **执行查询**：发送 GraphQL 查询

## 通用参数说明

| 参数 | 说明 | 示例 |
|------|------|------|
| url | 请求目标地址 | http://localhost:3000/api |
| header | HTTP 请求头 | Authorization: Bearer xxx |
| method | HTTP 方法 | GET/POST/PUT/DELETE |
| data | 请求体数据 | {"name": "Alice"} |
| timeout | 超时时间（毫秒） | 5000 |

## 常见场景

- **调试 API**：使用 curl -v 或 httpstat 查看详细过程
- **自动化测试**：Newman 运行 Collection 生成报告
- **文档维护**：apidoc/swagger-cli 保持文档同步
- **实时通信**：wscat 测试 WebSocket 服务
- **性能分析**：httpstat 定位 API 慢的原因
