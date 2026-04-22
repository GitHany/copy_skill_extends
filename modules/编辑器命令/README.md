# 编辑器命令文档

开发编辑器与 IDE 完整参考文档，涵盖 Vim/Neovim、VSCode CLI、JetBrains、终端工具及代码质量工具。

## 目录

- [Vim/Neovim](#vimneovim)
  - [导航命令](#导航命令)
  - [编辑命令](#编辑命令)
  - [搜索命令](#搜索命令)
  - [缓冲区与文件](#缓冲区与文件)
  - [Neovim 特有功能](#neovim-特有功能)
  - [Vim 插件管理](#vim-插件管理)
- [VSCode CLI](#vscode-cli)
- [JetBrains](#jetbrains)
- [终端工具](#终端工具)
- [代码质量工具](#代码质量工具)

---

## Vim/Neovim

### 导航命令

#### 基础光标移动

| 场景 | 命令 | 说明 |
|------|------|------|
| 左下上右移动 | `h j k l` | h=左，j=下，k=上，l=右 |
| 跳到行首 | `0` | 跳到当前行第一个字符 |
| 跳到行尾 | `$` | 跳到当前行最后一个字符 |
| 跳到文件开头 | `gg` | 跳到文件第一行 |
| 跳到文件结尾 | `G` | 跳到文件最后一行 |
| 跳到指定行 | `:{行号}` | 跳到指定行号 (例: `:50` 跳到第50行) |
| 跳到行首非空字符 | `^` | 跳到当前行第一个非空字符 |
| 跳到下一个词首 | `w` | forward word，光标跳到下一词首 |
| 跳到上一词首 | `b` | backward word，光标跳到上一词首 |
| 跳到当前词尾 | `e` | end of word，跳到当前词尾 |
| 跳到下一个词尾 | `ge` | 跳到上一词尾 |
| 跳到上一个句子首 | `(` | 跳到上一个句子开头 |
| 跳到下一个句子首 | `)` | 跳到下一个句子开头 |
| 屏幕首行 | `H` | Head of screen |
| 屏幕中行 | `M` | Middle of screen |
| 屏幕末行 | `L` | Last of screen |
| 向下滚动半屏 | `Ctrl+d` | 向下滚动半屏 |
| 向上滚动半屏 | `Ctrl+u` | 向上滚动半屏 |
| 向下滚动整屏 | `Ctrl+f` | Forward，向下翻一屏 |
| 向上滚动整屏 | `Ctrl+b` | Backward，向上翻一屏 |
| 跳到匹配的括号 | `%` | 跳到配对的括号处 |
| 返回上一个位置 | `Ctrl+o` | 在跳转历史中后退 |
| 前进到下一个位置 | `Ctrl+i` | 在跳转历史中前进 |

### 编辑命令

#### 基础编辑

| 场景 | 命令 | 说明 |
|------|------|------|
| 进入插入模式 | `i` | 在光标前插入 |
| 在行首插入 | `I` | 在当前行第一个非空字符前插入 |
| 在光标后插入 | `a` | append，在光标后插入 |
| 在行尾插入 | `A` | 在当前行最后一个字符后插入 |
| 在下行插入 | `o` | 在当前行下方新建一行 |
| 在上行插入 | `O` | 在当前行上方新建一行 |
| 删除当前行 | `dd` | 删除整行 |
| 删除 N 行 | `{N}dd` | 删除 N 行 (例: `3dd` 删除3行) |
| 删除当前字符 | `x` | 删除光标下的字符 |
| 删除前一个字符 | `X` | 删除光标前一个字符 |
| 复制当前行 | `yy` | yank，复制整行 |
| 复制 N 行 | `{N}yy` | 复制 N 行 (例: `3yy` 复制3行) |
| 复制当前单词 | `yiw` | 复制光标下的单词 |
| 粘贴 | `p` | 在光标后/下方粘贴 |
| 在光标前粘贴 | `P` | 在光标前/上方粘贴 |
| 撤销 | `u` | undo，撤销上一次操作 |
| 重做 | `Ctrl+r` | redo，重做已撤销的操作 |
| 重复上次命令 | `.` | 重复最近的修改操作 |
| 替换当前字符 | `r` | 替换光标下的单个字符后退出 |
| 进入替换模式 | `R` | 进入替换模式，连续替换 |
| 合并下一行 | `J` | 将下一行合并到当前行尾 |
| 大小写翻转 | `~` | 翻转光标下字符的大小写 |
| 转为大写 | `gUU` | 将当前行转为大写 |
| 转为小写 | `guu` | 将当前行转为小写 |
| 进入可视模式 | `v` | 字符级选择 |
| 进入行可视模式 | `V` | 行级选择 |
| 进入块可视模式 | `Ctrl+v` | 块级选择 |
| 删除选中内容 | `d` | 在可视模式下删除选中 |
| 复制选中内容 | `y` | 在可视模式下复制选中 |
| 缩进 | `>` | 在可视模式下缩进选中行 |
| 取消缩进 | `<` | 在可视模式下取消缩进 |
| 交换两行 | `ddp` | 删除当前行并粘贴到下一行 |
| 从光标处剪切到行尾 | `C` | Change，删除到行尾并进入插入模式 |
| 删除到行尾 | `D` | Delete，删除到行尾 |

### 搜索命令

#### 搜索与替换

| 场景 | 命令 | 说明 |
|------|------|------|
| 向前搜索 | `/` | 向下搜索指定字符串 |
| 向后搜索 | `?` | 向上搜索指定字符串 |
| 跳到下一个匹配 | `n` | next，跳到下一个搜索结果 |
| 跳到上一个匹配 | `N` | 跳到上一个搜索结果 |
| 搜索当前单词 | `*` | 向下搜索光标下的单词 |
| 向上搜索当前单词 | `#` | 向上搜索光标下的单词 |
| 替换当前行 | `:s/%{旧字符串}%/%{新字符串}%/` | 替换当前行第一个匹配 |
| 替换当前行所有 | `:s/%{旧字符串}%/%{新字符串}%/g` | 替换当前行所有匹配 |
| 替换所有行 | `:%s/%{旧字符串}%/%{新字符串}%/g` | 替换文件中所有匹配 |
| 替换所有行逐个确认 | `:%s/%{旧字符串}%/%{新字符串}%/gc` | g=全局，c=确认每个 |
| 搜索忽略大小写 | `/\c%{字符串}%` | \c 使搜索不区分大小写 |
| 高亮搜索结果 | `:set hlsearch` | 开启搜索高亮 |
| 清除搜索高亮 | `:nohlsearch` | 暂时清除搜索高亮 |

### 缓冲区与文件

#### 文件操作

| 场景 | 命令 | 说明 |
|------|------|------|
| 保存 | `:w` | write，保存当前文件 |
| 另存为 | `:w %{文件名}%` | 另存为指定文件名 |
| 退出 | `:q` | quit，退出当前窗口（未保存会失败） |
| 保存并退出 | `:wq` 或 `ZZ` | 保存并退出 |
| 强制退出 | `:q!` | 放弃修改并退出 |
| 强制保存 | `:w!` | 强制保存只读文件 |
| 打开文件 | `:e %{文件名}%` | edit，打开指定文件 |
| 新建缓冲区 | `:ene` | 新建空缓冲区 |
| 重新加载文件 | `:e!` | 放弃修改重新加载 |
| 浏览文件 | `:Explore` 或 `:E` | 打开文件浏览器 |

#### 缓冲区操作

| 场景 | 命令 | 说明 |
|------|------|------|
| 列出缓冲区 | `:ls` 或 `:buffers` | 显示所有缓冲区列表 |
| 切换到上一个缓冲区 | `:b#` 或 `Ctrl+^` | 切换到上一个缓冲区 |
| 切换到指定缓冲区 | `:b %{编号或名称}%` | 按编号或名称切换 (例: `:b2`, `:b main.js`) |
| 下一个缓冲区 | `:bn` | next buffer |
| 上一个缓冲区 | `:bp` | previous buffer |
| 删除缓冲区 | `:bd %{编号}%` | buffer delete，关闭指定缓冲区 |
| 在新标签页打开 | `:tabnew %{文件名}%` | 新建标签页 |
| 切换到下一标签 | `gt` | go to next tab |
| 切换到上一标签 | `gT` | go to previous tab |
| 关闭当前标签 | `:tabc` | tab close |
| 水平分屏 | `:sp %{文件名}%` | split，打开文件（省略文件名则当前文件） |
| 垂直分屏 | `:vsp %{文件名}%` | vertical split |
| 切换分屏 | `Ctrl+w h/j/k/l` | 切换到左/下/上/右的窗口 |
| 关闭当前分屏 | `Ctrl+w c` | close，关闭当前窗口 |
| 等分所有窗口 | `Ctrl+w =` | 等宽等高排列所有窗口 |
| 最大化当前窗口 | `Ctrl+w _` | 下划线，最大化高度 |
| 最大化宽度 | `Ctrl+w \|` | 竖线，最大化宽度 |

### Neovim 特有功能

#### Neovim 启动与配置

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动 Neovim | `nvim %{文件名}%` | 启动 Neovim 编辑器 |
| 启动 Neovim 极简模式 | `nvim --clean %{文件名}%` | 不加载任何插件/配置 |
| 启动 Neovim 只读模式 | `nvim -R %{文件名}%` | 只读模式打开 |
| 打开上次会话 | `nvim --restore` | 恢复上次会话 |
| 显示 Neovim 版本 | `nvim --version` | 显示版本信息 |

#### Neovim 内置 LSP

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看 LSP 客户端 | `:LspInfo` | 显示已连接的 LSP 客户端 |
| 列出诊断 | `:Diagnostics` | 显示所有诊断信息 |
| 当前文件诊断 | `:Diagnostics!` | 在消息区显示当前文件诊断 |
| 跳到上一个诊断 | `]d` | 跳到上一个诊断位置 |
| 跳到下一个诊断 | `[d` | 跳到下一个诊断位置 |
| 查看函数定义 | `gd` | go to definition |
| 查看函数引用 | `gD` | go to declaration |
| 显示悬停信息 | `K` | 在正常模式下显示符号信息 |
| 重命名符号 | `<leader>rn` | rename，重命名光标处的符号 |
| 代码操作 | `<leader>a` | 显示代码操作（可配合 LSP） |

#### Neovim 内置 Treesitter

| 场景 | 命令 | 说明 |
|------|------|------|
| 增量选择 | `n` / `N` | 在 Treesitter 增量选择中扩大/缩小选区 |
|  Treesitter 增强 | 需要 treesitter 插件 | 提供更好的语法高亮和增量选择 |

#### Mason 包管理器

| 场景 | 命令 | 说明 |
|------|------|------|
| 打开 Mason | `:Mason` | 打开 Mason UI 界面 |
| 安装 LSP 服务器 | `:MasonInstall %{lsp_server}%` | 安装指定 LSP 服务器 (例: `:MasonInstall pyright`) |
| 卸载 LSP 服务器 | `:MasonUninstall %{lsp_server}%` | 卸载指定 LSP 服务器 |
| 更新所有包 | `:MasonUpdate` | 更新所有已安装的包 |
| 查看可用包 | `:MasonInstallInfo` | 查看 Mason 包信息 |

### Vim 插件管理

#### vim-plug

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装插件 | `:PlugInstall` | 安装在 init.vim 中定义的插件 |
| 更新插件 | `:PlugUpdate` | 更新所有插件 |
| 更新单个插件 | `:PlugUpdate %{插件名}%` | 更新指定插件 |
| 删除插件 | `:PlugClean` | 清理已删除的插件（需先从配置中移除） |
| 查看插件状态 | `:PlugStatus` | 查看各插件的加载状态 |
| 升级 vim-plug 本身 | `:PlugUpgrade` | 升级 vim-plug 管理器 |

#### dein

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装插件 | `:call dein#install()` | 安装配置中的所有插件 |
| 更新插件 | `:call dein#update()` | 更新所有已安装插件 |
| 更新单个插件 | `:call dein#update('%{插件名}%')` | 更新指定插件 |
| 检查状态 | `:call dein#check_files()` | 检查缺失的插件文件 |
| 清理未使用插件 | `:call dein#recache_runtimepath()` | 清除缓存并重新生成 |
| 查看已加载插件 | `:call dein#types#display()` | 显示插件加载状态 |

#### packer (Neovim)

| 场景 | 命令 | 说明 |
|------|------|------|
| 同步插件 | `:PackerSync` | 安装/更新所有插件（推荐） |
| 安装插件 | `:PackerInstall` | 安装插件 |
| 更新插件 | `:PackerUpdate` | 更新插件 |
| 清理未使用插件 | `:PackerClean` | 清理已删除的插件 |
| 编译/生成 loader | `:PackerCompile` | 重新编译插件配置 |
| 状态查看 | `:PackerStatus` | 查看插件加载状态 |
| Profile 查看 | `:PackerProfile` | 查看插件加载性能分析 |

---

## VSCode CLI

### VSCode 命令行工具

| 场景 | 命令 | 说明 |
|------|------|------|
| 在当前目录打开 | `code .` | 用 VSCode 打开当前目录 |
| 打开指定文件 | `code %{文件名}%` | 用 VSCode 打开指定文件 |
| 新窗口打开 | `code --new-window %{路径}%` | 强制在新窗口中打开 |
| 复用现有窗口 | `code --reuse-window %{路径}%` | 在已打开的窗口中打开 |
| 只打开窗口不加载文件夹 | `code --empty` | 打开空白的 VSCode 窗口 |
| 打开文件并跳转到行 | `code --goto %{文件}%:%{行}%:%{列}%` | 跳转到指定位置 (例: `code --goto app.js:10:5`) |
| 比较两个文件 | `code --diff %{文件1}% %{文件2}%` | 打开 diff 视图比较两文件 |
| 打开远程文件 | `code --remote %{remote}% %{路径}%` | 通过 SSH Remote 打开远程文件 |
| 显示版本 | `code --version` | 显示 VSCode 版本号 |
| 显示帮助 | `code --help` | 显示命令行帮助 |

### VSCode 扩展管理

| 场景 | 命令 | 说明 |
|------|------|------|
| 列出已安装扩展 | `code --list-extensions` | 列出所有已安装的扩展 |
| 安装扩展 | `code --install-extension %{扩展ID或路径}%` | 安装指定扩展 (例: `code --install-extension ms-python.python`) |
| 卸载扩展 | `code --uninstall-extension %{扩展ID}%` | 卸载指定扩展 |
| 禁用扩展 | `code --disable-extension %{扩展ID}%` | 禁用指定扩展 |
| 启用扩展 | `code --enable-proposed-accessibility %{扩展ID}%` | 启用扩展的建议功能 |

### VSCode 设置与功能

| 场景 | 命令 | 说明 |
|------|------|------|
| 打开设置 | `code --open-settings` | 打开设置界面 |
| 导出设置 | `code --export-default-settings %{路径}%` | 导出默认设置到指定路径 |
| 以安全模式启动 | `code --safe-mode %{路径}%` | 禁用所有扩展启动 |
| 以无扩展模式启动 | `code --disable-extensions %{路径}%` | 禁用所有扩展启动 |
| 打开用户数据文件夹 | `code --open-external %{URL}%` | 用外部程序打开 URL |
| 开启隐藏功能 | `code --enable-proposed-feature %{featureId}%` | 开启隐藏功能 |

---

## JetBrains

### JetBrains CLI 工具

| 场景 | 命令 | 说明 |
|------|------|------|
| 用 IntelliJ IDEA 打开 | `idea %{目录或文件}%` | 用 IDEA 打开指定目录或文件 |
| 用 PyCharm 打开 | `pycharm %{目录或文件}%` | 用 PyCharm 打开 Python 项目 |
| 用 WebStorm 打开 | `webstorm %{目录或文件}%` | 用 WebStorm 打开前端项目 |
| 用 GoLand 打开 | `goland %{目录或文件}%` | 用 GoLand 打开 Go 项目 |
| 用 CLion 打开 | `clion %{目录或文件}%` | 用 CLion 打开 C/C++ 项目 |
| 用 Rider 打开 | `rider %{目录或文件}%` | 用 Rider 打开 .NET 项目 |
| 用 DataGrip 打开 | `datagrip %{数据库连接}%` | 用 DataGrip 打开数据库连接 |
| 用 Android Studio 打开 | `studio %{目录或文件}%` | 用 Android Studio 打开 Android 项目 |
| 用 RubyMine 打开 | `rubymine %{目录或文件}%` | 用 RubyMine 打开 Ruby 项目 |
| 用 PhpStorm 打开 | `phpstorm %{目录或文件}%` | 用 PhpStorm 打开 PHP 项目 |

### Toolbox 命令

| 场景 | 命令 | 说明 |
|------|------|------|
| 打开 Toolbox | `toolbox` | 启动 JetBrains Toolbox 管理器 |
| 用 Toolbox 打开项目 | `toolbox exec idea %{路径}%` | 通过 Toolbox 启动指定 IDE |
| 列出已安装 IDE | `toolbox list` | 列出 Toolbox 中已安装的所有 IDE |
| 更新 Toolbox | `toolbox update` | 检查并安装 Toolbox 更新 |
| 查看 Toolbox 日志 | `toolbox log` | 打开 Toolbox 日志目录 |
| 启动指定 IDE 版本 | `toolbox exec --version %{版本}% %{IDE}% %{路径}%` | 启动特定版本的 IDE |

### 项目创建 (IDEA)

| 场景 | 命令 | 说明 |
|------|------|------|
| 从命令行创建项目 | `idea create-project --name %{项目名}% --template %{模板}% --path %{路径}%` | 通过命令行创建项目 |
| 打开项目向导 | `idea project` | 打开项目创建向导 |

---

## 终端工具

### tmux 会话管理

| 场景 | 命令 | 说明 |
|------|------|------|
| 新建会话 | `tmux new -s %{会话名}%` | 创建名为 %{会话名}% 的新会话 |
| 列出所有会话 | `tmux ls` 或 `tmux list-sessions` | 显示所有 tmux 会话 |
| 附加到会话 | `tmux attach -t %{会话名}%` | 附加到指定会话 |
| 分离当前会话 | `Ctrl+b d` | 从当前会话分离（后台运行） |
| 关闭会话 | `tmux kill-session -t %{会话名}%` | 关闭指定会话 |
| 重命名会话 | `tmux rename-session -t %{旧名}% %{新名}%` | 重命名会话 |
| 发送命令到会话 | `tmux send-keys -t %{会话名}% "%{命令}%" C-m` | 在指定会话中执行命令 |

### tmux 窗口与面板

| 场景 | 命令 | 说明 |
|------|------|------|
| 水平分屏 | `Ctrl+b "` | 在当前窗口中水平分割 |
| 垂直分屏 | `Ctrl+b %` | 在当前窗口中垂直分割 |
| 切换面板 | `Ctrl+b 方向键` | 在面板之间切换 |
| 切换到上一个面板 | `Ctrl+b ;` | 切换到最近使用的面板 |
| 最大化/还原面板 | `Ctrl+b z` | toggle panel zoom |
| 关闭当前面板 | `Ctrl+b x` | 关闭当前面板 |
| 新建窗口 | `Ctrl+b c` | create，在当前会话中创建新窗口 |
| 切换窗口 | `Ctrl+b 数字` | 切换到指定编号的窗口 |
| 下一窗口 | `Ctrl+b n` | next window |
| 上一窗口 | `Ctrl+b p` | previous window |
| 重命名窗口 | `Ctrl+b ,` | 重命名当前窗口 |

### zsh 与 bash 配置

| 场景 | 命令 | 说明 |
|------|------|------|
| 编辑 zsh 配置 | `nano ~/.zshrc` 或 `vim ~/.zshrc` | 打开 zsh 配置文件 |
| 编辑 bash 配置 | `nano ~/.bashrc` 或 `vim ~/.bashrc` | 打开 bash 配置文件 |
| 生效配置（zsh） | `source ~/.zshrc` | 重新加载 zsh 配置 |
| 生效配置（bash） | `source ~/.bashrc` | 重新加载 bash 配置 |
| 编辑全局 zsh 配置 | `sudo nano /etc/zshrc` | 编辑全局 zsh 配置 |
| 查看所有别名 | `alias` | 列出所有已定义的别名 |
| 定义临时别名 | `alias %{名称}%="%{命令}%"` | 定义仅当前会话有效的别名 |
| 永久保存别名 | `echo "alias %{名称}%='%{命令}%'" >> ~/.zshrc` | 将别名写入配置文件 |
| 设置环境变量 | `export %{变量名}%="%{值}%"` | 设置环境变量（当前会话） |
| 永久设置环境变量 | `echo 'export %{变量名}%="%{值}%"' >> ~/.zshrc` | 永久保存环境变量 |
| 查看所有环境变量 | `env` 或 `printenv` | 列出所有环境变量 |
| 查看特定变量 | `echo $%{变量名}%` | 查看指定环境变量的值 |

### fzf 模糊搜索

| 场景 | 命令 | 说明 |
|------|------|------|
| 模糊查找文件 | `fzf` | 在当前目录中模糊搜索文件 |
| 查找所有文件含内容 | `fzf --preview 'cat {}'` | 带预览的模糊搜索 |
| 在文件内容中搜索 | `fzf --preview 'rg -N --color=always {}'` | 在文件内容中模糊搜索 |
| 组合使用（查找文件） | `find . -type f \| fzf` | 用 fzf 从 find 结果中筛选 |
| 组合使用（搜索历史） | `history \| fzf` | 从命令历史中模糊搜索 |
| 杀掉进程 | `ps aux \| fzf \| awk '{print $2}' \| xargs kill` | 用 fzf 搜索并杀掉进程 |
| 切换 git 分支 | `git branch \| fzf \| xargs git checkout` | 用 fzf 切换分支 |
| 在 tmux 中使用 | `Ctrl+t` | 在 tmux 配置中快速呼出 fzf |

### ripgrep 搜索

| 场景 | 命令 | 说明 |
|------|------|------|
| 递归搜索内容 | `rg "%{内容}%"` | 在当前目录递归搜索 (例: `rg "TODO"`) |
| 搜索指定文件类型 | `rg -t %{类型}% "%{内容}%"` | 只在指定类型文件中搜索 (例: `-t js`) |
| 搜索忽略大小写 | `rg -i "%{内容}%"` | 忽略大小写搜索 |
| 显示行号 | `rg -n "%{内容}%"` | 显示匹配行的行号 |
| 只显示文件名 | `rg -l "%{内容}%"` | 只显示包含匹配的文件名 |
| 显示匹配数量 | `rg -c "%{内容}%"` | 显示每个文件的匹配数量 |
| 显示匹配上下文 | `rg -C %{行数}% "%{内容}%"` | 显示匹配行及其上下文 (例: `-C 3`) |
| 排除目录搜索 | `rg "%{内容}%" --ignore-case -g "!node_modules"` | 排除指定目录 |
| 正则表达式搜索 | `rg -e "%{正则}%"` | 使用正则表达式 (例: `rg -e "error\d+"`) |
| 显示匹配统计 | `rg --stats "%{内容}%"` | 显示搜索统计信息 |
| 仅显示匹配部分 | `rg -o "%{内容}%"` | 只显示匹配的部分（高亮） |
| 搜索整个单词 | `rg -w "%{单词}%"` | 只匹配完整单词 |
| 搜索空行 | `rg -e "^$"` | 搜索空行 |
| 排除特定文件 | `rg "%{内容}%" --ignore-file .rgignore` | 使用忽略文件 |

---

## 代码质量工具

### ESLint CLI

| 场景 | 命令 | 说明 |
|------|------|------|
| 检查所有文件 | `npx eslint .` | 检查当前目录所有文件 |
| 检查指定文件 | `npx eslint %{文件名}%` | 检查指定文件 (例: `npx eslint src/app.js`) |
| 自动修复 | `npx eslint --fix .` | 自动修复可修复的问题 |
| 修复并输出 | `npx eslint --fix-dry-run .` | 预览修复但不实际修改 |
| 指定配置文件 | `npx eslint --config %{配置文件}% .` | 使用指定配置文件 (例: `.eslintrc.js`) |
| 指定规则 | `npx eslint --rule '{"quotes": ["error", "single"]}' .` | 指定 ESLint 规则 |
| 忽略文件检查 | `npx eslint --ignore-path .eslintignore .` | 指定忽略文件 |
| 输出格式化报告 | `npx eslint -f json .` | 输出 JSON 格式报告 |
| 输出 HTML 报告 | `npx eslint -f html -o report.html .` | 输出 HTML 格式报告 |
| 缓存检查结果 | `npx eslint --cache .` | 启用缓存，只检查变更文件 |
| 安静模式（只显示错误） | `npx eslint --quiet .` | 只显示错误，忽略警告 |
| 最大警告数 | `npx eslint --max-warnings %{数量}% .` | 超过警告数则返回非零退出码 |
| 指定解析器 | `npx eslint --parser-options=ecmaVersion:2020 .` | 指定 ECMAScript 版本 |

### Prettier CLI

| 场景 | 命令 | 说明 |
|------|------|------|
| 格式化所有文件 | `npx prettier --write .` | 格式化当前目录所有文件 |
| 格式化指定文件 | `npx prettier --write %{文件名}%` | 格式化指定文件 (例: `npx prettier --write src/app.js`) |
| 检查格式（不修改） | `npx prettier --check .` | 检查格式是否正确，不修改文件 |
| 指定配置文件 | `npx prettier --config %{配置文件}% .` | 使用指定配置 (例: `.prettierrc`) |
| 指定文件类型 | `npx prettier --write "**/*.{js,jsx,ts,tsx}"` | 只格式化指定类型的文件 |
| 忽略某些文件 | `npx prettier --write --ignore-path .prettierignore .` | 使用忽略文件 |
| 设置缩进宽度 | `npx prettier --write --tab-width 2 .` | 设置缩进为 2 个空格 |
| 设置分号 | `npx prettier --write --no-semi .` | 不在语句末尾添加分号 |
| 设置引号风格 | `npx prettier --write --single-quote .` | 使用单引号 |
| 设置最大行宽 | `npx prettier --write --print-width 100 .` | 设置最大行宽为 100 |
| 设置尾随逗号 | `npx prettier --write --trailing-comma all .` | 在所有可能位置添加尾随逗号 |
| 集成 Git Hook | `npx pretty-quick --staged` | 作为 pre-commit hook 使用 |

### pre-commit 钩子

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装 pre-commit | `pip install pre-commit` 或 `conda install -c conda-forge pre-commit` | 安装 pre-commit 工具 |
| 创建配置文件 | `touch .pre-commit-config.yaml` | 创建 pre-commit 配置文件 |
| 安装 Git 钩子 | `pre-commit install` | 在当前仓库安装 pre-commit 钩子 |
| 安装 Git 钩子（Git Hooks） | `pre-commit install --hook-type pre-commit` | 指定钩子类型 |
| 安装 commit-msg 钩子 | `pre-commit install --hook-type commit-msg` | 安装提交信息检查钩子 |
| 手动运行所有钩子 | `pre-commit run --all-files` | 在所有文件上运行所有钩子 |
| 手动运行指定钩子 | `pre-commit run %{钩子名}%` | 运行指定名称的钩子 (例: `pre-commit run trailing-whitespace`) |
| 更新钩子版本 | `pre-commit autoupdate` | 更新配置文件中引用的仓库版本 |
| 卸载 Git 钩子 | `pre-commit uninstall` | 从当前仓库移除 pre-commit 钩子 |
| 列出所有可用钩子 | `pre-commit list` | 列出当前配置中的所有钩子 |
| 跳过特定钩子 | `git commit --no-verify -m "%{消息}%"` | 跳过 pre-commit 钩子 |
| 清除缓存 | `pre-commit clean` | 清除 pre-commit 缓存 |
| 验证配置文件 | `pre-commit validate-config %{配置文件}%` | 验证配置文件格式 |

### EditorConfig

| 场景 | 命令 | 说明 |
|------|------|------|
| EditorConfig 根属性 | 在 .editorconfig 中添加 `root = true` | 标记为根配置，停止向上查找 |
| 缩进样式 | `indent_style = space \| tab` | 设置缩进方式 |
| 缩进大小 | `indent_size = %{数字}%` | 设置缩进宽度 (例: `indent_size = 4`) |
| 行尾符 | `end_of_line = lf \| cr \| crlf` | 设置行尾符 |
| 字符集 | `charset = utf-8 \| utf-8-bom \| latin1` | 设置文件字符集 |
| 尾部空白 | `trim_trailing_whitespace = true` | 去除行尾空白 |
| 文件结尾空行 | `insert_final_newline = true` | 确保文件以空行结尾 |
| 针对特定文件覆盖 | `[{*.js,*.json}]` 在 .editorconfig 中 | 为特定文件类型设置规则 |
| 排除文件 | `排除 = *.md` | 排除匹配的文件 |

---

## 实用场景示例

### 场景 1: 使用 Neovim + LSP 开发 Python

```bash
# 1. 安装 Neovim
# Ubuntu: sudo apt install neovim
# macOS: brew install neovim

# 2. 配置 LSP (以 pyright 为例)
nvim
# 在 Neovim 中执行:
# :MasonInstall pyright

# 3. 配置 Python 虚拟环境
python3 -m venv .venv
source .venv/bin/activate

# 4. 使用 LSP 功能
# K - 查看函数文档
# gd - 跳转到定义
# Ctrl+o - 返回上一个位置
```

### 场景 2: VSCode 远程开发

```bash
# 1. 在远程服务器上安装 VSCode Server
code --install-extension ms-vscode-remote.remote-ssh

# 2. 从本地连接
code --remote ssh-remote %{用户名}%@%{主机}% %{路径}%

# 3. 安装扩展到远程
code --install-extension ms-python.python --remote ssh-remote %{主机}%
```

### 场景 3: tmux 日常开发工作流

```bash
# 1. 创建开发会话
tmux new -s dev

# 2. 在会话中分屏
# Ctrl+b "  水平分屏
# Ctrl+b %  垂直分屏

# 3. 在一个面板运行服务器
# 在另一个面板编辑代码

# 4. 分离会话
# Ctrl+b d

# 5. 稍后恢复
tmux attach -t dev
```

### 场景 4: ESLint + Prettier 集成

```bash
# 1. 安装依赖
npm install --save-dev eslint prettier eslint-config-prettier eslint-plugin-prettier

# 2. 配置 .eslintrc.json
# {
#   "extends": ["eslint:recommended", "plugin:prettier/recommended"]
# }

# 3. 配置 .prettierrc
# {
#   "semi": true,
#   "singleQuote": true,
#   "tabWidth": 2,
#   "trailingComma": "all"
# }

# 4. 在 package.json 添加脚本
# "lint": "eslint .",
# "lint:fix": "eslint --fix .",
# "format": "prettier --write ."

# 5. 运行
npm run format
npm run lint
```

---

## 相关资源

- [快速开始指南](../quick-start.md)
- [Linux 命令文档](../Linux 命令/README.md)
- [Git 命令文档](../Git 命令/README.md)
