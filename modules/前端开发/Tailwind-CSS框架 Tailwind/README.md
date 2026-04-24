# Tailwind CSS 命令文档

Tailwind CSS 实用工具优先 CSS 框架完整参考文档。

## 目录

- [项目初始化](#项目初始化)
- [Tailwind 配置](#tailwind-配置)
- [PostCSS 集成](#postcss-集成)
- [Tailwind 指令](#tailwind-指令)
- [间距类](#间距类)
- [尺寸类](#尺寸类)
- [颜色类](#颜色类)
- [Flexbox 布局](#flexbox-布局)
- [Grid 网格布局](#grid-网格布局)
- [排版类](#排版类)
- [效果类](#效果类)
- [过渡与动画](#过渡与动画)
- [Tailwind 插件](#tailwind-插件)
- [Tailwind CLI](#tailwind-cli)
- [框架集成](#框架集成)

---

## 项目初始化

### npx tailwindcss init - 初始化项目

**基础用法**:
```bash
npx tailwindcss init
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建基础配置 | `npx tailwindcss init` | 在项目根目录生成 `tailwind.config.js` |
| 创建完整配置 | `npx tailwindcss init -p` | 同时生成 `tailwind.config.js` 和 `postcss.config.js` |
| 指定输出路径 | `npx tailwindcss init --esm` | 使用 ES 模块格式生成配置 |

---

## Tailwind 配置

### tailwind.config.js - 配置文件

**基础配置示例**:
```js
// tailwind.config.js
module.exports = {
  content: ['./src/**/*.{html,js}'],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 配置内容路径 | `content: ['./src/**/*.{html,js,ts,jsx,tsx,vue}']` | 指定扫描的文件路径 【常用】 |
| 扩展主题颜色 | `theme: { extend: { colors: { brand: '#3182ce' } } }` | 添加自定义颜色 【常用】 |
| 配置暗色模式 | `darkMode: 'media'` 或 `darkMode: 'class'` | 启用暗色模式支持 |
| 添加自定义间距 | `theme: { extend: { spacing: { '128': '32rem' } } }` | 添加自定义间距值 |
| 配置断点 | `theme: { extend: { screens: { '3xl': '1920px' } } }` | 添加自定义响应式断点 |
| 添加字体族 | `theme: { extend: { fontFamily: { sans: ['Inter', 'sans-serif'] } } }` | 自定义字体 |

---

## PostCSS 集成

### postcss.config.js - PostCSS 配置

**基础配置**:
```js
// postcss.config.js
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 基础配置 | `postcss postcss.config.js` | 初始化 PostCSS 配置 |
| 使用 Tailwind | `postcss.config.js` 中添加 `tailwindcss` 插件 | 启用 Tailwind 处理 |
| 添加前缀补全 | `postcss.config.js` 中添加 `autoprefixer` 插件 | 自动添加浏览器前缀 【常用】 |
| 生产环境压缩 | `postcss.config.js` 配置生产环境压缩 | 启用 CSS 压缩优化 |

---

## Tailwind 指令

### CSS 指令

**基础用法**:
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 基础指令 | `@tailwind base` | 注入 Tailwind 基础样式（重置样式） |
| 组件指令 | `@tailwind components` | 注入组件类样式 |
| 工具指令 | `@tailwind utilities` | 注入工具类样式 【常用】 |
| 全部指令 | `@tailwind base; @tailwind components; @tailwind utilities;` | 注入所有 Tailwind 样式 【常用】 |
| 使用 @apply | `@apply bg-blue-500 text-white p-4` | 在组件中使用工具类 【常用】 |

---

## 间距类

### 外边距与内边距

**基础用法**:
```html
<div class="m-4 p-4">间距示例</div>
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 外边距 | `m-%{数值}%` | `m-4` 表示 `margin: 1rem` 【常用】 |
| 内边距 | `p-%{数值}%` | `p-4` 表示 `padding: 1rem` 【常用】 |
| 水平外边距 | `mx-%{数值}%` | `mx-auto` 水平居中 【常用】 |
| 垂直外边距 | `my-%{数值}%` | `my-4` 上下外边距 |
| 顶部外边距 | `mt-%{数值}%` | `mt-4` 顶部外边距 【常用】 |
| 底部外边距 | `mb-%{数值}%` | `mb-4` 底部外边距 【常用】 |
| 左侧外边距 | `ml-%{数值}%` | `ml-4` 左侧外边距 【常用】 |
| 右侧外边距 | `mr-%{数值}%` | `mr-4` 右侧外边距 【常用】 |
| 负外边距 | `-m-%{数值}%` | `-m-4` 负外边距 |
| 精确间距 | `space-x-%{数值}%` | `space-x-4` 元素间水平间距 |

---

## 尺寸类

### 宽度与高度

**基础用法**:
```html
<div class="w-full h-64">尺寸示例</div>
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 固定宽度 | `w-%{数值}%` | `w-64` 表示 `width: 16rem` 【常用】 |
| 全宽 | `w-full` | `width: 100%` 【常用】 |
| 屏幕宽度 | `w-screen` | `width: 100vw` |
| 最小宽度 | `min-w-%{值}%` | `min-w-0` 重置 flex 收缩 |
| 最大宽度 | `max-w-%{值}%` | `max-w-screen-xl` 常用 【常用】 |
| 固定高度 | `h-%{数值}%` | `h-64` 表示 `height: 16rem` 【常用】 |
| 屏幕高度 | `h-screen` | `height: 100vh` 【常用】 |
| 最小高度 | `min-h-%{值}%` | `min-h-screen` 最小高度 |
| 最大高度 | `max-h-%{值}%` | `max-h-screen` 最大高度 |

---

## 颜色类

### 文本、背景与边框颜色

**基础用法**:
```html
<p class="text-blue-500 bg-white border-gray-300">颜色示例</p>
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 文本颜色 | `text-%{颜色代号}%` | `text-red-500` 红色文字 【常用】 |
| 背景颜色 | `bg-%{颜色代号}%` | `bg-blue-500` 蓝色背景 【常用】 |
| 边框颜色 | `border-%{颜色代号}%` | `border-gray-300` 灰色边框 【常用】 |
| 圆环颜色 | `ring-%{颜色代号}%` | `ring-blue-500` 轮廓环颜色 |
| 透明度 | `text-%{颜色代号}-%{透明度}%` | `text-blue-500/50` 半透明文字 |
| 分隔颜色 | `divide-%{颜色代号}%` | `divide-gray-200` 分隔线颜色 |
| 占位符颜色 | `placeholder-%{颜色代号}%` | `placeholder-gray-400` 占位符文字颜色 |
| 渐变背景 | `bg-gradient-to-r from-blue-500 to-green-500` | 渐变背景色 【常用】 |

---

## Flexbox 布局

### Flex 容器与对齐

**基础用法**:
```html
<div class="flex justify-center items-center">Flex 示例</div>
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启用 Flex | `flex` | `display: flex` 【常用】 |
| 行方向 | `flex-row` | 主轴为水平方向 【常用】 |
| 列方向 | `flex-col` | 主轴为垂直方向 【常用】 |
| 水平对齐-开始 | `justify-start` | 左对齐 【常用】 |
| 水平对齐-居中 | `justify-center` | 居中对齐 【常用】 |
| 水平对齐-结束 | `justify-end` | 右对齐 【常用】 |
| 水平对齐-两端 | `justify-between` | 两端对齐 【常用】 |
| 垂直对齐-开始 | `items-start` | 顶部对齐 【常用】 |
| 垂直对齐-居中 | `items-center` | 垂直居中 【常用】 |
| 垂直对齐-结束 | `items-end` | 底部对齐 【常用】 |
| 垂直对齐-拉伸 | `items-stretch` | 拉伸填满 【常用】 |
| Flex 增长 | `flex-1` | `flex: 1 1 0%` 增长填充 【常用】 |
| Flex 收缩 | `flex-shrink-0` | 防止收缩 【常用】 |
| Flex 换行 | `flex-wrap` | 自动换行 【常用】 |
| 独立对齐 | `self-start` / `self-center` / `self-end` | 单独元素对齐 |

---

## Grid 网格布局

### CSS Grid 布局

**基础用法**:
```html
<div class="grid grid-cols-3 gap-4">Grid 示例</div>
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启用 Grid | `grid` | `display: grid` 【常用】 |
| 列数定义 | `grid-cols-%{数值}%` | `grid-cols-3` 三列布局 【常用】 |
| 行数定义 | `grid-rows-%{数值}%` | `grid-rows-2` 两行布局 |
| 间隙 | `gap-%{数值}%` | `gap-4` 行列间隙 【常用】 |
| 水平间隙 | `gap-x-%{数值}%` | `gap-x-4` 仅水平间隙 |
| 垂直间隙 | `gap-y-%{数值}%` | `gap-y-4` 仅垂直间隙 |
| 列开始位置 | `col-start-%{数值}%` | `col-start-2` 指定列起始 |
| 列跨度 | `col-span-%{数值}%` | `col-span-2` 跨两列 【常用】 |
| 行开始位置 | `row-start-%{数值}%` | `row-start-2` 指定行起始 |
| 行跨度 | `row-span-%{数值}%` | `row-span-2` 跨两行 |
| 自动列 | `auto-cols-%{值}%` | `auto-cols-max` 自动列宽 |

---

## 排版类

### 字体与文本样式

**基础用法**:
```html
<p class="text-xl font-bold leading-relaxed tracking-wide">文本示例</p>
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 字体大小 | `text-%{尺寸}%` | `text-lg` 大号文字 【常用】 |
| 字体粗细 | `font-%{粗细}%` | `font-bold` 粗体 【常用】 |
| 字体系列 | `font-%{族}%` | `font-sans` 无衬线字体 【常用】 |
| 行高 | `leading-%{高度}%` | `leading-relaxed` 增加行高 【常用】 |
| 字间距 | `tracking-%{间距}%` | `tracking-wide` 宽字间距 |
| 文本对齐 | `text-%{方向}%` | `text-center` 居中对齐 【常用】 |
| 文本颜色 | `text-%{颜色代号}%` | `text-gray-700` 深灰色文字 【常用】 |
| 文本转换 | `uppercase` / `lowercase` / `capitalize` | 字母大小写转换 |
| 下划线 | `underline` | 添加下划线 【常用】 |
| 删除线 | `line-through` | 添加删除线 |
| 截断文本 | `truncate` | 单行截断显示省略号 【常用】 |
| 空白处理 | `whitespace-%{处理}%` | `whitespace-nowrap` 不换行 |
| 列表样式 | `list-disc` / `list-none` | 列表样式类型 |
| 列表缩进 | `list-inside` / `list-outside` | 列表缩进位置 |

---

## 效果类

### 阴影、透明度与混合模式

**基础用法**:
```html
<div class="shadow-lg opacity-75 mix-blend-multiply">效果示例</div>
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 无阴影 | `shadow-none` | 移除阴影 |
| 小阴影 | `shadow-sm` | 轻微阴影效果 |
| 常规阴影 | `shadow` | 默认阴影 【常用】 |
| 大阴影 | `shadow-lg` | 较大阴影效果 【常用】 |
| 超大阴影 | `shadow-xl` | 更大阴影效果 |
| 内阴影 | `shadow-inner` | 内部阴影效果 |
| 透明度 | `opacity-%{数值}%` | `opacity-50` 半透明效果 【常用】 |
| 混合模式 | `mix-blend-%{模式}%` | `mix-blend-multiply` 混合效果 |
| 背景混合 | `bg-blend-%{模式}%` | `bg-blend-darken` 背景混合效果 |
| 模糊 | `blur-%{程度}%` | `blur-sm` 模糊效果 |
| 灰度 | `grayscale` | 灰度滤镜效果 |
| 亮度 | `brightness-%{数值}%` | `brightness-110` 亮度调节 |
| 对比度 | `contrast-%{数值}%` | `contrast-125` 对比度调节 |
| 饱和度 | `saturate-%{数值}%` | `saturate-150` 饱和度调节 |
| 色相旋转 | `hue-rotate-%{角度}%` | `hue-rotate-90` 色相旋转 |

---

## 过渡与动画

### 过渡效果与动画类

**基础用法**:
```html
<button class="transition duration-300 ease-in-out hover:bg-blue-600">按钮</button>
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 过渡属性 | `transition` | 启用过渡效果 【常用】 |
| 过渡时间 | `duration-%{毫秒}%` | `duration-300` 300毫秒过渡 【常用】 |
| 缓动函数 | `ease-%{函数}%` | `ease-in-out` 缓动效果 【常用】 |
| 延迟 | `delay-%{毫秒}%` | `delay-150` 延迟执行 |
| 变换原点 | `origin-center` | 变换中心点 |
| 缩放 | `scale-%{比例}%` | `scale-105` 放大效果 【常用】 |
| 悬停缩放 | `hover:scale-%{比例}%` | 悬停时缩放 【常用】 |
| 悬停背景 | `hover:bg-%{颜色}%` | 悬停时变色 【常用】 |
| 旋转 | `rotate-%{角度}%` | `rotate-45` 旋转角度 |
| 平移 | `translate-x-%{值}%` | `translate-x-4` 水平移动 【常用】 |
| 关键帧动画 | `animate-%{动画名}%` | `animate-spin` 旋转动画 【常用】 |
| 脉冲动画 | `animate-pulse` | 脉冲动画效果 【常用】 |
| 跳动动画 | `animate-bounce` | 跳动动画效果 【常用】 |

---

## Tailwind 插件

### 官方插件安装与使用

**基础用法**:
```bash
npm install -D @tailwindcss/forms @tailwindcss/typography
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 表单插件 | `npm install -D @tailwindcss/forms` | 表单样式重置与美化 【常用】 |
| 排版插件 | `npm install -D @tailwindcss/typography` | Prose 排版类 【常用】 |
| 行截断插件 | `npm install -D @tailwindcss/line-clamp` | 多行文本截断 【常用】 |
| 宽高比插件 | `npm install -D @tailwindcss/aspect-ratio` | 响应式宽高比容器 |
| 在配置中启用 | `plugins: [require('@tailwindcss/forms')]` | 在 tailwind.config.js 中引入 |
| 使用 Prose 类 | `class="prose prose-lg"` | 文章排版容器 【常用】 |
| 使用行截断 | `line-clamp-3` | 显示3行后截断 【常用】 |
| 使用宽高比 | `aspect-video` / `aspect-square` | 视频比例 / 正方形比例 【常用】 |

---

## Tailwind CLI

### Tailwind 命令行工具

**基础用法**:
```bash
npx tailwindcss -o dist/output.css
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 构建输出 | `npx tailwindcss -o %{输出文件}%` | 编译并输出 CSS 文件 【常用】 |
| 监听模式 | `npx tailwindcss -o %{输出文件}% --watch` | 文件变化自动重新构建 【常用】 |
| 生产压缩 | `npx tailwindcss -o %{输出文件}% --minify` | 启用压缩减小文件体积 【常用】 |
| 指定配置文件 | `npx tailwindcss -o %{输出文件}% -c %{配置文件}%` | 使用指定配置文件 |
| 指定输入文件 | `npx tailwindcss -i %{输入文件}% -o %{输出文件}%` | 指定输入 CSS 文件 |
| JIT 模式 | `npx tailwindcss -o dist/style.css --watch --jit` | 启用即时编译模式 【常用】 |
| 显示帮助 | `npx tailwindcss --help` | 查看 CLI 帮助信息 |
| 显示版本 | `npx tailwindcss --version` | 查看 CLI 版本 |

---

## 框架集成

### 与主流前端框架集成

**基础用法**:

| 框架 | 安装命令 | 配置说明 |
|------|----------|----------|
| Next.js | `npm install -D tailwindcss postcss autoprefixer` | 配置 `tailwind.config.js` 和 `postcss.config.js`，在 `_app.js` 或 globals.css 中引入 |
| Vue | `npm install -D tailwindcss postcss autoprefixer` | 在 `main.js` 导入 CSS，或在 `postcss.config.js` 配置 |
| React (Vite) | `npm install -D tailwindcss postcss autoprefixer` | 在 `vite.config.js` 配置 PostCSS，使用 `npx tailwindcss init -p` 初始化 |
| React (CRA) | `npm install -D tailwindcss postcss autoprefixer` | 使用 `npx tailwindcss init -p` 初始化，在 `index.css` 中引入指令 |

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| Next.js 安装 | `npm install -D tailwindcss postcss autoprefixer` | Next.js 项目安装 Tailwind 【常用】 |
| Next.js 初始化 | `npx tailwindcss init -p` | 在 Next.js 项目中初始化配置 |
| Vue 安装 | `npm install -D tailwindcss postcss autoprefixer` | Vue 项目安装 Tailwind 【常用】 |
| Vue 初始化 | `npx tailwindcss init -p` | 在 Vue 项目中初始化配置 |
| Vite 安装 | `npm install -D tailwindcss postcss autoprefixer` | Vite 项目安装 Tailwind 【常用】 |
| Vite 初始化 | `npx tailwindcss init -p` | 在 Vite 项目中初始化配置 |
| React (CRA) 安装 | `npm install -D tailwindcss postcss autoprefixer` | CRA 项目安装 Tailwind 【常用】 |
| React (CRA) 初始化 | `npx tailwindcss init -p` | 在 CRA 项目中初始化配置 |
| 在 CSS 中引入 | `@tailwind base; @tailwind components; @tailwind utilities;` | 在入口 CSS 文件中添加指令 【常用】 |

---

## 实用场景示例

### 场景 1: 快速构建响应式卡片

```html
<div class="max-w-sm mx-auto bg-white rounded-xl shadow-lg overflow-hidden">
  <div class="md:flex">
    <div class="md:flex-shrink-0">
      <img class="h-48 w-full object-cover md:w-48" src="/img/card.jpg" alt="Card image">
    </div>
    <div class="p-8">
      <div class="uppercase tracking-wide text-sm text-indigo-500 font-semibold">案例标签</div>
      <h2 class="mt-2 text-xl font-semibold text-gray-900">卡片标题</h2>
      <p class="mt-2 text-gray-500">这是卡片的内容描述文字，使用 Tailwind 排版类进行样式控制。</p>
      <button class="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition duration-300">
        查看详情
      </button>
    </div>
  </div>
</div>
```

### 场景 2: Flex 导航栏

```html
<nav class="flex items-center justify-between flex-wrap bg-gray-800 p-6">
  <div class="flex items-center flex-shrink-0 text-white mr-6">
    <span class="font-semibold text-xl tracking-tight">Logo</span>
  </div>
  <div class="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
    <div class="lg:flex-grow">
      <a href="#" class="block mt-4 lg:inline-block lg:mt-0 text-gray-200 hover:text-white mr-4">
        首页
      </a>
      <a href="#" class="block mt-4 lg:inline-block lg:mt-0 text-gray-200 hover:text-white mr-4">
        关于
      </a>
      <a href="#" class="block mt-4 lg:inline-block lg:mt-0 text-gray-200 hover:text-white">
        联系
      </a>
    </div>
  </div>
</nav>
```

### 场景 3: 网格图片画廊

```html
<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 p-4">
  <div class="aspect-square overflow-hidden rounded-lg shadow-md hover:shadow-xl transition-shadow duration-300">
    <img class="w-full h-full object-cover hover:scale-105 transition-transform duration-300" src="/img/1.jpg" alt="Gallery 1">
  </div>
  <div class="aspect-square overflow-hidden rounded-lg shadow-md hover:shadow-xl transition-shadow duration-300">
    <img class="w-full h-full object-cover hover:scale-105 transition-transform duration-300" src="/img/2.jpg" alt="Gallery 2">
  </div>
  <!-- 更多图片... -->
</div>
```

### 场景 4: 表单布局

```html
<form class="w-full max-w-lg mx-auto p-6 bg-white rounded-lg shadow-md">
  <div class="mb-4">
    <label class="block text-gray-700 text-sm font-bold mb-2" for="username">
      用户名
    </label>
    <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
           id="username" type="text" placeholder="请输入用户名">
  </div>
  <div class="mb-6">
    <label class="block text-gray-700 text-sm font-bold mb-2" for="email">
      邮箱
    </label>
    <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
           id="email" type="email" placeholder="请输入邮箱">
  </div>
  <div class="flex items-center justify-between">
    <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="button">
      提交
    </button>
  </div>
</form>
```

---

## 命令速查表

| 操作 | 命令 | 说明 |
|------|------|------|
| 初始化项目 | `npx tailwindcss init` | 生成 tailwind.config.js |
| 完整初始化 | `npx tailwindcss init -p` | 同时生成 PostCSS 配置 |
| 构建 CSS | `npx tailwindcss -o` | 编译输出 CSS 文件 |
| 监听模式 | `npx tailwindcss --watch` | 监视文件变化自动构建 |
| 压缩模式 | `npx tailwindcss --minify` | 生产环境压缩输出 |
| 启用 JIT | `--jit` 标志 | 启用即时编译模式 |
| 安装表单插件 | `@tailwindcss/forms` | 表单样式插件 |
| 安装排版插件 | `@tailwindcss/typography` | Prose 排版插件 |
| 安装行截断插件 | `@tailwindcss/line-clamp` | 多行截断插件 |

---

## 相关资源

- [快速开始指南](../quick-start.md)
- [前端包管理器文档](../前端包管理器/README.md)
- [完整命令参考表](../../references/commands-reference.md)
