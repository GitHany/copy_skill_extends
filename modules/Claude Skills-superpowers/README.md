# Claude Skills-superpowers 命令文档

superpowers 超级能力模块 - 高级开发超级能力集合。

## 📚 目录

- [brainstorming 头脑风暴](#brainstorming-头脑风暴)
- [writing-plans 编写计划](#writing-plans-编写计划)
- [subagent-driven-development 子 Agent 开发](#subagent-driven-development-子-agent-开发)
- [executing-plans 执行计划](#executing-plans-执行计划)
- [finishing-a-development-branch 完成分支](#finishing-a-development-branch-完成分支)
- [skill-creator 技能创建](#skill-creator-技能创建)
- [writing-skills 编写技能](#writing-skills-编写技能)
- [using-superpowers 使用超级能力](#using-superpowers-使用超级能力)
- [find-skills 查找技能](#find-skills-查找技能)
- [dispatching-parallel-agents 并行代理调度](#dispatching-parallel-agents-并行代理调度)
- [changelog-generator 变更日志生成](#changelog-generator-变更日志生成)

---

## brainstorming 头脑风暴

通过头脑风暴明确需求和方案

**基础用法**:
```
/brainstorming %{需求}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 需求头脑风暴 | `/brainstorming 实现实时聊天功能` | 需求：实现实时聊天功能 |

---

## writing-plans 编写计划

编写详细的开发计划，分解任务为可执行步骤

**基础用法**:
```
/superpowers:writing-plans %{任务描述}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 编写开发计划 | `/superpowers:writing-plans 实现用户认证功能` | 任务描述：实现用户认证功能 |

---

## subagent-driven-development 子 Agent 开发

使用子 agent 驱动的开发流程，并行执行多个任务

**基础用法**:
```
/superpowers:subagent-driven-development %{任务描述}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 并行开发 | `/superpowers:subagent-driven-development 重构并测试所有模块` | 任务描述：重构并测试所有模块 |

---

## executing-plans 执行计划

按照计划执行实现任务

**基础用法**:
```
/superpowers:executing-plans %{计划内容}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 执行计划 | `/superpowers:executing-plans 按照开发计划完成用户模块` | 计划内容：按照开发计划完成用户模块 |

---

## finishing-a-development-branch 完成分支

完成开发分支前的最终验证和清理

**基础用法**:
```
/superpowers:finishing-a-development-branch %{操作}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 完成分支 | `/superpowers:finishing-a-development-branch 合并到主分支` | 操作：合并到主分支 |

---

## skill-creator 技能创建

创建新的 Claude Skills 技能

**基础用法**:
```
/superpowers:skill-creator %{技能描述}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建技能 | `/superpowers:skill-creator 创建一个 Git 提交辅助技能` | 技能描述：创建一个 Git 提交辅助技能 |

---

## writing-skills 编写技能

编写和编辑 Claude Skills 技能文件

**基础用法**:
```
/superpowers:writing-skills %{技能名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 编写技能 | `/superpowers:writing-skills 编写 Git 提交规范技能` | 技能名称：编写 Git 提交规范技能 |

---

## using-superpowers 使用超级能力

启动超级能力工作流

**基础用法**:
```
/superpowers:using-superpowers %{工作流类型}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动工作流 | `/superpowers:using-superpowers 启动 TDD 开发流程` | 工作流类型：启动 TDD 开发流程 |

---

## find-skills 查找技能

搜索和发现可用的 Claude Skills

**基础用法**:
```
/superpowers:find-skills %{搜索关键词}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 搜索技能 | `/superpowers:find-skills Git 操作` | 搜索关键词：Git 操作 |

---

## dispatching-parallel-agents 并行代理调度

并行调度多个子代理执行任务

**基础用法**:
```
/superpowers:dispatching-parallel-agents %{任务列表}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 并行调度 | `/superpowers:dispatching-parallel-agents 模块 A 重构、模块 B 测试、模块 C 文档` | 任务列表：模块 A 重构、模块 B 测试、模块 C 文档 |

---

## changelog-generator 变更日志生成

自动生成项目变更日志

**基础用法**:
```
/superpowers:changelog-generator %{版本范围}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 生成变更日志 | `/superpowers:changelog-generator v1.0.0..v1.1.0` | 版本范围：v1.0.0..v1.1.0 |