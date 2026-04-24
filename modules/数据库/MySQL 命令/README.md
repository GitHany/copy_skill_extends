# MySQL 命令文档

MySQL 数据库完整参考文档。

## 📚 目录

- [连接管理](#连接管理)
- [数据库操作](#数据库操作)
- [表操作](#表操作)
- [用户管理](#用户管理)
- [数据查询](#数据查询)
- [数据操作](#数据操作)
- [索引操作](#索引操作)
- [备份恢复](#备份恢复)
- [性能分析](#性能分析)
- [维护优化](#维护优化)

---

## 连接管理

### mysql - 连接数据库

**基础用法**:
```bash
mysql -u %{用户名}% -p%{密码}% -h %{主机}% -P %{端口}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 连接本地数据库 | `mysql -u root -p` | -u: 用户名(示例: root); -p: 密码(输入交互式); 无主机默认 localhost |
| 连接远程数据库 | `mysql -u root -p -h 192.168.1.100 -P 3306` | -u: 用户名(示例: root); -p: 密码; -h: 主机地址(示例: 192.168.1.100); -P: 端口(示例: 3306) |
| 指定数据库连接 | `mysql -u root -p -D mydb` | -u: 用户名(示例: root); -p: 密码; -D: 数据库名(示例: mydb) |
| 执行 SQL 文件 | `mysql -u root -p < backup.sql` | 重定向 SQL 文件(示例: backup.sql) 执行批量操作 |
| 带字符集连接 | `mysql -u root -p --default-character-set=utf8mb4` | --default-character-set: 字符集(示例: utf8mb4) 解决中文乱码 |

---

## 数据库操作

### CREATE DATABASE - 创建数据库

**基础用法**:
```bash
CREATE DATABASE %{数据库名}% CHARACTER SET %{字符集}% COLLATE %{排序规则}%;
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建数据库 | `CREATE DATABASE mydb;` | 数据库名(示例: mydb); 默认字符集 |
| 创建 UTF8 数据库 | `CREATE DATABASE mydb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;` | CHARACTER SET: 字符集(示例: utf8mb4); COLLATE: 排序规则(示例: utf8mb4_unicode_ci) |
| 查看所有数据库 | `SHOW DATABASES;` | 列出所有数据库 |
| 选择数据库 | `USE mydb;` | 数据库名(示例: mydb); 切换当前数据库 |
| 删除数据库 | `DROP DATABASE mydb;` | 数据库名(示例: mydb); 删除时无确认提示 |
| 修改数据库字符集 | `ALTER DATABASE mydb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;` | 数据库名(示例: mydb); 字符集(示例: utf8mb4); 排序规则(示例: utf8mb4_unicode_ci) |

---

## 表操作

### CREATE TABLE - 创建表

**基础用法**:
```bash
CREATE TABLE %{表名}% (%{字段定义}%);
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建简单表 | `CREATE TABLE users (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100));` | 表名(示例: users); 字段: id 自增主键(INT), name 字符串(VARCHAR 100) |
| 创建完整表 | `CREATE TABLE users (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100) NOT NULL, email VARCHAR(255) UNIQUE, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);` | 表名(示例: users); 字段: id 主键自增, name 非空, email 唯一, created_at 自动时间戳 |
| 查看所有表 | `SHOW TABLES;` | 查看当前数据库所有表 |
| 查看表结构 | `DESC table_name;` | 表名(示例: users); 显示字段名/类型/约束 |
| 查看建表语句 | `SHOW CREATE TABLE table_name;` | 表名(示例: users); 显示完整 CREATE 语句 |
| 修改表名 | `RENAME TABLE old_name TO new_name;` | 旧表名(示例: old_name); 新表名(示例: new_name) |
| 删除表 | `DROP TABLE table_name;` | 表名(示例: users); 删除后不可恢复 |
| 添加字段 | `ALTER TABLE table_name ADD COLUMN new_col VARCHAR(50);` | 表名(示例: users); 字段名(示例: phone); 字段类型(示例: VARCHAR(50)) |
| 修改字段 | `ALTER TABLE table_name MODIFY COLUMN col_name VARCHAR(100);` | 表名(示例: users); 字段名(示例: name); 新类型(示例: VARCHAR(100)) |

---

## 用户管理

### CREATE USER - 用户管理

**基础用法**:
```bash
CREATE USER '%{用户名}%'@'%{主机}%' IDENTIFIED BY '%{密码}%';
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建本地用户 | `CREATE USER 'appuser'@'localhost' IDENTIFIED BY 'password123';` | 用户名(示例: appuser); 主机(示例: localhost); 密码(示例: password123) |
| 创建远程用户 | `CREATE USER 'appuser'@'%' IDENTIFIED BY 'password123';` | 用户名(示例: appuser); 主机(示例: %) 允许任意主机; 密码(示例: password123) |
| 授予所有权限 | `GRANT ALL PRIVILEGES ON mydb.* TO 'appuser'@'localhost';` | 数据库名(示例: mydb); 用户名(示例: appuser); 主机(示例: localhost); 授予所有库所有表权限 |
| 授予特定权限 | `GRANT SELECT, INSERT, UPDATE ON mydb.* TO 'appuser'@'localhost';` | 权限(示例: SELECT, INSERT, UPDATE); 数据库名(示例: mydb); 用户名(示例: appuser) |
| 撤销权限 | `REVOKE DELETE ON mydb.* FROM 'appuser'@'localhost';` | 权限(示例: DELETE); 数据库名(示例: mydb); 用户名(示例: appuser) |
| 刷新权限 | `FLUSH PRIVILEGES;` | 使权限更改立即生效 |
| 查看用户权限 | `SHOW GRANTS FOR 'appuser'@'localhost';` | 用户名(示例: appuser); 主机(示例: localhost); 查看完整权限 |
| 删除用户 | `DROP USER 'appuser'@'localhost';` | 用户名(示例: appuser); 主机(示例: localhost) |
| 修改用户密码 | `ALTER USER 'appuser'@'localhost' IDENTIFIED BY 'newpassword';` | 用户名(示例: appuser); 主机(示例: localhost); 新密码(示例: newpassword) |

---

## 数据查询

### SELECT - 查询数据

**基础用法**:
```bash
SELECT %{字段}% FROM %{表名}% WHERE %{条件}%;
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查询所有字段 | `SELECT * FROM users;` | 【常用】* 表示所有字段; 表名(示例: users) |
| 查询指定字段 | `SELECT id, name, email FROM users;` | 【常用】字段列表(示例: id, name, email); 表名(示例: users) |
| 带条件查询 | `SELECT * FROM users WHERE id = 1;` | 【常用】表名(示例: users); 条件(示例: id = 1) |
| 模糊查询 | `SELECT * FROM users WHERE name LIKE '%张%';` | 【常用】表名(示例: users); 字段(示例: name); 关键字(示例: 张); % 匹配任意字符 |
| 排序查询 | `SELECT * FROM users ORDER BY created_at DESC;` | 【常用】表名(示例: users); 字段(示例: created_at); 方式(示例: DESC 降序, ASC 升序) |
| 分页查询 | `SELECT * FROM users LIMIT 10 OFFSET 20;` | 【常用】表名(示例: users); 条数(示例: 10); 偏移量(示例: 20) |
| 聚合统计 | `SELECT COUNT(*), AVG(age) FROM users WHERE status = 1;` | 【常用】COUNT 计数, AVG 平均值; 表名(示例: users); 条件(示例: status = 1) |
| 分组查询 | `SELECT department, COUNT(*) FROM employees GROUP BY department;` | 分组字段(示例: department); COUNT 统计每组数量; 表名(示例: employees) |
| 多表连接 | `SELECT u.name, o.total FROM users u JOIN orders o ON u.id = o.user_id;` | 【常用】字段(示例: u.name, o.total); 表1(示例: users 别名 u); 连接类型(示例: LEFT/INNER/RIGHT); 表2(示例: orders 别名 o); 关联字段(示例: id) |
| 子查询 | `SELECT * FROM users WHERE id IN (SELECT user_id FROM orders WHERE total > 100);` | 【常用】表名(示例: users); 字段(示例: id); 子查询字段(示例: user_id); 子查询表(示例: orders); 子查询条件(示例: total > 100) |

---

## 数据操作

### INSERT UPDATE DELETE - 数据操作

**基础用法**:
```bash
INSERT INTO %{表名}% (%{字段}%) VALUES (%{值}%);
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 插入单条数据 | `INSERT INTO users (name, email) VALUES ('张三', 'zhang@example.com');` | 【常用】表名(示例: users); 字段(示例: name, email); 值(示例: '张三', 'zhang@example.com') |
| 批量插入 | `INSERT INTO users (name, email) VALUES ('张三', 'zhang@example.com'), ('李四', 'li@example.com');` | 【常用】表名(示例: users); 字段(示例: name, email); 多组值用逗号分隔 |
| 更新数据 | `UPDATE users SET name = '新名字' WHERE id = 1;` | 【常用】表名(示例: users); 字段(示例: name); 新值(示例: '新名字'); 条件(示例: id = 1) |
| 删除数据 | `DELETE FROM users WHERE id = 1;` | 【常用】表名(示例: users); 条件(示例: id = 1); 无 WHERE 会删除所有数据 |
| 清空表数据 | `TRUNCATE TABLE users;` | 表名(示例: users); 删除并重建表, AUTO_INCREMENT 重置 |
| 替换数据 | `REPLACE INTO users (id, name) VALUES (1, '新名字');` | 【常用】表名(示例: users); 字段(示例: id, name); 值(示例: 1, '新名字'); 存在则删除再插入 |
| ON DUPLICATE KEY UPDATE | `INSERT INTO users (id, name) VALUES (1, '新名字') ON DUPLICATE KEY UPDATE name = '新名字';` | 【常用】表名(示例: users); 字段(示例: id, name); 值(示例: 1, '新名字'); 冲突时更新 |

---

## 索引操作

### CREATE INDEX - 索引管理

**基础用法**:
```bash
CREATE %{索引类型}% INDEX %{索引名}% ON %{表名}% (%{字段}%);
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建普通索引 | `CREATE INDEX idx_name ON users(name);` | 索引名(示例: idx_name); 表名(示例: users); 字段(示例: name) |
| 创建唯一索引 | `CREATE UNIQUE INDEX idx_email ON users(email);` | 索引名(示例: idx_email); 表名(示例: users); 字段(示例: email); 不允许重复值 |
| 创建全文索引 | `CREATE FULLTEXT INDEX idx_content ON articles(content);` | 索引名(示例: idx_content); 表名(示例: articles); 字段(示例: content); 用于文本搜索 |
| 创建复合索引 | `CREATE INDEX idx_name_status ON users(name, status);` | 索引名(示例: idx_name_status); 表名(示例: users); 字段1(示例: name); 字段2(示例: status) |
| 查看表索引 | `SHOW INDEX FROM users;` | 表名(示例: users); 显示所有索引信息 |
| 删除索引 | `DROP INDEX idx_name ON users;` | 索引名(示例: idx_name); 表名(示例: users) |
| 添加主键索引 | `ALTER TABLE users ADD PRIMARY KEY (id);` | 表名(示例: users); 字段(示例: id); 主键自动唯一非空 |

---

## 备份恢复

### mysqldump - 备份数据库

**基础用法**:
```bash
mysqldump -u %{用户名}% -p%{密码}% %{数据库名}% > %{备份文件}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 备份单个数据库 | `mysqldump -u root -p mydb > mydb_backup.sql` | 数据库名(示例: mydb); 导出为 SQL 文件(示例: mydb_backup.sql) |
| 备份所有数据库 | `mysqldump -u root -p --all-databases > all_backup.sql` | --all-databases 备份所有数据库(示例: all_backup.sql) |
| 备份多个表 | `mysqldump -u root -p mydb users orders > tables_backup.sql` | 数据库名(示例: mydb); 表名(示例: users, orders); 指定表备份 |
| 压缩备份 | `mysqldump -u root -p mydb \| gzip > mydb_backup.sql.gz` | 数据库名(示例: mydb); 管道压缩节省空间(示例: mydb_backup.sql.gz) |
| 远程备份 | `mysqldump -u root -p -h 192.168.1.100 mydb > remote_backup.sql` | 用户名(示例: root); 密码(示例: password); 主机(示例: 192.168.1.100); 数据库名(示例: mydb) |
| 仅结构备份 | `mysqldump -u root -p --no-data mydb > mydb_schema.sql` | --no-data 仅导出表结构(示例: mydb_schema.sql) |
| 仅数据备份 | `mysqldump -u root -p --no-create-info mydb > mydb_data.sql` | --no-create-info 仅导出数据(示例: mydb_data.sql) |

### mysql restore - 恢复数据库

**基础用法**:
```bash
mysql -u root -p mydb < backup.sql
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 恢复数据库 | `mysql -u root -p mydb < mydb_backup.sql` | 数据库名(示例: mydb); 导入 SQL 文件(示例: mydb_backup.sql) |
| 压缩文件恢复 | `gunzip < mydb_backup.sql.gz \| mysql -u root -p mydb` | 解压后管道导入; 数据库名(示例: mydb) |
| 恢复所有数据库 | `mysql -u root -p < all_backup.sql` | 导入全量备份(示例: all_backup.sql); 包括所有数据库 |

---

## 性能分析

### EXPLAIN - 查询分析

**基础用法**:
```bash
EXPLAIN %{SQL语句}%;
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 分析 SELECT | `EXPLAIN SELECT * FROM users WHERE id = 1;` | 表名(示例: users); 条件(示例: id = 1); 查看执行计划 |
| 详细分析 | `EXPLAIN ANALYZE SELECT * FROM users WHERE id = 1;` | 表名(示例: users); 条件(示例: id = 1); 实际执行并显示耗时(MySQL 8.0+) |
| 分析 INSERT | `EXPLAIN INSERT INTO users (name) VALUES ('test');` | 表名(示例: users); 字段(示例: name); 值(示例: 'test') |
| 分析 UPDATE | `EXPLAIN UPDATE users SET name = 'test' WHERE id = 1;` | 表名(示例: users); 字段(示例: name); 新值(示例: 'test'); 条件(示例: id = 1) |
| 查看慢查询 | `SHOW VARIABLES LIKE 'slow_query_log';` | 查看慢查询日志是否开启 |
| 查看进程列表 | `SHOW PROCESSLIST;` | 查看当前所有连接和查询状态 |
| 杀死进程 | `KILL 123;` | 进程ID(示例: 123); 从 SHOW PROCESSLIST 获取; 终止查询 |
| 查看连接数 | `SHOW STATUS LIKE 'Threads_connected';` | 查看当前连接数 |

---

## 维护优化

### OPTIMIZE TABLE - 维护操作

**基础用法**:
```bash
OPTIMIZE TABLE %{表名}%;
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 优化表 | `OPTIMIZE TABLE users;` | 表名(示例: users); 回收空闲空间, 重建索引 |
| 修复表 | `REPAIR TABLE users;` | 表名(示例: users); 修复损坏的表 |
| 检查表 | `CHECK TABLE users;` | 表名(示例: users); 检查表是否有错误 |
| 分析表 | `ANALYZE TABLE users;` | 表名(示例: users); 更新表统计信息, 帮助优化器 |
| 查看表状态 | `SHOW TABLE STATUS LIKE 'users';` | 表名(示例: users); 显示表详细信息 |
| 查看数据库大小 | `SELECT table_schema, SUM(data_length + index_length) FROM information_schema.tables GROUP BY table_schema;` | 统计每个数据库总大小(字节) |
| 查看表大小 | `SELECT table_name, (data_length + index_length) FROM information_schema.tables WHERE table_schema = 'mydb';` | 数据库名(示例: mydb); 查看各表大小 |
| 查看冗余索引 | `SELECT * FROM mysql.index_stats WHERE db = 'mydb';` | 数据库名(示例: mydb); MySQL 8.0+ 查看索引统计 |