# 前端包管理器文档

前端项目依赖管理完整参考文档，涵盖 npm、yarn、pnpm 三大主流包管理器的常用命令。

## 目录

- [npm 命令](#npm-命令)
- [yarn 命令](#yarn-命令)
- [pnpm 命令](#pnpm-命令)

---

## npm 命令

### npm install - 安装依赖

**基础用法**:
```bash
npm install %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装并保存到 dependencies | `npm install %{包名}%` | 默认保存到 package.json |
| 安装到 devDependencies | `npm install -D %{包名}%` | -D: 开发环境依赖 【常用】 |
| 全局安装 | `npm install -g %{包名}%` | -g: 全局安装 【常用】 |
| 安装所有依赖 | `npm install` | 读取 package.json 安装全部 【常用】 |
| 安装指定版本 | `npm install %{包名}%@%{版本}%` | 指定具体版本号 |

### npm uninstall - 卸载依赖

**基础用法**:
```bash
npm uninstall %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 卸载并从 package.json 移除 | `npm uninstall %{包名}%` | 自动更新 package.json |
| 卸载 devDependencies | `npm uninstall -D %{包名}%` | -D: 移除开发环境依赖 |
| 卸载全局包 | `npm uninstall -g %{包名}%` | -g: 移除全局安装的包 |

### npm run - 执行脚本

**基础用法**:
```bash
npm run %{脚本名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 列出所有可用脚本 | `npm run` | 显示 package.json 中定义的所有脚本 |
| 带参数运行脚本 | `npm run %{脚本名}% -- --%{参数}%` | 向脚本传递参数 【常用】 |

### npm dev - 启动开发服务器

**基础用法**:
```bash
npm run dev
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动开发服务器 | `npm run dev` | 启动热重载开发服务器 【常用】 |
| 带参数启动 | `npm run dev -- --port %{端口}%` | 指定开发服务器端口 【常用】 |

### npm build - 生产构建

**基础用法**:
```bash
npm run build
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 执行生产构建 | `npm run build` | 生成优化后的生产环境文件 【常用】 |

### npm list - 查看依赖列表

**基础用法**:
```bash
npm list %{选项}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 列出顶层依赖 | `npm list` | 显示直接依赖 【常用】 |
| 列出所有依赖树 | `npm list --all` | 显示完整依赖树 【常用】 |
| 列出特定包 | `npm list %{包名}%` | 查看某个包的版本信息 【常用】 |
| 列出 devDependencies | `npm list --dev` | 只显示开发依赖 |
| 深度显示 | `npm list --depth=%{深度}%` | 控制依赖树显示深度 |

### npm outdated - 检查过期依赖

**基础用法**:
```bash
npm outdated
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 检查所有过期依赖 | `npm outdated` | 显示有新版本的依赖列表 【常用】 |
| 检查特定包 | `npm outdated %{包名}%` | 查看指定包是否有更新 |
| JSON 格式输出 | `npm outdated --json` | 以 JSON 格式返回结果 |

### npm update - 更新依赖

**基础用法**:
```bash
npm update %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 更新所有依赖 | `npm update` | 更新所有包到兼容最新版本 【常用】 |
| 更新特定包 | `npm update %{包名}%` | 只更新指定的包 【常用】 |
| 更新全局包 | `npm update -g %{包名}%` | 更新全局安装的包 |

### npm init - 初始化项目

**基础用法**:
```bash
npm init %{选项}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 使用默认值初始化 | `npm init -y` | 快速生成 package.json 【常用】 |
| 初始化为 ES 模块 | `npm init -y --esm` | 创建 ESM 格式项目 |
| 指定作用域初始化 | `npm init -y --scope=%{作用域}%` | 初始化为 scoped 包 【常用】 |

---

## yarn 命令

### yarn add - 添加依赖

**基础用法**:
```bash
yarn add %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 添加依赖 | `yarn add %{包名}%` | 安装并保存到 package.json 【常用】 |
| 添加为 devDependencies | `yarn add -D %{包名}%` | -D: 开发环境依赖 【常用】 |
| 添加为 optionalDependencies | `yarn add -O %{包名}%` | -O: 可选依赖 |
| 全局添加 | `yarn global add %{包名}%` | 全局安装包 |
| 添加指定版本 | `yarn add %{包名}%@%{版本}%` | 指定具体版本号 【常用】 |

### yarn remove - 移除依赖

**基础用法**:
```bash
yarn remove %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 移除依赖 | `yarn remove %{包名}%` | 卸载并从 package.json 移除 【常用】 |
| 移除全局包 | `yarn global remove %{包名}%` | 移除全局安装的包 |

### yarn dev - 启动开发服务器

**基础用法**:
```bash
yarn dev
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动开发服务器 | `yarn dev` | 启动热重载开发服务器 【常用】 |
| 带参数启动 | `yarn dev -- --port %{端口}%` | 指定开发服务器端口 【常用】 |

### yarn build - 生产构建

**基础用法**:
```bash
yarn build
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 执行生产构建 | `yarn build` | 生成优化后的生产环境文件 【常用】 |

### yarn list - 查看依赖列表

**基础用法**:
```bash
yarn list %{选项}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 列出所有依赖 | `yarn list` | 显示完整依赖树 【常用】 |
| 列出顶层依赖 | `yarn list --level 0` | 只显示直接依赖 【常用】 |
| 过滤显示 | `yarn list --pattern %{包名}%` | 过滤显示匹配的包 |

### yarn upgrade - 升级依赖

**基础用法**:
```bash
yarn upgrade %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 升级所有依赖 | `yarn upgrade` | 更新所有包到最新兼容版本 【常用】 |
| 升级特定包 | `yarn upgrade %{包名}%` | 只升级指定的包 【常用】 |
| 升级到最新版本 | `yarn upgrade --latest %{包名}%` | 忽略 semver 限制升级到最新 【常用】 |
| 全局升级 | `yarn global upgrade` | 升级所有全局包 |

---

## pnpm 命令

### pnpm add - 添加依赖

**基础用法**:
```bash
pnpm add %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 添加依赖 | `pnpm add %{包名}%` | 安装并保存到 package.json 【常用】 |
| 添加为 devDependencies | `pnpm add -D %{包名}%` | -D: 开发环境依赖 【常用】 |
| 添加为 optionalDependencies | `pnpm add -O %{包名}%` | -O: 可选依赖 |
| 全局添加 | `pnpm add -g %{包名}%` | 全局安装包 【常用】 |
| 添加指定版本 | `pnpm add %{包名}%@%{版本}%` | 指定具体版本号 【常用】 |
| 从 workspace 添加 | `pnpm add %{包名}% --filter %{workspace}%` | 为指定 workspace 添加 【常用】 |

### pnpm remove - 移除依赖

**基础用法**:
```bash
pnpm remove %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 移除依赖 | `pnpm remove %{包名}%` | 卸载并从 package.json 移除 【常用】 |
| 移除全局包 | `pnpm remove -g %{包名}%` | 移除全局安装的包 |
| 从 workspace 移除 | `pnpm remove %{包名}% --filter %{workspace}%` | 从指定 workspace 移除 【常用】 |

### pnpm dev - 启动开发服务器

**基础用法**:
```bash
pnpm dev
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动开发服务器 | `pnpm dev` | 启动热重载开发服务器 【常用】 |
| 带参数启动 | `pnpm dev -- --port %{端口}%` | 指定开发服务器端口 【常用】 |

### pnpm build - 生产构建

**基础用法**:
```bash
pnpm build
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 执行生产构建 | `pnpm build` | 生成优化后的生产环境文件 【常用】 |

### pnpm list - 查看依赖列表

**基础用法**:
```bash
pnpm list %{选项}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 列出所有依赖 | `pnpm list` | 显示依赖列表 【常用】 |
| 列出顶层依赖 | `pnpm list --depth 0` | 只显示直接依赖 【常用】 |
| 列出特定包 | `pnpm list %{包名}%` | 查看某个包的版本信息 【常用】 |
| 按依赖项查看 | `pnpm list --recursive` | 递归列出所有 workspace 的依赖 |

---

## 三大包管理器对比

| 功能 | npm | yarn | pnpm |
|------|-----|------|------|
| 安装依赖 | `npm install` | `yarn add` | `pnpm add` |
| 卸载依赖 | `npm uninstall` | `yarn remove` | `pnpm remove` |
| 开发服务器 | `npm run dev` | `yarn dev` | `pnpm dev` |
| 生产构建 | `npm run build` | `yarn build` | `pnpm build` |
| 查看列表 | `npm list` | `yarn list` | `pnpm list` |
| 更新依赖 | `npm update` | `yarn upgrade` | `pnpm update` |
| 初始化项目 | `npm init` | `yarn init` | `pnpm init` |
| 全局安装 | `-g` | `global add` | `-g` |
| 锁定文件 | package-lock.json | yarn.lock | pnpm-lock.yaml |

---

## 相关资源

- [快速开始指南](../quick-start.md)
- [Git 命令文档](../git-commands/README.md)
- [完整命令参考表](../../references/commands-reference.md)
