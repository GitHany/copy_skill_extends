# TypeScript 命令文档

TypeScript 类型系统与工具链完整参考文档。

## 目录

- [TypeScript 核心](#typescript-核心)
- [高级类型](#高级类型)
- [工具链](#工具链)
- [集成应用](#集成应用)

---

## TypeScript 核心

### tsc --init - 生成 tsconfig.json

**基础用法**:
```bash
tsc --init
```

**说明**: 在当前目录生成默认的 `tsconfig.json` 配置文件。

### tsc --version - 查看版本

**基础用法**:
```bash
tsc --version
```

**说明**: 输出当前安装的 TypeScript 编译器版本号。

### tsc - 编译 TypeScript

**基础用法**:
```bash
tsc %{文件名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 编译所有文件 | `tsc` | 根据 tsconfig.json 编译全部 .ts 文件 |
| 监视模式 | `tsc -w` | 文件变化时自动重新编译 |
| 仅类型检查 | `tsc --noEmit` | 不生成 .js 文件，只检查类型错误 |
| 指定配置文件 | `tsc --project %{目录}%` | 使用指定目录下的 tsconfig.json |
| 编译为 ES2015 | `tsc --target ES2015 --module commonjs %{文件}%` | 指定编译目标和模块格式 |
| 编译为单文件 | `tsc --outFile bundle.js %{文件1}% %{文件2}%` | 将多个文件合并输出 |
| 保留注释 | `tsc --removeComments %{文件}%` | 移除源代码中的注释（加 --removeComments 则移除） |
| 生成声明文件 | `tsc --declaration %{文件}%` | 同时生成对应的 .d.ts 声明文件 |
| 严格模式编译 | `tsc --strict %{文件}%` | 启用所有严格类型检查选项 |

### tsconfig.json 核心选项

**示例配置**:
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "lib": ["ES2020"],
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "moduleResolution": "node",
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

| 选项 | 值 | 说明 |
|------|----|------|
| target | ES5 / ES6 / ES2020 | 编译目标 JavaScript 版本 |
| module | commonjs / es2015 / esnext | 模块系统 |
| strict | true | 启用所有严格检查（相当于 noImplicitAny, strictNullChecks 等） |
| noImplicitAny | true | 不允许隐式 any 类型 |
| strictNullChecks | true | 严格检查 null 和 undefined |
| esModuleInterop | true | 允许默认导入 export = 形式的模块 |
| skipLibCheck | true | 跳过库文件的类型检查 |
| outDir | ./dist | 编译输出目录 |
| rootDir | ./src | 源代码根目录 |
| include | ["src/**/*"] | 要包含的文件的 glob 模式 |
| exclude | ["node_modules"] | 要排除的文件或目录 |

### 严格模式配置

**基础用法**:
```bash
tsc --strict
```

**说明**: 启用所有严格类型检查选项，相当于同时设置:
- `--strictNullChecks`
- `--strictFunctionTypes`
- `--strictBindCallApply`
- `--strictPropertyInitialization`
- `--noImplicitAny`
- `--noImplicitThis`
- `--alwaysStrict`

**JSON 配置**:
```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true
  }
}
```

---

## 高级类型

### 泛型命令

**基础用法**:
```typescript
function identity<T>(arg: T): T {
  return arg;
}
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 约束泛型 | `function getLength<T extends { length: number }>(arg: T): number` | 限制 T 必须有 length 属性 |
| 多类型参数 | `function pair<K, V>(key: K, value: V): [K, V]` | 使用多个泛型参数 |
| 泛型接口 | `interface Result<T, E = Error> { ok: boolean; data?: T; error?: E }` | 带默认类型的泛型接口 |
| 泛型类 | `class Box<T> { value: T; constructor(v: T) { this.value = v } }` | 泛型类 |
| 泛型别名 | `type Pair<T, U> = { first: T; second: U }` | 泛型类型别名 |

### 实用类型 (Utility Types)

**Partial - 全部属性可选**

**基础用法**:
```typescript
type Partial<T> = { [P in keyof T]?: T[P] };
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 用户更新 | `type UserUpdate = Partial<User>` | 将 User 的所有属性变为可选 |
| 部分配置 | `type PartialConfig = Partial<Config>` | 用于接收部分配置的场景 |

**Required - 全部属性必需**

**基础用法**:
```typescript
type Required<T> = { [P in keyof T]-?: T[P] };
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 确保必填 | `type CompleteUser = Required<PartialUser>` | 将可选属性转为必填 |

**Pick - 选取属性**

**基础用法**:
```typescript
type Pick<T, K extends keyof T> = { [P in K]: T[P] };
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 基础选择 | `type UserName = Pick<User, 'name' \| 'email'>` | 仅选取 name 和 email |
| 表单字段 | `type FormFields = Pick<FormDef, 'label' \| 'placeholder'>` | 选取表单相关字段 |

**Omit - 排除属性**

**基础用法**:
```typescript
type Omit<T, K extends keyof T> = Pick<T, Exclude<keyof T, K>>;
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 排除密码 | `type PublicUser = Omit<User, 'password'>` | 排除敏感字段 |
| 排除方法 | `type DataOnly<T> = Omit<T, keyof Function>` | 排除所有函数类型成员 |

**Record - 键值映射**

**基础用法**:
```typescript
type Record<K extends keyof any, V> = { [P in K]: V };
```

**扩展开例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 状态映射 | `type StatusMap = Record<'pending' \| 'done', string>` | 固定键的映射 |
| 实体集合 | `type UserMap = Record<string, User>` | 字符串键到用户对象的映射 |
| 分类统计 | `type ScoreMap = Record<string, number>` | 任意字符串键到数字的映射 |

**Exclude - 排除联合类型**

**基础用法**:
```typescript
type Exclude<T, U> = T extends U ? never : T;
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 排除字符串 | `type NonString = Exclude<string \| number \| boolean, string>` | 结果为 number \| boolean |
| 排除 null | `type NonNullable<T> = Exclude<T, null \| undefined>` | 排除 null 和 undefined |

**Extract - 提取联合类型**

**基础用法**:
```typescript
type Extract<T, U> = T extends U ? T : never;
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 提取字符串 | `type StringOnly = Extract<string \| number \| symbol, string>` | 结果为 string |

### 类型守卫

**基础用法**:
```typescript
function isString(value: unknown): value is string {
  return typeof value === 'string';
}
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 对象类型守卫 | `function isUser(obj: unknown): obj is User { return 'name' in obj && 'email' in obj }` | 检查对象属性 |
| 非空守卫 | `function assertDefined<T>(v: T \| undefined \| null): asserts v is T { if (v === undefined) throw new Error() }` | 断言已定义 |
| in 守卫 | `'swim' in animal` | 检查属性是否存在 |
| instanceof 守卫 | `value instanceof Error` | 检查实例类型 |

### 条件类型

**基础用法**:
```typescript
type ExtractPromise<T> = T extends Promise<infer U> ? U : T;
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 提取 Promise 值 | `type Awaited<T> = T extends Promise<infer U> ? Awaited<U> : T` | 递归提取嵌套 Promise |
| 返回类型 | `type ReturnType<T extends (...args: any) => any> = T extends (...args: any) => infer R ? R : never` | 获取函数返回值类型 |
| 参数类型 | `type FirstArg<T> = T extends (arg: infer A, ...rest: any) => any ? A : never` | 获取函数第一个参数类型 |
| 三元条件 | `type IsArray<T> = T extends any[] ? true : false` | 基于类型分支 |

### 映射类型

**基础用法**:
```typescript
type Readonly<T> = { readonly [P in keyof T]: T[P] };
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 只读 | `type FrozenUser = Readonly<User>` | 所有属性只读 |
| 可选 | `type OptionalUser = Partial<User>` | 所有属性可选 |
| 键重映射 | `type Getters<T> = { [K in keyof T as \`get\${Capitalize<string & K>}\`]: () => T[K] }` | 通过键重映射生成 getter |
| 值变换 | `type Stringify<T> = { [K in keyof T]: string }` | 所有值转为字符串 |
| 条件映射 | `{ [K in keyof T as T[K] extends string ? K : never]: T[K] }` | 仅映射特定值类型的键 |

---

## 工具链

### ts-node - 直接执行 TypeScript

**基础用法**:
```bash
npx ts-node %{文件}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 快速执行 | `npx ts-node src/index.ts` | 直接运行 .ts 文件 |
| 加载配置 | `npx ts-node --project tsconfig.json src/index.ts` | 指定配置文件 |
| REPL 模式 | `npx ts-node` | 进入交互式解释器 |
| 编译并执行 | `npx ts-node --transpile-only src/index.ts` | 跳过类型检查直接转译 |
| 使用 SWC | `npx ts-node --transpiler swc src/index.ts` | 使用 SWC 转译器加速 |

### tsx - 更快的 TS 执行

**基础用法**:
```bash
npx tsx %{文件}%
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 快速运行 | `npx tsx src/index.ts` | ESM 优先的快速转译 |
| 监视模式 | `npx tsx watch src/index.ts` | 文件变化自动重启 |
| TypeCheck | `npx tsx --tsconfig tsconfig.json src/index.ts` | 指定配置并启用类型检查 |
| 内联执行 | `npx tsx -e 'console.log("hello")'` | 执行内联代码 |

### SWC (swc-node) - 高速编译

**基础用法**:
```bash
npx swc src -d dist
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 批量编译 | `npx swc src -d dist -w` | 监视模式编译整个目录 |
| 指定配置 | `npx swc src -d dist --config-file .swcrc` | 使用 .swcrc 配置文件 |
| 仅转译 | `npx swc src -d dist --no-type-inspection` | 跳过类型检查 |
| 指定目标 | `npx swc src -d dist --target es2020` | 指定输出 ECMAScript 版本 |

### TSC 编译选项详解

**常用命令行选项**:

| 选项 | 说明 |
|------|------|
| `--help --all` | 显示所有编译器选项 |
| `--target ES2020` | 指定 ECMAScript 目标版本 |
| `--module commonjs` | 指定模块系统 |
| `--outDir ./dist` | 设置输出目录 |
| `--declaration` | 生成 .d.ts 声明文件 |
| `--declarationMap` | 生成声明文件的 source map |
| `--sourceMap` | 生成 .js.map 源映射 |
| `--noEmit` | 不输出文件，仅做类型检查 |
| `--watch` / `-w` | 监视文件变化 |
| `--strict` | 启用所有严格检查 |
| `--noImplicitAny` | 不允许隐式 any |
| `--strictNullChecks` | 严格 null/undefined 检查 |
| `--lib` | 指定要包含的库文件 |
| `--jsx react` | JSX 处理模式 |
| `--esModuleInterop` | 启用 ES 模块互操作 |
| `--skipLibCheck` | 跳过库文件检查 |
| `--forceConsistentCasingInFileNames` | 强制文件名大小写一致 |

### type-fest 实用类型

**基础用法**:
```bash
npm install type-fest
```

**扩展示例**:

| 工具类型 | 代码 | 说明 |
|----------|------|------|
| 深层 Partial | `type DeepPartial<T> = Partial<{ [K in keyof T]: DeepPartial<T[K]> }>` | 递归 Partial（可使用 type-fest 的 DeepPartial） |
| 深层只读 | `import { DeepReadonly } from 'type-fest'` | 递归只读 |
| 可选键 | `import { OptionalKeys } from 'type-fest'` | 获取所有可选键的联合类型 |
| 必填键 | `import { RequiredKeys } from 'type-fest'` | 获取所有必填键的联合类型 |
| 键值类型 | `import { ValueOf } from 'type-fest'` | 获取联合类型中值的类型 |
| 解冻 | `import { Mutable } from 'type-fest'` | 移除只读修饰符 |

### Zod schema 验证

**基础用法**:
```bash
npm install zod
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 基本 schema | `import { z } from 'zod'; const UserSchema = z.object({ name: z.string(), age: z.number() })` | 定义对象 schema |
| 验证数据 | `const result = UserSchema.safeParse({ name: 'Alice', age: 30 })` | 安全解析并验证 |
| 类型提取 | `type User = z.infer<typeof UserSchema>` | 从 schema 提取 TypeScript 类型 |
| 可选字段 | `z.object({ email: z.string().optional() })` | 可选字段 |
| 默认值 | `z.string().default('匿名用户')` | 提供默认值 |
| 嵌套 schema | `z.object({ address: z.object({ city: z.string() }) })` | 嵌套结构 |
| 数组验证 | `z.array(z.string())` | 数组元素类型验证 |
| 联合类型 | `z.union([z.string(), z.number()])` | 联合类型验证 |
| 枚举 | `z.enum(['A', 'B', 'C'])` | 枚举值验证 |

---

## 集成应用

### TypeScript + React (tsx)

**基础用法**:
```bash
npx tsx src/App.tsx
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 运行 React 组件 | `npx tsx src/components/Button.tsx` | 执行 React 组件 |
| React 项目构建 | `npx tsx node_modules/vite/bin/vite.js` | 使用 Vite 构建 React |
| 开发服务器 | `npx tsx node_modules/react-scripts/scripts/start.js` | CRA 开发模式 |

### TypeScript + Node.js

**基础用法**:
```bash
npx ts-node src/server.ts
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| Express 服务 | `npx ts-node src/express-app.ts` | 运行 Express 服务器 |
| 快速脚本 | `npx tsx src/script.ts` | 使用 tsx 运行脚本 |
| API 服务 | `npx tsx src/api/index.ts` | 运行 API 服务 |

### TypeScript + Express

**基础用法**:
```bash
npx ts-node src/server.ts
```

**示例代码**:
```typescript
import express, { Request, Response, NextFunction } from 'express';

const app = express();
app.use(express.json());

app.get('/api/users', (req: Request, res: Response) => {
  res.json([{ id: 1, name: 'Alice' }]);
});

app.post('/api/users', (req: Request, res: Response) => {
  const user = req.body;
  res.status(201).json(user);
});

app.use((err: Error, req: Request, res: Response, _next: NextFunction) => {
  res.status(500).json({ error: err.message });
});

app.listen(3000, () => console.log('Server running on port 3000'));
```

### .d.ts 声明文件

**基础用法**:
```typescript
// src/types/modules.d.ts
declare module 'my-module' {
  export function doSomething(input: string): void;
  export const VERSION: string;
}
```

**扩展示例**:

| 场景 | 代码 | 说明 |
|------|------|------|
| 模块声明 | `declare module '*.svg' { const content: string; export default content }` | 声明 SVG 模块 |
| 全局声明 | `declare const API_KEY: string;` | 全局变量声明 |
| 函数重载声明 | `declare function greet(name: string): string; declare function greet(names: string[]): string[];` | 函数重载 |
| 类声明 | `declare class Greeter { greeting: string; constructor(message: string); greet(): string; }` | 全局类声明 |
| 命名空间声明 | `declare namespace MyLib { function foo(): void; }` | 命名空间声明 |
| 三斜线引用 | `/// <reference path="node.d.ts" />` | 引用其他声明文件 |

**全局.d.ts 示例**:
```typescript
// global.d.ts
declare global {
  namespace NodeJS {
    interface ProcessEnv {
      NODE_ENV: 'development' | 'production' | 'test';
      PORT?: string;
      API_URL: string;
    }
  }
}

export {};
```
