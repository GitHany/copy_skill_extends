# Claude Skills-ultrawork 命令文档

ultrawork 最大并行模块 - 多 agent 最大并行执行。

## 📚 目录

- [ultrawork 并行执行](#ultrawork-并行执行)

---

## ultrawork 并行执行

多 agent 最大并行执行 【常用】

**基础用法**:
```
/ultrawork %{任务描述}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 并行执行任务 | `/ultrawork 并行实现所有 API 端点` | 任务描述：并行实现所有 API 端点 |
| 查看状态 | `/ultrawork status` | 无参数 |
| 快速修复 Bug | `/ultrawork "修复项目中所有的 TypeScript 类型错误"` | 无参数 |
| 批量重构 | `/ultrawork "重构 src/components 目录下所有组件"` | 无参数 |
| 并行测试 | `/ultrawork "为所有 API 端点编写集成测试"` | 无参数 |