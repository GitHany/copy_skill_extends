# React 命令文档

React 与 Next.js 完整命令参考文档，涵盖项目创建、开发、构建、测试和部署全流程。

## 目录

- [项目创建](#项目创建)
- [依赖管理](#依赖管理)
- [React Hooks](#react-hooks)
- [Next.js CLI](#nextjs-cli)
- [TypeScript 编译](#typescript-编译)
- [路由](#路由)
- [状态管理](#状态管理)
- [测试](#测试)
- [构建和部署](#构建和部署)
- [常见问题](#常见问题)

---

## 项目创建

### npx create-react-app - 创建 React 项目

**基础用法**:
```bash
npx create-react-app %{项目名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 TypeScript 项目 | `npx create-react-app %{项目名}% --template typescript` | 项目名: 项目名称 (例: my-react-app) |
| 创建 JavaScript 项目 | `npx create-react-app %{项目名}% --template cra-template` | 项目名: 项目名称 (例: my-react-app) |

### npx create-next-app - 创建 Next.js 项目

**基础用法**:
```bash
npx create-next-app %{项目名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 TypeScript 项目 | `npx create-next-app %{项目名}% --typescript` | 项目名: 项目名称 (例: my-next-app) |
| 创建 App Router 项目 | `npx create-next-app %{项目名}% --app` | 项目名: 项目名称 (例: my-next-app) |
| 创建 Tailwind CSS 项目 | `npx create-next-app %{项目名}% --tailwind` | 项目名: 项目名称 (例: my-next-app) |
| 创建 ESLint 项目 | `npx create-next-app %{项目名}% --eslint` | 项目名: 项目名称 (例: my-next-app) |
| 创建 src 目录项目 | `npx create-next-app %{项目名}% --src-dir` | 项目名: 项目名称 (例: my-next-app) |
| 组合多个选项创建 | `npx create-next-app %{项目名}% --typescript --tailwind --eslint --app --src-dir` | 项目名: 项目名称 (例: my-next-app) |

---

## 依赖管理

### npm/yarn/pnpm 安装依赖

**基础用法**:
```bash
npm install %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| npm 安装依赖 | `npm install` | 安装 package.json 中的所有依赖 |
| npm 安装开发依赖 | `npm install %{包名}% --save-dev` | 包名: npm 包名称 (例: typescript @types/react) |
| yarn 安装依赖 | `yarn add %{包名}%` | 包名: 包名称 (例: react-router-dom) |
| pnpm 安装依赖 | `pnpm add %{包名}%` | 包名: 包名称 (例: zustand) |
| npm 卸载依赖 | `npm uninstall %{包名}%` | 包名: 包名称 (例: lodash) |
| npm 更新依赖 | `npm update %{包名}%` | 包名: 包名称 (例: react) |

### npm run start - 启动开发服务器

**基础用法**:
```bash
npm start
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| npm 启动开发服务器 | `npm start` | 启动 React 开发服务器 |
| yarn 启动开发服务器 | `yarn start` | 使用 yarn 启动开发服务器 |
| pnpm 启动开发服务器 | `pnpm dev` | 使用 pnpm 启动开发服务器 |
| 指定端口启动 | `PORT=%{端口}% npm start` | 端口: 端口号 (例: 3001) |

---

## React Hooks

### useState Hook 状态管理

**基础用法**:
```tsx
const [state, setState] = useState(initialValue)
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 基础状态声明 | `const [count, setCount] = useState(0)` | 声明一个计数器状态 |
| 对象状态声明 | `const [user, setUser] = useState({ name: '', age: 0 })` | 声明对象类型状态 |
| 函数式更新 | `setCount(prev => prev + 1)` | 基于前一个状态计算新值 |
| 泛型类型声明 | `const [data, setData] = useState<DataType | null>(null)` | TypeScript 类型化声明 |

### useEffect Hook 副作用

**基础用法**:
```tsx
useEffect(() => { effect; return () => cleanup; }, [deps])
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 组件挂载时执行 | `useEffect(() => { console.log('mounted') }, [])` | 空依赖数组，仅挂载时执行一次 |
| 依赖变化时执行 | `useEffect(() => { fetchData(id) }, [id])` | id 变化时重新执行 |
| 清理副作用 | `useEffect(() => { const timer = setInterval(...); return () => clearInterval(timer) }, [])` | 组件卸载时清理定时器 |
| 条件执行副作用 | `useEffect(() => { if (userId) fetchData(userId) }, [userId])` | 仅在条件满足时执行 |

### useContext Hook 跨组件通信

**基础用法**:
```tsx
const value = useContext(MyContext)
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 消费 Context | `const theme = useContext(ThemeContext)` | 在组件中获取 Context 值 |
| 创建 Context | `const ThemeContext = createContext(defaultValue)` | 创建新的 Context 对象 |
| 提供 Context 值 | `<ThemeContext.Provider value={theme}>...</ThemeContext.Provider>` | 在组件树中提供 Context |
| 自定义 Provider Hook | 自定义 Hook 封装 Provider | 封装状态和 Provider 逻辑 |

### useReducer Hook 复杂状态逻辑

**基础用法**:
```tsx
const [state, dispatch] = useReducer(reducer, initialState)
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 基础 reducer 用法 | 使用 switch 处理 action | 适合复杂状态转换逻辑 |
| 指定初始状态 | `useReducer(reducer, { count: 0 })` | 提供初始状态对象 |
| 惰性初始化 | `useReducer(reducer, initArg, init)` | 延迟计算初始状态 |

### useMemo 与 useCallback Hook 性能优化

**基础用法**:
```tsx
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b])
const memoizedCallback = useCallback(() => { doSomething(a, b) }, [a, b])
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| useMemo 缓存计算值 | `const sortedList = useMemo(() => items.sort(...), [items])` | 避免每次渲染重新排序 |
| useCallback 缓存回调 | `const handleClick = useCallback((id) => { ... }, [])` | 避免子组件不必要重渲染 |
| 配合 React.memo 使用 | `const MemoComponent = React.memo(({ data }) => ...)` | 高阶组件缓存 |

---

## Next.js CLI

### next dev - 启动开发服务器

**基础用法**:
```bash
next dev
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 默认端口启动 | `next dev` | 默认端口 3000 |
| 指定端口启动 | `next dev --port %{端口}%` | 端口: 端口号 (例: 8080) |
| 指定主机启动 | `next dev -H %{主机}%` | 主机: 主机地址 (例: 0.0.0.0) |
| Turbo 模式启动 | `next dev --turbo` | 使用 Turbopack 加速开发 |

### next build - 构建生产版本

**基础用法**:
```bash
next build
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 构建生产版本 | `next build` | 优化构建产物 |
| 分析构建产物 | `next build --analyze` | 分析包大小 |
| 仅生成静态导出 | `next build --export` | 静态 HTML 导出 |

### next start - 启动生产服务器

**基础用法**:
```bash
next start
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 默认端口启动 | `next start` | 默认端口 3000 |
| 指定端口启动 | `next start -p %{端口}%` | 端口: 端口号 (例: 3000) |
| 指定主机启动 | `next start -H %{主机}%` | 主机: 主机地址 (例: 0.0.0.0) |

### next lint - ESLint 检查

**基础用法**:
```bash
next lint
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 运行 ESLint 检查 | `next lint` | 检查代码规范 |
| 修复可自动修复的问题 | `next lint --fix` | 自动修复问题 |
| 指定目录检查 | `next lint --dir %{目录}%` | 目录: 目录路径 (例: src) |

---

## TypeScript 编译

### npx tsc TypeScript 编译

**基础用法**:
```bash
npx tsc --noEmit
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 类型检查不生成文件 | `npx tsc --noEmit` | 仅做类型检查，不输出 JS 文件 |
| 初始化 tsconfig | `npx tsc --init` | 生成 tsconfig.json |
| 编译所有 TypeScript 文件 | `npx tsc` | 输出编译后的 JS 文件 |
| 指定配置文件编译 | `npx tsc --project %{配置文件}%` | 配置文件: tsconfig 文件路径 (例: tsconfig.json) |
| 严格模式编译 | `npx tsc --strict` | 启用所有严格类型检查选项 |
| 观察模式自动编译 | `npx tsc --watch` | 文件变化时自动重新编译 |

---

## 路由

### React Router 路由

**基础用法**:
```bash
npm install react-router-dom
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装 React Router DOM | `npm install react-router-dom` | 安装 v6 版本路由库 |
| 安装 React Router v7 | `npm install react-router` | 安装最新版本路由库 |
| 安装 TypeScript 类型 | `npm install @types/react-router-dom --save-dev` | 安装类型定义文件 |

---

## 状态管理

### Zustand 状态管理

**基础用法**:
```bash
npm install zustand
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装 Zustand | `npm install zustand` | 安装轻量状态管理库 |
| 创建状态 store | `import { create } from 'zustand'` | 创建全局状态 store |
| 使用持久化中间件 | `npm install zustand/middleware` | 数据持久化存储 |

### Redux Toolkit 状态管理

**基础用法**:
```bash
npm install @reduxjs/toolkit react-redux
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装 Redux Toolkit | `npm install @reduxjs/toolkit react-redux` | 安装官方推荐状态管理方案 |
| 创建 store | `configureStore({ reducer: { counter: counterReducer } })` | 配置 Redux store |
| 创建 slice | `createSlice({ name: 'counter', initialState, reducers })` | 创建状态切片 |

---

## 测试

### @testing-library/react 测试

**基础用法**:
```bash
npm install --save-dev @testing-library/react @testing-library/jest-dom
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装 React Testing Library | `npm install --save-dev @testing-library/react @testing-library/jest-dom` | 安装测试库 |
| 安装用户交互测试 | `npm install --save-dev @testing-library/user-event` | 模拟用户交互 |
| 运行测试 | `npm test` | 运行所有测试 |
| 监视模式运行测试 | `npm test -- --watch` | 文件变化时重新运行测试 |
| 覆盖率测试 | `npm test -- --coverage` | 生成测试覆盖率报告 |

---

## 构建和部署

### npm run build 构建生产版本

**基础用法**:
```bash
npm run build
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| npm 构建生产版本 | `npm run build` | 构建 React 项目 |
| yarn 构建生产版本 | `yarn build` | 使用 yarn 构建 |
| 分析构建产物 | `npm run build -- --analyze` | 分析包大小组成 |

### Vercel 部署 Next.js

**基础用法**:
```bash
vercel
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装 Vercel CLI | `npm install -g vercel` | 全局安装 Vercel 命令行工具 |
| 登录 Vercel | `vercel login` | 关联 Vercel 账号 |
| 部署项目 | `vercel` | 部署到预览环境 |
| 部署到生产环境 | `vercel --prod` | 部署到正式环境 |
| 拉取线上环境变量 | `vercel env pull` | 同步线上环境变量到本地 |
| 查看环境变量列表 | `vercel env list` | 查看所有环境变量 |

---

## 常见问题

### Q: create-react-app 和 create-next-app 有什么区别？

create-react-app 适用于纯 React SPA 项目，不包含服务端渲染功能。create-next-app 适用于 Next.js 全栈框架，支持 SSR、SSG、API Routes 等高级特性。

### Q: useEffect 的依赖数组为空和不为空有什么区别？

依赖数组为空 `[]` 时，effect 只在组件挂载时执行一次（类似 componentDidMount）。有依赖项时，每次依赖变化都会重新执行 effect。

### Q: Next.js App Router 和 Pages Router 有什么区别？

App Router 是 Next.js 13+ 推出的新路由系统，支持 React Server Components、嵌套布局、流式渲染等新特性。Pages Router 是传统路由方式，兼容性更好。

### Q: 如何选择状态管理方案？

简单场景使用 useState/useReducer 即可。跨组件共享状态可使用 Context API 或 Zustand（轻量）。复杂应用建议使用 Redux Toolkit。

### Q: Next.js 构建后如何部署？

Next.js 官方推荐部署到 Vercel（nextjs.vercel.com），零配置即可部署。也支持 Docker、Node.js 服务器、静态导出等多种部署方式。

---

## 相关资源

- [React 官方文档](https://react.dev)
- [Next.js 官方文档](https://nextjs.org/docs)
- [TypeScript 官方文档](https://www.typescriptlang.org/docs)
- [React Testing Library 文档](https://testing-library.com/docs/react-testing-library/intro/)
- [Vercel 部署文档](https://vercel.com/docs)
