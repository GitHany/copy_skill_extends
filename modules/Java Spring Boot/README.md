# Java Spring Boot 命令文档

Java Spring Boot 全栈开发完整参考文档，涵盖项目初始化、核心开发、数据访问、安全配置、监控运维及构建部署。

## 目录

- [Spring Boot 初始化](#spring-boot-初始化)
- [Spring Boot 核心命令](#spring-boot-核心命令)
- [Spring Boot CLI](#spring-boot-cli)
- [Spring Data 数据访问](#spring-data-数据访问)
- [Spring Security 安全配置](#spring-security-安全配置)
- [Spring Boot Actuator 监控](#spring-boot-actuator-监控)
- [Maven 构建工具](#maven-构建工具)
- [Gradle 构建工具](#gradle-构建工具)
- [Docker 容器化](#docker-容器化)

---

## Spring Boot 初始化

### spring init - 项目初始化

**基础用法**:
```bash
curl https://start.spring.io/starter.tgz \
  -d type=maven-project \
  -d language=java \
  -d bootVersion=3.2.0 \
  -d baseDir=%{项目名称}% \
  -d groupId=%{组ID}% \
  -d artifactId=%{制品ID}% \
  -d name=%{项目名称}% \
  -d packageName=%{包名}% \
  -d javaVersion=17 \
  -d dependencies=web,data-jpa,security,actuator | tar -xzf -
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| Maven 项目 | `spring init --name=%{名称}% --type=maven-project --java-version=%{版本}% %{目录}%` | Java 版本示例：`17`；目录示例：`myapp` 【常用】 |
| Gradle 项目 | `spring init --type=gradle-project --dependencies=web,data-jpa %{目录}%` | 依赖示例：`web,data-jpa` 【常用】 |
| 指定包名 | `spring init --package-name=%{包名}% %{目录}%` | 包名示例：`com.example.app` 【常用】 |
| 交互式初始化 | `spring init` | 启动交互式项目初始化向导 【常用】 |
| 添加依赖 | `spring init --dependencies=web,actuator,security %{目录}%` | Web、监控、安全依赖 【常用】 |

---

## Spring Boot 核心命令

### mvn spring-boot:run - 运行应用

**基础用法**:
```bash
mvn spring-boot:run
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定 profile | `mvn spring-boot:run -Dspring-boot.run.profiles=%{环境}%` | 环境示例：`dev`、`prod` 【常用】 |
| 指定参数 | `mvn spring-boot:run -Dspring-boot.run.arguments='--server.port=9000'` | 端口示例：`9000` 【常用】 |
| Maven Wrapper | `./mvnw spring-boot:run` | 无需安装 Maven，直接运行 【常用】 |
| 指定 JVM 参数 | `mvn spring-boot:run -Djvm.args='-Xmx512m'` | 内存示例：`-Xmx512m` |

### mvn spring-boot:build-image - 构建镜像

**基础用法**:
```bash
mvn spring-boot:build-image
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定镜像名 | `mvn spring-boot:build-image -Dspring-boot.build-image.imageName=%{镜像名}%` | 镜像名示例：`myapp:v1.0` 【常用】 |
| 指定 Builder | `mvn spring-boot:build-image -Dspring-boot.build-image.builder=paketobuildpacks/builder:tiny` | 使用 Tiny Builder 【常用】 |
| 带标签构建 | `mvn spring-boot:build-image -DImageName=%{镜像名}%:%{标签}%` | 标签示例：`latest` 【常用】 |

### mvn clean - 清理构建

**基础用法**:
```bash
mvn clean
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 清理并打包 | `mvn clean package` | 清理后重新打包 【常用】 |
| 清理并安装 | `mvn clean install` | 清理后安装到本地仓库 【常用】 |
| 清理并跳过测试 | `mvn clean package -DskipTests` | 跳过单元测试 【常用】 |

### mvn compile - 编译项目

**基础用法**:
```bash
mvn compile
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 编译测试代码 | `mvn test-compile` | 编译主代码和测试代码 【常用】 |
| 指定编码 | `mvn compile -Dproject.reporting.outputEncoding=UTF-8` | 指定编译编码 |
| 增量编译 | `mvn compile -o` | 离线增量编译 |

### mvn test - 运行测试

**基础用法**:
```bash
mvn test
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 运行单个测试类 | `mvn test -Dtest=%{测试类名}%` | 测试类名示例：`UserServiceTest` 【常用】 |
| 运行单个测试方法 | `mvn test -Dtest=%{类名}#%{方法名}%` | 方法名示例：`testSaveUser` 【常用】 |
| 生成测试报告 | `mvn test surefire-report:report` | 生成测试报告 |
| 跳过测试 | `mvn package -DskipTests` | 打包时跳过测试 【常用】 |

### mvn package - 打包应用

**基础用法**:
```bash
mvn package
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 跳过测试打包 | `mvn package -DskipTests` | 快速打包 【常用】 |
| 指定打包格式 | `mvn package -Dpackaging=jar` | 指定为 JAR 包 【常用】 |
| 包含源码 | `mvn package -Dsource=true` | 同时打包源码 |

### ./mvnw - Maven Wrapper

**基础用法**:
```bash
./mvnw %{命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 运行应用 | `./mvnw spring-boot:run` | 使用 Wrapper 运行 【常用】 |
| 打包项目 | `./mvnw clean package` | 使用 Wrapper 打包 【常用】 |
| 查看版本 | `./mvnw -version` | 查看 Maven Wrapper 版本 【常用】 |
| 升级 Wrapper | `./mvnw wrapper:wrapper` | 升级 Wrapper 版本 |

### ./gradlew bootRun - Gradle 运行

**基础用法**:
```bash
./gradlew bootRun
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定 profile | `./gradlew bootRun --args='--spring.profiles.active=dev'` | 环境示例：`dev`、`prod` 【常用】 |
| 跳过测试运行 | `./gradlew bootRun -x test` | 不运行测试直接启动 【常用】 |
| 带调试端口 | `./gradlew bootRun --debug-jvm` | 开启 JVM 调试模式 |

---

## Spring Boot CLI

### spring run - 运行应用

**基础用法**:
```bash
spring run %{文件名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 运行 Groovy 脚本 | `spring run app.groovy` | 运行 Groovy 应用 【常用】 |
| 指定参数 | `spring run app.groovy -- --server.port=9000` | 自定义端口 |
| 跳过依赖下载 | `spring run app.groovy --offline` | 离线模式运行 |

### spring test - 测试应用

**基础用法**:
```bash
spring test %{测试文件}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 运行所有测试 | `spring test` | 运行所有测试文件 |
| 运行单个测试 | `spring test %{测试文件}%` | 测试文件示例：`AppTests.groovy` 【常用】 |
| 生成报告 | `spring test --report` | 生成测试报告 |

### Spring Shell - 交互式 Shell

**基础用法**:
```bash
spring shell
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 退出 Shell | `exit` 或 `quit` | 退出交互式 Shell 【常用】 |
| 内嵌命令 | `spring --version` | 在 Shell 内执行 Spring 命令 |
| 加载脚本 | `spring script %{脚本文件}%` | 执行 Groovy 脚本文件 |

### BeanShell 集成

**基础用法**:
```bash
spring grab
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 解析依赖 | `spring grab *.groovy` | 自动解析并下载依赖 【常用】 |
| 编译 Groovy | `spring compile *.groovy` | 预编译 Groovy 文件 |
| 测试脚本 | `spring test *.groovy` | 运行 Groovy 测试 |

---

## Spring Data 数据访问

### Spring Data JPA

**基础用法**:
```bash
mvn spring-boot:run -Dspring-boot.run.arguments='--spring.datasource.url=jdbc:postgresql://localhost:5432/%{库名}%'
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 生成实体 | `mvn spring-boot:run` 配合 `@Entity` 注解 | JPA 自动建表 【常用】 |
| 启用 SQL 日志 | `mvn spring-boot:run -Dspring-boot.run.arguments='--logging.level.org.hibernate.SQL=DEBUG'` | 显示 SQL 语句 【常用】 |
| 初始化数据 | `--spring.jpa.defer-datasource-initialization=true` | 配合 `data.sql` 初始化数据 【常用】 |
| 验证 Schema | `--spring.jpa.hibernate.ddl-auto=validate` | 启动时验证数据库结构 【常用】 |
| 显示DDL | `--spring.jpa.show-sql=true` | 显示数据定义语句 【常用】 |

### Spring Data Redis

**基础用法**:
```bash
mvn spring-boot:run -Dspring-boot.run.arguments='--spring.data.redis.host=%{主机}% --spring.data.redis.port=%{端口}%'
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 连接 Redis 集群 | `--spring.data.redis.cluster.nodes=%{节点}%` | 集群节点示例：`localhost:7000,localhost:7001` 【常用】 |
| 设置密码 | `--spring.data.redis.password=%{密码}%` | Redis 认证密码 【常用】 |
| 启用 SSL | `--spring.data.redis.ssl=true` | 启用 SSL 加密连接 |
| 配置超时 | `--spring.data.redis.timeout=%{超时}%` | 超时示例：`10s` 【常用】 |
| 连接池配置 | `--spring.data.redis.jedis.pool.max-active=8` | 配置连接池 【常用】 |

### Spring Data MongoDB

**基础用法**:
```bash
mvn spring-boot:run -Dspring-boot.run.arguments='--spring.data.mongodb.uri=mongodb://%{主机}%:%{端口}%/%{数据库}%'
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 认证连接 | `--spring.data.mongodb.authentication-database=%{认证库}%` | 认证数据库示例：`admin` 【常用】 |
| 副本集连接 | `--spring.data.mongodb.uri=mongodb://%{主机}%/%{库名}%?replicaSet=%{副本集}%` | 副本集名称示例：`rs0` 【常用】 |
| GridFS 存储 | `--spring.data.mongodb.grid-fs-database=%{数据库}%` | 配置 GridFS 数据库 |
| 关闭自动索引 | `--spring.data.mongodb.auto-index-creation=false` | 禁用自动创建索引 |

### Spring Data Elasticsearch

**基础用法**:
```bash
mvn spring-boot:run -Dspring-boot.run.arguments='--spring.elasticsearch.uris=http://%{主机}%:%{端口}%'
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 多节点连接 | `--spring.elasticsearch.uris=http://%{节点1}%:%{端口1}%,http://%{节点2}%:%{端口2}%` | 多节点集群 【常用】 |
| 设置用户名密码 | `--spring.elasticsearch.username=%{用户名}% --spring.elasticsearch.password=%{密码}%` | Basic 认证 【常用】 |
| 连接超时 | `--spring.elasticsearch.connection-timeout=%{超时}%` | 超时示例：`5s` 【常用】 |
| 索引自动创建 | `--spring.elasticsearch.data.repositories.enabled=true` | 启用 ES 数据仓库 【常用】 |

---

## Spring Security 安全配置

### Spring Security 配置

**基础用法**:
```bash
mvn spring-boot:run -Dspring-boot.run.arguments='--spring.security.user.name=%{用户名}% --spring.security.user.password=%{密码}%'
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 配置角色 | `--spring.security.user.roles=%{角色}%` | 角色示例：`ADMIN`、`USER` 【常用】 |
| 内存认证 | `mvn spring-boot:run -Dspring-boot.run.arguments='--spring.security.enabled=false'` | 临时禁用 Security |
| 启用 LDAP | `--spring.ldap.urls=ldap://%{主机}%:%{端口}%` | 配置 LDAP 认证 【常用】 |

### OAuth2 资源服务器

**基础用法**:
```bash
mvn spring-boot:run -Dspring-boot.run.arguments='--spring.security.oauth2.resourceserver.jwt.issuer-uri=%{发行者URI}%'
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| JWKS 端点 | `--spring.security.oauth2.resourceserver.jwt.jwk-set-uri=%{jwks_uri}%` | JWKS 端点示例：`https://auth.example.com/.well-known/jwks.json` 【常用】 |
| 公开密钥 | `--spring.security.oauth2.resourceserver.jwt.public-key-location=classpath:public.pem` | 本地公钥文件 |
| JWT 解码器 | `--spring.security.oauth2.resourceserver.jwt.decoder-jwk-set-uri=%{uri}%` | 自定义 JWK 解码器 【常用】 |

### JWT 集成

**基础用法**:
```bash
mvn spring-boot:run -Dspring-boot.run.arguments='--jwt.secret=%{密钥}% --jwt.expiration=%{过期时间}%'
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 生成令牌 | `curl -X POST http://localhost:8080/auth/token -d "username=%{用户名}%&password=%{密码}%"` | 获取 JWT 令牌 【常用】 |
| 验证令牌 | `curl -H "Authorization: Bearer %{令牌}%" http://localhost:8080/api/resource` | 访问受保护资源 【常用】 |
| 刷新令牌 | `curl -X POST http://localhost:8080/auth/refresh -H "Authorization: Bearer %{令牌}%"` | 刷新过期令牌 |

### 方法安全 @PreAuthorize

**基础用法**:
```bash
mvn spring-boot:run -Dspring-boot.run.arguments='--spring.security.enable-method-security=true'
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启用方法安全 | `--spring.security.enable-method-security=true` | 开启 `@PreAuthorize` 等注解 【常用】 |
| 角色校验 | `@PreAuthorize("hasRole('ADMIN')")` | 限制为 ADMIN 角色 【常用】 |
| 权限校验 | `@PreAuthorize("hasAuthority('WRITE')")` | 限制为 WRITE 权限 【常用】 |
| SpEL 表达式 | `@PreAuthorize("#owner == authentication.name")` | 自定义权限表达式 【常用】 |
| 开启 CSRF | `--server.servlet.session.cookie.http-only=false`（需配合 CSRF 配置） | 启用 CSRF 防护 【常用】 |

---

## Spring Boot Actuator 监控

### /actuator/health - 健康检查

**基础用法**:
```bash
curl http://localhost:%{端口}%/actuator/health
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 详细信息 | `curl http://localhost:8080/actuator/health?mediatype=details` | 显示各组件健康详情 【常用】 |
| 自定义健康指示器 | `curl http://localhost:8080/actuator/health/custom` | 查看自定义健康检查结果 |
| 显示全部端点 | `curl http://localhost:8080/actuator` | 列出所有 Actuator 端点 【常用】 |

### /actuator/info - 应用信息

**基础用法**:
```bash
curl http://localhost:%{端口}%/actuator/info
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| Git 信息 | `--management.info.git.mode=full` | 显示 Git 提交信息 【常用】 |
| 构建信息 | `--management.info.build.enabled=true` | 显示构建信息 【常用】 |
| 自定义 info | `spring.application.admin.enabled=true` | 注册为管理应用 |

### /actuator/metrics - 指标监控

**基础用法**:
```bash
curl http://localhost:%{端口}%/actuator/metrics
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| JVM 内存 | `curl http://localhost:8080/actuator/metrics/jvm.memory.used` | 查看 JVM 内存使用 【常用】 |
| HTTP 请求 | `curl http://localhost:8080/actuator/metrics/http.server.requests` | 查看 HTTP 请求统计 【常用】 |
| 自定义指标 | `curl http://localhost:8080/actuator/metrics/%{指标名}%` | 查看自定义指标 【常用】 |
| 显示标签 | `curl http://localhost:8080/actuator/metrics/%{指标}%?tag=%{标签}%:%{值}%` | 按标签过滤 【常用】 |
| Tomcat 指标 | `curl http://localhost:8080/actuator/metrics/tomcat.threads.busy` | Tomcat 线程繁忙度 【常用】 |

### /actuator/env - 环境变量

**基础用法**:
```bash
curl http://localhost:%{端口}%/actuator/env
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看特定属性 | `curl http://localhost:8080/actuator/env/%{属性名}%` | 查看单个配置属性 【常用】 |
| 刷新配置 | `curl -X POST http://localhost:8080/actuator/refresh` | 刷新上下文配置 【常用】 |
| 启用敏感数据 | `--management.endpoint.env.show-values=always` | 显示环境变量值 |
| 属性源 | `curl http://localhost:8080/actuator/env?factor=%{factor}%` | 查看指定 Factor 的属性 |

### /actuator/configprops - 配置属性

**基础用法**:
```bash
curl http://localhost:%{端口}%/actuator/configprops
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 按前缀过滤 | `curl http://localhost:8080/actuator/configprops?prefix=%{前缀}%` | 前缀示例：`spring.datasource` 【常用】 |
| 查看特定属性 | `curl http://localhost:8080/actuator/configprops/%{id}%` | 查看指定 ID 的配置属性 【常用】 |
| 验证配置 | `curl http://localhost:8080/actuator/configprops --head=accept:application/json` | 验证配置是否正确加载 【常用】 |

### Actuator 其他常用端点

**基础用法**:
```bash
curl http://localhost:%{端口}%/actuator/%{端点}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| beans | `curl http://localhost:8080/actuator/beans` | 查看所有 Spring Bean 【常用】 |
| conditions | `curl http://localhost:8080/actuator/conditions` | 查看自动配置条件 【常用】 |
| httpexchanges | `curl http://localhost:8080/actuator/httpexchanges` | 查看 HTTP 调用记录 【常用】 |
| mappings | `curl http://localhost:8080/actuator/mappings` | 查看所有请求映射 【常用】 |
| scheduledtasks | `curl http://localhost:8080/actuator/scheduledtasks` | 查看定时任务 【常用】 |
| threaddump | `curl http://localhost:8080/actuator/threaddump` | 查看线程 dump 【常用】 |
| heapdump | `curl -o heapdump.hprof http://localhost:8080/actuator/heapdump` | 下载堆转储文件 【常用】 |

---

## Maven 构建工具

### mvn clean install - 安装到本地仓库

**基础用法**:
```bash
mvn clean install
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 跳过测试 | `mvn clean install -DskipTests` | 跳过单元测试 【常用】 |
| 跳过检查 | `mvn clean install -DskipChecks` | 跳过代码检查 【常用】 |
| 指定 profile | `mvn clean install -P%{profile}%` | Profile 示例：`prod` 【常用】 |
| 离线模式 | `mvn clean install -o` | 使用本地缓存构建 |
| 带源码安装 | `mvn clean install -Dsource=true` | 包含源码包 【常用】 |

### mvn dependency:tree - 依赖树

**基础用法**:
```bash
mvn dependency:tree
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 过滤依赖 | `mvn dependency:tree -Dincludes=%{groupId}%:%{artifactId}%` | 过滤示例：`org.springframework` 【常用】 |
| 排除依赖 | `mvn dependency:tree -Dexcludes=%{groupId}%:%{artifactId}%` | 排除示例：`junit:junit` |
| 输出到文件 | `mvn dependency:tree > dependency.txt` | 导出依赖树 【常用】 |
| 完整输出 | `mvn dependency:tree -Dverbose` | 显示被裁剪的传递依赖 |
| 分析依赖 | `mvn dependency:analyze` | 分析未使用/缺失的依赖 【常用】 |

### mvn dependency:resolve - 解析依赖

**基础用法**:
```bash
mvn dependency:resolve
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 解析插件 | `mvn dependency:resolve-plugins` | 解析插件依赖 【常用】 |
| 列出依赖 | `mvn dependency:list` | 列出已解析依赖 【常用】 |
| 复制依赖 | `mvn dependency:copy-dependencies -DoutputDirectory=%{目录}%` | 复制依赖到指定目录 【常用】 |

---

## Gradle 构建工具

### gradle build - 构建项目

**基础用法**:
```bash
./gradlew build
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 跳过测试构建 | `./gradlew build -x test` | 跳过测试 【常用】 |
| 清理后构建 | `./gradlew clean build` | 清理后重新构建 【常用】 |
| 检查代码 | `./gradlew check` | 运行所有检查 【常用】 |
| 仅编译 | `./gradlew classes` | 仅编译主代码 |
| 生成文档 | `./gradlew javadoc` | 生成 JavaDoc 文档 |

### bootJar - 打包可执行 JAR

**基础用法**:
```bash
./gradlew bootJar
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定主类 | `./gradlew bootJar --main-class=%{主类}%` | 主类示例：`com.example.Application` 【常用】 |
| 排除依赖 JAR | `./gradlew bootJar -PexcludeJarTask=true` | 不打包依赖为 fat jar |
| 查看构建文件 | `./gradlew bootJar --info` | 显示构建详细信息 |
| 运行打包产物 | `java -jar build/libs/%{文件名}%.jar` | 运行可执行 JAR 【常用】 |

### gradle bootBuildImage - 构建 Docker 镜像

**基础用法**:
```bash
./gradlew bootBuildImage
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定镜像名 | `./gradlew bootBuildImage --imageName=%{镜像名}%` | 镜像名示例：`myapp:v1.0` 【常用】 |
| 指定 Builder | `./gradlew bootBuildImage --builder=%{builder}%` | Builder 示例：`paketobuildpacks/builder:tiny` 【常用】 |
| 镜像拉取策略 | `./gradlew bootBuildImage --pullPolicy=ifNotPresent` | 避免每次拉取 【常用】 |

---

## Docker 容器化

### 构建 Spring Boot Docker 镜像

**基础用法**:
```bash
mvn spring-boot:build-image -Dspring-boot.build-image.imageName=%{镜像名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 带版本标签 | `mvn spring-boot:build-image -DImageName=%{镜像名}%:%{版本}%` | 版本示例：`1.0.0` 【常用】 |
| 运行容器 | `docker run -p 8080:8080 %{镜像名}%` | 运行 Docker 容器 【常用】 |
| 多架构构建 | `mvn spring-boot:build-image -Dplatform.list=linux/amd64,linux/arm64` | 多平台镜像 |
| 自定义 Dockerfile | `docker build -t %{镜像名}% -f Dockerfile %{上下文}%` | 使用自定义 Dockerfile 【常用】 |

### Docker Compose 与 Spring Boot

**基础用法**:
```bash
docker-compose up -d
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动应用和数据库 | `docker-compose -f docker-compose.yml up -d` | 启动完整环境 【常用】 |
| 只启动数据库 | `docker-compose up -d postgres` | 只启动数据库 【常用】 |
| 查看日志 | `docker-compose logs -f %{服务}%` | 服务示例：`app` 【常用】 |
| 停止并清理 | `docker-compose down -v` | 停止并删除卷 【常用】 |

### 多阶段构建 Dockerfile

**Dockerfile 示例**:
```dockerfile
# 构建阶段
FROM maven:3.9-eclipse-temurin-17 AS builder
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline
COPY src ./src
RUN mvn package -DskipTests

# 运行阶段
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY --from=builder /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app/app.jar"]
```

---

## 实用场景示例

### 场景 1: 从零创建并运行 Spring Boot 项目

```bash
# 1. 初始化项目
curl https://start.spring.io/starter.tgz \
  -d type=maven-project \
  -d language=java \
  -d bootVersion=3.2.0 \
  -d baseDir=myapp \
  -d groupId=com.example \
  -d artifactId=myapp \
  -d name=myapp \
  -d packageName=com.example.myapp \
  -d javaVersion=17 \
  -d dependencies=web,data-jpa,security,actuator | tar -xzf -

# 2. 进入项目目录
cd myapp

# 3. 编译打包
./mvnw clean package -DskipTests

# 4. 构建 Docker 镜像
./mvnw spring-boot:build-image -DImageName=myapp:latest

# 5. 运行应用
docker run -p 8080:8080 myapp:latest
```

### 场景 2: 开发模式快速启动

```bash
# 启用热重载开发模式
./mvnw spring-boot:run -Dspring-boot.run.fork=false

# 指定开发环境 profile
./mvnw spring-boot:run -Dspring-boot.run.profiles=dev

# 开启 SQL 日志
./mvnw spring-boot:run -Dspring-boot.run.arguments='--logging.level.org.hibernate.SQL=DEBUG --logging.level.org.hibernate.type.descriptor.sql.BasicBinder=TRACE'

# 开启 Actuator 端点
./mvnw spring-boot:run -Dspring-boot.run.arguments='--management.endpoints.web.exposure.include=* --management.endpoint.health.show-details=always'
```

### 场景 3: 生产环境部署

```bash
# 1. 编译并跳过测试
./gradlew clean build -x test

# 2. 构建 Docker 镜像
./gradlew bootBuildImage --imageName=myapp:prod

# 3. 推送到镜像仓库
docker tag myapp:prod registry.example.com/myapp:prod
docker push registry.example.com/myapp:prod

# 4. 使用 Docker Compose 启动
docker-compose -f docker-compose.prod.yml up -d

# 5. 检查健康状态
curl http://localhost:8080/actuator/health
```

### 场景 4: 性能压测与监控

```bash
# 1. 启动应用并开启完整监控
./mvnw spring-boot:run -Dspring-boot.run.arguments='--management.endpoints.web.exposure.include=*,metrics,prometheus --management.metrics.export.prometheus.enabled=true'

# 2. 查看 JVM 内存
curl http://localhost:8080/actuator/metrics/jvm.memory.used

# 3. 查看 HTTP 请求延迟
curl http://localhost:8080/actuator/metrics/http.server.requests?tag=uri:/api/users

# 4. 查看活跃线程
curl http://localhost:8080/actuator/metrics/tomcat.threads.current

# 5. 查看连接池状态
curl http://localhost:8080/actuator/metrics/hikaricp.connections.active
```

---

## 命令速查表

| 操作 | 命令 | 说明 |
|------|------|------|
| 初始化项目 | `spring init` | 创建 Spring Boot 项目 |
| 运行应用 | `mvn spring-boot:run` | Maven 运行应用 |
| 运行应用 | `./gradlew bootRun` | Gradle 运行应用 |
| 构建镜像 | `mvn spring-boot:build-image` | Maven 构建 Docker 镜像 |
| 构建镜像 | `./gradlew bootBuildImage` | Gradle 构建 Docker 镜像 |
| 打包 | `mvn clean package` | Maven 打包 |
| 打包 | `./gradlew build` | Gradle 打包 |
| 运行测试 | `mvn test` | Maven 运行测试 |
| 依赖树 | `mvn dependency:tree` | 查看 Maven 依赖树 |
| 健康检查 | `/actuator/health` | Actuator 健康端点 |
| 指标监控 | `/actuator/metrics` | Actuator 指标端点 |
| 环境配置 | `/actuator/env` | Actuator 环境端点 |
| 配置属性 | `/actuator/configprops` | Actuator 配置属性端点 |
| Docker 运行 | `docker run -p 8080:8080 %{镜像}%` | 运行 Spring Boot 容器 |

---

## 相关资源

- [Spring Boot 官方文档](https://spring.io/projects/spring-boot)
- [Spring Data 官方文档](https://spring.io/projects/spring-data)
- [Spring Security 官方文档](https://spring.io/projects/spring-security)
- [Spring Boot Actuator 官方文档](https://docs.spring.io/spring-boot/docs/current/actuator-api/html/)
- [Spring Initializr](https://start.spring.io/)
