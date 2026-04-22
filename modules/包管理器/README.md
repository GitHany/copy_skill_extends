# 包管理器文档

非前端语言（npm/yarn/pnpm）之外的包管理器完整参考文档，涵盖 Rust/Cargo、Go Modules、PHP/Composer、Ruby/Bundler、Python/pip-tools、Unity/.NET 等主流生态。

## 目录

- [Rust/Cargo](#rustcargo)
- [Go Modules](#go-modules)
- [PHP/Composer](#phpcomposer)
- [Ruby/Bundler](#rubybundler)
- [Python/pip-tools](#pythonpip-tools)
- [Unity/.NET (NuGet)](#unitynet-nuget)

---

## Rust/Cargo

### cargo new - 创建新项目

**基础用法**:
```bash
cargo new %{项目名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建二进制项目 | `cargo new %{项目名}%` | 默认创建可执行程序 【常用】 |
| 创建库项目 | `cargo new --lib %{项目名}%` | 创建为库项目 【常用】 |
| 在当前目录创建 | `cargo new .` | 在当前目录初始化项目 |
| 指定路径创建 | `cargo new %{路径}%/%{项目名}%` | 指定创建路径 |
| 指定版本 | `cargo new --edition %{版本}% %{项目名}%` | 指定 Rust 版本 【常用】 |

### cargo build - 编译项目

**基础用法**:
```bash
cargo build %{选项}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 调试编译 | `cargo build` | 生成调试符号，开发使用 【常用】 |
| 发布编译 | `cargo build --release` | 优化编译，发布使用 【常用】 |
| 编译指定包 | `cargo build --package %{包名}%` | 只编译指定包 |
| 编译指定目标 | `cargo build --target %{目标}%` | 交叉编译到指定平台 |
| 并行编译 | `cargo build -j %{数量}%` | 指定并行任务数 |
| 只检查不生成 | `cargo check` | 快速检查代码错误 【常用】 |

### cargo run - 运行项目

**基础用法**:
```bash
cargo run %{选项}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 运行项目 | `cargo run` | 编译并运行主程序 【常用】 |
| 传递参数 | `cargo run -- %{参数}%` | 向程序传递参数 【常用】 |
| 发布模式运行 | `cargo run --release` | 以优化模式运行 |
| 指定示例 | `cargo run --example %{示例名}%` | 运行 examples 中的示例 |
| 运行指定包 | `cargo run --package %{包名}%` | 运行指定包的二进制 |

### cargo test - 运行测试

**基础用法**:
```bash
cargo test %{选项}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 运行所有测试 | `cargo test` | 运行所有单元测试和集成测试 【常用】 |
| 运行特定测试 | `cargo test %{测试名}%` | 只运行匹配的测试 【常用】 |
| 运行文档测试 | `cargo test --doc` | 只运行文档中的示例代码 |
| 显示测试输出 | `cargo test -- --nocapture` | 显示 print 输出 【常用】 |
| 并行运行 | `cargo test -- --test-threads=%{数量}%` | 指定并行线程数 |
| 运行时包含性能测试 | `cargo test -- --ignored` | 运行被忽略的长时间测试 |

### cargo bench - 运行基准测试

**基础用法**:
```bash
cargo bench %{选项}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 运行所有基准测试 | `cargo bench` | 执行所有 #[bench] 标记的基准测试 【常用】 |
| 运行特定基准测试 | `cargo bench %{基准测试名}%` | 只运行匹配的基准测试 |
| 基准测试并比较 | `cargo bench -- --compare %{基线}%` | 与历史基准比较 |
| 导出基准数据 | `cargo bench -- --save-baseline %{基线名}%` | 保存基准数据 |

### cargo add - 添加依赖

**基础用法**:
```bash
cargo add %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 添加依赖 | `cargo add %{包名}%` | 添加到 Cargo.toml 【常用】 |
| 添加开发依赖 | `cargo add %{包名}% --dev` | 添加到 [dev-dependencies] 【常用】 |
| 添加构建依赖 | `cargo add %{包名}% --build` | 添加到 [build-dependencies] |
| 指定版本 | `cargo add %{包名}%@%{版本}%` | 指定具体版本 【常用】 |
| 添加可选功能 | `cargo add %{包名}% --features %{功能}%` | 启用包的特定功能 【常用】 |
| 添加 Git 依赖 | `cargo add %{包名}% --git %{git地址}%` | 从 Git 仓库添加 【常用】 |
| 添加路径依赖 | `cargo add %{包名}% --path %{路径}%` | 从本地路径添加 |

### cargo remove - 移除依赖

**基础用法**:
```bash
cargo remove %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 移除依赖 | `cargo remove %{包名}%` | 从 Cargo.toml 中移除 【常用】 |
| 移除开发依赖 | `cargo remove %{包名}% --dev` | 移除开发依赖 |
| 移除构建依赖 | `cargo remove %{包名}% --build` | 移除构建依赖 |
| 移除可选功能 | `cargo remove %{包名}% --features %{功能}%` | 禁用特定功能 |

### cargo clean - 清理构建产物

**基础用法**:
```bash
cargo clean %{选项}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 清理所有构建产物 | `cargo clean` | 删除 target 目录 【常用】 |
| 清理并重新构建 | `cargo clean && cargo build` | 完全重新编译 |
| 清理指定配置 | `cargo clean --release` | 只清理发布模式的构建 |

### cargo doc - 生成文档

**基础用法**:
```bash
cargo doc %{选项}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 生成项目文档 | `cargo doc` | 生成 Rustdoc 文档 【常用】 |
| 打开文档 | `cargo doc --open` | 生成并自动打开文档 【常用】 |
| 生成依赖文档 | `cargo doc --document-private-items` | 包含私有项文档 |
| 只生成库文档 | `cargo doc --lib` | 只为库 crate 生成文档 |

### cargo update - 更新依赖

**基础用法**:
```bash
cargo update %{选项}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 更新所有依赖 | `cargo update` | 按 semver 规则更新 【常用】 |
| 更新特定包 | `cargo update %{包名}%` | 只更新指定包 【常用】 |
| 更新到最新补丁版 | `cargo update -p %{包名}% --precise %{版本}%` | 精确指定版本 |

---

## Go Modules

### go mod init - 初始化模块

**基础用法**:
```bash
go mod init %{模块名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 初始化模块 | `go mod init %{模块名}%` | 创建 go.mod 文件 【常用】 |
| 初始化带路径 | `go mod init %{github.com/组织/项目}%` | 完整模块路径 【常用】 |
| 初始化为库 | `go mod init %{模块名}%` | 初始化为可复用库 |
| 在已存在项目中 | `go mod init` | 在已有代码的目录初始化 |

### go mod tidy - 整理依赖

**基础用法**:
```bash
go mod tidy
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 整理依赖 | `go mod tidy` | 添加缺失依赖，移除无用依赖 【常用】 |
| 详细模式 | `go mod tidy -v` | 显示详细操作信息 |
| 调试模式 | `go mod tidy -x` | 显示下载过程 |

### go mod download - 下载依赖

**基础用法**:
```bash
go mod download %{模块}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 下载所有依赖 | `go mod download` | 下载 go.mod 中的所有模块 【常用】 |
| 下载特定模块 | `go mod download %{模块名}%` | 只下载指定模块 【常用】 |
| 列出可更新 | `go mod download -x` | 显示将要下载的模块列表 |
| 并行下载 | `go mod download -json` | 以 JSON 格式输出下载信息 |

### go get - 获取或更新包

**基础用法**:
```bash
go get %{包}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 获取包 | `go get %{包名}%` | 下载并添加依赖 【常用】 |
| 获取指定版本 | `go get %{包名}%@%{版本}%` | 指定具体版本标签 【常用】 |
| 获取最新版 | `go get %{包名}%@latest` | 更新到最新版本 【常用】 |
| 获取主干 | `go get %{包名}%@master` | 获取 master/main 分支 |
| 降级到上一个兼容版本 | `go get %{包名}%@upgrade` | 按 semver 升级 |
| 获取特定提交 | `go get %{包名}%@%{commit_hash}%` | 获取特定 commit |

### go mod why - 解释依赖

**基础用法**:
```bash
go mod why %{模块}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 解释依赖原因 | `go mod why %{模块}%` | 解释为何需要某模块 【常用】 |
| 显示依赖链 | `go mod why -m %{模块}%` | 显示模块之间的依赖关系 |
| 图形化依赖 | `go mod graph` | 显示完整依赖图 【常用】 |

### go mod vendor - 管理 vendor

**基础用法**:
```bash
go mod vendor
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 vendor 目录 | `go mod vendor` | 将依赖复制到 vendor 目录 【常用】 |
| 使用 vendor 构建 | `go build -mod=vendor` | 使用本地 vendor 构建 【常用】 |
| 清理 vendor | `go mod vendor -e` | 显示 vendor 中多余的文件 |
| 验证 vendor | `go mod verify` | 验证依赖完整性 【常用】 |

### go list - 列出包

**基础用法**:
```bash
go list %{包}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 列出所有包 | `go list ./...` | 列出所有包 【常用】 |
| 列出依赖 | `go list -m all` | 列出所有模块依赖 【常用】 |
| 显示模块信息 | `go list -m %{模块名}%` | 显示模块详细信息 |
| 列出可执行文件 | `go list -f '{{.Target}}' ./...` | 列出编译目标路径 |

---

## PHP/Composer

### composer install - 安装依赖

**基础用法**:
```bash
composer install %{选项}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装依赖 | `composer install` | 根据 composer.lock 安装 【常用】 |
| 忽略平台要求 | `composer install --ignore-platform-reqs` | 忽略 PHP 扩展要求 【常用】 |
| 仅开发依赖 | `composer install --dev` | 只安装 require-dev 中的包 |
| 无自动加载 | `composer install --no-autoloader` | 不生成自动加载文件 |
| 无脚本 | `composer install --no-scripts` | 跳过 scripts 【常用】 |
| 优化自动加载 | `composer install --optimize-autoloader` | 生成类映射 【常用】 |
| 只更新 lock | `composer install --lock` | 只更新 lock 文件不安装 |
| 预览模式 | `composer install --dry-run` | 模拟安装不实际执行 【常用】 |

### composer require - 添加依赖

**基础用法**:
```bash
composer require %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 添加生产依赖 | `composer require %{包名}%` | 添加到 require 【常用】 |
| 添加开发依赖 | `composer require --dev %{包名}%` | 添加到 require-dev 【常用】 |
| 指定版本 | `composer require %{包名}%:%{版本}%` | 指定版本约束 【常用】 |
| 全局添加 | `composer global require %{包名}%` | 全局安装包 【常用】 |
| 更新现有包 | `composer require %{包名}%:%{版本}% --update-with-dependencies` | 更新并处理依赖 【常用】 |
| 无脚本 | `composer require --no-scripts %{包名}%` | 不执行 scripts |

### composer update - 更新依赖

**基础用法**:
```bash
composer update %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 更新所有依赖 | `composer update` | 按 semver 更新所有包 【常用】 |
| 更新特定包 | `composer update %{包名}%` | 只更新指定包 【常用】 |
| 更新到最新 | `composer update --with-all-dependencies %{包名}%` | 更新包及其依赖 【常用】 |
| 忽略平台要求 | `composer update --ignore-platform-reqs` | 忽略 PHP 扩展要求 |
| 稳定版本 | `composer update --prefer-stable` | 优先使用稳定版本 【常用】 |
| 预览更新 | `composer update --dry-run` | 模拟更新显示结果 【常用】 |
| 锁定到版本 | `composer update %{包名}% --lock` | 更新并锁定版本 |

### composer dump-autoload - 重新生成自动加载

**基础用法**:
```bash
composer dump-autoload %{选项}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 重新生成自动加载 | `composer dump-autoload` | 更新 autoload.php 【常用】 |
| 优化自动加载 | `composer dump-autoload -o` | 生成类映射文件 【常用】 |
| 忽略平台要求 | `composer dump-autoload --ignore-platform-reqs` | 生成时不检查平台要求 |
| 仅 ClassMap | `composer dump-autoload --classmap-authoritative` | 强制使用 ClassMap 【常用】 |
| 优化并预热 | `composer dump-autoload --optimize --apcu` | 使用 APCu 缓存 【常用】 |
| 显示自动加载映射 | `composer dump-autoload --print` | 打印自动加载配置 |

### composer remove - 移除依赖

**基础用法**:
```bash
composer remove %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 移除依赖 | `composer remove %{包名}%` | 卸载并从 composer.json 移除 【常用】 |
| 移除开发依赖 | `composer remove --dev %{包名}%` | 移除开发依赖 |
| 移除多个 | `composer remove %{包1}% %{包2}%` | 同时移除多个包 【常用】 |
| 移除并更新 | `composer remove --update-with-dependencies %{包名}%` | 移除并处理依赖关系 |

### composer show - 查看包信息

**基础用法**:
```bash
composer show %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看包信息 | `composer show %{包名}%` | 显示包详细信息 【常用】 |
| 列出所有包 | `composer show --all` | 列出所有已安装包 |
| 查看可用版本 | `composer show %{包名}% --available` | 显示所有可用版本 【常用】 |
| 列出过期包 | `composer show --outdated` | 显示有新版本的包 【常用】 |
| 查看依赖树 | `composer show --tree %{包名}%` | 显示依赖树 【常用】 |

---

## Ruby/Bundler

### bundle install - 安装依赖

**基础用法**:
```bash
bundle install %{选项}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装依赖 | `bundle install` | 根据 Gemfile.lock 安装 【常用】 |
| 跳过 Gemfile 更新 | `bundle install --deployment` | 使用预配置部署模式 【常用】 |
| 忽略已安装 | `bundle install --local` | 使用本地缓存不下载 |
| 并行安装 | `bundle install --jobs=%{数量}%` | 并行安装多个 gem 【常用】 |
| 清理未使用 | `bundle install --clean` | 安装后清理未使用的 gems |
| 跳过脚本 | `bundle install --without %{组名}%` | 跳过指定组的安装 【常用】 |
| 详细输出 | `bundle install --verbose` | 显示详细安装过程 |
| 预渲染 | `bundle install --retry %{次数}%` | 下载失败时重试 【常用】 |

### bundle exec - 在 Bundle 环境中执行

**基础用法**:
```bash
bundle exec %{命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 执行命令 | `bundle exec %{命令}%` | 在正确的 gem 环境中运行 【常用】 |
| 执行 Ruby | `bundle exec ruby %{脚本}%` | 运行 Ruby 脚本使用 bundle gem 【常用】 |
| 执行 Rake | `bundle exec rake %{任务}%` | 在 bundle 环境中运行 Rake 任务 【常用】 |
| 执行 IRB | `bundle exec irb` | 启动带有 bundle 上下文的 IRB 【常用】 |
| 执行 RSpec | `bundle exec rspec` | 运行 RSpec 测试 【常用】 |
| 执行 Rails | `bundle exec rails %{命令}%` | 在 bundle 环境中运行 Rails 【常用】 |
| 显示环境 | `bundle exec --keep-spec-dirs %{命令}%` | 保留 spec 目录 |

### bundle add - 添加 Gem

**基础用法**:
```bash
bundle add %{gem名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 添加 Gem | `bundle add %{gem名}%` | 添加到 Gemfile 【常用】 |
| 添加到组 | `bundle add %{gem名}% --group=%{组名}%` | 添加到指定组 【常用】 |
| 添加开发依赖 | `bundle add %{gem名}% --group=test --skip-install` | 添加到测试组不安装 |
| 指定版本 | `bundle add %{gem名}% --version="%{版本}"` | 指定版本约束 【常用】 |
| 跳过安装 | `bundle add %{gem名}% --skip-install` | 只添加不立即安装 【常用】 |
| 源指定 | `bundle add %{gem名}% --source=%{源}%` | 指定 gem 源 |

### bundle update - 更新 Gem

**基础用法**:
```bash
bundle update %{gem名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 更新所有 | `bundle update` | 更新所有 gems 到最新 【常用】 |
| 更新特定 gem | `bundle update %{gem名}%` | 只更新指定 gem 【常用】 |
| 更新并处理依赖 | `bundle update %{gem名}% --conservative` | 保守更新只升级必要的 【常用】 |
| 更新所有指定组 | `bundle update --group=%{组名}%` | 只更新指定组的 gems |
| 完整更新 | `bundle update --full-index` | 使用完整索引更新 【常用】 |
| 预渲染 | `bundle update --dry-run` | 模拟更新显示结果 【常用】 |

### bundle list - 列出已安装的 Gems

**基础用法**:
```bash
bundle list %{选项}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 列出所有 gems | `bundle list` | 显示已安装 gems 列表 【常用】 |
| 只列出名称 | `bundle list --only-explicit` | 只列出 Gemfile 中声明的 |
| 显示路径 | `bundle list --paths` | 显示每个 gem 的路径 【常用】 |

---

## Python/pip-tools

### pip install - 安装包

**基础用法**:
```bash
pip install %{包名}%
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装包 | `pip install %{包名}%` | 从 PyPI 安装 【常用】 |
| 指定版本 | `pip install %{包名}%==%{版本}%` | 指定版本 【常用】 |
| 从 requirements | `pip install -r %{requirements文件}%` | 从 requirements.txt 安装 【常用】 |
| 升级包 | `pip install --upgrade %{包名}%` | 升级到最新版本 【常用】 |
| 安装到用户目录 | `pip install --user %{包名}%` | 用户级安装 【常用】 |
| 忽略已安装 | `pip install --ignore-installed %{包名}%` | 忽略已安装的包 |
| 模拟安装 | `pip install --dry-run %{包名}%` | 模拟安装不实际执行 【常用】 |
| 从 URL 安装 | `pip install %{git_url}%` | 从 Git 安装 【常用】 |
| 卸载前先安装 | `pip install --force-reinstall %{包名}%` | 强制重新安装 【常用】 |

### pip freeze - 导出依赖

**基础用法**:
```bash
pip freeze %{选项}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 导出所有依赖 | `pip freeze` | 输出所有已安装包及版本 【常用】 |
| 导出到文件 | `pip freeze > requirements.txt` | 导出到 requirements.txt 【常用】 |
| 过滤本地包 | `pip freeze | grep -v "^#"` | 排除注释行 |
| 按环境过滤 | `pip freeze --all` | 包含所有包包括 pip/setuptools/wheel |
| 显示包信息 | `pip freeze | grep %{包名}%` | 查找特定包版本 |

### pip-compile - 编译依赖

**基础用法**:
```bash
pip-compile %{输入文件}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 编译依赖 | `pip-compile requirements.in` | 生成锁定的 requirements.txt 【常用】 |
| 指定输出 | `pip-compile requirements.in --output-file requirements.txt` | 指定输出文件 |
| 冻结版本 | `pip-compile --generate-hashes requirements.in` | 生成含 hash 的锁定文件 【常用】 |
| 使用源码包 | `pip-compile --allow-unsafe requirements.in` | 允许安装源码包 |
| 预渲染 | `pip-compile --dry-run requirements.in` | 模拟编译不生成文件 |
| 指定 Python 版本 | `pip-compile --python-version=%{版本}% requirements.in` | 为特定 Python 版本编译 【常用】 |
| 合并多个输入 | `pip-compile requirements.in dev-requirements.in` | 合并多个输入文件 |
| 添加注释 | `pip-compile --annotate requirements.in` | 在输出中添加注释 【常用】 |
| 禁止升级 | `pip-compile --no-upgrade requirements.in` | 禁止升级已有包 |

### pip-sync - 同步环境

**基础用法**:
```bash
pip-sync %{文件}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 同步环境 | `pip-sync requirements.txt` | 确保环境与锁文件完全一致 【常用】 |
| 删除未使用 | `pip-sync requirements.txt --pip-args="--some-flag"` | 同步并传递额外参数 |
| 详细模式 | `pip-sync --verbose requirements.txt` | 显示详细同步信息 【常用】 |
| 预览模式 | `pip-sync --dry-run requirements.txt` | 预览要做的更改 【常用】 |
| 强制安装 | `pip-sync requirements.txt --force` | 强制安装所有包 |
| 同步多个文件 | `pip-sync requirements.txt dev-requirements.txt` | 同步多个 requirements 文件 【常用】 |

---

## Unity/.NET (NuGet)

### dotnet add package - 添加 NuGet 包

**基础用法**:
```bash
dotnet add package %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 添加包 | `dotnet add package %{包名}%` | 添加到项目 【常用】 |
| 指定版本 | `dotnet add package %{包名}% --version %{版本}%` | 指定版本 【常用】 |
| 添加到指定项目 | `dotnet add %{项目路径}% package %{包名}%` | 为特定项目添加 【常用】 |
| 添加预览版 | `dotnet add package %{包名}% --prerelease` | 添加预发布版本 【常用】 |
| 源指定 | `dotnet add package %{包名}% --source %{源}%` | 从特定源添加 【常用】 |
| 添加框架特定 | `dotnet add package %{包名}% -f %{框架}%` | 针对特定框架添加 |

### dotnet remove package - 移除 NuGet 包

**基础用法**:
```bash
dotnet remove package %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 移除包 | `dotnet remove package %{包名}%` | 从 csproj 中移除 【常用】 |
| 移除指定项目 | `dotnet remove %{项目路径}% package %{包名}%` | 从特定项目移除 |

### nuget install - 安装包

**基础用法**:
```bash
nuget install %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装包 | `nuget install %{包名}%` | 下载并解压到当前目录 【常用】 |
| 指定版本 | `nuget install %{包名}% -Version %{版本}%` | 指定版本 【常用】 |
| 指定输出目录 | `nuget install %{包名}% -OutputDirectory %{目录}%` | 指定安装目录 【常用】 |
| 排除依赖 | `nuget install %{包名}% -ExcludeVersion` | 不创建版本子目录 |
| 安装到工具 | `nuget install %{工具名}% -Global` | 全局安装工具 |

### nuget restore - 还原包

**基础用法**:
```bash
nuget restore %{解决方案}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 还原解决方案 | `nuget restore %{解决方案文件}%` | 还原所有项目依赖 【常用】 |
| 指定包源 | `nuget restore -Source %{源}%` | 指定 NuGet 源 【常用】 |
| 包含跳过失败 | `nuget restore -PackagesDirectory %{目录}%` | 指定包缓存目录 |
| 禁用并行 | `nuget restore -DisableParallelProcessing` | 禁用并行下载 |
| 强制还原 | `nuget restore -Force` | 强制重新下载所有包 |
| 详细输出 | `nuget restore -Verbosity detailed` | 显示详细还原信息 【常用】 |

### nuget pack - 打包

**基础用法**:
```bash
nuget pack %{nuspec文件}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 打包 | `nuget pack %{nuspec文件}%` | 从 nuspec 创建 nupkg 【常用】 |
| 包含依赖项目 | `nuget pack -IncludeReferencedProjects` | 包含引用的项目 |
| 替换符号 | `nuget pack -symbols` | 同时创建符号包 【常用】 |
| 指定版本 | `nuget pack -Version %{版本}%` | 覆盖版本号 【常用】 |
| 基目录 | `nuget pack -BasePath %{目录}%` | 指定基目录 |

### nuget push - 发布包

**基础用法**:
```bash
nuget push %{nupkg文件}% -Source %{源}% -ApiKey %{密钥}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 发布到官方源 | `nuget push %{包文件}%` | 上传到 nuget.org 【常用】 |
| 指定源发布 | `nuget push %{包文件}% -Source %{URL}%` | 发布到私有源 【常用】 |
| 指定 API 密钥 | `nuget push %{包文件}% -ApiKey %{密钥}%` | 提供发布认证 【常用】 |
| 跳过重复 | `nuget push %{包文件}% -SkipDuplicate` | 跳过已存在的包 |
| 不等待 | `nuget push %{包文件}% -NonInteractive` | 非交互模式快速推送 |

### dotnet restore / dotnet build / dotnet run - 完整流程

**基础用法**:
```bash
dotnet restore %{项目}%
dotnet build %{项目}%
dotnet run %{项目}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 还原依赖 | `dotnet restore` | 还原项目依赖 【常用】 |
| 发布构建 | `dotnet build --configuration Release` | 发布模式编译 【常用】 |
| 发布应用 | `dotnet publish --configuration Release --output %{输出}%` | 发布可部署应用 【常用】 |
| 运行项目 | `dotnet run` | 编译并运行 【常用】 |
| 打包发布 | `dotnet pack` | 创建 NuGet 包 【常用】 |

---

## 各语言包管理器对比

| 功能 | Cargo (Rust) | go mod (Go) | composer (PHP) | bundle (Ruby) | pip-tools (Python) | dotnet/nuget (.NET) |
|------|------|------|------|------|------|------|
| 初始化 | `cargo new` | `go mod init` | `composer init` | `bundle init` | — (手动创建) | `dotnet new` |
| 安装依赖 | `cargo build` | `go mod download` | `composer install` | `bundle install` | `pip install` | `dotnet restore` |
| 添加依赖 | `cargo add` | `go get` | `composer require` | `bundle add` | 直接编辑 | `dotnet add package` |
| 移除依赖 | `cargo remove` | `go mod rm` | `composer remove` | `bundle remove` | `pip uninstall` | `dotnet remove package` |
| 更新依赖 | `cargo update` | `go get -u` | `composer update` | `bundle update` | `pip-compile` | `dotnet restore` |
| 锁定文件 | Cargo.lock | go.sum | composer.lock | Gemfile.lock | requirements.txt | packages.lock.json |
| 生成锁文件 | 自动 | `go mod tidy` | `composer install` | `bundle install` | `pip-compile` | `dotnet restore` |
| 包注册处 | crates.io | proxy.golang.org | packagist.org | rubygems.org | PyPI | nuget.org |

---

## 相关资源

- [快速开始指南](../quick-start.md)
- [前端包管理器文档](../前端包管理器/README.md)
- [Git 命令文档](../Git 命令/README.md)
- [完整命令参考表](../../references/commands-reference.md)