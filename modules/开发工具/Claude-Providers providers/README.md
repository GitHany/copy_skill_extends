# Claude Skills-providers 命令文档

providers 模型提供商模块 - 多模型提供商切换和管理。

## 📚 目录

- [providers 操作](#providers-操作)

---

## providers 操作

多模型提供商切换和管理

**基础用法**:
```
/providers %{操作}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 切换到 claude | `/providers use claude` | 操作：切换到 claude |
| 切换到 codex | `/providers use codex` | 操作：切换到 codex |
| 切换到 gemini | `/providers use gemini` | 操作：切换到 gemini |
| 查看当前提供商 | `/providers status` | 无参数 |
| 列出可用提供商 | `/providers list` | 无参数 |