# Python 命令文档

Python 包管理与环境命令完整参考文档。

## 📚 目录

- [pip 包管理](#pip-包管理)
- [虚拟环境](#虚拟环境)
- [python -m 内置模块](#python--m-内置模块)
- [Pipenv](#pipenv)
- [Poetry](#poetry)

---

## pip 包管理

### pip install - 安装包

**基础用法**:
```bash
pip install %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装指定版本 | `pip install %{包名}%==%{版本号}%` | 包名: 包名称 (例: requests)；版本号: 版本号 (例: 2.28.0) |
| 从 requirements 安装 | `pip install -r requirements.txt` | 批量安装依赖 |
| 安装多个包 | `pip install %{包1}% %{包2}%` | 包1: 第一个包名 (例: flask)【常用】；包2: 第二个包名 (例: django)【常用】 |
| 安装到用户目录 | `pip install --user %{包名}%` | 包名: 包名称 (例: virtualenv)，避免权限问题 |
| 升级包 | `pip install --upgrade %{包名}%` | 包名: 包名称 (例: pip)【常用】 |
| 从 Git 安装 | `pip install git+%{仓库URL}%` | 仓库URL: Git 仓库地址 (例: https://github.com/user/repo.git) |

### pip uninstall - 卸载包

**基础用法**:
```bash
pip uninstall %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 卸载多个包 | `pip uninstall %{包1}% %{包2}%` | 包1: 第一个包名 (例: requests)；包2: 第二个包名 (例: flask) |
| 自动确认卸载 | `pip uninstall -y %{包名}%` | 包名: 包名称 (例: numpy)【常用】 |
| 从 requirements 卸载 | `pip uninstall -r requirements.txt -y` | 批量卸载依赖 |

### pip list - 查看已安装包

**基础用法**:
```bash
pip list
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 输出为 requirements 格式 | `pip freeze` | 生成 requirements.txt 格式 |
| 保存依赖到文件 | `pip freeze > requirements.txt` | 导出依赖列表 |
| 查看可编辑包 | `pip list -e` | 显示开发模式安装的包 |
| 按格式输出 | `pip freeze --format=%{格式}%` | 格式: 输出格式 (例: freeze) |
| 查看过期包 | `pip list --outdated` | 显示可升级的包 |
| 查看可升级包 | `pip list --upgradable` | 显示所有可升级的包 |

### pip show - 查看包信息

**基础用法**:
```bash
pip show %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看包含文件 | `pip show -f %{包名}%` | 包名: 包名称 (例: requests)【常用】 |
| 输出 JSON 格式 | `pip show %{包名}% --format=json` | 包名: 包名称 (例: flask) |

### pip check - 检查依赖

**基础用法**:
```bash
pip check
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 检查特定包 | `pip check %{包名}%` | 包名: 包名称 (例: numpy) |

---

## 虚拟环境

### python -m venv - 创建虚拟环境

**基础用法**:
```bash
python -m venv %{环境名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建虚拟环境 | `python -m venv venv` | 创建名为 venv 的环境 |
| Windows 激活 | `venv\Scripts\activate` | Windows 下激活环境 |
| Linux/Mac 激活 | `source venv/bin/activate` | Unix 下激活环境 |
| 退出虚拟环境 | `deactivate` | 退出当前虚拟环境 |
| 创建指定版本环境 | `python3 -m venv %{环境名}% --python=%{版本}%` | 环境名: 环境名称 (例: py38)；版本: Python 版本 (例: python3.8) |

---

## python -m 内置模块

### python -m pip - 调用 pip 模块

**基础用法**:
```bash
python -m pip %{操作}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 升级 pip | `python -m pip install --upgrade pip` | 推荐使用此方式升级 pip |
| 检查版本 | `python -m pip --version` | 查看 pip 版本 |
| 安装包 | `python -m pip install %{包名}%` | 包名: 包名称 (例: numpy)【常用】 |
| 冻结依赖 | `python -m pip freeze` | 输出已安装包列表 |

### python -m http.server - 启动 HTTP 服务

**基础用法**:
```bash
python -m http.server %{端口}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 默认端口 8000 | `python -m http.server` | 启动当前目录服务 |
| 指定端口 | `python -m http.server %{端口}%` | 端口: 端口号 (例: 8080)【常用】 |
| 绑定指定 IP | `python -m http.server %{端口}% --bind %{IP}%` | 端口: 端口号 (例: 8000)；IP: 绑定地址 (例: 0.0.0.0) |
| 指定目录 | `python -m http.server %{端口}% --directory %{目录}%` | 端口: 端口号 (例: 8000)；目录: 服务目录 (例: ./public) |

### python -m json.tool - JSON 格式化

**基础用法**:
```bash
python -m json.tool %{文件}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 格式化文件 | `python -m json.tool %{文件}%.json` | 文件: JSON 文件路径 (例: data)【常用】 |
| 从 stdin 读取 | `cat %{文件}%.json | python -m json.tool` | 文件: JSON 文件路径 (例: config) |
| 排序并输出 | `python -m json.tool --indent 2 %{文件}%.json > %{输出}%` | 文件: 输入文件 (例: data)；输出: 输出文件 (例: formatted) |
| 验证 JSON | `python -c "import json; json.load(open('%{文件}%.json'))"` | 文件: JSON 文件路径 (例: config) |

---

## Pipenv

### pipenv install - 安装依赖

**基础用法**:
```bash
pipenv install %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装所有依赖 | `pipenv install` | 读取 Pipfile 安装全部依赖 |
| 安装开发依赖 | `pipenv install --dev %{包名}%` | 包名: 包名称 (例: pytest) |
| 安装特定版本 | `pipenv install %{包名}%==%{版本}%` | 包名: 包名称 (例: flask)；版本: 版本号 (例: 2.0.0) |
| 从 Pipfile 安装 | `pipenv install --ignore-pipfile` | 忽略 Pipfile.lock |
| 同步依赖 | `pipenv sync` | 与 Pipfile.lock 同步 |
| 生成 requirements | `pipenv lock --requirements` | 输出 requirements 格式 |

### pipenv shell - 进入环境

**基础用法**:
```bash
pipenv shell
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 进入交互式环境 | `pipenv shell` | 激活虚拟环境 |
| 运行命令不激活 | `pipenv run %{命令}%` | 命令: 要执行的命令 (例: python app.py)【常用】 |
| 运行 Python 脚本 | `pipenv run python %{脚本}%` | 脚本: Python 脚本路径 (例: main.py)【常用】 |
| 退出环境 | `exit` | 退出交互式环境 |

---

## Poetry

### poetry install - 安装依赖

**基础用法**:
```bash
poetry install
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装所有依赖 | `poetry install` | 读取 pyproject.toml 安装全部依赖 |
| 安装开发依赖 | `poetry install --with dev` | 同时安装开发依赖 |
| 仅生产依赖 | `poetry install --only prod` | 不安装开发依赖 |
| 安装并同步 | `poetry install --sync` | 确保虚拟环境与 lock 文件同步 |
| 离线安装 | `poetry install --no-interaction --offline` | 使用缓存依赖 |

### poetry add - 添加依赖

**基础用法**:
```bash
poetry add %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 添加生产依赖 | `poetry add %{包名}%` | 包名: 包名称 (例: flask)【常用】 |
| 添加开发依赖 | `poetry add --group dev %{包名}%` | 包名: 包名称 (例: pytest) |
| 添加特定版本 | `poetry add %{包名}%^%{版本}%` | 包名: 包名称 (例: requests)；版本: 版本号 (例: 2.28) |
| 添加 Git 依赖 | `poetry add git+%{仓库URL}%` | 仓库URL: Git 仓库地址 (例: https://github.com/user/repo.git) |
| 添加路径依赖 | `poetry add --path %{路径}%` | 路径: 本地路径 (例: ./packages/mylib) |
| 移除依赖 | `poetry remove %{包名}%` | 包名: 包名称 (例: flask) |

### poetry shell - 进入环境

**基础用法**:
```bash
poetry shell
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 进入交互式环境 | `poetry shell` | 激活虚拟环境 |
| 运行命令不激活 | `poetry run %{命令}%` | 命令: 要执行的命令 (例: python app.py)【常用】 |
| 运行 Python 脚本 | `poetry run python %{脚本}%` | 脚本: Python 脚本路径 (例: main.py)【常用】 |
| 运行 pytest | `poetry run pytest` | 运行测试 |
| 退出环境 | `exit` | 退出交互式环境 |

### poetry run - 执行命令

**基础用法**:
```bash
poetry run %{命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 运行 Python 脚本 | `poetry run python %{脚本}%` | 脚本: Python 脚本路径 (例: main.py)【常用】 |
| 运行 pytest | `poetry run pytest` | 运行测试套件 |
| 运行 black 格式化 | `poetry run black %{目录}%` | 目录: 目录路径 (例: src)，代码格式化 |
| 运行 flake8 检查 | `poetry run flake8` | 代码风格检查 |
| 运行 mypy 类型检查 | `poetry run mypy %{目录}%` | 目录: 目录路径 (例: src)，静态类型检查 |
| 运行自定义脚本 | `poetry run %{脚本名}%` | 脚本名: 脚本名称 (例: dev)，需在 pyproject.toml 定义 |

---

## 💡 实用场景示例

### 场景 1: 项目依赖管理

```bash
# 方式一：使用 pip + requirements
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt

# 冻结依赖
pip freeze > requirements.txt

# 方式二：使用 Pipenv
pipenv install
pipenv install --dev pytest
pipenv shell
pipenv run python app.py

# 方式三：使用 Poetry
poetry install
poetry add requests
poetry run python script.py
```

### 场景 2: 本地 HTTP 服务

```bash
# 快速共享当前目录
python -m http.server 8080

# 绑定所有网卡（局域网访问）
python -m http.server 8000 --bind 0.0.0.0

# 指定目录
python -m http.server 9000 --directory /path/to/share
```

### 场景 3: JSON 处理

```bash
# 格式化 JSON 文件（美化输出）
python -m json.tool data.json

# 验证 JSON 语法
python -m json.tool data.json > /dev/null && echo "Valid JSON"

# 排序键并输出
python -m json.tool --indent 2 unsorted.json > sorted.json
```

### 场景 4: 环境隔离

```bash
# 创建独立环境
python -m venv myenv
source myenv/bin/activate

# 安装依赖
pip install flask numpy pandas

# 导出环境信息
pip freeze > requirements.txt

# 退出
deactivate

# 重建环境
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

---

## 🔗 相关资源

- [完整命令参考表](../../references/commands-reference.md)
- [快速开始指南](../quick-start.md)