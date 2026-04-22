# 测试框架命令文档

软件测试完整参考文档，涵盖单元测试、E2E测试、API测试、覆盖率统计、测试运行器和Mock工具。

## 📚 目录

- [单元测试](#单元测试)
- [端到端测试 (E2E)](#端到端测试-e2e)
- [API 测试](#api-测试)
- [覆盖率统计](#覆盖率统计)
- [测试运行器](#测试运行器)
- [Mock 工具](#mock-工具)

---

## 单元测试

### Jest 测试命令

**基础用法**:
```bash
jest
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 监视模式 | `jest --watch` | 监视文件变化并自动重新运行测试 【常用】 |
| 覆盖率 | `jest --coverage` | 生成测试覆盖率报告 【常用】 |
| 指定文件 | `jest %{测试文件路径}%` | 测试文件路径示例：`src/__tests__/math.test.ts` |
| 匹配测试名 | `jest -t %{测试名称模式}%` | 测试名称示例：`toBe` 或 `toEqual` |
| 跳过覆盖率 | `jest --coverage=false` | 运行测试但不生成覆盖率报告 |
| 配置文件 | `jest --config %{配置文件路径}%` | 配置文件示例：`jest.config.js` |
| 强制退出 | `jest --forceExit` | 强制测试完成后退出 【常用】 |
| 调试模式 | `jest --debug` | 输出调试信息 |
| 清除缓存 | `jest --clearCache` | 清除 Jest 缓存 |

### Vitest 测试命令

**基础用法**:
```bash
vitest
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 监视模式 | `vitest --watch` | 监视文件变化 【常用】 |
| 覆盖率 | `vitest --coverage` | 生成覆盖率报告 【常用】 |
| 指定文件 | `vitest run %{测试文件}%` | 测试文件示例：`test/math.test.ts` |
| UI 模式 | `vitest --ui` | 启动 Vitest UI 界面 【常用】 |
| 运行所有 | `vitest run` | 单次运行所有测试（不监视） 【常用】 |
| 指定环境 | `vitest --environment %{环境}%` | 环境示例：`jsdom`、`happy-dom`、`node` |
| 更新快照 | `vitest update` | 更新快照文件 【常用】 |
| 并行执行 | `vitest --parallel` | 并行运行测试 【常用】 |

### Pytest 测试命令

**基础用法**:
```bash
pytest
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 详细输出 | `pytest -v` | 详细输出模式 【常用】 |
| 覆盖率 | `pytest --cov=%{源码路径}%` | 源码路径示例：`src` 【常用】 |
| 指定测试 | `pytest %{测试文件或目录}%` | 路径示例：`tests/test_api.py` |
| 标记过滤 | `pytest -m %{标记名}%` | 标记名示例：`slow` 或 `unit` 【常用】 |
| 失败优先 | `pytest --ff` | 从上次失败的测试开始运行 |
| 第一失败即停 | `pytest -x` | 遇到第一个失败就停止 【常用】 |
| 显示print | `pytest -s` | 显示 print 输出 【常用】 |
| 生成报告 | `pytest --html=%{报告路径}% --self-contained-html` | 生成 HTML 报告 |
| 跳过处理 | `pytest --collect-only` | 仅收集测试用例不执行 |

### JUnit 测试命令 (Maven/Gradle)

**基础用法 (Maven)**:
```bash
mvn test
```

**扩展示例 (Maven)**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定测试类 | `mvn test -Dtest=%{测试类名}%` | 测试类名示例：`AppTest` 【常用】 |
| 跳过测试 | `mvn package -DskipTests` | 跳过测试打包 |
| 生成报告 | `mvn test surefire-report:report` | 生成测试报告 |
| 包含测试 | `mvn test -Dincludes=%{测试模式}%` | 模式示例：`**/Test*.java` |

**基础用法 (Gradle)**:
```bash
./gradlew test
```

**扩展示例 (Gradle)**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定测试任务 | `./gradlew test --tests %{测试类名}%` | 测试类名示例：`com.example.AppTest` 【常用】 |
| 生成报告 | `./gradlew test --info` | 详细测试信息输出 |
| 并行测试 | `./gradlew test --parallel` | 并行运行测试 【常用】 |
| 跳过测试 | `./gradlew build -x test` | 跳过测试构建 |

---

## 端到端测试 (E2E)

### Playwright 测试命令

**基础用法**:
```bash
playwright test
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 监视模式 | `playwright test --ui` | 启动 UI 交互模式 【常用】 |
| 调试模式 | `playwright test --debug` | 进入调试模式 【常用】 |
| 指定文件 | `playwright test %{测试文件}%` | 测试文件示例：`tests/login.spec.ts` |
| 生成代码 | `playwright codegen %{URL}%` | 录制生成测试代码 【常用】 |
| 列表浏览器 | `playwright list-browsers` | 列出可用浏览器 |
| 安装浏览器 | `playwright install %{浏览器名}%` | 浏览器名示例：`chromium` 【常用】 |
| 显示报告 | `playwright show-report` | 显示 HTML 测试报告 【常用】 |
| 截图 | `playwright screenshot %{URL}% %{输出文件}%` | 截取页面截图 |
| 并行执行 | `playwright test --workers=%{数量}%` | 数量示例：`4` 【常用】 |

### Cypress 测试命令

**基础用法**:
```bash
cypress run
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 交互模式 | `cypress open` | 打开 Cypress 测试界面 【常用】 |
| 指定规格 | `cypress run --spec %{测试文件}%` | 测试文件示例：`cypress/e2e/login.cy.js` |
| 指定浏览器 | `cypress run --browser %{浏览器名}%` | 浏览器名示例：`chrome`、`firefox`、`electron` |
| 录像模式 | `cypress run --record` | 录制测试视频 【常用】 |
| 并行运行 | `cypress run --parallel` | 并行运行测试 【常用】 |
| 配置环境 | `cypress run --env %{环境变量}%` | 变量示例：`API_BASE_URL=https://staging.example.com` |
| 生成报告 | `cypress run --reporter %{报告类型}%` | 报告类型示例：`junit`、`mocha-junit` |
| 标签过滤 | `cypress run --tag %{标签}%` | 标签示例：`smoke`、`regression` |

### Selenium WebDriver 命令

**基础用法**:
```bash
selenium-side-runner %{项目文件}.side
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定浏览器 | `selenium-side-runner --browser %{浏览器名}%` | 浏览器名示例：`chrome`、`firefox`、`edge` |
| 节点URL | `selenium-side-runner --webdriver-url %{Grid地址}%` | Grid地址示例：`http://localhost:4444/wd/hub` |
| 并行数 | `selenium-side-runner -c "%{配置项}%` | 配置示例：`chromeOptions: { args: [\"--headless\"] }` |
| 输出日志 | `selenium-side-runner --output-directory %{目录}%` | 目录示例：`./test-results` |
| 项目文件 | `selenium-side-runner %{项目路径}%` | 项目路径示例：`tests/my-project.side` |

---

## API 测试

### Newman (Postman CLI) 命令

**基础用法**:
```bash
newman run %{集合文件}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 详细输出 | `newman run %{集合文件}% -r cli` | CLI 详细输出 |
| 环境变量 | `newman run %{集合文件}% -e %{环境文件}%` | 环境文件示例：`env.json` 【常用】 |
| 覆盖率 | `newman run %{集合文件}% --reporters cli,junit` | 多格式报告 【常用】 |
| 全局变量 | `newman run %{集合文件}% -g %{全局文件}%` | 全局文件示例：`globals.json` |
| 迭代次数 | `newman run %{集合文件}% -n %{次数}%` | 次数示例：`10` |
| 超时设置 | `newman run %{集合文件}% --timeout %{毫秒}%` | 毫秒示例：`30000` |
| 导出报告 | `newman run %{集合文件}% --export-report %{输出目录}%` | 输出目录示例：`./reports` |
| 忽略SSL | `newman run %{集合文件}% --insecure` | 忽略 SSL 证书错误 【常用】 |
| 数据文件 | `newman run %{集合文件}% -d %{数据文件}%` | 数据文件示例：`data.csv` 【常用】 |

### curl API 测试命令

**基础用法**:
```bash
curl %{URL}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| POST 请求 | `curl -X POST %{URL}% -H "Content-Type: application/json" -d '%{JSON数据}%'` | JSON数据示例：`{"name":"test"}` 【常用】 |
| 请求头 | `curl -H "%{请求头}%` | 请求头示例：`Authorization: Bearer token123` 【常用】 |
| 响应输出 | `curl -i %{URL}%` | 显示响应头和内容 |
| 下载文件 | `curl -O %{URL}%` | 下载文件到当前目录 |
| 详细输出 | `curl -v %{URL}%` | 显示完整请求/响应详情 【常用】 |
| 保存响应 | `curl -o %{输出文件}% %{URL}%` | 输出文件示例：`response.json` |
| 表单提交 | `curl -X POST -F "file=@%{文件路径}%" %{上传URL}%` | 文件路径示例：`./data.txt` 【常用】 |
| 跟随重定向 | `curl -L %{URL}%` | 跟随 301/302 重定向 |
| 用户认证 | `curl -u %{用户名}%:%{密码}% %{URL}%` | 基本认证 【常用】 |

### Node.js HTTP 测试库

**httptest (Go) 命令**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 运行测试 | `go test -v ./...` | 运行所有 Go 测试 【常用】 |
| 覆盖率 | `go test -cover ./...` | 生成覆盖率报告 【常用】 |
| 基准测试 | `go test -bench=.` | 运行基准测试 【常用】 |
| 详细覆盖 | `go test -coverprofile=%{覆盖文件}%` | 覆盖文件示例：`coverage.out` |

**supertest (Node.js) 命令**:

```bash
npm test
```

| 场景 | 说明 |
|------|------|
| 使用 supertest | `const request = require('supertest'); const app = require('./app'); request(app).get('/users').expect(200, done);` |
| POST 测试 | `request(app).post('/users').send({name: 'John'}).expect(201, done);` |
| 认证测试 | `request(app).get('/profile').set('Authorization', 'Bearer token').expect(200, done);` |

---

## 覆盖率统计

### Istanbul/NYC 覆盖率命令

**基础用法**:
```bash
npx nyc %{命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 运行并覆盖 | `npx nyc jest` | 使用 Istanbul 统计 Jest 覆盖率 【常用】 |
| 报告格式 | `npx nyc report --reporter=text` | 文本格式报告 |
| HTML 报告 | `npx nyc report --reporter=html` | 生成 HTML 报告 【常用】 |
| LCOV 格式 | `npx nyc report --reporter=lcov` | 生成 LCOV 格式 (用于 Codecov) 【常用】 |
| 输出目录 | `npx nyc report --report-dir=%{目录}%` | 目录示例：`./coverage` |
| 检查阈值 | `npx nyc --check-coverage --branches %{阈值}%` | 阈值示例：`80` 【常用】 |
| 排除文件 | `npx nyc --exclude=%{文件或目录}%` | 示例：`--exclude='**/node_modules/**'` |
| 合并报告 | `npx nyc merge ./coverage .nyc_output/out.json` | 合并多次运行的覆盖率数据 |

### coverage (Python) 命令

**基础用法**:
```bash
coverage run -m pytest
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 生成报告 | `coverage report` | 显示覆盖率报告 【常用】 |
| HTML 报告 | `coverage html` | 生成 HTML 覆盖率报告 【常用】 |
| XML 报告 | `coverage xml` | 生成 Cobertura XML 格式 【常用】 |
| 合并数据 | `coverage combine` | 合并多数据文件 【常用】 |
| 详细报告 | `coverage report -m` | 显示未覆盖的行号 |
| 百分比过滤 | `coverage report --precision=2` | 显示两位小数精度 |
| 检查阈值 | `coverage report --fail-under=%{阈值}%` | 阈值示例：`80` 【常用】 |

### Codecov 上传命令

**基础用法**:
```bash
codecov
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| Token 上传 | `codecov --token=%{TOKEN}%` | 使用项目 Token 上传 【常用】 |
| 指定报告 | `codecov --file=%{覆盖率文件}%` | 文件示例：`coverage/lcov.info` |
| CI 环境 | `codecov --env CI=true` | 设置 CI 环境变量 |
| 提交SHA | `codecov --sha %{COMMIT_SHA}%` | 指定提交 SHA |
| 分支名 | `codecov --branch %{分支名}%` | 分支名示例：`main` |
| 强制覆盖 | `codecov --pr %{PR号}%` | 指定 PR 编号 |

---

## 测试运行器

### npm / yarn 测试命令

**基础用法**:
```bash
npm test
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 监视模式 | `npm test -- --watch` | 持续监视文件变化 【常用】 |
| 覆盖率 | `npm test -- --coverage` | 生成覆盖率报告 【常用】 |
| 指定文件 | `npm test -- %{测试文件路径}%` | 文件示例：`src/__tests__/user.test.js` |
| 单次运行 | `npm test -- --watchAll=false` | 不进入监视模式 【常用】 |
| CI 模式 | `npm test -- --ci` | CI 环境优化模式 【常用】 |

**yarn 测试命令**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 运行测试 | `yarn test` | 运行测试 【常用】 |
| 监视模式 | `yarn test --watch` | 监视模式 【常用】 |
| 覆盖率 | `yarn test --coverage` | 覆盖率 【常用】 |

### 跨环境测试命令

**基础用法**:
```bash
npm run test:all
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| Node 版本测试 | `nvm exec 18 npm test` | 在 Node 18 中运行测试 |
| 多版本测试 | `npx concurrently "npm test" "npm run test:node16"` | 并行多版本测试 |
| 浏览器测试 | `npx playwright test --browser=chromium,firefox,webkit` | 多浏览器测试 【常用】 |
| 平台测试 | `npm run test:linux && npm run test:windows` | 跨平台测试 |
| Docker 测试 | `docker run -v %(pwd):/app node:18 npm test` | 在容器中测试 |

### 并行测试执行命令

**基础用法**:
```bash
npm test -- --maxWorkers=4
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| Jest 并行 | `jest --maxWorkers=50%` | 使用 50% CPU 核心 【常用】 |
| Vitest 并行 | `vitest --threads` | 启用多线程 【常用】 |
| Pytest 并行 | `pytest -n auto` | pytest-xdist 自动并行 【常用】 |
| Cypress 并行 | `cypress run --parallel --record --key %{CYPRESS_KEY}%` | Cypress 并行记录 【常用】 |
| 进程数 | `npm test -- --parallel --workers=%{数量}%` | 数量示例：`4` 【常用】 |

---

## Mock 工具

### MSW (Mock Service Worker) 命令

**基础用法**:
```bash
npx msw init %{公共目录}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 初始化 | `npx msw init public/ --save` | 初始化 MSW 服务 worker 【常用】 |
| 创建处理器 | `npx msw init && npx msw add https://api.example.com/users --method GET` | 创建请求处理器 |
| 启动服务 | `npx msw service-worker.js` | 启动 mock 服务 |
| 开发模式 | `npm run msw init` | 在开发脚本中初始化 |

### nock (HTTP Mock) 命令

**基础用法**:
```javascript
const nock = require('nock');
nock('https://api.example.com').get('/users').reply(200, { users: [] });
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| GET 请求 | `nock('https://api.example.com').get('/users').reply(200, {users: [{id: 1}]});` | Mock GET 请求 【常用】 |
| POST 请求 | `nock('https://api.example.com').post('/users').reply(201, {id: 1});` | Mock POST 请求 【常用】 |
| 带查询参数 | `nock('https://api.example.com').get('/users').query({active: true}).reply(200, []);` | 带查询参数的 Mock |
| 延迟响应 | `nock('https://api.example.com').get('/slow').delay(2000).reply(200, 'ok');` | 模拟网络延迟 |
| 清理 | `nock.cleanAll()` | 清理所有 Mock 【常用】 |
| 持久 Mock | `nock('https://api.example.com').persist().get('/users').reply(200, []);` | 持久 Mock |
| 验证请求 | `nock('https://api.example.com').post('/users', {name: 'John'}).reply(201);` | 验证请求体 |

### sinon 命令

**基础用法**:
```javascript
const sinon = require('sinon');
const spy = sinon.spy();
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 创建 Spy | `sinon.spy(obj, 'method')` | 创建方法监视 【常用】 |
| 创建 Stub | `sinon.stub(obj, 'method').returns(value)` | 替换方法实现 【常用】 |
| 创建 Mock | `const mock = sinon.mock(obj); mock.expects('method').returns(value);` | 创建 Mock 对象 【常用】 |
| 恢复 Stub | `stub.restore()` | 恢复原始方法 【常用】 |
| 断言调用 | `spy.calledWith(arg1, arg2)` | 断言调用参数 |
| 伪造时间 | `sinon.useFakeTimers()` | 伪造定时器 【常用】 |
| 伪造服务器 | `sinon.fakeServer.create()` | 伪造 XMLHttpRequest |
| 断言预期 | `mock.verify()` | 验证 Mock 调用 【常用】 |

---

## 💡 实用场景示例

### 场景 1: Jest 完整测试流程

```bash
# 1. 运行所有测试（监视模式）
jest --watch

# 2. 运行并生成覆盖率
jest --coverage

# 3. 检查覆盖率阈值（必须达到 80%）
jest --coverage --coverageThreshold='{"global":{"branches":80,"functions":80,"lines":80,"statements":80}}'

# 4. 输出 JUnit 格式报告
jest --reporters=default --reporters=jest-junit

# 5. 强制退出（避免僵尸进程）
jest --forceExit
```

### 场景 2: Playwright E2E 测试

```bash
# 1. 安装浏览器
playwright install chromium

# 2. 运行测试（ headed 模式）
playwright test --debug

# 3. 生成测试报告
playwright show-report

# 4. 截取关键页面截图
playwright screenshot https://example.com ./screenshots/home.png

# 5. 并行运行（4个 worker）
playwright test --workers=4
```

### 场景 3: API 端到端测试 (Postman/Newman)

```bash
# 1. 运行测试集并输出到 CLI
newman run ./postman/collection.json -e ./postman/env.json

# 2. 生成 HTML 报告
newman run ./postman/collection.json -e ./postman/env.json \
  --reporters html,cli \
  --export-html-report report.html

# 3. 忽略 SSL 错误，在 CI 环境运行
newman run ./postman/collection.json -e ./postman/ci-env.json --insecure

# 4. 使用数据文件进行批量测试
newman run ./postman/collection.json -e ./postman/env.json -d ./data/users.csv
```

### 场景 4: Python 测试与覆盖率

```bash
# 1. 运行所有测试（详细模式）
pytest -v

# 2. 生成覆盖率报告
coverage run -m pytest
coverage report

# 3. 生成 HTML 报告
coverage html
# 访问 htmlcov/index.html 查看详细报告

# 4. 合并多环境覆盖率
coverage combine
coverage report --fail-under=80
```

---

## 📊 命令速查表

| 操作 | 命令 | 说明 |
|------|------|------|
| Jest 监视 | `jest --watch` | 持续监视并运行测试 |
| Jest 覆盖 | `jest --coverage` | 生成覆盖率报告 |
| Vitest 运行 | `vitest run` | 单次运行（不监视） |
| Pytest 详细 | `pytest -v` | 详细输出 |
| Pytest 覆盖 | `pytest --cov=src` | Python 覆盖率 |
| Maven 测试 | `mvn test` | 运行 Maven 测试 |
| Gradle 测试 | `./gradlew test` | 运行 Gradle 测试 |
| Playwright | `playwright test` | 运行 Playwright 测试 |
| Playwright 录制 | `playwright codegen` | 录制生成测试代码 |
| Cypress 运行 | `cypress run` | CLI 运行 Cypress |
| Cypress 打开 | `cypress open` | 交互模式打开 |
| Newman 运行 | `newman run` | 运行 Postman 集合 |
| curl GET | `curl -X GET` | HTTP GET 请求 |
| curl POST | `curl -X POST` | HTTP POST 请求 |
| NYC 覆盖 | `npx nyc jest` | Jest 覆盖率统计 |
| coverage 报告 | `coverage report` | Python 覆盖率报告 |
| MSW 初始化 | `npx msw init` | 初始化 Mock Service Worker |
| nock GET | `nock(...).get(...)` | HTTP Mock GET |
| sinon spy | `sinon.spy()` | 创建 spy |
| npm 测试 | `npm test` | 运行 npm 测试脚本 |
| 并行测试 | `--parallel --workers=4` | 并行执行测试 |

---

## 🔗 相关资源

- [快速开始指南](../quick-start.md)
- [Docker 命令文档](../Docker 命令/README.md)
- [GitHubActions 文档](../GitHubActions/README.md)