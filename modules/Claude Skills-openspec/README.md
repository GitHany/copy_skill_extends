# Claude Skills-openspec 命令文档

openspec 规范初始化模块。

## 📚 目录

- [openspec init](#openspec-init)
- [openspec propose](#openspec-propose)
- [openspec apply](#openspec-apply)
- [openspec archive](#openspec-archive)
- [openspec explore](#openspec-explore)

---

## openspec init

OpenSpec 规范初始化 【常用】

**基础用法**:
```
/openspec init %{项目名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 初始化项目 | `/openspec init my-api-project` | 项目名称：my-api-project |

---

## openspec propose

提议新规范 【常用】

**基础用法**:
```
/openspec propose %{规范内容}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 提议新规范 | `/openspec propose 添加新的 API 版本管理规范` | 规范内容：添加新的 API 版本管理规范 |

---

## openspec apply

应用规范变更

**基础用法**:
```
/openspec apply
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 应用规范变更 | `/openspec apply` | 无参数 |

---

## openspec archive

归档规范

**基础用法**:
```
/openspec archive %{规范名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 归档规范 | `/openspec archive v1-api-versioning` | 规范名称：v1-api-versioning |

---

## openspec explore

浏览现有规范

**基础用法**:
```
/openspec explore
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 浏览现有规范 | `/openspec explore` | 无参数 |