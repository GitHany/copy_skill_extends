# 消息队列与事件驱动架构

消息队列与事件驱动架构完整参考文档，涵盖 RabbitMQ、Kafka、Redis Pub/Sub 及主流云服务（SQS/SNS/EventBridge）。

## 目录

- [RabbitMQ](#rabbitmq)
- [Apache Kafka](#apache-kafka)
- [Redis Pub/Sub](#redis-pubsub)
- [Docker 部署消息队列](#docker-部署消息队列)
- [BullMQ (Node.js)](#bullmq-nodejs)
- [Celery (Python)](#celery-python)
- [AWS SQS](#aws-sqs)
- [AWS SNS](#aws-sns)
- [AWS EventBridge](#aws-eventbridge)
- [命令速查表](#命令速查表)

---

## RabbitMQ

### 基础管理

```bash
# 查看状态
rabbitmqctl status

# 启动/停止应用
rabbitmqctl start_app
rabbitmqctl stop_app

# 重置节点
rabbitmqctl reset
rabbitmqctl force_reset
```

### 队列和交换机

```bash
# 查看队列/交换机/绑定
rabbitmqctl list_queues
rabbitmqctl list_exchanges
rabbitmqctl list_bindings

# 声明队列
rabbitmqctl declare_queue -p / -d my_queue

# 删除队列
rabbitmqctl delete_queue my_queue

# 清空队列消息
rabbitmqctl purge_queue my_queue

# 声明交换机（direct/fanout/topic/headers）
rabbitmqctl declare_exchange -p / my_exchange direct true

# 声明绑定
rabbitmqctl bind_queue -p / -q my_queue -e my_exchange -r my.routing.key
```

### 用户和权限

```bash
# 添加/删除用户
rabbitmqctl add_user admin password123
rabbitmqctl delete_user admin

# 设置管理员标签
rabbitmqctl set_user_tags admin administrator

# 列出所有用户
rabbitmqctl list_users

# 创建虚拟主机
rabbitmqctl add_vhost myvhost
rabbitmqctl delete_vhost myvhost

# 授权权限
rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"
rabbitmqctl list_permissions -p /
```

### 集群管理

```bash
# 查看集群状态
rabbitmqctl cluster_status
```

### 插件管理

```bash
# 启用管理界面
rabbitmq-plugins enable rabbitmq_management

# 列出所有插件
rabbitmq-plugins list

# 启用指定插件
rabbitmq-plugins enable rabbitmq_stomp

# 启动服务器（后台）
rabbitmq-server -detached
```

---

## Apache Kafka

### 主题管理

```bash
# 创建主题
kafka-topics.sh --bootstrap-server localhost:9092 --create \
  --topic my-topic --partitions 3 --replication-factor 1

# 列出所有主题
kafka-topics.sh --bootstrap-server localhost:9092 --list

# 查看主题详情
kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic my-topic

# 删除主题
kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic my-topic

# 修改分区数（只能增加）
kafka-topics.sh --bootstrap-server localhost:9092 --alter \
  --topic my-topic --partitions 6
```

### 生产者与消费者

```bash
# 启动控制台生产者
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic my-topic

# 带 key 的生产者
kafka-console-producer.sh --bootstrap-server localhost:9092 \
  --topic my-topic --property parse.key=true --property key.separator=,

# 启动消费者（从头消费）
kafka-console-consumer.sh --bootstrap-server localhost:9092 \
  --topic my-topic --from-beginning

# 消费者组消费
kafka-console-consumer.sh --bootstrap-server localhost:9092 \
  --topic my-topic --group my-group

# 显示 key 和 value
kafka-console-consumer.sh --bootstrap-server localhost:9092 \
  --topic my-topic --from-beginning \
  --property print.key=true --property key.separator=,
```

### 消费者组

```bash
# 列出所有消费组
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list

# 查看消费组详情
kafka-consumer-groups.sh --bootstrap-server localhost:9092 \
  --describe --group my-group

# 重置偏移量到最早
kafka-consumer-groups.sh --bootstrap-server localhost:9092 \
  --group my-group --topic my-topic \
  --reset-offsets --to-earliest --execute

# 删除消费组
kafka-consumer-groups.sh --bootstrap-server localhost:9092 \
  --delete --group my-group
```

### 配置管理

```bash
# 查看主题配置
kafka-configs.sh --bootstrap-server localhost:9092 \
  --describe --entity-type topics --entity-name my-topic

# 修改保留时间（7天）
kafka-configs.sh --bootstrap-server localhost:9092 \
  --alter --entity-type topics --entity-name my-topic \
  --add-config retention.ms=604800000

# 删除配置
kafka-configs.sh --bootstrap-server localhost:9092 \
  --alter --entity-type topics --entity-name my-topic \
  --delete-config retention.ms
```

### 服务器启停

```bash
# 前台启动
kafka-server-start.sh config/server.properties

# 后台启动
nohup kafka-server-start.sh config/server.properties > kafka.log 2>&1 &

# 停止
kafka-server-stop.sh

# 强制停止
pkill -f kafka.Kafka
```

---

## Redis Pub/Sub

```bash
# 发布消息到频道
redis-cli PUBLISH news "Hello World"

# 订阅频道
redis-cli SUBSCRIBE news sports

# 按模式订阅（支持 glob）
redis-cli PSUBSCRIBE "news.*"

# 取消订阅
redis-cli UNSUBSCRIBE news

# 按模式取消订阅
redis-cli PUNSUBSCRIBE "news.*"

# PUBSUB 查看活跃频道
redis-cli PUBSUB CHANNELS
redis-cli PUBSUB CHANNELS news*

# PUBSUB 查看订阅数
redis-cli PUBSUB NUMSUB news

# PUBSUB 查看模式订阅总数
redis-cli PUBSUB NUMPAT
```

---

## Docker 部署消息队列

### RabbitMQ

```bash
# 运行 RabbitMQ（推荐）
docker run -d --name rabbitmq \
  -p 5672:5672 -p 15672:15672 \
  -v rabbitmq_data:/var/lib/rabbitmq \
  rabbitmq:management

# 查看日志
docker logs -f rabbitmq

# 进入容器
docker exec -it rabbitmq /bin/bash
```

### Kafka (Docker)

```bash
# 运行 Kafka（需要 Zookeeper）
docker run -d --name kafka \
  -p 9092:9092 \
  -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper:2181 \
  -e ALLOW_PLAINTEXT_HOST=yes \
  confluentinc/cp-kafka:latest
```

### Docker Compose

```bash
# 启动所有服务
docker-compose -f docker-compose.yml up -d

# 查看状态
docker-compose -f docker-compose.yml ps

# 查看日志
docker-compose -f docker-compose.yml logs -f rabbitmq

# 停止并清理
docker-compose -f docker-compose.yml down
```

---

## BullMQ (Node.js)

```bash
# 创建队列
import { Queue } from 'bullmq';
const queue = new Queue('send-email', {
  connection: { host: 'localhost', port: 6379 }
});

# 添加任务（带重试）
await queue.add('send-email', { to: 'user@example.com' }, {
  attempts: 3,
  backoff: { type: 'exponential', delay: 1000 }
});

# 创建 Worker
import { Worker } from 'bullmq';
const worker = new Worker('send-email', async job => {
  console.log('Processing:', job.data);
}, { connection: { host: 'localhost', port: 6379 } });

# 查看任务数
const counts = await queue.getJobCounts('wait', 'active', 'completed', 'failed');

# 暂停/恢复队列
await queue.pause();
await queue.resume();

# 清空队列
await queue.empty();
```

---

## Celery (Python)

```bash
# 启动 Worker
celery -A tasks worker --loglevel=info --concurrency=4

# 启动 Beat（定时任务调度器）
celery -A tasks beat --loglevel=info

# 启动 Flower 监控面板
celery -A tasks flower --port=5555

# 调用任务
celery -A tasks call tasks.send_email --args='["user@example.com"]'

# 查看活跃任务
celery -A tasks inspect active

# 查看已注册任务
celery -A tasks inspect registered

# 查看任务结果
celery -A tasks result <task-id>

# 撤销任务
celery -A tasks revoke <task-id>

# 清空所有任务
celery -A tasks purge
```

Python 代码示例：

```python
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def send_email(to):
    print(f"Sending email to {to}")

# 调用任务
send_email.delay('user@example.com')

# 定时任务
@app.task
def periodic_task():
    print("Running periodically")
```

---

## AWS SQS

```bash
# 创建标准队列
aws sqs create-queue --queue-name my-queue \
  --attributes file://attributes.json

# attributes.json 示例
# { "DelaySeconds": "0", "ReceiveMessageWaitTimeSeconds": "20" }

# 创建 FIFO 队列
aws sqs create-queue --queue-name my-queue.fifo

# 列出队列
aws sqs list-queues

# 发送消息
aws sqs send-message \
  --queue-url https://sqs.us-east-1.amazonaws.com/123456789/my-queue \
  --message-body "Hello World"

# FIFO 发送（带 group id）
aws sqs send-message \
  --queue-url https://sqs.us-east-1.amazonaws.com/123456789/my-queue.fifo \
  --message-body "Hello" \
  --message-group-id group-1

# 接收消息（长轮询）
aws sqs receive-message \
  --queue-url https://sqs.us-east-1.amazonaws.com/123456789/my-queue \
  --max-number-of-messages 10 \
  --wait-time-seconds 20

# 删除消息（需要 receipt handle）
aws sqs delete-message \
  --queue-url https://sqs.us-east-1.amazonaws.com/123456789/my-queue \
  --receipt-handle <receipt-handle>

# 批量发送
aws sqs send-message-batch \
  --queue-url https://sqs.us-east-1.amazonaws.com/123456789/my-queue \
  --entries file://messages.json

# 删除队列
aws sqs delete-queue --queue-url https://sqs.us-east-1.amazonaws.com/123456789/my-queue
```

---

## AWS SNS

```bash
# 创建标准主题
aws sns create-topic --name my-topic

# 创建 FIFO 主题
aws sns create-topic --name my-topic.fifo \
  --attributes file://fifo.json
# fifo.json: { "FifoTopic": "true", "ContentBasedDeduplication": "true" }

# 列出主题
aws sns list-topics

# 发布消息
aws sns publish \
  --topic-arn arn:aws:sns:us-east-1:123456789:my-topic \
  --message "Hello World" \
  --subject "Alert"

# FIFO 发布
aws sns publish \
  --topic-arn arn:aws:sns:us-east-1:123456789:my-topic.fifo \
  --message "Hello" \
  --message-group-id group-1

# 订阅 SQS 队列
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:123456789:my-topic \
  --protocol sqs \
  --notification-endpoint arn:aws:sqs:us-east-1:123456789:my-queue

# 订阅 Lambda
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:123456789:my-topic \
  --protocol lambda \
  --notification-endpoint arn:aws:lambda:us-east-1:123456789:function:my-function

# 订阅 Email
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:123456789:my-topic \
  --protocol email \
  --notification-endpoint user@example.com

# 列出订阅
aws sns list-subscriptions

# 删除主题
aws sns delete-topic --topic-arn arn:aws:sns:us-east-1:123456789:my-topic

# 撤销订阅
aws sns unsubscribe --subscription-arn arn:aws:sns:us-east-1:123456789:my-topic:xxxxx
```

---

## AWS EventBridge

```bash
# 创建事件总线
aws events create-event-bus --name my-bus

# 列出事件总线
aws events list-event-buses

# 创建规则（事件模式）
aws events put-rule \
  --name my-rule \
  --event-pattern file://pattern.json \
  --event-bus-name default
# pattern.json: { "source": ["my-app"] }

# 添加 Lambda 目标
aws events put-targets \
  --rule my-rule \
  --event-bus-name default \
  --targets file://targets.json
# targets.json: [{ "Id": "1", "Arn": "arn:aws:lambda:us-east-1:123456789:function:my-function" }]

# 列出规则
aws events list-rules

# 删除规则
aws events delete-rule --name my-rule --event-bus-name default

# 发送事件
aws events put-events --entries file://events.json
```

---

## 命令速查表

| 工具 | 操作 | 命令 | 说明 |
|------|------|------|------|
| RabbitMQ | 查看状态 | `rabbitmqctl status` | 节点状态信息 |
| RabbitMQ | 启动应用 | `rabbitmqctl start_app` | 启动应用层 |
| RabbitMQ | 列出队列 | `rabbitmqctl list_queues` | 所有队列信息 |
| RabbitMQ | 启用插件 | `rabbitmq-plugins enable rabbitmq_management` | Web 管理界面 |
| Kafka | 创建主题 | `kafka-topics.sh --create --topic my-topic --partitions 3` | 创建主题 |
| Kafka | 列出主题 | `kafka-topics.sh --list` | 所有主题 |
| Kafka | 消费者 | `kafka-console-consumer.sh --from-beginning --topic my-topic` | 消费消息 |
| Kafka | 消费组 | `kafka-consumer-groups.sh --describe --group my-group` | 查看消费组 |
| Redis | 发布 | `redis-cli PUBLISH channel message` | 发布消息 |
| Redis | 订阅 | `redis-cli SUBSCRIBE channel` | 订阅频道 |
| Redis | 查看订阅 | `redis-cli PUBSUB CHANNELS` | 活跃频道 |
| Docker | RabbitMQ | `docker run -p 5672:5672 -p 15672:15672 rabbitmq:management` | 容器运行 |
| BullMQ | 添加任务 | `queue.add('name', { data })` | 添加异步任务 |
| Celery | Worker | `celery -A tasks worker --loglevel=info` | 启动 Worker |
| SQS | 创建队列 | `aws sqs create-queue --queue-name my-queue` | 创建队列 |
| SQS | 发送消息 | `aws sqs send-message --message-body "hello"` | 发送消息 |
| SNS | 创建主题 | `aws sns create-topic --name my-topic` | 创建主题 |
| SNS | 发布消息 | `aws sns publish --topic-arn <arn> --message "hello"` | 发布消息 |
| EventBridge | 创建总线 | `aws events create-event-bus --name my-bus` | 创建事件总线 |
| EventBridge | 创建规则 | `aws events put-rule --name my-rule --event-pattern <json>` | 创建规则 |

---

## 相关资源

- [Docker 命令文档](../Docker 命令/README.md)
- [Linux 命令文档](../Linux 命令/README.md)
- [Redis 基本操作文档](../Redis-基本操作/README.md)
- [完整命令参考表](../../references/commands-reference.md)
