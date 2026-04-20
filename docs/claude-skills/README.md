# Claude Skills 文档

Claude 技能命令完整参考文档。

## 📚 目录

- [Oh-My-Claude](#oh-my-claude)
- [Superpowers](#superpowers)
- [Everything Claude Code](#everything-claude-code)
- [OpenSpec](#openspec)
- [Spec-Kit](#spec-kit)

---

## Oh-My-Claude

Oh-My-Claude 是一套强大的自动化和协作技能，支持任务自动执行、深度访谈、循环执行和团队协作。

### 安装

**基础命令**:
```
/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode
/plugin install oh-my-claudecode
/omc-setup
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 更新插件 | `/plugin update oh-my-claudecode` |
| 查看状态 | `/plugin list` |
| 卸载插件 | `/plugin uninstall oh-my-claudecode` |

### 1-01 autopilot 自动执行

**基础命令**:
```
/oh-my-claudecode:autopilot %{执行任务}%
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 带详细日志 | `/oh-my-claudecode:autopilot %{任务}% --verbose` |
| 需要确认 | `/oh-my-claudecode:autopilot %{任务}% --interactive` |
| 查看历史 | `/oh-my-claudecode:autopilot --history` |

### 1-01-1 autopilot 验证修复方案

对修复方案进行全面的功能影响评估：

```
/oh-my-claudecode:autopilot 对刚才实施的修复进行全面的功能影响评估，以确定是否存在任何可能影响系统正常功能使用的潜在问题...
```

### 1-01-2 autopilot 性能优化排查bug

系统性诊断项目的性能瓶颈和bug：

```
/oh-my-claudecode:autopilot 我现在负责的项目需要进行优化和bug修复工作...
```

### 1-02 deep-interview 沟通交流

通过深度访谈式提问明确需求。

**基础命令**:
```
/oh-my-claudecode:deep-interview %{想法}%
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 技术选型 | `/oh-my-claudecode:deep-interview 我有一个项目需要选型...` |
| 需求澄清 | `/oh-my-claudecode:deep-interview 我有一个功能需求需要澄清...` |

### 1-03 ralph 循环

循环执行任务直到完成。

**基础命令**:
```
/oh-my-claudecode:ralph %{任务}%
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 最大次数限制 | `/oh-my-claudecode:ralph %{任务}% --max-iterations %{次数}%` |
| 超时限制 | `/oh-my-claudecode:ralph %{任务}% --timeout %{分钟}%` |

### 1-04 ralplan 规划-循环

循环规划并执行任务。

**基础命令**:
```
/oh-my-claudecode:ralplan %{任务}% 。use context7
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 仅规划 | `/oh-my-claudecode:ralplan %{任务}% --plan-only` |
| 带风险评估 | `/oh-my-claudecode:ralplan %{任务}% --with-risk-assessment` |

### 1-05 team 团队协作

使用多agent协作完成任务。

**基础命令**:
```
/oh-my-claudecode:team 3:executor %{任务}% 。use context7
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 代码审查 | `/oh-my-claudecode:team 2:reviewer %{代码}%` |
| 功能开发 | `/oh-my-claudecode:team 1:architect + 2:developer + 1:tester %{需求}%` |

### 1-06 ultrawork 最大并行执行

最大并行度执行任务，AI会同时处理多个子任务直到完成。

**基础命令**:
```
/ultrawork "%{任务}%"
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 修复多个bug | `/ultrawork "修复项目中所有的 TypeScript 类型错误，ultrawork"` |
| 重构多个模块 | `/ultrawork "重构 src/components 目录下所有组件，添加 TypeScript 类型定义，ulw"` |
| 并行测试 | `/ultrawork "为所有 API 端点编写集成测试，并行执行测试套件，ulw"` |

### 1-07 ccg 三角模型合成

使用 Codex + Gemini 三角模型进行混合审查和设计。

**基础命令**:
```
/ccg %{任务}%
```

**扩展**:
| 场景 | 命令 |
|------|------|
| PR架构审查 | `/ccg Review this PR — architecture (Codex) and UI components (Gemini)` |
| 后端审查 | `/ccg --codex-focus architecture "审查后端 API 的架构设计"` |
| 前端设计审查 | `/ccg --gemini-focus design "审查前端组件的设计一致性和用户体验问题"` |

### 1-08 ask providers

使用不同AI提供者进行审查和建议。

**基础命令**:
```
/ask claude "%{任务}%"
/ask codex "%{任务}%"
/ask gemini "%{任务}%"
```

**扩展**:
| 场景 | 命令 |
|------|------|
| Claude审查代码 | `/ask claude "审查 src/auth/service.ts 的代码质量"` |
| Codex架构验证 | `/ask codex "review auth module for security issues"` |
| Gemini设计审查 | `/ask gemini "propose UI polish ideas for the new dashboard"` |

### 1-09 autoresearch 自动研究

自动研究模式，循环执行研究直到达到目标。

**基础命令**:
```
/oh-my-claudecode:autoresearch "%{任务}%"
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 性能优化 | `/deep-interview --autoresearch improve startup performance` |
| 技术选型 | `/oh-my-claudecode:autoresearch --mission "研究最佳的技术栈选型方案"` |

### 1-10 omc-doctor 诊断工具

诊断OMC配置和运行状态，排查问题。

**基础命令**:
```
/omc-doctor
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 详细诊断 | `/omc-doctor --detail` |
| 检查冲突 | `/omc-doctor conflicts` |

### 1-11 omc-hud HUD状态显示

显示HUD状态栏，实时显示编排进度。

**基础命令**:
```
/oh-my-claudecode:hud setup
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 设置预设 | `/oh-my-claudecode:hud setup` |
| 聚焦模式 | `/oh-my-claudecode:hud setup --preset focused` |

### 1-12 omc-wait 速率限制等待

等待速率限制重置并自动恢复会话。

**基础命令**:
```
omc wait
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 启用自动恢复 | `omc wait --start` |
| 停止守护进程 | `omc wait --stop` |

---

## Superpowers

Superpowers 提供头脑风暴、Git 工作流、计划编写、子agent开发和测试驱动开发等能力。

### 安装

```
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

### 1-01 brainstorming 沟通需求

通过头脑风暴明确需求和方案。

**基础命令**:
```
/brainstorming %{需求}%
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 技术方案探索 | `/brainstorming 针对「实现实时聊天功能」进行头脑风暴...` |
| 产品功能设计 | `/brainstorming 围绕「用户积分系统」进行创意发散...` |
| API设计 | `/brainstorming 针对「订单退款 API」设计多种方案...` |
| 技术选型 | `/brainstorming 围绕「前端框架选型」进行技术调研...` |

### 1-02 git-worktrees 新建分支

使用git worktree管理多分支开发，实现并行开发。

**基础命令**:
```
/superpowers:using-git-worktrees
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 创建功能分支 | `git worktree add ../myapp-feature-auth feature/auth` |
| 创建修复分支 | `git worktree add ../myapp-fix-login bugfix/login` |
| 查看所有分支 | `git worktree list` |
| 删除分支 | `git worktree remove ../myapp-feature-auth` |
| 清理孤岛 | `git worktree prune` |

### 1-03 writing-plans 编写计划

编写详细的开发计划，将任务分解为可执行步骤。

**基础命令**:
```
/superpowers:writing-plans
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 功能开发计划 | `/superpowers:writing-plans 为「用户评论功能」编写开发计划...` |
| 重构计划 | `/superpowers:writing-plans 为「订单模块」编写重构计划...` |
| 修复计划 | `/superpowers:writing-plans 为「登录性能问题」编写修复计划...` |

### 1-04 subagent-driven-development 执行计划

使用子agent驱动的开发流程，并行执行多个任务。

**基础命令**:
```
/superpowers:subagent-driven-development
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 批量任务 | `/superpowers:subagent-driven-development，为每个任务启动子agent执行...` |
| 并发开发 | `/superpowers:subagent-driven-development，并行启动多个子agent同时开发...` |

### 1-05 test-driven-development 测试

测试驱动开发，遵循 RED-GREEN-REFACTOR 循环。

**基础命令**:
```
/superpowers:test-driven-development
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 单元测试 | `/superpowers:test-driven-development，为 calculateDiscount 函数编写单元测试...` |
| 集成测试 | `/superpowers:test-driven-development，为 POST /api/orders 端点编写集成测试...` |
| 组件测试 | `/superpowers:test-driven-development，为 UserProfile 组件编写测试...` |
| 数据库测试 | `/superpowers:test-driven-development，为 OrderRepository 编写数据库测试...` |

### 1-06 requesting-code-review 代码审查

请求代码审查，在任务之间进行质量把关。

**基础命令**:
```
/superpowers:requesting-code-review
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 安全性审查 | `/superpowers:requesting-code-review，请重点审查代码的安全性...` |
| 性能审查 | `/superpowers:requesting-code-review，请重点审查代码的性能...` |
| 代码规范 | `/superpowers:requesting-code-review，请检查代码是否符合团队规范...` |
| 架构审查 | `/superpowers:requesting-code-review，请审查代码的架构合理性...` |

### 1-07 finishing-a-development-branch 验证测试

完成开发分支前的最终验证和清理。

**基础命令**:
```
/superpowers:finishing-a-development-branch
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 合并主分支 | `/superpowers:finishing-a-development-branch，验证测试通过后合并到主分支...` |
| 创建PR | `/superpowers:finishing-a-development-branch，验证通过后创建 Pull Request...` |
| 保留分支 | `/superpowers:finishing-a-development-branch，验证通过但继续在当前分支开发...` |
| 丢弃分支 | `/superpowers:finishing-a-development-branch，验证后发现方案不可行...` |

---

## Everything Claude Code

Everything Claude Code (ECC) 提供完整的开发工作流支持，包括需求分析、TDD开发、代码审查、安全扫描和测试验证。

### 安装

```
# 添加市场
/plugin marketplace add affaan-m/everything-claude-code

# 安装插件
/plugin install ecc@ecc
```

### 1-01 plan 需求分析

对需求进行详细分析和规划，制定功能开发计划。

**基础命令**:
```
/ecc:plan %{需求}%
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 用户故事拆分 | `/ecc:plan 将「用户权限管理功能」拆分为用户故事...` |
| 技术方案设计 | `/ecc:plan 为「实时通知系统」设计技术方案...` |
| 性能优化 | `/ecc:plan 为「数据库查询性能问题」分析并制定优化方案...` |

### 1-03 tdd 测试驱动开发

测试驱动开发模式，RED-GREEN-REFACTOR 循环。

**基础命令**:
```
/tdd use context7
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 函数开发 | `/tdd use context7，为 validateEmail 函数编写测试...` |
| API开发 | `/tdd use context7，使用 TDD 方式开发 GET /api/users/:id 端点...` |
| 组件开发 | `/tdd use context7，使用 TDD 方式开发 Modal 组件...` |

### 1-04 code-review 代码审查

全面的代码审查，识别问题和改进建议。

**基础命令**:
```
/code-review
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 代码规范检查 | `/code-review，请检查代码是否符合团队规范...` |
| 架构设计审查 | `/code-review，请审查代码的架构合理性...` |
| 安全性审查 | `/code-review，请重点审查代码的安全性...` |
| 性能审查 | `/code-review，请重点审查代码的性能...` |

### 1-05 build-fix 修复错误

修复构建错误和编译问题。

**基础命令**:
```
/ecc:build-fix
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 分析编译错误 | `/ecc:build-fix，分析以下 TypeScript 编译错误...` |
| 自动修复 | `/ecc:build-fix --auto-fix，尝试自动修复构建错误...` |
| 依赖冲突 | `/ecc:build-fix --resolve-deps，解决依赖版本冲突...` |

### 1-06 security-scan 安全扫描

扫描代码中的安全漏洞和风险。

**基础命令**:
```
/security-scan
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 依赖漏洞 | `/security-scan --dependencies，使用 npm audit/pip-audit/trivy 检查...` |
| 代码注入 | `/security-scan --injection，使用 AgentShield 检查代码...` |
| 认证授权 | `/security-scan --auth，检查认证授权漏洞...` |

### 1-07 e2e 端到端测试

执行 Playwright 端到端测试。

**基础命令**:
```
/ecc:e2e
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 用户登录流程 | `/ecc:e2e，执行用户登录流程的端到端测试...` |
| 购买流程 | `/ecc:e2e，执行完整的购买流程测试...` |
| 移动端测试 | `/ecc:e2e --viewport mobile，在移动端视口下测试...` |

### 1-08 test-coverage 测试覆盖率检查

检查并提升测试覆盖率。

**基础命令**:
```
/test-coverage
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 行覆盖率 | `/test-coverage --line，检查并提升行覆盖率，目标 > 80%...` |
| 分支覆盖率 | `/test-coverage --branch，检查分支覆盖率，目标 > 70%...` |
| 函数覆盖率 | `/test-coverage --function，报告函数覆盖率...` |

### 1-09 verify 验证循环

持续验证直到所有检查通过。

**基础命令**:
```
/verify
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 功能验证 | `/verify，持续验证新功能是否正常工作...` |
| 修复验证 | `/verify，持续验证 bug 修复是否有效...` |
| 部署验证 | `/verify，验证部署是否成功...` |

### 1-10 update-docs 更新文档

更新项目文档，保持文档与代码同步。

**基础命令**:
```
/update-docs
```

**扩展**:
| 场景 | 命令 |
|------|------|
| README | `/update-docs README.md，更新项目说明...` |
| API文档 | `/update-docs API.md，根据代码更新 API 文档...` |
| 架构文档 | `/update-docs ARCHITECTURE.md，更新系统架构文档...` |

---

## OpenSpec

OpenSpec 是规范驱动的变更管理工具，支持提出、执行、归档和探索规范变更。

### 1-01 openspec init

初始化 openspec 项目，创建规范变更管理的基础结构。

**基础命令**:
```
openspec init
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 当前目录 | `openspec init，在当前目录初始化 openspec 项目...` |
| 指定目录 | `openspec init /path/to/project，在指定目录初始化...` |

### 1-02 opsx propose 提出规范变更

提出新的规范变更，创建变更提案。

**基础命令**:
```
/opsx:propose %{任务}%
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 新功能 | `/opsx:propose 新功能「用户积分系统」，包括...` |
| 缺陷修复 | `/opsx:propose 缺陷修复「登录页面加载缓慢」，包括...` |
| 技术重构 | `/opsx:propose 技术重构「数据库迁移到 PostgreSQL」，包括...` |

### 1-03 opsx apply 执行规范变更

执行已批准的规范变更，实施计划中的变更。

**基础命令**:
```
/opsx:apply use context7
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 执行新功能 | `/opsx:apply use context7，执行「用户积分系统」规范变更...` |
| 执行修复 | `/opsx:apply use context7，执行「登录性能优化」修复...` |
| 执行迁移 | `/opsx:apply use context7，执行「数据库迁移」方案...` |

### 1-04 opsx archive 归档规范变更

归档已完成的规范变更。

**基础命令**:
```
/opsx:archive
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 归档已完成 | `/opsx:archive，归档所有已完成的规范变更...` |
| 归档特定变更 | `/opsx:archive --id abc123，归档指定 ID 的规范变更...` |

### 1-05 opsx explore 探索扩展

探索规范的扩展可能性，发现新的机会。

**基础命令**:
```
/opsx:explore %{任务}%
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 功能扩展分析 | `/opsx:explore 针对「用户积分系统」当前实现...` |
| 技术扩展探索 | `/opsx:explore 针对「订单服务」探索技术扩展...` |

---

## Spec-Kit

Spec-Kit 是规格说明书工具包，支持需求编写、计划制定、任务分解和实施。

### 1-01 specify init 初始化项目

使用 spec-kit 初始化项目，创建规范开发的基础结构。

**基础命令**:
```
specify init --here --ai claude
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 当前目录 | `specify init --here --ai claude，在当前目录初始化项目...` |
| 指定目录 | `specify init --path /project --ai claude，在指定目录初始化...` |

### 1-02 constitution 项目规则

定义项目规则和约束，确立开发准则。

**基础命令**:
```
/speckit-constitution %{项目规则}%
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 代码规范 | `/speckit-constitution 定义代码规范：TypeScript 4.0+、ESLint + Prettier...` |
| 安全规范 | `/speckit-constitution 定义安全规范：所有 API 必须认证...` |
| 测试规范 | `/speckit-constitution 定义测试规范：单元测试覆盖率 > 80%...` |

### 1-03 specify 编写需求

编写详细需求规格，定义功能和验收标准。

**基础命令**:
```
/speckit-specify %{需求 Spec}%
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 用户故事 | `/speckit-specify 为「用户下单功能」编写用户故事规格...` |
| API规格 | `/speckit-specify 为「用户登录 API」编写完整的 API 规格...` |
| 功能模块 | `/speckit-specify 为「评论系统」编写功能规格...` |

### 1-03-1 specify 需求完善

完善现有需求规格，识别不足和风险。

**基础命令**:
```
/speckit-specify 请对当前方案进行全面评估...
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 完整性检查 | `/speckit-specify，请对「实时通知功能」的当前规格进行完整性检查...` |
| 风险识别 | `/speckit-specify，请评估「支付模块」规格的技术风险...` |

### 1-03-2 clarify 澄清需求

结构化地澄清规格中的模糊部分，明确未定义的内容。

**基础命令**:
```
/speckit-clarify 结构化地澄清规格中的模糊部分
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 模糊术语 | `/speckit-clarify，请澄清「实时通知」中的「实时」具体指什么...` |
| 未定义场景 | `/speckit-clarify，请澄清「用户权限」中管理员和普通用户的边界...` |

### 1-04 plan 制定方案

制定实施方案，将需求转化为可执行的技术方案。

**基础命令**:
```
/speckit-plan
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 功能实施方案 | `/speckit-plan，为「用户下单功能」制定实施方案...` |
| 重构方案 | `/speckit-plan，为「订单服务重构」制定方案...` |

### 1-05 tasks 分解任务

将方案分解为可执行任务，粒度细化到 2-5 分钟。

**基础命令**:
```
/speckit-tasks
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 功能任务分解 | `/speckit-tasks，将「用户评论功能」分解为可执行任务...` |
| 修复任务分解 | `/speckit-tasks，将「登录性能优化」分解为任务...` |

### 1-06 implement 实施任务

实施任务，遵循规范完成开发。

**基础命令**:
```
/speckit-implement use context7
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 功能开发 | `/speckit-implement use context7，实施「用户评论功能」...` |
| 测试开发 | `/speckit-implement use context7，使用 TDD 方式实施「积分计算功能」...` |

### 1-06-1 analyze 分析任务

分析任务实施情况，评估进度和质量。

**基础命令**:
```
/speckit-analyze
```

**扩展**:
| 场景 | 命令 |
|------|------|
| 实施进度 | `/speckit-analyze，分析「用户评论功能」的实施进度...` |
| 质量评估 | `/speckit-analyze，评估「积分计算功能」的实施质量...` |

```
/speckit-clarify 结构化地澄清规格中的模糊部分
```

### 1-04 plan 方案

制定实施方案。

```
/speckit-plan
```

### 1-05 tasks 分解任务

将方案分解为可执行任务。

```
/speckit-tasks
```

### 1-06 implement 实施任务

实施任务。

```
/speckit-implement use context7
```

### 1-06-1 analyze 分析任务

分析任务实施情况。

```
/speckit-analyze
```

---

## 💡 使用场景示例

### 场景 1: 新功能开发

```
1. /oh-my-claudecode:deep-interview %{想法}%
2. /ecc:plan %{需求}%
3. /speckit-specify %{需求 Spec}%
4. /speckit-tasks
5. /speckit-implement
6. /code-review
7. /verify
```

### 场景 2: 规范驱动开发

```
1. openspec init
2. /opsx:propose %{任务}%
3. /opsx:apply use context7
4. /opsx:archive
5. /opsx:explore %{任务}%
```

### 场景 3: 团队协作

```
1. /brainstorming %{需求}%
2. /superpowers:writing-plans
3. /superpowers:subagent-driven-development
4. /oh-my-claudecode:team 3:executor %{任务}%
5. /superpowers:finishing-a-development-branch
```

---

## 📊 技能对比

| 技能 | 核心能力 | 适用场景 |
|------|----------|----------|
| Oh-My-Claude | 自动化执行、深度访谈、团队协作 | 复杂任务、需求沟通 |
| Superpowers | 头脑风暴、Git工作流、TDD | 创意发散、开发流程 |
| ECC | 需求分析、代码审查、安全扫描 | 完整开发周期 |
| OpenSpec | 规范变更管理 | 规范化开发 |
| Spec-Kit | 需求编写、任务分解 | 规格驱动开发 |

---

## 🔗 相关资源

- [快速开始指南](../quick-start.md)
- [完整命令参考表](../../references/commands-reference.md)
- [软件工程提示词](../software-engineering/README.md)
