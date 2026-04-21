# Claude Skills-ecc 命令文档

ecc 开发命令集合模块。

## 📚 目录

- [plan 计划](#plan-计划)
- [tdd 测试驱动开发](#tdd-测试驱动开发)
- [code-review 代码审查](#code-review-代码审查)
- [build-fix 构建修复](#build-fix-构建修复)
- [security-scan 安全扫描](#security-scan-安全扫描)
- [e2e 端到端测试](#e2e-端到端测试)
- [test-coverage 测试覆盖率](#test-coverage-测试覆盖率)
- [verify 验证](#verify-验证)
- [update-docs 更新文档](#update-docs-更新文档)
- [architecture 架构](#architecture-架构)
- [debug 调试](#debug-调试)

---

## plan 计划

制定项目实施计划 【常用】

**基础用法**:
```
/plan %{任务描述}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 制定计划 | `/plan 开发用户管理模块` | 任务描述：开发用户管理模块 |
| 详细计划 | `/plan 开发用户管理模块 --detailed` | 任务：开发用户管理模块 |

---

## tdd 测试驱动开发

测试先行开发工作流 【常用】

**基础用法**:
```
/tdd %{任务描述}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 执行 TDD | `/tdd 实现用户登录功能` | 任务描述：实现用户登录功能 |
| TDD 完整流程 | `/tdd 实现用户登录功能 --full` | 任务：实现用户登录功能 |

---

## code-review 代码审查

代码审查与反馈 【常用】

**基础用法**:
```
/code-review %{范围}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 审查代码 | `/code-review src/api/users.ts` | 范围：src/api/users.ts |
| 详细审查 | `/code-review src/api/users.ts --detailed` | 范围：src/api/users.ts |

---

## build-fix 构建修复

修复构建错误

**基础用法**:
```
/build-fix
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 强制构建 | `/build-fix --force` | 无参数 |
| 清理后构建 | `/build-fix --clean` | 无参数 |

---

## security-scan 安全扫描

安全漏洞扫描

**基础用法**:
```
/security-scan
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 深度扫描 | `/security-scan --deep` | 无参数 |
| 快速扫描 | `/security-scan --quick` | 无参数 |

---

## e2e 端到端测试

端到端测试执行

**基础用法**:
```
/e2e %{测试文件}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 执行测试 | `/e2e tests/e2e/login.spec.ts` | 测试文件：tests/e2e/login.spec.ts |
| E2E 调试模式 | `/e2e tests/e2e/login.spec.ts --debug` | 文件：tests/e2e/login.spec.ts |

---

## test-coverage 测试覆盖率

生成测试覆盖率报告

**基础用法**:
```
/test-coverage
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 详细覆盖率报告 | `/test-coverage --verbose` | 无参数 |
| HTML 报告 | `/test-coverage --html` | 无参数 |

---

## verify 验证

验证代码正确性 【常用】

**基础用法**:
```
/verify %{目标}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 验证功能 | `/verify 用户登录功能` | 目标：用户登录功能 |
| 完整验证 | `/verify 用户登录功能 --full` | 目标：用户登录功能 |

---

## update-docs 更新文档

自动更新项目文档

**基础用法**:
```
/update-docs %{范围}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 更新文档 | `/update-docs README.md` | 范围：README.md |
| 全量更新 | `/update-docs all` | 无参数 |
| API 文档 | `/update-docs api` | 无参数 |

---

## architecture 架构

架构设计与分析

**基础用法**:
```
/architecture %{项目}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 架构分析 | `/architecture 微服务架构` | 项目：微服务架构 |
| 架构评审 | `/architecture 微服务架构 --review` | 项目：微服务架构 |

---

## debug 调试

问题诊断与调试

**基础用法**:
```
/debug %{问题描述}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 问题调试 | `/debug 数据库连接超时` | 问题描述：数据库连接超时 |
| 详细调试 | `/debug 数据库连接超时 --verbose` | 问题：数据库连接超时 |