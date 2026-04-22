# AI/ML 工具命令文档

AI 与机器学习工具完整命令参考文档，覆盖 Python ML 生态、AI CLI 工具、向量数据库、模型服务和 MLOps 全流程。

## 目录

- [Python ML 生态](#python-ml-生态)
- [AI CLI 工具](#ai-cli-工具)
- [向量数据库](#向量数据库)
- [模型服务](#模型服务)
- [MLOps 工具](#mlops-工具)

---

## Python ML 生态

### pip install - 安装 ML 框架

**基础用法**:
```bash
pip install %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装 scikit-learn | `pip install scikit-learn` | 经典机器学习库 |
| 安装 TensorFlow | `pip install tensorflow` | 深度学习框架（CPU） |
| 安装 PyTorch | `pip install torch` | PyTorch 深度学习框架 |
| 安装 Keras | `pip install keras` | 高层神经网络 API |
| 安装 JAX | `pip install jax jaxlib` | Google 高性能 ML 库 |
| 安装 transformers | `pip install transformers` | Hugging Face Transformer 库 |
| 安装 datasets | `pip install datasets` | Hugging Face 数据集库 |
| 安装 accelerate | `pip install accelerate` | 分布式训练加速 |
| 指定 CUDA 版本 | `pip install torch --index-url https://download.pytorch.org/whl/cu118` | 指定 CUDA 11.8 版本 |

### python -c - 验证 ML 库

**基础用法**:
```bash
python -c "import %{模块名}%"
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 验证 TensorFlow | `python -c "import tensorflow as tf; print(tf.__version__)"` | 检查 TensorFlow 版本 |
| 验证 PyTorch + CUDA | `python -c "import torch; print(torch.cuda.is_available())"` | 检查 CUDA 是否可用 |
| 验证 NumPy | `python -c "import numpy as np; print(np.__version__)"` | 检查 NumPy 版本 |
| 验证 Pandas | `python -c "import pandas as pd; print(pd.__version__)"` | 检查 Pandas 版本 |
| 验证 scikit-learn | `python -c "import sklearn; print(sklearn.__version__)"` | 检查 scikit-learn 版本 |

### Jupyter 环境

**基础用法**:
```bash
jupyter %{命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动 Notebook | `jupyter notebook` | 启动 Jupyter Notebook 服务 |
| 启动 JupyterLab | `jupyter lab` | 启动 JupyterLab 界面 |
| 指定端口 | `jupyter notebook --port %{端口}%` | 端口: 端口号 (例: 8888) |
| 禁止浏览器自动打开 | `jupyter notebook --no-browser` | 服务器模式运行 |
| 指定工作目录 | `jupyter notebook --notebook-dir %{目录}%` | 目录: 工作目录 (例: ~/projects) |
| 列出运行中的笔记本 | `jupyter notebook list` | 查看已启动的 Notebook 实例 |
| 停止 Notebook | `jupyter notebook stop %{端口}%` | 端口: 端口号 (例: 8888) |

### Pandas / NumPy CLI

**基础用法**:
```bash
python -c "import %{模块}%; print(%{模块}%.__version__)"
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| NumPy 版本检查 | `python -c "import numpy as np; print(np.__version__)"` | 检查 NumPy 版本 |
| Pandas 版本检查 | `python -c "import pandas as pd; print(pd.__version__)"` | 检查 Pandas 版本 |
| Matplotlib 版本 | `python -c "import matplotlib; print(matplotlib.__version__)"` | 检查 Matplotlib 版本 |
| SciPy 版本 | `python -c "import scipy; print(scipy.__version__)"` | 检查 SciPy 版本 |

---

## AI CLI 工具

### OpenAI CLI

**基础用法**:
```bash
openai %{命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看工具列表 | `openai tools` | 列出可用工具 |
| 设置 API Key | `openai apikey set %{API密钥}%` | API密钥: OpenAI API Key (例: sk-...) |
| 查看当前配置 | `openai whoami` | 显示账户信息 |
| 调用 chat 模型 | `openai chat.do " %{内容}%"` | 内容: 对话内容 (例: Hello) |
| 查看可用模型 | `openai models list` | 列出所有可用模型 |

### Anthropic CLI (Claude)

**基础用法**:
```bash
claude %{命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动交互式对话 | `claude` | 启动 Claude 交互式会话 |
| 发送单条消息 | `claude " %{消息}%"` | 消息: 发送的消息 (例: Explain ML) |
| 指定模型 | `claude --model %{模型}% " %{消息}%"` | 模型: 模型名称 (例: opus) |
| 流式输出 | `claude --print " %{消息}%"` | 禁用彩色输出，直接打印 |
| 设置 API Key | `export ANTHROPIC_API_KEY=%{密钥}%` | 密钥: Anthropic API Key |

### Hugging Face CLI

**基础用法**:
```bash
huggingface-cli %{命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 登录 HF 账号 | `huggingface-cli login` | 交互式登录 Hugging Face |
| 下载模型 | `huggingface-cli download %{模型名}%` | 模型名: 模型标识 (例: bert-base-chinese) |
| 下载数据集 | `huggingface-cli download --repo-type dataset %{数据集}%` | 数据集: 数据集名称 (例: squad) |
| 查看缓存路径 | `huggingface-cli cache-dir` | 显示模型/数据集缓存目录 |
| 列出本地模型 | `huggingface-cli ls` | 列出已下载模型 |
| 上传模型 | `huggingface-cli upload %{本地路径}% %{远程路径}%` | 上传到 HF Hub |

---

## 向量数据库

### Chroma CLI

**基础用法**:
```bash
chroma %{命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动 Chroma 服务 | `chroma run` | 启动 Chroma 服务（默认 8000 端口） |
| 指定端口 | `chroma run --port %{端口}%` | 端口: 端口号 (例: 8000) |
| 禁止自动创建目录 | `chroma run --no-reset` | 持久化存储模式 |
| 查看帮助 | `chroma --help` | 查看所有可用命令 |

### Qdrant CLI

**基础用法**:
```bash
qdrant %{命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动 Qdrant 服务 | `qdrant` | 启动 Qdrant 嵌入式模式 |
| 指定存储路径 | `qdrant --storage-path %{路径}%` | 路径: 数据目录 (例: ./qdrant_storage) |
| 指定端口 | `qdrant --http-port %{端口}%` | 端口: HTTP 端口 (例: 6333) |
| Docker 启动 | `docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant` | Docker 方式启动 |
| 查看版本 | `qdrant --version` | 查看 Qdrant 版本 |

### Milvus CLI (Milvus CLI / Attu)

**基础用法**:
```bash
milvus %{命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动 Milvus 服务 | `docker run -d -p 19530:19530 milvusdb/milvus` | Docker 方式启动 |
| Milvus CLI 连接 | `milvus_cli --host %{主机}% --port %{端口}%` | 主机: 服务器地址 (例: localhost)；端口: 端口号 (例: 19530) |
| 创建 Collection | `create collection %{集合名}%` | 在 CLI 内执行 |
| 查看 Collections | `list collections` | 列出所有 Collection |
| 插入向量 | `insert %{集合名}%` | 插入向量数据 |

### pgvector SQL 命令

**基础用法**:
```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 安装扩展 | `CREATE EXTENSION IF NOT EXISTS vector;` | PostgreSQL pgvector 扩展 |
| 创建向量列 | `CREATE TABLE items (id bigserial PRIMARY KEY, embedding vector(%{维度}%));` | 维度: 向量维度 (例: 1536) |
| 插入向量 | `INSERT INTO items (embedding) VALUES ('[%{值}%]');` | 值: 向量值 (例: 0.1,0.2) |
| 相似度搜索 | `SELECT * FROM items ORDER BY embedding <=> '[%{查询向量}%]' LIMIT %{数量}%;` | 数量: 返回数量 (例: 5) |
| L2 距离搜索 | `SELECT id FROM items ORDER BY embedding <-> '%{向量}%' LIMIT 5;` | 最近邻搜索（L2 距离） |
| 内积搜索 | `SELECT id FROM items ORDER BY embedding <#> '%{向量}%' LIMIT 5;` | 内积搜索（需归一化） |
| 余弦相似度 | `SELECT id FROM items ORDER BY embedding <=> '%{向量}%' LIMIT 5;` | 余弦距离搜索 |

---

## 模型服务

### FastAPI for ML Serving

**基础用法**:
```bash
uvicorn %{模块}%:app --host %{主机}% --port %{端口}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动 FastAPI 服务 | `uvicorn main:app --host 0.0.0.0 --port 8000` | 主机: 绑定地址 (例: 0.0.0.0)；端口: 端口号 (例: 8000) |
| 自动重载 | `uvicorn main:app --reload` | 开发模式热重载 |
| 指定 workers | `uvicorn main:app --workers %{数量}%` | 数量: Worker 数量 (例: 4) |
| HTTPS | `uvicorn main:app --ssl-keyfile %{密钥}% --ssl-certfile %{证书}%` | 密钥: 密钥文件；证书: 证书文件 |
| 查看健康检查 | `curl http://localhost:8000/health` | 健康检查端点 |

### TorchServe

**基础用法**:
```bash
torchserve %{命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动 TorchServe | `torchserve --start` | 启动 TorchServe 服务 |
| 停止 TorchServe | `torchserve --stop` | 停止 TorchServe 服务 |
| 注册模型 | `torchserve-register %{模型名}%` | 注册已打包的模型 |
| 查看版本 | `torchserve --version` | 查看 TorchServe 版本 |
| 打包模型 | `torch-model-archiver --model-name %{名称}% --version %{版本}% --serialized-file %{模型文件}% --handler %{处理器}%` | 名称: 模型名；处理器: 处理函数 |

### TensorFlow Serving

**基础用法**:
```bash
tensorflow_model_server --port=%{端口}% --model_name=%{名称}% --model_base_path=%{路径}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动 TF Serving | `tensorflow_model_server --port=8501 --model_name=my_model --model_base_path=/models/my_model` | 端口: 端口号 (例: 8501)；名称: 模型名 (例: my_model)；路径: 模型路径 |
| gRPC 模式 | `tensorflow_model_server --port=8500 --rest_api_port=8501 --model_name=%{名称}% --model_base_path=%{路径}%` | 同时启用 gRPC 和 REST API |
| 指定模型版本 | `tensorflow_model_server --port=8501 --model_name=%{名称}% --model_base_path=%{路径}% --model_version_policy=specific --model_version=%{版本}%` | 版本: 版本号 (例: 1) |
| Docker 启动 TF Serving | `docker run -p 8501:8501 --mount type=bind,source=/models,target=/models -e MODEL_NAME=%{名称}% tensorflow/serving` | Docker 方式启动 |

---

## MLOps 工具

### MLflow

**基础用法**:
```bash
mlflow %{命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动 MLflow UI | `mlflow ui` | 启动 MLflow Tracking Server |
| 指定端口和目录 | `mlflow ui --port %{端口}% --backend-store-uri %{存储}%` | 端口: 端口号 (例: 5000)；存储: 存储路径 (例: sqlite:///mlflow.db) |
| 运行实验 | `mlflow run %{项目路径}%` | 项目路径: MLflow 项目目录 (例: ./project) |
| 指定实验 | `mlflow run %{路径}% --experiment-name %{实验名}%` | 实验名: 实验名称 (例: my_experiment) |
| 记录参数 | `mlflow.log_param("%{参数}%", %{值}%)` | 在 Python 代码中记录参数 |
| 记录指标 | `mlflow.log_metric("%{指标}%", %{值}%)` | 在 Python 代码中记录指标 |
| 记录模型 | `mlflow.sklearn.log_model(model, "%{名称}%")` | 记录 scikit-learn 模型 |
| 列出实验 | `mlflow experiments list` | 列出所有实验 |
| 查看运行记录 | `mlflow runs list --experiment-id %{ID}%` | ID: 实验 ID (例: 0) |

### DVC (Data Version Control)

**基础用法**:
```bash
dvc %{命令}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 初始化 DVC | `dvc init` | 在项目中初始化 DVC |
| 添加数据文件 | `dvc add %{文件}%` | 文件: 数据文件路径 (例: data/raw) |
| 提交变更 | `dvc commit` | 提交当前 DVC 跟踪的变更 |
| 推送到远程 | `dvc push` | 上传数据到远程存储 |
| 从远程拉取 | `dvc pull` | 从远程存储下载数据 |
| 展示依赖图 | `dvc dag` | 显示 Pipeline 依赖图 |
| 重现 Pipeline | `dvc repro %{阶段}%` | 阶段: Stage 名称 (例: train) |
| 列出 tracked 文件 | `dvc list %{路径}%` | 路径: 目录路径 (例: .) |
| 迁移 S3 远程 | `dvc remote add -d myremote s3://mybucket/data` | 添加 S3 远程存储 |

### Kubeflow

**基础用法**:
```bash
kubectl %{命令}% -n kubeflow
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 部署 Kubeflow | `kubectl apply -f %{部署文件}%` | 部署文件: YAML 文件路径 |
| 查看 Pods | `kubectl get pods -n kubeflow` | 列出 Kubeflow 命名空间中的 Pods |
| 查看训练任务 | `kubectl get tfjob -n kubeflow` | 列出 TensorFlow 训练任务 |
| 查看 PyTorch 任务 | `kubectl get pytorchjob -n kubeflow` | 列出 PyTorch 训练任务 |
| 查看 Pipeline | `kubectl get pipeline -n kubeflow` | 列出 Kubeflow Pipelines |
| 提交 TF 训练任务 | `kubectl create -f %{tfjob文件}% -n kubeflow` | 提交 TensorFlow 分布式训练 |
| 查看训练日志 | `kubectl logs %{pod名}% -n kubeflow` | pod名: Pod 名称 (例: tf-training-worker-0) |
| 缩容/扩容 | `kubectl scale tfjob %{任务名}% --replicas=%{副本}% -n kubeflow` | 副本: 副本数量 (例: 3) |

---

## 实用场景示例

### 场景 1: ML 项目环境搭建

```bash
# 创建虚拟环境
python -m venv ml-env
source ml-env/bin/activate  # Linux/Mac
# ml-env\Scripts\activate  # Windows

# 安装核心 ML 库
pip install numpy pandas scikit-learn
pip install tensorflow  # 或 pip install torch
pip install jupyterlab
pip install matplotlib seaborn

# 验证安装
python -c "import sklearn; print('sklearn', sklearn.__version__)"
python -c "import torch; print('CUDA:', torch.cuda.is_available())"
```

### 场景 2: 模型训练与追踪

```bash
# 使用 MLflow 追踪实验
export MLFLOW_TRACKING_URI=http://localhost:5000
mlflow ui --port 5000 &

# 在 Python 脚本中使用 MLflow
# mlflow.sklearn.autolog()
# mlflow.log_param("learning_rate", 0.01)
# mlflow.log_metric("accuracy", 0.95)

# 使用 DVC 管理数据
dvc init
dvc add data/
git commit -m "Add raw data"

# 设置远程存储
dvc remote add -d myremote s3://mybucket/project
dvc push
```

### 场景 3: 模型部署服务

```bash
# FastAPI 部署
# 1. 创建 app.py
# from fastapi import FastAPI
# app = FastAPI()
# @app.post("/predict")
# def predict(data: dict): return {"result": "ok"}

# 2. 启动服务
uvicorn app:app --host 0.0.0.0 --port 8000

# TorchServe 部署
torch-model-archiver --model-name mymodel --version 1.0 \
  --serialized-file model.pt --handler handler.py
mv mymodel.mar /model_store/
torchserve --start --model-store /model_store --models mymodel=mymodel.mar

# TensorFlow Serving (Docker)
docker run -p 8501:8501 \
  --mount type=bind,source=/models/mymodel,target=/models/mymodel \
  -e MODEL_NAME=mymodel tensorflow/serving
```

### 场景 4: RAG 向量数据库搭建

```bash
# Chroma 本地向量库
pip install chromadb
chroma run --port 8000

# Qdrant 向量数据库
docker run -d -p 6333:6333 -p 6334:6334 \
  -v $(pwd)/qdrant_storage:/qdrant/storage \
  qdrant/qdrant

# pgvector 向量扩展
# psql -U postgres
# CREATE EXTENSION IF NOT EXISTS vector;
# CREATE TABLE embeddings (id serial PRIMARY KEY, text text, embedding vector(1536));
# INSERT INTO embeddings (text, embedding) VALUES ('example', '[0.1, 0.2, ...]');
```

---

## 相关资源

- [完整命令参考表](../../references/commands-reference.md)
- [快速开始指南](../quick-start.md)
