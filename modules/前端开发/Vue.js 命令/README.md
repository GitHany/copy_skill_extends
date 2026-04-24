# Vue.js 命令文档

Vue.js 3 现代前端框架完整参考文档，包含项目创建、组合式 API、路由、状态管理等命令。

## 📚 目录

- [项目创建](#项目创建)
- [开发与构建](#开发与构建)
- [Vue Router](#vue-router)
- [Pinia 状态管理](#pinia-状态管理)
- [组合式 API](#组合式-api)
- [Vue 3 特性](#vue-3-特性)
- [TypeScript 支持](#typescript-支持)
- [Vue I18n 国际化](#vue-i18n-国际化)
- [测试](#测试)
- [Vite 配置](#vite-配置)

---

## 项目创建

### npm create vue@latest - 创建 Vue 3 项目

**基础用法**:
```bash
npm create vue@latest %{项目名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 TypeScript 项目 | `npm create vue@latest %{项目名称}% --typescript` | 常用 |
| 创建包含路由的项目 | `npm create vue@latest %{项目名称}% --vue-router` | 常用 |
| 创建包含 Pinia 的项目 | `npm create vue@latest %{项目名称}% --pinia` | 常用 |
| 完整功能项目 | `npm create vue@latest %{项目名称}% --typescript --vue-router --pinia --vitest --playwright` | 常用 |
| 创建包含 JSX 的项目 | `npm create vue@latest %{项目名称}% --jsx` | JSX 支持 |

### npm create vite@latest - 创建 Vite+Vue 项目

**基础用法**:
```bash
npm create vite@latest %{项目名称}% -- --template vue
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| Vue + TypeScript | `npm create vite@latest %{项目名称}% -- --template vue-ts` | 常用 |
| Vue + JSX | `npm create vite@latest %{项目名称}% -- --template vue-tsc` | 常用 |
| CDN 引入式项目 | `npm create vite@latest %{项目名称}% -- --template vue --cdn` | 原型演示 |

### Vue CLI 创建项目（已不推荐）

**基础用法**:
```bash
npm install -g @vue/cli && vue create %{项目名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装 Vue CLI | `npm install -g @vue/cli` | 全局安装 CLI |
| 交互式创建 | `vue create %{项目名称}% --preset vue3` | 交互式创建 |
| Vue CLI 启动 | `vue serve` | 启动开发服务器 |
| Vue CLI 构建 | `vue build` | 构建生产包 |
| 添加插件 | `vue add %{插件名}%` | 添加插件，示例：vue-router |

---

## 开发与构建

### npm run dev - 启动开发服务器

**基础用法**:
```bash
npm run dev
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定端口启动 | `npm run dev -- --port %{端口}%` | 端口示例：`3000` 【常用】 |
| 开启 HTTPS | `npm run dev -- --https` | HTTPS 开发 |
| 指定主机访问 | `npm run dev -- --host %{主机}%` | 主机示例：`0.0.0.0` |
| 打开浏览器 | `npm run dev -- --open` | 自动打开浏览器 【常用】 |

### npm run build - 构建生产包

**基础用法**:
```bash
npm run build
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 构建并预览 | `npm run build && npm run preview` | 构建后预览 【常用】 |
| 类型检查+构建 | `npm run build -- --mode production` | 生产模式构建 |
| 生成分析报告 | `npm run build -- --generateReport` | 分析打包体积 |

### npm run preview - 预览构建结果

**基础用法**:
```bash
npm run preview
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定预览端口 | `npm run preview -- --port %{端口}%` | 端口示例：`4173` 【常用】 |

---

## Vue Router

### 安装与配置 Vue Router

**基础用法**:
```bash
npm install vue-router
```

**扩展开示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装 Vue Router 4 | `npm install vue-router@4` | 指定版本 【常用】 |
| 基础路由配置 | 创建 `src/router/index.js` 包含 `createRouter` 和 `createWebHistory` | 常用 |
| 动态路由 | `path: '/user/:id'` 动态路径参数 | 常用 |
| 嵌套路由 | `children` 属性配置子路由 | 多层页面结构 |
| 编程式导航 | `router.push('/path')` 或 `router.replace('/path')` | JS 导航 【常用】 |
| 命名路由 | `router.push({ name: 'User', params: { id: 1 } })` | 使用路由名称 |
| 路由守卫 | `router.beforeEach((to, from) => { ... })` | 权限验证 【常用】 |

---

## Pinia 状态管理

### 安装与配置 Pinia

**基础用法**:
```bash
npm install pinia
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 Store（选项式） | 定义 `state`、`getters`、`actions` | 常用 |
| 创建 Store（组合式） | 使用 `ref`、`computed`、`function` | 常用 |
| 在 main.js 中注册 | `app.use(createPinia())` | 常用 |
| 使用 Store | `const store = useStore()` 在组件中调用 | 常用 |
| Store 到 Store 通信 | 在一个 Store 中使用另一个 Store | 跨模块通信 |

---

## 组合式 API

### ref 和 reactive 创建响应式数据

**基础用法**:
```javascript
import { ref } from 'vue'
const %{变量}% = ref(%{初始值}%)
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| ref 创建响应式变量 | `const count = ref(0)` | 基本类型 【常用】 |
| ref 访问值 | `count.value` 读取或修改 | 常用 |
| reactive 创建响应式对象 | `const state = reactive({ name: 'Alice' })` | 对象类型 【常用】 |
| reactive 数组 | `const list = reactive([1, 2, 3])` | 数组类型 |
| 解构响应式对象 | 使用 `toRefs` 保持解构后响应性 | 常用 |

### computed 计算属性

**基础用法**:
```javascript
import { computed } from 'vue'
const %{计算属性}% = computed(() => %{表达式}%)
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 只读计算属性 | `const double = computed(() => count.value * 2)` | 【常用】 |
| 可写计算属性 | 使用 `get`/`set` 定义读写 | 常用 |
| 计算属性缓存 | 依赖不变时不重新计算 | 性能优化 |

### watch 和 watchEffect 监听

**基础用法**:
```javascript
import { watch } from 'vue'
watch(%{数据源}%, (新值, 旧值) => {
  %{处理逻辑}%
})
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| watchEffect 立即执行 | 自动追踪回调中的响应式依赖 | 【常用】 |
| 深度监听 | `{ deep: true }` 深度监听对象变化 | 常用 |
| 监听多个数据源 | `watch([ref1, ref2], ...)` 同时监听多个 | 常用 |
| 立即执行监听 | `{ immediate: true }` 组件创建时立即执行 | 数据初始化 |

### 生命周期钩子

**基础用法**:
```javascript
import { %{钩子名}% } from 'vue'
%{钩子名}%(() => {
  %{逻辑}%
})
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| onMounted 挂载完成 | DOM 已挂载，可访问 DOM 元素 | 【常用】 |
| onUpdated 更新完成 | DOM 更新后执行 | 常用 |
| onUnmounted 卸载完成 | 清理定时器、事件监听器 | 【常用】 |
| onBeforeMount 等前置钩子 | 对应生命周期前置执行 | 常用 |

---

## Vue 3 特性

### Teleport 传送组件

**基础用法**:
```vue
<Teleport to="body">
  <div class="modal">模态框内容</div>
</Teleport>
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 传送到 body | 将模态框传送到 body 下渲染 | 【常用】 |
| 条件传送 | `:disabled="!isOpen"` 控制是否传送 | 常用 |
| 传送到指定元素 | `<Teleport to="#portal-target">` | 自定义目标 |

### Suspense 异步组件

**基础用法**:
```vue
<Suspense>
  <template #default>
    <AsyncComponent />
  </template>
  <template #fallback>
    <div>加载中...</div>
  </template>
</Suspense>
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| async setup | setup 函数返回 Promise | 【常用】 |
| 多层嵌套 | Suspense 嵌套使用 | 复杂异步场景 |
| 配合 Promise.all | 并行加载多个异步组件 | 性能优化 |

### Fragment 多根节点

**基础用法**:
```vue
<template>
  <header>标题</header>
  <main>内容</main>
  <footer>页脚</footer>
</template>
```

> Vue 3 支持模板中有多个根节点，无需额外包裹元素。

### provide / inject 依赖注入

**基础用法**:
```javascript
// 父组件
import { provide } from 'vue'
provide('key', value)

// 子组件
import { inject } from 'vue'
const value = inject('key')
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| provide 响应式数据 | `provide('theme', ref('dark'))` | 深层组件共享 |
| inject 带默认值 | `inject('key', 'default')` | 提供默认值 |
| 组合式函数中使用 | 在 composable 中封装 provide/inject | 代码复用 【常用】 |

---

## TypeScript 支持

### 安装 TypeScript 依赖

**基础用法**:
```bash
npm install -D typescript vue-tsc
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| defineProps 类型定义 | `defineProps<{ title: string; count?: number }>()` | 【常用】 |
| defineEmits 类型定义 | `defineEmits<{ (e: 'update', value: string): void }>()` | 【常用】 |
| ref 泛型类型 | `const count: Ref<number> = ref(0)` | 常用 |
| 类型检查构建 | `npx vue-tsc --noEmit` | 构建前类型检查 【常用】 |
| 组合式函数泛型 | `function useList<T>(items: T[])` | 通用逻辑封装 |

---

## Vue I18n 国际化

### 安装与配置 Vue I18n

**基础用法**:
```bash
npm install vue-i18n
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建语言包 | `src/locales/zh-CN.json` 中文语言包 | 【常用】 |
| 配置 I18n 实例 | `createI18n` 配置 locale 和 messages | 常用 |
| 模板中使用 | `{{ $t('message.hello') }}` | 【常用】 |
| 切换语言 | `locale.value = 'en'` | 常用 |
| 插件注册 | `app.use(i18n)` 在 main.js 中 | 常用 |

---

## 测试

### 安装测试依赖

**基础用法**:
```bash
npm install -D @vue/test-utils vitest
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 挂载组件 | `mount(Component, { props: { ... } })` | 【常用】 |
| 触发事件 | `await wrapper.find('button').trigger('click')` | 【常用】 |
| 断言文本 | `expect(wrapper.text()).toContain('hello')` | 常用 |
| 运行测试 | `npx vitest run` | CI 集成 【常用】 |
| 监听模式 | `npx vitest` | 开发时实时运行 【常用】 |

---

## Vite 配置

### vite.config.js 常用配置

**基础用法**:
```javascript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()]
})
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 配置路径别名 | `@` 指向 `src` 目录 | 【常用】 |
| 配置代理 | `/api` 代理到后端服务器 | 开发联调 【常用】 |
| 配置环境变量 | `.env.production` 生产环境变量 | 常用 |
| 配置 SCSS | `sass` 预处理器配置 | 样式开发 |
| 构建优化 | 分包、压缩、sourcemap | 生产优化 【常用】 |
| 端口与主机 | `server.port` 和 `server.host` | 环境定制 |

---

## 💡 实用场景示例

### 场景 1: 从零创建完整 Vue 3 项目

```bash
# 1. 使用 Vite 创建项目（推荐）
npm create vite@latest my-vue-app -- --template vue-ts

# 2. 进入目录并安装依赖
cd my-vue-app
npm install

# 3. 安装 Vue Router
npm install vue-router

# 4. 安装 Pinia 状态管理
npm install pinia

# 5. 安装国际化
npm install vue-i18n

# 6. 安装测试工具
npm install -D @vue/test-utils vitest

# 7. 启动开发服务器
npm run dev

# 8. 构建生产版本
npm run build
```

### 场景 2: Pinia 状态管理完整流程

```javascript
// src/stores/counter.js
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useCounter = defineStore('counter', () => {
  const count = ref(0)
  const double = computed(() => count.value * 2)

  function increment() {
    count.value++
  }

  function reset() {
    count.value = 0
  }

  return { count, double, increment, reset }
})
```

```javascript
// 在组件中使用
import { useCounter } from '@/stores/counter'
const counter = useCounter()
counter.increment()
```

### 场景 3: 组合式 API 封装可复用逻辑

```javascript
// src/composables/useTitle.js
import { ref, onMounted, onUnmounted } from 'vue'

export function useTitle(initialTitle) {
  const title = ref(initialTitle)

  function setTitle(newTitle) {
    title.value = newTitle
    document.title = newTitle
  }

  return { title, setTitle }
}
```

```vue
<!-- 在组件中使用 -->
<script setup>
import { useTitle } from '@/composables/useTitle'
const { title, setTitle } = useTitle('默认标题')
setTitle('新标题')
</script>
```

### 场景 4: Vue Router 完整配置

```javascript
// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/Home.vue')
  },
  {
    path: '/user/:id',
    name: 'User',
    component: () => import('@/views/User.vue'),
    props: true
  },
  {
    path: '/dashboard',
    component: () => import('@/layouts/Dashboard.vue'),
    children: [
      { path: 'stats', component: () => import('@/views/Stats.vue') }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
```

---

## 📊 命令速查表

| 操作 | 命令 | 说明 |
|------|------|------|
| 创建项目 | `npm create vue@latest` | create-vue 脚手架 |
| 创建 Vite 项目 | `npm create vite@latest -- --template vue` | Vite 脚手架 【推荐】 |
| 启动开发服务器 | `npm run dev` | 本地开发 【常用】 |
| 构建生产包 | `npm run build` | 打包部署 【常用】 |
| 预览构建 | `npm run preview` | 预览产物 【常用】 |
| 安装路由 | `npm install vue-router` | Vue Router 4 |
| 安装状态管理 | `npm install pinia` | Pinia 【推荐】 |
| 安装国际化 | `npm install vue-i18n` | Vue I18n |
| 安装测试工具 | `npm install -D @vue/test-utils vitest` | 单元测试 |
| 安装 TypeScript | `npm install -D typescript vue-tsc` | TypeScript 支持 |
| 类型检查 | `npx vue-tsc --noEmit` | TS 类型检查 【常用】 |
| 运行测试 | `npx vitest run` | 执行测试 【常用】 |
| 创建 ref | `ref(value)` | 组合式 API 【常用】 |
| 创建 reactive | `reactive(object)` | 组合式 API 【常用】 |
| 创建 computed | `computed(() => expr)` | 组合式 API 【常用】 |
| 监听变化 | `watch(ref, callback)` | 组合式 API 【常用】 |

---

## 🔗 相关资源

- [快速开始指南](../quick-start.md)
- [前端包管理器文档](../前端包管理器/README.md)
- [Git 命令文档](../Git 命令/README.md)
- [完整命令参考表](../../references/commands-reference.md)
- [Vue.js 官方文档](https://vuejs.org/)
- [Vue Router 文档](https://router.vuejs.org/)
- [Pinia 文档](https://pinia.vuejs.org/)
- [Vite 文档](https://vitejs.dev/)
