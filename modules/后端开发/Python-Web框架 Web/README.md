# Python Web框架 命令文档

Python Web 开发框架（Django / Flask）命令完整参考文档。

## 📚 目录

- [Django 命令](#django-命令)
- [Flask 命令](#flask-命令)
- [Python 工具链](#python-工具链)
- [实用场景示例](#实用场景示例)

---

## Django 命令

### django-admin startproject - 创建项目

**基础用法**:
```bash
django-admin startproject %{项目名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建项目 | `django-admin startproject %{项目名称}%` | 项目名称: 项目名称 (例: mysite)【常用】 |
| 在当前目录创建 | `django-admin startproject .` | 在当前目录创建项目 |
| 指定项目路径 | `django-admin startproject %{项目名称}% %{路径}%` | 项目名称: 项目名称 (例: mysite)；路径: 路径 (例: ./projects) |

### python manage.py startapp - 创建应用

**基础用法**:
```bash
python manage.py startapp %{应用名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建应用 | `python manage.py startapp %{应用名称}%` | 应用名称: 应用名称 (例: blog)【常用】 |
| 创建应用（指定目录） | `python manage.py startapp %{应用名称}% %{目录}%` | 应用名称: 应用名称 (例: blog)；目录: 目录 (例: apps/) |

### python manage.py runserver - 启动开发服务器

**基础用法**:
```bash
python manage.py runserver %{端口}%
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 默认端口 8000 | `python manage.py runserver` | 启动开发服务器 |
| 指定端口 | `python manage.py runserver %{端口}%` | 端口: 端口号 (例: 8080)【常用】 |
| 指定 IP 和端口 | `python manage.py runserver %{IP}%:%{端口}%` | IP: IP地址 (例: 0.0.0.0)；端口: 端口号 (例: 8000) |
| 自动重载 | `python manage.py runserver --reload` | 监视文件变化自动重载【常用】 |
| 生产模式 | `python manage.py runserver --skip-checks` | 跳过系统检查快速启动 |

### python manage.py makemigrations - 生成迁移文件

**基础用法**:
```bash
python manage.py makemigrations %{应用名称}%
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 为所有应用生成迁移 | `python manage.py makemigrations` | 所有应用的迁移【常用】 |
| 为指定应用生成 | `python manage.py makemigrations %{应用名称}%` | 应用名称: 应用名称 (例: blog)【常用】 |
| 指定迁移文件名 | `python manage.py makemigrations %{应用名称}% --name %{迁移名}%` | 应用名称: 应用名称 (例: blog)；迁移名: 迁移名 (例: add_field) |
| 查看 SQL 而不创建 | `python manage.py makemigrations --dry-run` | 仅显示将要生成的 SQL |

### python manage.py migrate - 执行数据库迁移

**基础用法**:
```bash
python manage.py migrate
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 执行所有迁移 | `python manage.py migrate` | 执行所有待处理的迁移【常用】 |
| 迁移指定应用 | `python manage.py migrate %{应用名称}%` | 应用名称: 应用名称 (例: blog)【常用】 |
| 迁移到指定版本 | `python manage.py migrate %{应用名称}% %{版本}%` | 应用名称: 应用名称 (例: blog)；版本: 版本号 (例: 0001) |
| 显示迁移状态 | `python manage.py showmigrations` | 显示所有应用的迁移状态 |
| 标记为已应用 | `python manage.py migrate %{应用名称}% --fake` | 手动标记迁移为已应用 |

### django-admin createsuperuser - 创建管理员

**基础用法**:
```bash
python manage.py createsuperuser
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建超级用户 | `python manage.py createsuperuser` | 交互式创建【常用】 |
| 指定用户名 | `python manage.py createsuperuser --username %{用户名}%` | 用户名: 用户名 (例: admin)【常用】 |
| 指定邮箱 | `python manage.py createsuperuser --email %{邮箱}%` | 邮箱: 邮箱地址 (例: admin@example.com) |
| 非交互创建 | `DJANGO_SUPERUSER_PASSWORD=pass python manage.py createsuperuser --noinput` | 脚本中使用 |

### python manage.py shell - Django Shell

**基础用法**:
```bash
python manage.py shell
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动交互式 Shell | `python manage.py shell` | 默认 IPython/BPython【常用】 |
| 使用纯 Python Shell | `python manage.py shell --plain` | 不使用 IPython【常用】 |
| 启动 iPython | `python manage.py shell -i ipython` | 指定使用 iPython |
| 执行脚本 | `python manage.py shell < %{脚本}%.py` | 脚本: 脚本文件 (例: seed) |

### python manage.py dbshell - 数据库命令行

**基础用法**:
```bash
python manage.py dbshell
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 进入数据库 CLI | `python manage.py dbshell` | 根据配置打开数据库客户端【常用】 |
| SQLite 直接访问 | `sqlite3 db.sqlite3` | 直接访问 SQLite 文件 |

### python manage.py test - 运行测试

**基础用法**:
```bash
python manage.py test %{应用名称}%
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 运行所有测试 | `python manage.py test` | 运行所有测试【常用】 |
| 运行指定应用测试 | `python manage.py test %{应用名称}%` | 应用名称: 应用名称 (例: blog)【常用】 |
| 运行指定测试类 | `python manage.py test %{应用名称}%.tests.%{类名}%` | 应用名称: 应用名称 (例: blog)；类名: 类名 (例: ModelTest) |
| 显示详细输出 | `python manage.py test --verbosity=2` | 详细测试输出【常用】 |
| 失败时停止 | `python manage.py test --failfast` | 首个失败后停止 |

### pytest-django - Pytest 运行 Django 测试

**基础用法**:
```bash
pytest
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 运行所有测试 | `pytest` | 使用 pytest 运行 Django 测试【常用】 |
| 运行指定文件 | `pytest %{路径}%.py` | 路径: 测试文件路径 (例: tests/test_models.py)【常用】 |
| 运行指定测试函数 | `pytest %{路径}%::%{函数}%` | 路径: 文件路径 (例: tests/test_models.py)；函数: 函数名 (例: test_create_user) |
| 显示覆盖率 | `pytest --cov=%{应用}% --cov-report=%{报告}%` | 应用: 应用名 (例: myapp)；报告: 报告类型 (例: html) |
| 标记过滤 | `pytest -m %{标记}%` | 标记: 标记名 (例: slow) |

### Django REST Framework - 测试 API

**基础用法**:
```bash
python manage.py runserver
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动开发服务器 | `python manage.py runserver` | 启动后访问 API 端点【常用】 |
| 使用 Django Shell | `python manage.py shell` | 在 Shell 中操作 DRF Serializer |
| 列出所有 URL | `python manage.py show_urls` | 查看所有注册的 API URL |

### Django Crispy Forms - 表单渲染

**基础用法**:
```bash
pip install crispy-bootstrap5
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装 | `pip install crispy-bootstrap5` | 安装 crispy-forms Bootstrap5 模板包【常用】 |
| 迁移 | `python manage.py migrate` | 执行迁移 |
| 渲染模板标签 | `{% load crispy_forms_tags %}` | 在模板中加载 |
| 渲染表单 | `{% crispy form %}` | 渲染表单 |

### Django Celery - 异步任务

**基础用法**:
```bash
celery -A %{项目名}% worker -l info
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动 Worker | `celery -A %{项目名}% worker -l info` | 项目名: 项目名 (例: mysite)【常用】 |
| 启动 Beat（定时任务） | `celery -A %{项目名}% beat -l info` | 项目名: 项目名 (例: mysite)【常用】 |
| 查看活跃任务 | `celery -A %{项目名}% inspect active` | 项目名: 项目名 (例: mysite) |
| 列出任务 | `celery -A %{项目名}% inspect registered` | 项目名: 项目名 (例: mysite) |
| Flower 监控 | `celery -A %{项目名}% flower` | 启动 Flower 监控界面 |

---

## Flask 命令

### flask run - 启动 Flask 开发服务器

**基础用法**:
```bash
flask run
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动开发服务器 | `flask run` | 读取 FLASK_APP 和 FLASK_ENV【常用】 |
| 指定 host 和 port | `flask run --host=%{IP}% --port=%{端口}%` | IP: IP地址 (例: 0.0.0.0)；端口: 端口号 (例: 5000)【常用】 |
| 启用调试模式 | `flask run --debug` | 开启热重载和调试器【常用】 |
| 生产模式 | `FLASK_ENV=production flask run` | 生产环境运行 |
| 指定应用 | `FLASK_APP=%{应用}% flask run` | 应用: 应用名 (例: app:create_app) |

### FLASK_APP 环境变量

**基础用法**:
```bash
export FLASK_APP=%{应用}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 设置应用 | `export FLASK_APP=app` | 设置 app.py 为 Flask 应用【常用】 |
| 设置模块中的工厂函数 | `export FLASK_APP=app:create_app('%{环境}%')` | 应用: 应用名 (例: app)；环境: 环境名 (例: development) |
| Windows 设置 | `set FLASK_APP=app` | Windows 命令行 |
| PowerShell 设置 | `$env:FLASK_APP="app"` | PowerShell |

### FLASK_ENV 环境变量

**基础用法**:
```bash
export FLASK_ENV=%{环境}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 开发模式 | `export FLASK_ENV=development` | 开启调试模式【常用】 |
| 生产模式 | `export FLASK_ENV=production` | 生产环境【常用】 |
| 组合使用 | `FLASK_APP=app FLASK_ENV=development flask run` | 同时设置多个环境变量【常用】 |

### Flask-SQLAlchemy - 数据库操作

**基础用法**:
```bash
flask db init
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 初始化迁移目录 | `flask db init` | 创建 migrations 目录【常用】 |
| 创建迁移 | `flask db migrate -m "%{消息}%"` | 消息: 迁移消息 (例: add users table)【常用】 |
| 应用迁移 | `flask db upgrade` | 将迁移应用到数据库【常用】 |
| 回滚迁移 | `flask db downgrade` | 回滚上一个迁移【常用】 |
| 查看迁移状态 | `flask db current` | 显示当前数据库版本 |
| 显示迁移历史 | `flask db history` | 显示所有迁移版本 |

### Flask-Migrate - 数据库迁移

**基础用法**:
```bash
flask db migrate
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 生成迁移脚本 | `flask db migrate -m "%{描述}%"` | 描述: 迁移描述 (例: add posts table)【常用】 |
| 应用所有迁移 | `flask db upgrade` | 升级数据库【常用】 |
| 降级数据库 | `flask db downgrade` | 降级数据库【常用】 |
| 升级到指定版本 | `flask db upgrade %{版本}%` | 版本: 版本号 (例: head) |
| 生成 SQL 脚本 | `flask db migrate --sql > %{文件}%.sql` | 文件: 输出文件 (例: migration) |

### Flask-Bcrypt - 密码哈希

**基础用法**:
```bash
flask shell
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 在 Shell 中测试哈希 | `flask shell` 然后 `from app import bcrypt; bcrypt.generate_password_hash('password')` | 测试密码哈希【常用】 |
| 验证密码 | `flask shell` 然后 `bcrypt.check_password_hash(hash, 'password')` | 验证密码哈希【常用】 |

### Flask-JWT-Extended - JWT 认证

**基础用法**:
```bash
flask run
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动服务器 | `flask run` | 配合 JWT 使用【常用】 |
| 生成访问令牌 | `flask shell` | 在 Shell 中 `create_access_token(identity='user_id')` |
| 生成刷新令牌 | `flask shell` | 在 Shell 中 `create_refresh_token(identity='user_id')` |
| 撤销令牌 | `flask shell` | 在 Shell 中 `revoke_jwt(token)` |

### Flask-CORS - 跨域资源共享

**基础用法**:
```bash
flask run
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动服务器 | `flask run` | CORS 默认允许所有源【常用】 |
| 指定允许的源 | `CORS(app, origins=["http://example.com"])` | 限制允许的源 |
| 允许凭证 | `CORS(app, supports_credentials=True)` | 允许携带 Cookie |
| 暴露响应头 | `CORS(app, expose_headers=["X-Total-Count"])` | 暴露自定义响应头 |

---

## Python 工具链

### black - 代码格式化

**基础用法**:
```bash
black %{路径}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 格式化目录 | `black %{路径}%` | 路径: 目录 (例: src)【常用】 |
| 检查格式（不修改） | `black --check %{路径}%` | 路径: 目录 (例: src)【常用】 |
| 显示差异 | `black --diff %{路径}%` | 路径: 目录 (例: src)【常用】 |
| 排除目录 | `black --exclude '%{正则}%' %{路径}%` | 正则: 正则表达式 (例: '/migrations/')；路径: 目录 (例: .) |
| 管道输入 | `cat app.py | black -` | 格式化 stdin 输入 |

### flake8 - 代码检查

**基础用法**:
```bash
flake8 %{路径}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 检查目录 | `flake8 %{路径}%` | 路径: 目录 (例: app)【常用】 |
| 忽略错误码 | `flake8 --ignore=%{错误码}% %{路径}%` | 错误码: 错误码 (例: E501,W503)；路径: 目录 (例: .)【常用】 |
| 显示错误上下文 | `flake8 --show-source %{路径}%` | 路径: 目录 (例: app) |
| 最大行长度 | `flake8 --max-line-length=%{长度}% %{路径}%` | 长度: 长度 (例: 120)；路径: 目录 (例: .) |
| 输出格式 | `flake8 --format='%(row)d:%(col)d: %(text)s' %{路径}%` | 路径: 目录 (例: app) |
| 统计错误 | `flake8 --statistics %{路径}%` | 路径: 目录 (例: .) |

### mypy - 静态类型检查

**基础用法**:
```bash
mypy %{路径}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 类型检查目录 | `mypy %{路径}%` | 路径: 目录 (例: src)【常用】 |
| 严格模式 | `mypy --strict %{路径}%` | 路径: 目录 (例: src)【常用】 |
| 忽略缺失导入 | `mypy --ignore-missing-imports %{路径}%` | 路径: 目录 (例: src) |
| 显示错误上下文 | `mypy --show-error-context %{路径}%` | 路径: 目录 (例: src) |
| 增量检查 | `mypy --incremental %{路径}%` | 路径: 目录 (例: src) |
| 配置文件检查 | `mypy --config-file mypy.ini %{路径}%` | 路径: 目录 (例: .) |

### pytest - 测试框架

**基础用法**:
```bash
pytest %{路径}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 运行所有测试 | `pytest` | 查找当前目录测试【常用】 |
| 运行指定测试文件 | `pytest %{路径}%` | 路径: 测试文件 (例: tests/test_api.py)【常用】 |
| 运行指定测试函数 | `pytest %{路径}%::%{函数}%` | 路径: 文件 (例: tests/test_api.py)；函数: 函数名 (例: test_login) |
| 详细输出 | `pytest -v` | 详细测试结果【常用】 |
| 显示局部变量 | `pytest -l` | 失败时显示局部变量 |
| 显示 print 输出 | `pytest -s` | 显示所有 print 输出【常用】 |
| 在首次失败后停止 | `pytest -x` | 首个失败后停止【常用】 |
| 运行最后失败的测试 | `pytest --lf` | 只运行上次失败的测试 |
| 标记过滤 | `pytest -m %{标记}%` | 标记: 标记名 (例: slow)【常用】 |
| 指定 fixtures | `pytest --fixtures` | 列出所有可用的 fixtures |

### pytest-cov - 测试覆盖率

**基础用法**:
```bash
pytest --cov=%{包名}% --cov-report=%{报告类型}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 生成覆盖率报告 | `pytest --cov=%{包名}% --cov-report=term-missing` | 包名: 包名 (例: app)【常用】 |
| HTML 覆盖率报告 | `pytest --cov=%{包名}% --cov-report=html` | 包名: 包名 (例: app)【常用】 |
| XML 覆盖率报告 | `pytest --cov=%{包名}% --cov-report=xml` | 包名: 包名 (例: app) |
| 最小覆盖率阈值 | `pytest --cov=%{包名}% --cov-fail-under=%{阈值}%` | 包名: 包名 (例: app)；阈值: 阈值 (例: 80) |
| 排除文件 | `pytest --cov=%{包名}% --cov-exclude='%{模式}%'` | 包名: 包名 (例: app)；模式: 模式 (例: */migrations/*) |

### Django Debug Toolbar - 调试工具

**基础用法**:
```bash
python manage.py runserver
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动开发服务器 | `python manage.py runserver` | Debug Toolbar 自动激活【常用】 |
| 安装包 | `pip install django-debug-toolbar` | 安装调试工具栏 |
| 配置中间件 | 在 settings.py 的 MIDDLEWARE 添加 debug_toolbar.middleware.DebugToolbarMiddleware | 配置中间件 |
| 配置 INTERNAL_IPS | `INTERNAL_IPS = ['127.0.0.1']` | 配置允许的 IP |

### uv - 快速的 Python 包管理器

**基础用法**:
```bash
uv pip install %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装包 | `uv pip install %{包名}%` | 包名: 包名 (例: flask)【常用】 |
| 安装 requirements.txt | `uv pip install -r requirements.txt` | 批量安装依赖 |
| 同步依赖 | `uv pip sync requirements.txt` | 与 lock 文件同步 |
| 创建虚拟环境 | `uv venv %{环境名}%` | 环境名: 环境名 (例: .venv)【常用】 |
| 运行脚本 | `uv run %{命令}%` | 命令: 命令 (例: pytest)【常用】 |
| 升级包 | `uv pip install --upgrade %{包名}%` | 包名: 包名 (例: flask) |
| 显示已安装 | `uv pip list` | 列出已安装的包 |

### virtualenv - 虚拟环境管理

**基础用法**:
```bash
virtualenv %{环境名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建虚拟环境 | `virtualenv %{环境名}%` | 环境名: 环境名 (例: venv)【常用】 |
| 指定 Python 版本 | `virtualenv --python=%{Python路径}% %{环境名}%` | Python路径: Python路径 (例: python3.10)；环境名: 环境名 (例: venv) |
| 无包安装 | `virtualenv --no-site-packages %{环境名}%` | 环境名: 环境名 (例: venv) |
| 激活环境（Linux/Mac） | `source %{环境名}%/bin/activate` | 环境名: 环境名 (例: venv)【常用】 |
| 激活环境（Windows） | `%{环境名}%\Scripts\activate` | 环境名: 环境名 (例: venv)【常用】 |
| 退出环境 | `deactivate` | 退出虚拟环境 |

---

## 实用场景示例

### 场景 1: 从零创建 Django 项目

```bash
# 创建项目
django-admin startproject mysite
cd mysite

# 创建应用
python manage.py startapp blog

# 数据库初始化
python manage.py makemigrations
python manage.py migrate

# 创建管理员
python manage.py createsuperuser

# 启动开发服务器
python manage.py runserver 8080
```

### 场景 2: 从零创建 Flask 项目

```bash
# 设置环境变量
export FLASK_APP=app
export FLASK_ENV=development

# 安装依赖
pip install flask flask-sqlalchemy flask-migrate flask-cors

# 初始化数据库迁移
flask db init
flask db migrate -m "initial migration"
flask db upgrade

# 启动服务器
flask run --debug
```

### 场景 3: Django 测试驱动开发

```bash
# 创建测试
python manage.py test --verbosity=2

# 使用 pytest-django
pip install pytest pytest-django pytest-cov
pytest --cov=myapp --cov-report=term-missing

# 查看覆盖率 HTML 报告
pytest --cov=myapp --cov-report=html
open htmlcov/index.html
```

### 场景 4: Python 代码质量检查

```bash
# 安装工具
pip install black flake8 mypy

# 代码格式化
black .

# 代码检查
flake8 . --ignore=E501,W503

# 类型检查
mypy . --ignore-missing-imports
```

### 场景 5: 使用 uv 管理项目

```bash
# 创建项目并初始化
uv init myproject
cd myproject

# 添加依赖
uv add flask django djangorestframework

# 安装开发依赖
uv add --dev pytest black mypy

# 运行命令
uv run flask run
uv run pytest
uv run black .
```

---

## 🔗 相关资源

- [完整命令参考表](../../references/commands-reference.md)
- [Python 基础命令](../Python命令/README.md)
- [快速开始指南](../quick-start.md)
