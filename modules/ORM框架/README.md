# ORM 框架命令文档

主流 ORM 框架完整参考文档，涵盖 SQLAlchemy、Alembic、Prisma、TypeORM 和 Django ORM。

## 目录

- [SQLAlchemy (Python)](#sqlalchemy-python)
- [Alembic 数据库迁移](#alembic-数据库迁移)
- [Prisma (Node.js/TypeScript)](#prisma-nodejstypescript)
- [TypeORM](#typeorm)
- [Django ORM](#django-orm)

---

## SQLAlchemy (Python)

### create_engine - 创建数据库引擎

**基础用法**:
```python
from sqlalchemy import create_engine
engine = create_engine("%{数据库URL}%", %{参数}%)
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 连接 SQLite | `create_engine("sqlite:///mydb.db")` | 相对路径数据库(示例: mydb.db); sqlite:/// 前缀 |
| 连接 MySQL | `create_engine("mysql+pymysql://user:pass@localhost:3306/mydb")` | 用户(示例: user); 密码(示例: pass); 主机(示例: localhost); 端口(示例: 3306); 数据库(示例: mydb) |
| 连接 PostgreSQL | `create_engine("postgresql://user:pass@localhost:5432/mydb")` | 用户(示例: user); 密码(示例: pass); 主机(示例: localhost); 端口(示例: 5432); 数据库(示例: mydb) |
| 连接池配置 | `create_engine("sqlite:///mydb.db", pool_size=10, max_overflow=20)` | 连接池大小(示例: 10); 最大溢出(示例: 20) |
| Echo SQL | `create_engine("sqlite:///mydb.db", echo=True)` | echo=True 输出所有 SQL 语句(示例: True); 用于调试 |
| Echo False | `create_engine("sqlite:///mydb.db", echo=False)` | echo=False 静默模式(示例: False); 生产环境使用 |
| 连接池回收 | `create_engine("mysql://user:pass@localhost/mydb", pool_recycle=3600)` | pool_recycle 设置连接回收时间(示例: 3600 秒) |

---

### Session - 会话管理

**基础用法**:
```python
from sqlalchemy.orm import Session
session = Session(bind=%{引擎}%)
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建会话 | `session = Session(bind=engine)` | 【常用】引擎(示例: engine); 从 engine 创建会话 |
| 创建会话工厂 | `Session = sessionmaker(bind=engine)` | 【常用】引擎(示例: engine); 创建会话工厂类 |
| 开启事务 | `with session.begin():` | 【常用】自动提交/回滚; session 是 Session 实例 |
| 添加对象 | `session.add(%{对象}%)` | 【常用】对象(示例: user_instance); 添加到会话待提交 |
| 提交事务 | `session.commit()` | 【常用】提交所有待定更改; 常用 session.commit() |
| 回滚事务 | `session.rollback()` | 【常用】回滚所有待定更改; 常用 session.rollback() |
| 关闭会话 | `session.close()` | 关闭会话释放连接; 常用 session.close() |
| 查询对象 | `session.query(%{模型}%).filter_by(%{条件}%).all()` | 【常用】模型(示例: User); 条件(示例: id=1) |
| 删除对象 | `session.delete(%{对象}%)` | 【常用】对象(示例: user_instance); 标记删除待提交 |

---

### Base.metadata.create_all - 创建所有表

**基础用法**:
```python
Base.metadata.create_all(bind=%{引擎}%)
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建所有表 | `Base.metadata.create_all(bind=engine)` | 【常用】引擎(示例: engine); 根据所有模型创建表 |
| 仅创建特定表 | `Base.metadata.create_all(bind=engine, tables=[%{表列表}%])` | 【常用】引擎(示例: engine); 表列表(示例: [users_table, orders_table]) |
| 检查表存在 | `engine.dialect.has_table(engine, "%{表名}%")` | 【常用】引擎(示例: engine); 表名(示例: users); 检查表是否存在 |
| 删除所有表 | `Base.metadata.drop_all(bind=engine)` | 【常用】引擎(示例: engine); 删除所有表(危险操作) |
| 元数据检视 | `Base.metadata.tables` | 【常用】访问所有已注册表; 返回字典 |
| 反射表结构 | `Table("%{表名}%", Base.metadata, autoload=True, autoload_with=engine)` | 【常用】表名(示例: users); 从数据库反射表结构 |

---

## Alembic 数据库迁移

### alembic init - 初始化迁移环境

**基础用法**:
```bash
alembic init %{目录名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 初始化迁移 | `alembic init alembic` | 【常用】目录名(示例: alembic); 在当前目录创建迁移目录 |
| 指定模板 | `alembic init %{目录名}% -t %{模板}%` | 目录名(示例: alembic); 模板(示例: generic); 使用自定义模板 |
| 初始化 PG | `alembic init alembic -x sqlalchemy.url=postgresql://user:pass@localhost/mydb` | 指定数据库 URL(示例: postgresql://user:pass@localhost/mydb) |

---

### alembic revision - 创建迁移版本

**基础用法**:
```bash
alembic revision -m "%{消息}%"
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建迁移 | `alembic revision -m "add users table"` | 【常用】消息(示例: add users table); 创建空迁移文件 |
| 自动生成 | `alembic revision --autogenerate -m "add email column"` | 【常用】--autogenerate 自动检测模型变化; 消息(示例: add email column) |
| 指定依赖 | `alembic revision -m "v2" --depends-on %{上一个版本}%` | 版本ID(示例: v2); 依赖版本(示例: abc1234) |
| 创建空迁移 | `alembic revision -m "empty migration"` | 【常用】不含 upgrade/downgrade 的空迁移; 用于手工编写 |

---

### alembic upgrade - 执行迁移升级

**基础用法**:
```bash
alembic upgrade %{目标版本}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 升级到最新 | `alembic upgrade head` | 【常用】head 升级到最新版本; 常用 alembic upgrade head |
| 升级一步 | `alembic upgrade +1` | 【常用】+1 向上一步; 常用 alembic upgrade +1 |
| 升级到指定版本 | `alembic upgrade %{版本ID}%` | 【常用】版本ID(示例: abc1234); 迁移到指定版本 |
| 升级所有 | `alembic upgrade +%(步数}%` | 【常用】步数(示例: 3); 向上迁移多步 |
| 离线升级 | `alembic upgrade head --sql > upgrade.sql` | 输出 SQL 脚本(示例: upgrade.sql); 用于手动执行 |

---

### alembic downgrade - 执行迁移降级

**基础用法**:
```bash
alembic downgrade %{目标版本}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 降一级 | `alembic downgrade -1` | 【常用】-1 向下一步; 常用 alembic downgrade -1 |
| 降级到最初 | `alembic downgrade base` | 【常用】base 降级到最初版本; 常用 alembic downgrade base |
| 降级到指定版本 | `alembic downgrade %{版本ID}%` | 【常用】版本ID(示例: abc1234); 降级到指定版本 |
| 降级多步 | `alembic downgrade -%{步数}%` | 步数(示例: 3); 向下迁移多步 |

---

### alembic migrate - 迁移命令

**基础用法**:
```bash
alembic upgrade %{目标版本}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 显示历史 | `alembic history` | 【常用】列出所有迁移版本; 显示版本链 |
| 当前版本 | `alembic current` | 【常用】显示当前数据库版本; 常用 alembic current |
| 历史详情 | `alembic history --verbose` | 详细模式显示每个版本的依赖关系; 常用 alembic history --verbose |
| 标记迁移 | `alembic stamp %{版本ID}%` | 【常用】版本ID(示例: head); 标记当前数据库版本(不执行迁移) |

---

## Prisma (Node.js/TypeScript)

### prisma init - 初始化 Prisma

**基础用法**:
```bash
npx prisma init
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 初始化项目 | `npx prisma init` | 【常用】在项目目录初始化 Prisma; 创建 prisma/schema.prisma |
| 指定数据库 | `npx prisma init --datasource-provider postgresql` | 数据库类型(示例: postgresql); 支持: postgresql, mysql, sqlite, mongodb |
| 指定模板 | `npx prisma init --template quark` | 使用社区模板(示例: quark); 可选模板 |

---

### prisma generate - 生成客户端

**基础用法**:
```bash
npx prisma generate
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 生成客户端 | `npx prisma generate` | 【常用】根据 schema.prisma 生成 Prisma Client; 常用 npx prisma generate |
| 指定生成器 | `npx prisma generate --generator=%{生成器名}%` | 【常用】生成器名(示例: client); 只生成指定生成器 |
| 跳过验证 | `npx prisma generate --no-validation` | 跳过 schema 验证; 用于CI环境 |

---

### prisma migrate dev - 开发环境迁移

**基础用法**:
```bash
npx prisma migrate dev
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 开发迁移 | `npx prisma migrate dev --name %{迁移名称}%` | 【常用】迁移名称(示例: add_users_table); 创建并执行迁移 |
| 跳过种子 | `npx prisma migrate dev --name %{名称}% --skip-seed` | 【常用】跳过种子文件执行; 迁移名称(示例: init) |
| 跳过生成 | `npx prisma migrate dev --name %{名称}% --skip-generate` | 跳过客户端生成; 迁移名称(示例: init) |
| 创建迁移 | `npx prisma migrate dev --create-only --name %{名称}%` | 【常用】仅创建迁移文件(示例: init); 不执行 |
| 指定数据库 | `npx prisma migrate dev --name %{名称}% --schema=./prisma/schema.prisma` | 指定 schema 路径(示例: ./prisma/schema.prisma) |

---

### prisma migrate deploy - 生产环境部署

**基础用法**:
```bash
npx prisma migrate deploy
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 部署迁移 | `npx prisma migrate deploy` | 【常用】部署所有待执行迁移; 用于生产环境 |
| 指定 schema | `npx prisma migrate deploy --schema=./prisma/schema.prisma` | 指定 schema 路径(示例: ./prisma/schema.prisma) |
| 跳过删除 | `npx prisma migrate deploy --skip-delete` | 跳过失败迁移回滚; 谨慎使用 |

---

### prisma studio - 数据库可视化

**基础用法**:
```bash
npx prisma studio
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 打开 studio | `npx prisma studio` | 【常用】启动 Prisma Studio 可视化界面; 默认 http://localhost:5555 |
| 指定端口 | `npx prisma studio --port %{端口}%` | 【常用】端口(示例: 5555); 指定访问端口 |
| 指定环境 | `npx prisma studio --environment production` | 环境名(示例: production); 使用对应 .env |

---

### prisma db commands - 数据库操作

**基础用法**:
```bash
npx prisma db %{子命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 推送 schema | `npx prisma db push` | 【常用】将 schema 推送到数据库; 不创建迁移历史 |
| 拉取结构 | `npx prisma db pull` | 【常用】从数据库拉取结构到 schema; 反向工程 |
| 重置数据库 | `npx prisma db reset` | 【常用】重置数据库; 删除所有数据 |
| 执行 seed | `npx prisma db seed` | 【常用】执行种子文件; 填充初始数据 |
| 保留数据推送 | `npx prisma db push --accept-data-loss` | 【常用】接受数据丢失风险; schema 有破坏性变更时使用 |

---

## TypeORM

### typeorm entity:create - 创建实体

**基础用法**:
```bash
npx typeorm entity:create %{实体名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建实体 | `npx typeorm entity:create User` | 【常用】实体名(示例: User); 在 src/entities 创建实体类 |
| 指定目录 | `npx typeorm entity:create User --dir src/models` | 目录(示例: src/models); 指定存放目录 |
| 指定连接 | `npx typeorm entity:create User -c main` | 连接名(示例: main); 使用指定数据源 |

---

### typeorm migration:generate - 生成迁移

**基础用法**:
```bash
npx typeorm migration:generate %{迁移名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 生成迁移 | `npx typeorm migration:generate src/migrations/AddUsersTable` | 【常用】迁移名(示例: AddUsersTable); 自动比较实体和数据库 |
| 指定连接 | `npx typeorm migration:generate %{迁移名}% -c %{连接名}%` | 【常用】连接名(示例: main); 使用指定数据源 |
| 指定目录 | `npx typeorm migration:generate %{迁移名}% -d src/database/migrations` | 目录(示例: src/database/migrations) |

---

### typeorm subscriber:create - 创建订阅者

**基础用法**:
```bash
npx typeorm subscriber:create %{订阅者名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建订阅者 | `npx typeorm subscriber:create UserSubscriber` | 【常用】订阅者名(示例: UserSubscriber); 创建事件监听器 |
| 指定目录 | `npx typeorm subscriber:create %{名称}% --dir src/subscribers` | 目录(示例: src/subscribers); 指定存放目录 |

---

### typeorm migration - 其他迁移命令

**基础用法**:
```bash
npx typeorm migration:%{子命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建迁移 | `npx typeorm migration:create %{迁移名}%` | 【常用】迁移名(示例: CreateUsers); 创建空白迁移文件 |
| 运行迁移 | `npx typeorm migration:run` | 【常用】执行所有待运行迁移; 常用 npx typeorm migration:run |
| 回滚迁移 | `npx typeorm migration:revert` | 【常用】撤销上次迁移; 常用 npx typeorm migration:revert |
| 显示迁移 | `npx typeorm migration:show` | 【常用】显示所有迁移状态; 哪些已运行/未运行 |

---

## Django ORM

### python manage.py makemigrations - 生成迁移文件

**基础用法**:
```bash
python manage.py makemigrations %{应用名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 所有应用迁移 | `python manage.py makemigrations` | 【常用】为所有已注册应用生成迁移; 常用 python manage.py makemigrations |
| 指定应用迁移 | `python manage.py makemigrations %{应用名}%` | 【常用】应用名(示例: blog); 只为指定应用生成迁移 |
| 指定迁移名 | `python manage.py makemigrations %{应用名}% --name %{迁移名}%` | 【常用】应用名(示例: blog); 迁移名(示例: add_field); 自定义迁移文件名 |
| 合并迁移 | `python manage.py makemigrations --merge` | 合并冲突迁移; 用于多分支开发场景 |

---

### python manage.py migrate - 执行迁移

**基础用法**:
```bash
python manage.py migrate %{应用名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 执行所有迁移 | `python manage.py migrate` | 【常用】执行所有待执行迁移; 常用 python manage.py migrate |
| 指定应用迁移 | `python manage.py migrate %{应用名}%` | 【常用】应用名(示例: blog); 只执行指定应用迁移 |
| 指定版本 | `python manage.py migrate %{应用名}% %{版本号}%` | 【常用】应用名(示例: blog); 版本号(示例: 0001); 迁移到指定版本 |
| 假迁移 | `python manage.py migrate %{应用名}% --fake` | 标记为已执行但不实际执行; 用于手动修改数据库后同步状态 |
| 显示状态 | `python manage.py showmigrations` | 【常用】显示所有应用迁移状态; 显示哪些已执行 |

---

### python manage.py shell - 交互式 Shell

**基础用法**:
```bash
python manage.py shell
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 打开 Shell | `python manage.py shell` | 【常用】打开 Django 交互式 Shell; 加载 Django 环境 |
| IPython Shell | `pip install ipython && python manage.py shell` | 使用 IPython; 需要先 pip install ipython |
| Jupyter Shell | `pip install ipykernel && python manage.py shell_plus --kernel` | 【常用】使用 Jupyter 内核; 需要先安装 ipykernel |
| 执行脚本 | `python manage.py shell -c "from myapp.models import User; print(User.objects.count())"` | 【常用】直接执行命令; 脚本模式 |

---

### python manage.py 常用 ORM 命令

**基础用法**:
```bash
python manage.py %{命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建超级用户 | `python manage.py createsuperuser` | 【常用】创建管理员账户; 常用 python manage.py createsuperuser |
| 导出数据 | `python manage.py dumpdata %{应用名}%.%{模型名}% > data.json` | 【常用】应用名(示例: blog); 模型名(示例: Post); 导出为 JSON |
| 导入数据 | `python manage.py loaddata data.json` | 【常用】导入 fixture 数据; 常用 python manage.py loaddata |
| 清空数据库 | `python manage.py flush` | 【常用】删除所有数据但保留表结构; 常用 python manage.py flush |
| 列出所有模型 | `python manage.py inspectdb` | 【常用】从数据库逆向生成模型; 常用 python manage.py inspectdb |

