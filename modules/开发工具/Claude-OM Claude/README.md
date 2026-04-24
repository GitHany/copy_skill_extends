# Claude Skills-oh-my-claude 命令文档

oh-my-claude 智能多 Agent 编排模块。

## 📚 目录

- [autopilot 自动执行](#autopilot-自动执行)
- [deep-interview 深度访谈](#deep-interview-深度访谈)
- [ralph 代码审查](#ralph-代码审查)
- [ralplan 共识规划](#ralplan-共识规划)
- [team 多 Agent 协作](#team-多-agent-协作)
- [ultrawork 并行执行](#ultrawork-并行执行)
- [ccg 三模型编排](#ccg-三模型编排)
- [ask 顾问咨询](#ask-顾问咨询)
- [omc-setup 安装配置](#omc-setup-安装配置)
- [omc-doctor 诊断检查](#omc-doctor-诊断检查)
- [omc-teams CLI 团队协作](#omc-teams-cli-团队协作)
- [self-improve 自我改进](#self-improve-自我改进)
- [trace 证据追踪](#trace-证据追踪)
- [verify 验证](#verify-验证)
- [cancel 取消模式](#cancel-取消模式)

---

## autopilot 自动执行

AI 自动执行完整任务流程 【常用】

**基础用法**:
```
/oh-my-claudecode:autopilot %{任务描述}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 执行任务 | `/oh-my-claudecode:autopilot 实现用户登录功能` | 任务描述：实现用户登录功能 |
| 详细日志模式 | `/oh-my-claudecode:autopilot 实现用户登录功能 --verbose` | 任务：实现用户登录功能 |
| 交互确认模式 | `/oh-my-claudecode:autopilot 实现用户登录功能 --interactive` | 任务：实现用户登录功能 |
| 查看历史 | `/oh-my-claudecode:autopilot --history` | 无参数 |
| 恢复执行 | `/oh-my-claudecode:autopilot --resume` | 无参数 |

---

## deep-interview 深度访谈

Socratic 深度访谈明确需求

**基础用法**:
```
/oh-my-claudecode:deep-interview %{问题领域}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 技术选型咨询 | `/oh-my-claudecode:deep-interview "技术栈选型"` | 问题领域：技术栈选型 |
| 需求澄清 | `/oh-my-claudecode:deep-interview "功能需求澄清"` | 问题领域：功能需求澄清 |
| 架构设计讨论 | `/oh-my-claudecode:deep-interview "系统架构设计"` | 问题领域：系统架构设计 |
| Bug 复现分析 | `/oh-my-claudecode:deep-interview "Bug 复现与根因分析"` | 问题领域：Bug 复现与根因分析 |

---

## ralph 代码审查

AI 代码审查助手 【常用】

**基础用法**:
```
/oh-my-claudecode:ralph %{审查内容}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 审查代码质量 | `/oh-my-claudecode:ralph "审查 src/utils/helpers.ts 的代码质量"` | 审查内容：审查 src/utils/helpers.ts 的代码质量 |
| 安全漏洞检查 | `/oh-my-claudecode:ralph "检查登录模块的安全漏洞"` | 审查内容：检查登录模块的安全漏洞 |
| 性能问题诊断 | `/oh-my-claudecode:ralph "诊断 API 性能瓶颈"` | 审查内容：诊断 API 性能瓶颈 |

---

## ralplan 共识规划

共识规划入口自动验证需求

**基础用法**:
```
/oh-my-claudecode:ralplan %{规划内容}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建实施计划 | `/oh-my-claudecode:ralplan "创建用户系统实施计划"` | 规划内容：创建用户系统实施计划 |
| 审查现有计划 | `/oh-my-claudecode:ralplan --review` | 无参数 |

---

## team 多 Agent 协作

多 Agent 团队协作模式 【常用】

**基础用法**:
```
/oh-my-claudecode:team %{任务描述}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 前端开发团队 | `/oh-my-claudecode:team "组建前端开发团队"` | 任务描述：组建前端开发团队 |
| 全栈开发团队 | `/oh-my-claudecode:team "组建全栈开发团队"` | 任务描述：组建全栈开发团队 |
| 审查团队 | `/oh-my-claudecode:team "组建代码审查团队"` | 任务描述：组建代码审查团队 |

---

## ultrawork 并行执行

高吞吐量并行执行引擎 【常用】

**基础用法**:
```
/oh-my-claudecode:ultrawork %{任务列表}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 并行执行任务 | `/oh-my-claudecode:ultrawork 实现登录、注册、密码重置` | 任务列表：实现登录、注册、密码重置 |
| 查看任务队列 | `/oh-my-claudecode:ultrawork --queue` | 无参数 |
| 清理已完成任务 | `/oh-my-claudecode:ultrawork --clear` | 无参数 |

---

## ccg 三模型编排

Claude-Codex-Gemini 三模型编排

**基础用法**:
```
/oh-my-claudecode:ccg %{任务描述}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 代码生成任务 | `/oh-my-claudecode:ccg "生成 RESTful API 代码"` | 任务描述：生成 RESTful API 代码 |
| 审查任务 | `/oh-my-claudecode:ccg --review` | 无参数 |

---

## ask 顾问咨询

流程优先的顾问路由

**基础用法**:
```
/oh-my-claudecode:ask %{问题描述}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 架构咨询 | `/oh-my-claudecode:ask "系统应该采用微服务还是单体架构"` | 问题描述：系统应该采用微服务还是单体架构 |
| 技术选型 | `/oh-my-claudecode:ask "前端框架应该选 React 还是 Vue"` | 问题描述：前端框架应该选 React 还是 Vue |

---

## omc-setup 安装配置

安装或刷新 oh-my-claudecode

**基础用法**:
```
/oh-my-claudecode:omc-setup
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 重新初始化 | `/oh-my-claudecode:omc-setup --force` | 无参数 |
| 仅更新配置 | `/oh-my-claudecode:omc-setup --config-only` | 无参数 |

---

## omc-doctor 诊断检查

诊断并修复 oh-my-claudecode 安装问题

**基础用法**:
```
/oh-my-claudecode:omc-doctor
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 检查配置 | `/oh-my-claudecode:omc-doctor --config` | 无参数 |
| 检查插件 | `/oh-my-claudecode:omc-doctor --plugins` | 无参数 |
| 检查网络 | `/oh-my-claudecode:omc-doctor --network` | 无参数 |
| 重置配置 | `/oh-my-claudecode:omc-doctor --reset` | 无参数 |

---

## omc-teams CLI 团队协作

Claude、Codex、Gemini 工作流 CLI 团队

**基础用法**:
```
/oh-my-claudecode:omc-teams %{任务描述}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动并行团队 | `/oh-my-claudecode:omc-teams --parallel` | 无参数 |
| 查看团队状态 | `/oh-my-claudecode:omc-teams --status` | 无参数 |

---

## self-improve 自我改进

自主进化代码改进引擎

**基础用法**:
```
/oh-my-claudecode:self-improve %{改进目标}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 改进代码质量 | `/oh-my-claudecode:self-improve "改进 src/utils/helpers.ts 的代码质量"` | 改进目标：改进 src/utils/helpers.ts 的代码质量 |
| 性能优化 | `/oh-my-claudecode:self-improve "优化 API 响应时间"` | 改进目标：优化 API 响应时间 |

---

## trace 证据追踪

证据驱动的追踪通道编排检查

**基础用法**:
```
/oh-my-claudecode:trace %{追踪目标}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 追踪代码执行 | `/oh-my-claudecode:trace "追踪 API 请求流程"` | 追踪目标：追踪 API 请求流程 |
| 追踪性能问题 | `/oh-my-claudecode:trace "追踪页面加载性能问题"` | 追踪目标：追踪页面加载性能问题 |

---

## verify 验证

验证修改是否真正有效 【常用】

**基础用法**:
```
/oh-my-claudecode:verify %{验证内容}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 验证构建 | `/oh-my-claudecode:verify "验证构建是否成功"` | 验证内容：验证构建是否成功 |
| 验证测试 | `/oh-my-claudecode:verify "验证所有测试是否通过"` | 验证内容：验证所有测试是否通过 |

---

## cancel 取消模式

取消任何活动的 OMC 模式

**基础用法**:
```
/oh-my-claudecode:cancel
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 取消 autopilot | `/oh-my-claudecode:cancel autopilot` | 无参数 |
| 取消 ralph | `/oh-my-claudecode:cancel ralph` | 无参数 |
| 取消 ultrawork | `/oh-my-claudecode:cancel ultrawork` | 无参数 |