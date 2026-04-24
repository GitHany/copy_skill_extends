# PostgreSQL 命令文档

PostgreSQL 数据库完整参考文档。

## 目录

- [连接管理](#连接管理)
- [备份恢复](#备份恢复)
- [表操作](#表操作)
- [索引操作](#索引操作)
- [用户管理](#用户管理)
- [数据导入导出](#数据导入导出)
- [维护优化](#维护优化)
- [查询分析](#查询分析)
- [进程管理](#进程管理)
- [实用场景](#实用场景)

---

## 连接管理

### psql - 连接数据库

**基础用法**:
```bash
psql -U %{用户名}% -h %{主机}% -p %{端口}% -d %{数据库名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 连接本地数据库 | `psql -U postgres` | -U: 用户名，示例: postgres |
| 连接远程数据库 | `psql -U postgres -h 192.168.1.100 -p 5432 -d mydb` | -U: 用户名示例: postgres; -h: 主机示例: 192.168.1.100; -p: 端口示例: 5432; -d: 数据库名示例: mydb |
| 执行 SQL 文件 | `psql -U postgres -d mydb -f backup.sql` | -f: SQL文件路径，示例: /path/to/backup.sql |
| 导出查询结果 | `psql -U postgres -d mydb -c "SELECT * FROM users;" -o output.csv` | -c: SQL语句; -o: 输出文件 |
| 带密码连接 | `PGPASSWORD=密码 psql -U 用户 -h 主机 -d 数据库` | PGPASSWORD: 环境变量传密码，示例: your_password |

---

## 备份恢复

### pg_dump - 备份数据库 【常用】

**基础用法**:
```bash
pg_dump -U %{用户名}% -h %{主机}% -p %{端口}% -d %{数据库名}% -f %{备份文件}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 普通备份 | `pg_dump -U postgres -d mydb > mydb_backup.sql` | -U: 用户名示例: postgres; -d: 数据库名示例: mydb |
| 压缩备份 | `pg_dump -U postgres -d mydb \| gzip > mydb_backup.sql.gz` | 使用 gzip 压缩备份文件 |
| 仅结构备份 | `pg_dump -U postgres -d mydb --schema-only > mydb_schema.sql` | --schema-only: 只备份结构，不含数据 |
| 仅数据备份 | `pg_dump -U postgres -d mydb --data-only > mydb_data.sql` | --data-only: 只备份数据，不含结构 |
| 指定表备份 | `pg_dump -U postgres -d mydb -t users -t orders > tables_backup.sql` | -t: 指定表名，示例: users, orders |
| 远程备份 | `pg_dump -U postgres -h 192.168.1.100 -p 5432 -d mydb > remote_backup.sql` | -h: 主机示例: 192.168.1.100; -p: 端口示例: 5432 |
| 压缩格式备份 | `pg_dump -U postgres -d mydb -Fc > mydb_backup.dump` | -Fc: 自定义压缩格式，支持并行恢复 |

### pg_restore - 恢复数据库

**基础用法**:
```bash
pg_restore -U %{用户名}% -h %{主机}% -p %{端口}% -d %{数据库名}% %{备份文件}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 普通恢复 | `pg_restore -U postgres -d mydb mydb_backup.sql` | -U: 用户名示例: postgres; -d: 数据库名示例: mydb |
| 恢复压缩格式 | `pg_restore -U postgres -d mydb -Fc mydb_backup.dump` | -Fc: 自定义格式备份文件示例: mydb_backup.dump |
| 创建新数据库恢复 | `pg_restore -U postgres -C -d postgres mydb_backup.dump` | -C: 先创建数据库再恢复; -d: 临时连接数据库示例: postgres |

### pg_dumpall - 全量备份

**基础用法**:
```bash
pg_dumpall -U %{用户名}% -h %{主机}% -p %{端口}% > %{备份文件}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 全量备份 | `pg_dumpall -U postgres > all_backup.sql` | -U: 用户名示例: postgres; 备份所有数据库和全局对象 |
| 压缩备份 | `pg_dumpall -U postgres \| gzip > all_backup.sql.gz` | 使用 gzip 压缩备份文件 |
| 仅全局对象 | `pg_dumpall -U postgres --globals-only > globals.sql` | --globals-only: 只备份全局对象(用户/角色/表空间等) |

---

## 表操作

### CREATE TABLE - 创建表 【常用】

**基础用法**:
```bash
CREATE TABLE %{表名}% (%{字段定义}%);
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建简单表 | `CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(100));` | 创建含自增主键和 VARCHAR 字段的表，示例: users |
| 创建完整表 | `CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, email VARCHAR(255) UNIQUE, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);` | 创建完整表，含 NOT NULL/UNIQUE 约束和 TIMESTAMP 默认值 |
| 查看所有表 | `\dt` | 元命令，列出当前数据库所有表 |
| 查看表结构 | `\d %{表名}%` | 元命令查看表结构，示例: users |
| 查看建表语句 | `SELECT pg_dump -s -t %{表名}% %{数据库名}%;` | 查看建表 DDL，示例: users, mydb |
| 修改表名 | `ALTER TABLE old_name RENAME TO new_name;` | 重命名表，示例: old_name → new_name |
| 删除表 | `DROP TABLE %{表名}%;` | 删除表，示例: users |
| 添加字段 | `ALTER TABLE %{表名}% ADD COLUMN %{字段名}% %{类型}%;` | 添加列，示例: users, email, VARCHAR(255) |
| 删除字段 | `ALTER TABLE %{表名}% DROP COLUMN %{字段名}%;` | 删除列，示例: users, email |

### ALTER TABLE - 修改表

**基础用法**:
```bash
ALTER TABLE %{表名}% %{操作}%;
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 添加字段 | `ALTER TABLE users ADD COLUMN email VARCHAR(255);` | ADD COLUMN: 添加 email 字段，类型 VARCHAR(255) |
| 删除字段 | `ALTER TABLE users DROP COLUMN email;` | DROP COLUMN: 删除 email 字段 |
| 修改字段类型 | `ALTER TABLE users ALTER COLUMN name TYPE VARCHAR(200);` | ALTER COLUMN TYPE: 将 name 改为 VARCHAR(200) |
| 重命名字段 | `ALTER TABLE users RENAME COLUMN name TO username;` | RENAME COLUMN: 重命名字段，name → username |
| 添加主键 | `ALTER TABLE users ADD PRIMARY KEY (id);` | ADD PRIMARY KEY: 将 id 设为主键 |
| 添加外键 | `ALTER TABLE orders ADD FOREIGN KEY (user_id) REFERENCES users(id);` | ADD FOREIGN KEY: 添加外键约束，关联 users 表 |
| 重命名表 | `ALTER TABLE old_name RENAME TO new_name;` | RENAME TO: 重命名表，old_name → new_name |

---

## 索引操作

### CREATE INDEX - 创建索引 【常用】

**基础用法**:
```bash
CREATE INDEX %{索引名}% ON %{表名}% (%{字段}%);
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 B-tree 索引 | `CREATE INDEX idx_name ON users(name);` | 默认索引类型，适用于普通查询优化 |
| 创建 BRIN 索引 | `CREATE INDEX idx_created_brin ON orders USING BRIN (created_at);` | BRIN: 适合范围扫描和大表时序数据 |
| 创建 GiST 索引 | `CREATE INDEX idx_geom ON places USING GIST (geometry);` | GiST: 适合几何/地理数据类型 |
| 创建 GiN 索引 | `CREATE INDEX idx_content ON articles USING GIN (to_tsvector('english', content));` | GiN: 适合全文搜索和数组类型 |
| 创建唯一索引 | `CREATE UNIQUE INDEX idx_email ON users(email);` | UNIQUE: 约束字段唯一性，示例: email |
| 创建复合索引 | `CREATE INDEX idx_name_status ON users(name, status);` | 复合索引: 多字段组合，示例: (name, status) |
| 查看表索引 | `\di %{表名}%` | 元命令查看表索引，示例: users |
| 删除索引 | `DROP INDEX %{索引名}%;` | 删除索引，示例: idx_name |

### REINDEX - 重建索引

**基础用法**:
```bash
REINDEX %{类型}% %{目标}%;
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 重建单个索引 | `REINDEX INDEX %{索引名}%;` | 重建指定索引，示例: idx_name |
| 重建表的所有索引 | `REINDEX TABLE %{表名}%;` | 重建表及所有关联索引，示例: users |
| 重建整个数据库 | `REINDEX DATABASE %{数据库名}%;` | 重建数据库所有索引，示例: mydb |
| 重建系统表 | `REINDEX SYSTEM %{数据库名}%;` | 重建系统表索引，示例: mydb |

---

## 用户管理

### CREATE USER - 用户管理

**基础用法**:
```bash
CREATE USER %{用户名}% WITH PASSWORD '%{密码}%';
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建用户 | `CREATE USER appuser WITH PASSWORD 'password123';` | 创建普通用户，示例: appuser |
| 创建超级用户 | `CREATE USER admin WITH SUPERUSER PASSWORD 'password123';` | SUPERUSER: 创建管理员账号，示例: admin |
| 修改用户密码 | `ALTER USER %{用户名}% WITH PASSWORD '%{新密码}%';` | 修改密码，示例: appuser, newpass123 |
| 删除用户 | `DROP USER %{用户名}%;` | 删除用户，示例: appuser |
| 查看所有用户 | `\du` | 元命令列出所有用户和角色 |
| 授予数据库权限 | `GRANT ALL PRIVILEGES ON DATABASE %{数据库}% TO %{用户名}%;` | 授予数据库所有权限，示例: mydb, appuser |
| 撤销数据库权限 | `REVOKE ALL PRIVILEGES ON DATABASE %{数据库}% FROM %{用户名}%;` | 撤销数据库权限，示例: mydb, appuser |
| 授予表权限 | `GRANT SELECT, INSERT, UPDATE ON %{表名}% TO %{用户名}%;` | 授予表 CRUD 权限，示例: users, appuser |

---

## 数据导入导出

### COPY - 导入导出数据 【常用】

**基础用法**:
```bash
COPY %{表名}% (%{字段}%) FROM '%{文件路径}%' WITH (FORMAT csv, HEADER true);
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 导出表到 CSV | `COPY users TO '/tmp/users.csv' WITH (FORMAT csv, HEADER);` | 导出表数据到 CSV 文件，示例: users |
| 从 CSV 导入 | `COPY users FROM '/tmp/users.csv' WITH (FORMAT csv, HEADER);` | 从 CSV 文件导入数据到表，示例: users |
| 导出查询结果 | `COPY (SELECT * FROM users WHERE status = 1) TO '/tmp/active_users.csv' WITH (FORMAT csv, HEADER);` | 导出符合条件的查询结果 |
| 导出到标准输出 | `COPY users TO STDOUT WITH (FORMAT csv, HEADER);` | STDOUT: 输出到标准输出，用于管道传输 |

---

## 维护优化

### VACUUM ANALYZE - 维护优化

**基础用法**:
```bash
VACUUM %{选项}% %{表名}%;
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| VACUUM 回收空间 | `VACUUM;` | 回收已删除元组空间，不锁定表 |
| VACUUM ANALYZE | `VACUUM ANALYZE;` | 回收空间并更新统计信息，用于查询优化 |
| VACUUM FULL | `VACUUM FULL;` | FULL: 重建表文件，收缩空间但需排他锁，建议低峰期使用 |
| VACUUM 指定表 | `VACUUM ANALYZE %{表名}%;` | 针对特定表回收空间并分析，示例: users |
| ANALYZE 更新统计 | `ANALYZE;` | 更新统计信息供查询规划器使用 |
| ANALYZE 指定表 | `ANALYZE %{表名}%;` | 分析特定表统计信息，示例: users |
| 查看表大小 | `SELECT pg_size_pretty(pg_total_relation_size('%{表名}%'));` | 查看表总大小(含索引)，示例: users |
| 查看索引大小 | `SELECT pg_size_pretty(pg_indexes_size('%{表名}%'));` | 查看表所有索引大小，示例: users |

---

## 查询分析

### EXPLAIN ANALYZE - 查询分析 【常用】

**基础用法**:
```bash
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT) %{SQL语句}%;
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 分析 SELECT | `EXPLAIN ANALYZE SELECT * FROM users WHERE id = 1;` | 分析 SELECT 执行计划，显示实际运行时间 |
| 分析 UPDATE | `EXPLAIN ANALYZE UPDATE users SET name = 'test' WHERE id = 1;` | 分析 UPDATE 执行计划，含写入成本 |
| 分析 INSERT | `EXPLAIN ANALYZE INSERT INTO users (name) VALUES ('test');` | 分析 INSERT 执行计划，含写入成本 |
| 分析 DELETE | `EXPLAIN ANALYZE DELETE FROM users WHERE id = 1;` | 分析 DELETE 执行计划，含删除成本 |
| 查看执行计划 | `EXPLAIN %{SQL语句}%;` | 不执行只显示计划，用于预估成本 |

---

## 进程管理

### pg_stat_activity - 查看进程

**基础用法**:
```bash
SELECT * FROM pg_stat_activity WHERE datname = '%{数据库名}%';
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看所有连接 | `SELECT pid, usename, datname, state, query, query_start FROM pg_stat_activity;` | 查看所有连接及当前状态和执行的 SQL |
| 查看活跃查询 | `SELECT pid, query, query_start FROM pg_stat_activity WHERE state = 'active';` | state='active': 只看正在执行的查询 |
| 查看等待中的查询 | `SELECT * FROM pg_stat_activity WHERE wait_event IS NOT NULL;` | wait_event: 查看因锁等待的查询 |
| 查看慢查询 | `SELECT pid, query, query_start, now() - query_start AS duration FROM pg_stat_activity WHERE (now() - query_start) > interval '5 minutes' AND state = 'active';` | duration > 5分钟 且状态活跃的查询 |
| 杀掉慢查询 | `SELECT pg_cancel_backend(%{pid}%);` | 优雅取消查询，让其自行回滚，示例: 1234 |
| 强制终止连接 | `SELECT pg_terminate_backend(%{pid}%);` | 强制断开连接，会丢失未提交事务，示例: 1234 |
| 查看连接数 | `SELECT count(*) FROM pg_stat_activity;` | 当前总连接数 |

### pg_size - 查看大小

**基础用法**:
```bash
SELECT %{函数}%('%{对象}%');
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看表大小 | `SELECT pg_size_pretty(pg_total_relation_size('users'));` | pg_total_relation_size: 含数据和索引总大小 |
| 查看表物理大小 | `SELECT pg_size_pretty(pg_relation_size('users'));` | pg_relation_size: 仅表数据大小，不含索引 |
| 查看索引大小 | `SELECT pg_size_pretty(pg_indexes_size('users'));` | pg_indexes_size: 表所有索引大小总和 |
| 查看数据库大小 | `SELECT pg_size_pretty(pg_database_size('mydb'));` | pg_database_size: 整个数据库大小 |
| 查看所有表大小 | `SELECT relname, pg_size_pretty(pg_total_relation_size(relid)) FROM pg_catalog.pg_statio_user_tables ORDER BY pg_total_relation_size(relid) DESC;` | 按表大小降序排列 |

---

## 实用场景

### 场景 1: 日常备份脚本

```bash
# 创建备份目录
mkdir -p /backups/postgresql

# 普通备份（SQL 格式）
pg_dump -U postgres -d mydb > /backups/postgresql/mydb_$(date +%Y%m%d).sql

# 压缩备份
pg_dump -U postgres -d mydb | gzip > /backups/postgresql/mydb_$(date +%Y%m%d).sql.gz

# 自定义格式备份（支持并行恢复）
pg_dump -U postgres -d mydb -Fc > /backups/postgresql/mydb_$(date +%Y%m%d).dump

# 全量备份
pg_dumpall -U postgres > /backups/postgresql/all_$(date +%Y%m%d).sql

# 保留最近 7 天的备份
find /backups/postgresql -name "*.sql" -mtime +7 -delete
find /backups/postgresql -name "*.dump" -mtime +7 -delete
```

### 场景 2: 恢复数据库

```bash
# 从 SQL 文件恢复
psql -U postgres -d mydb < /backups/postgresql/mydb_20260401.sql

# 从压缩文件恢复
gunzip < /backups/postgresql/mydb_20260401.sql.gz | psql -U postgres -d mydb

# 从自定义格式恢复
pg_restore -U postgres -d mydb -Fc /backups/postgresql/mydb_20260401.dump

# 创建新数据库并恢复
pg_restore -U postgres -C -d postgres /backups/postgresql/mydb_20260401.dump
```

### 场景 3: 性能优化

```bash
# 定期维护（建议在低峰期执行）
VACUUM ANALYZE;

# 对特定表进行维护
VACUUM ANALYZE users;

# 查看慢查询
SELECT pid, query, query_start, now() - query_start AS duration
FROM pg_stat_activity
WHERE (now() - query_start) > interval '5 minutes'
AND state = 'active';

# 杀掉慢查询
SELECT pg_cancel_backend(1234);

# 强制终止（如果 cancel 不生效）
SELECT pg_terminate_backend(1234);

# 查看表和索引大小
SELECT relname, pg_size_pretty(pg_total_relation_size(relid)) AS total_size
FROM pg_catalog.pg_statio_user_tables
ORDER BY pg_total_relation_size(relid) DESC;
```

### 场景 4: 用户权限管理

```bash
# 创建应用用户
CREATE USER appuser WITH PASSWORD 'StrongPassword123';

# 授予数据库权限
GRANT CONNECT ON DATABASE mydb TO appuser;
GRANT TEMPORARY ON DATABASE mydb TO appuser;

# 授予表权限
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO appuser;

# 授予序列权限（对于 SERIAL 类型的字段）
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO appuser;

# 修改默认权限（对新创建的表也生效）
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO appuser;
```

---

## 命令速查表

| 操作 | 命令 | 说明 |
|------|------|------|
| 连接数据库 | `psql -U postgres -d mydb` | 连接 PostgreSQL 数据库 |
| 备份数据库 | `pg_dump -U postgres -d mydb > backup.sql` | 备份数据库 |
| 恢复数据库 | `pg_restore -U postgres -d mydb backup.dump` | 恢复数据库 |
| 全量备份 | `pg_dumpall -U postgres > all.sql` | 备份所有数据库 |
| 创建表 | `CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(100));` | 创建数据表 |
| 创建索引 | `CREATE INDEX idx_name ON users(name);` | 创建 B-tree 索引 |
| 创建用户 | `CREATE USER appuser WITH PASSWORD 'pass';` | 创建数据库用户 |
| 授予权限 | `GRANT ALL ON mydb TO appuser;` | 授予用户权限 |
| 分析查询 | `EXPLAIN ANALYZE SELECT * FROM users;` | 分析查询性能 |
| 查看进程 | `SELECT * FROM pg_stat_activity;` | 查看数据库连接 |
| 杀掉查询 | `SELECT pg_cancel_backend(pid);` | 取消慢查询 |
| 维护表 | `VACUUM ANALYZE users;` | 回收空间并更新统计 |
| 重建索引 | `REINDEX INDEX idx_name;` | 重建索引 |
| 导出数据 | `COPY users TO '/tmp/users.csv'` | 导出数据到 CSV |
| 导入数据 | `COPY users FROM '/tmp/users.csv'` | 从 CSV 导入 |
| 查看大小 | `SELECT pg_size_pretty(pg_total_relation_size('users'));` | 查看表大小 |

---

## 相关资源

- [快速开始指南](../quick-start.md)
- [Linux 命令文档](../linux-commands/README.md)
- [MySQL 命令文档](../MySQL 命令/README.md)
- [Docker 命令文档](../Docker 命令/README.md)
- [完整命令参考表](../../references/commands-reference.md)