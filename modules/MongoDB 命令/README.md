# MongoDB 命令文档

MongoDB 数据库完整参考文档。

## 目录

- [MongoDB 核心命令](#mongodb-核心命令)
- [数据库操作](#数据库操作)
- [集合操作](#集合操作)
- [CRUD 操作](#crud-操作)
- [聚合操作](#聚合操作)
- [索引管理](#索引管理)
- [用户认证与角色](#用户认证与角色)
- [MongoDB 工具](#mongodb-工具)
- [Mongoose ODM](#mongoose-odm)
- [复制集与分片](#复制集与分片)

---

## MongoDB 核心命令

### mongod - 启动 MongoDB 服务

**基础用法**:
```bash
mongod --dbpath %{数据目录}% --port %{端口}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动服务 | `mongod --dbpath /data/db --port 27017` | --dbpath: 数据目录(示例: /data/db); --port: 端口(示例: 27017) |
| 带认证启动 | `mongod --dbpath /data/db --port 27017 --auth` | --auth: 启用认证(示例: 安全模式) |
| 副本集启动 | `mongod --dbpath /data/db --port 27017 --replSet rs0` | --replSet: 副本集名称(示例: rs0) |
| 配置文件启动 | `mongod --config /etc/mongod.conf` | --config: 配置文件路径(示例: /etc/mongod.conf) |
| 日志输出到文件 | `mongod --dbpath /data/db --logpath /var/log/mongodb.log --fork` | --logpath: 日志文件(示例: /var/log/mongodb.log); --fork: 后台运行 |

---

### mongosh / mongo - 连接数据库

**基础用法**:
```bash
mongosh "mongodb://%{主机}%:%{端口}%/%{数据库}%"
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 连接本地 | `mongosh` | 默认连接 localhost:27017 |
| 连接远程 | `mongosh "mongodb://192.168.1.100:27017"` | 主机(示例: 192.168.1.100); 端口(示例: 27017) |
| 指定数据库 | `mongosh "mongodb://localhost:27017/mydb"` | 数据库名(示例: mydb) |
| 带用户名密码 | `mongosh "mongodb://user:password@localhost:27017/mydb"` | 用户名(示例: user); 密码(示例: password); 数据库(示例: mydb) |
| 带认证库 | `mongosh "mongodb://user:password@localhost:27017/mydb?authSource=admin"` | authSource: 认证数据库(示例: admin) |

---

## 数据库操作

### use / show / db - 数据库管理

**基础用法**:
```bash
use %{数据库名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 切换数据库 | `use mydb` | 数据库名(示例: mydb); 不存在则创建 |
| 显示所有数据库 | `show dbs` | 需要至少一个文档才会显示新数据库 |
| 显示当前数据库 | `db` | 查看当前操作的数据库 |
| 删除数据库 | `db.dropDatabase()` | 删除当前数据库(示例: mydb) |
| 创建集合 | `db.createCollection('users')` | 集合名(示例: users) |
| 显示集合 | `show collections` | 查看当前数据库所有集合 |
| 显示用户 | `show users` | 查看当前数据库用户 |
| 显示角色 | `show roles` | 查看所有内置角色 |

---

## 集合操作

### createCollection / drop / rename - 集合管理

**基础用法**:
```bash
db.createCollection('%{集合名}%')
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建集合 | `db.createCollection('users')` | 集合名(示例: users) |
| 创建带选项集合 | `db.createCollection('logs', {capped: true, size: 10000000})` | capped: 是否上限集合(示例: true); size: 大小(示例: 10000000 字节) |
| 删除集合 | `db.users.drop()` | 集合名(示例: users); 删除后不可恢复 |
| 重命名集合 | `db.users.renameCollection('new_users')` | 旧名(示例: users); 新名(示例: new_users) |
| 查看集合统计 | `db.users.stats()` | 集合名(示例: users); 查看大小、索引等信息 |
| 查看集合大小 | `db.users.dataSize()` | 集合名(示例: users); 查看数据大小 |
| 清空集合 | `db.users.remove({})` | 集合名(示例: users); 删除所有文档 |

---

## CRUD 操作

### insert / find - 插入和查询

**基础用法**:
```bash
db.%{集合}%.insertOne(%{文档}%)
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 插入单条 | `db.users.insertOne({name: '张三', age: 25})` | 集合(示例: users); 文档(示例: {name: '张三', age: 25}) |
| 插入多条 | `db.users.insertMany([{name: '张三'}, {name: '李四'}])` | 集合(示例: users); 文档数组 |
| 插入并返回 | `db.users.insert({name: '张三'}, {writeConcern: {w: 'majority'}})` | 集合(示例: users); writeConcern 控制写入确认 |
| 查询所有 | `db.users.find()` | 集合(示例: users); 返回所有文档 |
| 条件查询 | `db.users.find({age: {$gte: 18}})` | 集合(示例: users); age >= 18 |
| 查询单条 | `db.users.findOne({name: '张三'})` | 集合(示例: users); 返回第一条匹配文档 |
| 投影查询 | `db.users.find({}, {name: 1, _id: 0})` | 只返回 name 字段(示例: users) |
| 限制条数 | `db.users.find().limit(10)` | 限制返回条数(示例: 10) |
| 跳过条数 | `db.users.find().skip(20)` | 跳过前N条(示例: 20) |
| 排序查询 | `db.users.find().sort({age: -1})` | 按 age 降序(示例: users); 1 升序, -1 降序 |
| 统计数量 | `db.users.countDocuments({age: {$gte: 18}})` | 条件统计(示例: users) |
| 存在判断 | `db.users.find({name: {$exists: true}})` | 查询存在 name 字段的文档 |

---

### update - 更新操作

**基础用法**:
```bash
db.%{集合}%.updateOne(%{条件}%, {$set: %{更新}%})
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 更新单条 | `db.users.updateOne({name: '张三'}, {$set: {age: 30}})` | 集合(示例: users); 条件(示例: name='张三'); 更新(示例: age=30) |
| 更新多条 | `db.users.updateMany({status: 'inactive'}, {$set: {status: 'active'}})` | 集合(示例: users); 条件(示例: status='inactive'); 批量更新 |
| 替换文档 | `db.users.replaceOne({name: '张三'}, {name: '张三', age: 30, city: '北京'})` | 完全替换除 _id 外的字段 |
| 字段增值 | `db.users.updateOne({name: '张三'}, {$inc: {age: 1}})` | $inc: 增加字段值(示例: users); age +1 |
| 字段重命名 | `db.users.updateMany({}, {$rename: {old_name: 'new_name'}})` | $rename: 重命名字段 |
| 数组添加 | `db.users.updateOne({name: '张三'}, {$push: {tags: 'vip'}})` | $push: 添加数组元素(示例: users) |
| 数组删除 | `db.users.updateOne({name: '张三'}, {$pull: {tags: 'vip'}})` | $pull: 删除数组元素(示例: users) |
| upsert 更新 | `db.users.updateOne({name: '张三'}, {$set: {age: 30}}, {upsert: true})` | 不存在则插入(示例: users) |

---

### delete - 删除操作

**基础用法**:
```bash
db.%{集合}%.deleteOne(%{条件}%)
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 删除单条 | `db.users.deleteOne({name: '张三'})` | 集合(示例: users); 删除第一条匹配 |
| 删除多条 | `db.users.deleteMany({status: 'inactive'})` | 集合(示例: users); 删除所有匹配 |
| 删除所有 | `db.users.deleteMany({})` | 集合(示例: users); 删除集合中所有文档 |
| 按 ID 删除 | `db.users.deleteOne({_id: ObjectId('507f1f77bcf86cd799439011')})` | 使用 ObjectId(示例: users) |

---

## 聚合操作

### aggregate - 聚合管道

**基础用法**:
```bash
db.%{集合}%.aggregate([%{管道操作}%])
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 分组统计 | `db.orders.aggregate([{$group: {_id: '$customer', total: {$sum: '$amount'}}}])` | 按 customer 分组求和(示例: orders) |
| 过滤统计 | `db.orders.aggregate([{$match: {status: 'completed'}}, {$group: {_id: '$customer', total: {$sum: '$amount'}}}])` | 先过滤再分组(示例: orders) |
| 字段投影 | `db.users.aggregate([{$project: {name: 1, age: 1, _id: 0}}])` | 只显示指定字段(示例: users) |
| 排序分组 | `db.orders.aggregate([{$sort: {amount: -1}}, {$limit: 5}])` | 排序后取前5(示例: orders) |
| 数组展开 | `db.users.aggregate([{$unwind: '$tags'}])` | 展开数组字段(示例: users) |
| 多字段分组 | `db.orders.aggregate([{$group: {_id: {customer: '$customer', month: '$month'}, total: {$sum: '$amount'}}}])` | 复合分组(示例: orders) |
| 累计求和 | `db.sales.aggregate([{$group: {_id: null, total: {$sum: '$amount'}}}, {$project: {total: 1}}])` | 求总和(示例: sales) |
| 平均计算 | `db.users.aggregate([{$group: {_id: '$city', avgAge: {$avg: '$age'}}}])` | 按城市计算平均年龄(示例: users) |
| 最大最小 | `db.orders.aggregate([{$group: {_id: '$customer', maxAmount: {$max: '$amount'}}}])` | 求最大值(示例: orders) |
| 数组聚合 | `db.users.aggregate([{$group: {_id: '$city', skills: {$addToSet: '$skill'}}}])` | 去重收集(示例: users) |

---

## 索引管理

### createIndex / dropIndexes - 索引操作

**基础用法**:
```bash
db.%{集合}%.createIndex(%{字段}%)
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建单字段索引 | `db.users.createIndex({name: 1})` | 集合(示例: users); name 升序索引 |
| 创建复合索引 | `db.users.createIndex({name: 1, age: -1})` | name 升序, age 降序(示例: users) |
| 创建唯一索引 | `db.users.createIndex({email: 1}, {unique: true})` | email 唯一约束(示例: users) |
| 创建稀疏索引 | `db.users.createIndex({phone: 1}, {sparse: true})` | 仅索引非空值(示例: users) |
| 创建文本索引 | `db.articles.createIndex({content: 'text'})` | 全文搜索索引(示例: articles) |
| 创建TTL索引 | `db.logs.createIndex({createdAt: 1}, {expireAfterSeconds: 3600})` | 自动过期(示例: logs); 3600秒后删除 |
| 查看索引 | `db.users.getIndexes()` | 集合(示例: users); 查看所有索引 |
| 删除索引 | `db.users.dropIndex('name_1')` | 删除指定索引(示例: users) |
| 删除所有索引 | `db.users.dropIndexes()` | 删除所有非_id索引(示例: users) |
| 后台建索引 | `db.users.createIndex({email: 1}, {background: true})` | 后台创建不阻塞读写(示例: users) |

---

## 用户认证与角色

### createUser / grantRoles - 用户管理

**基础用法**:
```bash
db.createUser({user: '%{用户名}%', pwd: '%{密码}%', roles: [%{角色}%]})
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建管理员 | `db.createUser({user: 'admin', pwd: 'password', roles: [{role: 'root', db: 'admin'}]})` | 超级管理员(示例: admin) |
| 创建用户 | `db.createUser({user: 'appuser', pwd: 'password', roles: [{role: 'readWrite', db: 'mydb'}]})` | 读写权限(示例: appuser); 数据库(示例: mydb) |
| 创建只读用户 | `db.createUser({user: 'reader', pwd: 'password', roles: [{role: 'read', db: 'mydb'}]})` | 只读权限(示例: reader) |
| 更新用户角色 | `db.updateUser('appuser', {roles: [{role: 'readWrite', db: 'mydb'}]})` | 更新用户权限(示例: appuser) |
| 授予角色 | `db.grantRolesToUser('appuser', [{role: 'read', db: 'otherdb'}])` | 授予额外角色(示例: appuser) |
| 撤销角色 | `db.revokeRolesFromUser('appuser', [{role: 'read', db: 'otherdb'}])` | 撤销角色(示例: appuser) |
| 删除用户 | `db.dropUser('appuser')` | 删除用户(示例: appuser) |
| 修改密码 | `db.changeUserPassword('appuser', 'newpassword')` | 修改密码(示例: appuser) |
| 查看用户 | `db.getUser('appuser')` | 查看用户信息(示例: appuser) |
| 查看所有用户 | `db.getUsers()` | 查看数据库所有用户 |

---

## MongoDB 工具

### mongodump / mongorestore - 备份恢复

**基础用法**:
```bash
mongodump --uri="mongodb://%{主机}%:%{端口}%/%{数据库}%" --out=%{输出目录}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 备份数据库 | `mongodump --db=mydb --out=/backup` | 数据库(示例: mydb); 输出目录(示例: /backup) |
| 备份集合 | `mongodump --db=mydb --collection=users --out=/backup` | 集合(示例: users) |
| 带认证备份 | `mongodump --db=mydb --username=admin --password=password --authenticationDatabase=admin --out=/backup` | 认证备份(示例: mydb) |
| 压缩备份 | `mongodump --db=mydb --gzip --out=/backup` | gzip 压缩(示例: mydb) |
| 恢复数据库 | `mongorestore --db=mydb --drop /backup/mydb` | 恢复(示例: mydb); --drop 先删除现有数据 |
| 带认证恢复 | `mongorestore --db=mydb --username=admin --password=password --authenticationDatabase=admin /backup/mydb` | 认证恢复(示例: mydb) |
| 压缩恢复 | `mongorestore --db=mydb --gzip /backup/mydb` | gzip 解压恢复(示例: mydb) |

---

### mongoexport / mongoimport - 数据导入导出

**基础用法**:
```bash
mongoexport --uri="mongodb://%{主机}%:%{端口}%/%{数据库}%" --collection=%{集合}% --out=%{输出文件}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 导出 JSON | `mongoexport --db=mydb --collection=users --out=users.json` | 导出为 JSON(示例: users) |
| 导出 CSV | `mongoexport --db=mydb --collection=users --type=csv --fields=name,age --out=users.csv` | CSV 格式导出(示例: users) |
| 带查询导出 | `mongoexport --db=mydb --collection=users --query='{"age": {$gte: 18}}' --out=adults.json` | 条件导出(示例: users) |
| 导入 JSON | `mongoimport --db=mydb --collection=users --file=users.json` | 导入 JSON(示例: users) |
| 导入 CSV | `mongoimport --db=mydb --collection=users --type=csv --headerline --file=users.csv` | CSV 导入(示例: users) |
| 导入并清空 | `mongoimport --db=mydb --collection=users --file=users.json --drop` | --drop 先清空(示例: users) |
| 导入并upsert | `mongoimport --db=mydb --collection=users --file=users.json --upsertFields=name` | 存在则更新(示例: users) |

---

### mongostat / mongotop - 监控工具

**基础用法**:
```bash
mongostat --uri="mongodb://%{主机}%:%{端口}%"
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看状态 | `mongostat --uri="mongodb://localhost:27017"` | 默认每1秒刷新(示例: localhost) |
| 指定次数 | `mongostat --uri="mongodb://localhost:27017" --count 10` | 显示10次(示例: localhost) |
| 间隔2秒 | `mongostat --uri="mongodb://localhost:27017" --rowcount 20 --interval 2000` | 2秒间隔显示20行(示例: localhost) |
| 查看热点 | `mongotop --uri="mongodb://localhost:27017"` | 查看集合读写时间(示例: localhost) |
| 指定间隔 | `mongotop --uri="mongodb://localhost:27017" 5` | 每5秒报告一次(示例: localhost) |
| 只看锁 | `mongotop --uri="mongodb://localhost:27017" --locks` | 查看锁信息(示例: localhost) |

---

## Mongoose ODM

### mongoose.connect / Schema - 连接与建模

**基础用法**:
```javascript
mongoose.connect('mongodb://%{主机}%:%{端口}%/%{数据库}%')
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 基本连接 | `mongoose.connect('mongodb://localhost:27017/mydb')` | 主机(示例: localhost); 端口(示例: 27017); 数据库(示例: mydb) |
| 带认证连接 | `mongoose.connect('mongodb://user:password@localhost:27017/mydb?authSource=admin')` | 用户名(示例: user); 密码(示例: password); authSource(示例: admin) |
| 连接选项 | `mongoose.connect('mongodb://localhost:27017/mydb', {useNewUrlParser: true, useUnifiedTopology: true})` | 新解析器(示例: mydb) |
| 断开连接 | `mongoose.disconnect()` | 关闭连接 |
| 定义 Schema | `const userSchema = new mongoose.Schema({ name: String, age: Number })` | 字段类型(示例: name String, age Number) |
| 严格模式 | `new mongoose.Schema({name: String}, {strict: false})` | 允许额外字段(示例: Schema) |

---

### Model methods - 模型方法

**基础用法**:
```javascript
const User = mongoose.model('User', userSchema)
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建文档 | `User.create({name: '张三', age: 25})` | 创建并保存(示例: User) |
| 插入单条 | `User.insertOne({name: '张三', age: 25})` | 直接插入(示例: User) |
| 插入多条 | `User.insertMany([{name: '张三'}, {name: '李四'}])` | 批量插入(示例: User) |
| 查询单条 | `User.findOne({name: '张三'})` | 返回第一条(示例: User) |
| 条件查询 | `User.find({age: {$gte: 18}}).select('name age').limit(10)` | 链式调用(示例: User) |
| 按 ID 查询 | `User.findById('507f1f77bcf86cd799439011')` | 使用 ObjectId(示例: User) |
| 排序查询 | `User.find().sort({age: -1}).skip(10).limit(5)` | 链式排序分页(示例: User) |
| 更新单条 | `User.updateOne({name: '张三'}, {$set: {age: 30}})` | 更新第一条(示例: User) |
| 更新多条 | `User.updateMany({status: 'inactive'}, {$set: {status: 'active'}})` | 批量更新(示例: User) |
| 按 ID 更新 | `User.findByIdAndUpdate('507f1f77bcf86cd799439011', {age: 30})` | 查找并更新(示例: User) |
| 查找并删除 | `User.findOneAndDelete({name: '张三'})` | 返回删除的文档(示例: User) |
| 统计数量 | `User.countDocuments({age: {$gte: 18}})` | 条件计数(示例: User) |
| 存在判断 | `User.exists({name: '张三'})` | 返回布尔值(示例: User) |

---

### Middleware / Hooks - 中间件

**基础用法**:
```javascript
schema.pre('save', function(next) {})
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 保存前钩子 | `schema.pre('save', function(next) { this.updatedAt = new Date(); next() })` | 保存前执行(示例: schema) |
| 保存后钩子 | `schema.post('save', function(doc) { console.log('保存完成', doc._id) })` | 保存后执行(示例: schema) |
| 更新前钩子 | `schema.pre('updateOne', function(next) { this.set({updatedAt: new Date()}); next() })` | 更新前执行(示例: schema) |
| 删除前钩子 | `schema.pre('remove', function(next) { console.log('准备删除')(); next() })` | 删除前执行(示例: schema) |
| 验证前钩子 | `schema.pre('validate', function(next) { if (this.age < 0) next(new Error('年龄不能为负')); else next() })` | 验证前修改(示例: schema) |
| find 前钩子 | `schema.pre('find', function() { console.log('执行查询') })` | find 前执行(示例: schema) |
| 错误处理 | `schema.post('save', function(error, doc, next) { if (error) next(error) })` | 错误后处理(示例: schema) |

---

### Population / Refs - 关联查询

**基础用法**:
```javascript
schema.pre('populate', function(next) {})
```

**扩展开例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 定义 ref | `const orderSchema = new mongoose.Schema({ user: {type: mongoose.Schema.Types.ObjectId, ref: 'User'}, amount: Number})` | 关联 User 模型(示例: orderSchema) |
| populate 查询 | `Order.find().populate('user').exec((err, orders) => {})` | 填充关联数据(示例: Order) |
| 指定字段 | `Order.find().populate('user', 'name email').exec()` | 只填充 name 和 email(示例: Order) |
| 条件过滤 | `Order.find().populate({path: 'user', match: {status: 'active'}}).exec()` | 过滤条件(示例: Order) |
| 多级填充 | `User.find().populate({path: 'orders', populate: {path: 'items'}}).exec()` | 嵌套填充(示例: User) |
| 手动 populate | `const order = await Order.findById(id); await order.populate('user')` | 手动调用(示例: Order) |
| 虚拟属性填充 | `userSchema.virtual('orders', {ref: 'Order', localField: '_id', foreignField: 'user', count: true})` | 虚拟字段(示例: userSchema) |

---

### Virtuals - 虚拟属性

**基础用法**:
```javascript
schema.virtual('%{属性名}%').get(function() {})
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 定义虚拟属性 | `userSchema.virtual('fullName').get(function() { return this.firstName + ' ' + this.lastName })` | 组合字段(示例: userSchema) |
| 虚拟 setter | `userSchema.virtual('fullName').set(function(name) { const [first, last] = name.split(' '); this.firstName = first; this.lastName = last })` | 设置器(示例: userSchema) |
| JSON 包含虚拟 | `userSchema.set('toJSON', {virtuals: true}); userSchema.set('toObject', {virtuals: true})` | 序列化时包含(示例: userSchema) |

---

## 复制集与分片

### Replica Set - 复制集

**基础用法**:
```javascript
rs.initiate(%{配置}%)
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 初始化副本集 | `rs.initiate({_id: 'rs0', members: [{_id: 0, host: 'localhost:27017'}]})` | 副本集名称(示例: rs0) |
| 添加副本节点 | `rs.add('192.168.1.101:27017')` | 添加从节点(示例: 192.168.1.101) |
| 添加仲裁节点 | `rs.addArb('192.168.1.102:27017')` | 添加仲裁节点(示例: 192.168.1.102) |
| 查看状态 | `rs.status()` | 查看副本集状态 |
| 查看配置 | `rs.conf()` | 查看副本集配置 |
| 移除节点 | `rs.remove('192.168.1.101:27017')` | 移除节点(示例: 192.168.1.101) |
| 设为优先 | `cfg = rs.conf(); cfg.members[0].priority = 2; rs.reconfig(cfg)` | 设置优先级(示例: cfg) |
| 设为隐藏 | `cfg = rs.conf(); cfg.members[0].hidden = true; rs.reconfig(cfg)` | 隐藏节点(示例: cfg) |
| 故障转移 | `rs.stepDown()` | 触发选举(主节点降级) |

---

### Sharding - 分片集群

**基础用法**:
```bash
mongos --configdb "%{配置服务器}%" --port %{端口}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启用分片 | `sh.enableSharding('mydb')` | 启用数据库分片(示例: mydb) |
| 分片集合 | `sh.shardCollection('mydb.users', {userId: 'hashed'})` | 按 userId 哈希分片(示例: mydb.users) |
| 分片集合范围 | `sh.shardCollection('mydb.orders', {orderId: 1})` | 按 orderId 范围分片(示例: mydb.orders) |
| 添加分片 | `sh.addShard('shard1/192.168.1.101:27017')` | 添加分片副本集(示例: shard1) |
| 查看分片状态 | `sh.status()` | 查看集群分片状态 |
| 查看集群配置 | `db.adminCommand({listShards: 1})` | 列出所有分片 |
| 查看块分布 | `db.adminCommand({getShardDistribution: 1})` | 查看数据块分布 |
| 手动分割块 | `db.adminCommand({split: 'mydb.users', middle: {userId: 5000}})` | 手动分割块(示例: mydb.users) |
| 移动块 | `db.adminCommand({moveChunk: 'mydb.users', find: {userId: 5000}, to: 'shard2'})` | 迁移块(示例: mydb.users) |

---

### Change Streams - 变更流

**基础用法**:
```javascript
db.%{集合}%.watch([%{管道}%])
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 监听集合变更 | `db.users.watch()` | 监听 users 集合所有变更(示例: users) |
| 过滤插入 | `db.users.watch([{$match: {operationType: 'insert'}}])` | 只监听插入操作(示例: users) |
| 过滤更新 | `db.users.watch([{$match: {operationType: {$in: ['update', 'replace']}}}])` | 监听更新和替换(示例: users) |
| 监听数据库 | `db.watch([{$match: {operationType: 'drop'}}])` | 监听数据库级别变更(示例: db) |
| 监听所有变更 | `db.adminCommand({watch: 1})` | 监听所有数据库变更 |
| 恢复 token 监听 | `db.users.watch([], {resumeAfter: {_data: '...'}})` | 从指定 token 恢复(示例: users) |
| 全量变更流 | `db.users.watch([{$match: {operationType: {$in: ['insert', 'update', 'delete', 'replace']}}}])` | 监听 CRUD 所有操作(示例: users) |

---

## Compass GUI 工具

### Compass - MongoDB 官方图形界面

**基础用法**:
连接字符串: `mongodb://%{主机}%:%{端口}%`

**扩展示例**:

| 场景 | 说明 |
|------|------|
| 基本连接 | 输入 Hostname 和 Port，默认 localhost:27017 |
| 认证连接 | 选择 "Password" 认证方式，填写用户名密码和认证数据库 |
| SSL 连接 | 在连接选项中启用 SSL，选择相应证书 |
| 副本集连接 | 使用副本集种子列表: host1:27017,host2:27017 |
| 分片集群连接 | 连接到 mongos 路由器，默认端口 27017 |
| 查询编辑器 | 使用可视化查询构建器或直接编写聚合管道 |
| 聚合构建器 | 拖拽式的聚合管道构建器，支持 $match, $group, $sort 等 |
| Explain Plan | 查看查询执行计划，分析查询性能 |
| 索引管理 | 可视化创建、删除、重建索引 |
| 数据导入导出 | 支持 JSON、CSV 格式的导入导出 |
| Schema 分析 | 自动分析集合字段类型和数据分布 |