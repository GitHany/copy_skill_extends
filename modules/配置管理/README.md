# 配置管理与环境工具

本模块涵盖主流配置管理、密钥管理、包管理和构建配置工具的命令参考。

---

## 1. 环境变量管理

### dotenv (Node.js)

| 命令 | 说明 |
|------|------|
| `DOTENV_CONFIG_PATH=/path/to/.env node server.js` | 指定.env文件路径启动 |
| `node -r dotenv/config server.js` | 通过require加载dotenv配置 |
| `dotenv -e .env.local -e .env.development config` | 加载多个.env文件 |

**关键词**: `dotenv`, `env`, `环境变量`, `NODE_ENV`

### python-dotenv

| 命令 | 说明 |
|------|------|
| `python -m dotenv.cli run server.py` | 使用.env运行脚本 |
| `dotenv run python server.py` | 使用dotenv命令行运行 |
| `python -c "from dotenv import load_dotenv; load_dotenv(); print('OK')"` | 手动加载.env |
| `dotenv set KEY=value && dotenv run python app.py` | 设置变量并运行 |

**关键词**: `python-dotenv`, `python env`, `dotenv python`

### direnv

| 命令 | 说明 |
|------|------|
| `direnv allow` | 允许当前目录的.envrc执行 |
| `direnv deny` | 拒绝当前目录的.envrc |
| `direnv edit` | 编辑当前目录的.envrc |
| `direnv export bash` | 输出当前环境的变量声明 |
| `direnv status` | 查看direnv状态和加载情况 |

**关键词**: `direnv`, `auto env`, `envrc`

### envchain

| 命令 | 说明 |
|------|------|
| `envchain --namespace myapp python script.py` | 使用命名空间运行脚本 |
| `envchain --namespace myapp --env SERVICE_API_KEY printenv SERVICE_API_KEY` | 读取存储的密钥 |
| `envchain --namespace myapp set SERVICE_API_KEY` | 交互式设置密钥 |
| `envchain --namespace myapp unset SERVICE_API_KEY` | 删除密钥 |
| `envchain --namespace myapp env` | 列出该命名空间所有变量 |

**关键词**: `envchain`, `secret`, `密钥`, `credential`

---

## 2. 密钥与敏感信息管理

### SOPS (Secrets OPerationS)

| 命令 | 说明 |
|------|------|
| `sops -e --inplace secrets.yaml` | 原地加密YAML文件 |
| `sops -d secrets.yaml` | 解密并输出到stdout |
| `sops set secrets.yaml api_key "newvalue"` | 更新指定字段值 |
| `sops update-secret secrets.yaml new_secrets.yaml` | 替换整个加密文件 |
| `sops --aws-profile prod publish update.enc.json` | 使用指定AWS Profile发布 |
| `sops -e --kms arn:aws:kms:us-east-1:123:key/xxx secrets.yaml` | 指定KMS密钥加密 |
| `sops -e --gcp-kms projects/p/locations/k/likeys publish.enc.yaml` | 使用GCP KMS加密 |
| `sops set-file secrets.yaml img ./photo.jpg` | 将文件作为二进制值嵌入加密 |

**关键词**: `sops`, `encrypt`, `secret ops`, `加密`, `kms`, `age`

### age

| 命令 | 说明 |
|------|------|
| `age-keygen -o key.txt` | 生成age密钥对 |
| `age -r age1xxxxxxxxxxxxxxxxxxxxxxxx -p -o out.enc in.txt` | 使用接收者公钥加密 |
| `age --passphrase -p -o out.enc in.txt` | 使用密码加密 |
| `age -d -o out.txt in.enc` | 解密文件 |
| `age -d -i key.txt -o out.txt in.enc` | 使用密钥文件解密 |
| `echo "secret" | age -r age1xxx -p` | 管道加密 |
| `age -p in.txt | aws kms encrypt --key-id xxx --output text` | 与KMS结合加密 |

**关键词**: `age`, `encryption`, `加密`, `file encrypt`

### GPG

| 命令 | 说明 |
|------|------|
| `gpg --gen-key` | 生成新密钥对 |
| `gpg --export -a "Name" > pub.asc` | 导出公钥 |
| `gpg --import pub.asc` | 导入公钥 |
| `gpg -e -r "Name" secrets.txt` | 用指定密钥加密文件 |
| `gpg -d secrets.txt.gpg > secrets.txt` | 解密文件 |
| `gpg --edit-key "Name"` | 编辑密钥（签名、过期等） |
| `gpg --armor --export-secret-keys "Name" > priv.asc` | 导出私钥（备份） |
| `echo "passphrase" | gpg --batch --passphrase-fd 0 -c file.txt` | 自动化密码加密 |
| `gpg --symmetric --cipher-algo AES256 file.txt` | 对称加密（仅密码） |

**关键词**: `gpg`, `gnupg`, `pgp`, `加密`, `密钥`

### 1Password CLI

| 命令 | 说明 |
|------|------|
| `op signin --account my.1password.com` | 登录1Password账户 |
| `op item get "SSH Keys" --fields label=private` | 获取指定字段值 |
| `op item create --title "API Token" --category "Password" --password "xxx"` | 创建密码项 |
| `op run --env-file=ops_secrets.env -- node app.js` | 加载1Password环境变量运行命令 |
| `op injection get api_key --token-name "production"` | 获取注入令牌 |
| `op vault list` | 列出所有保险库 |
| `op document get "backup.tar.gz" --output ./backup.tar.gz` | 下载文档附件 |

**关键词**: `1password`, `1password-cli`, `op signin`, `secret`

### Bitwarden CLI

| 命令 | 说明 |
|------|------|
| `bw login` | 交互式登录Bitwarden |
| `bw unlock` | 解锁已保存的保险库 |
| `bw list items --search "api"` | 搜索项目 |
| `bw get item "API Key"` | 获取指定条目完整JSON |
| `bw get password "API Key"` | 仅获取密码字段 |
| `bw generate` | 生成随机密码 |
| `bw sync` | 同步保险库 |
| `BW_SESSION=$(bw login --raw) && export BW_SESSION` | 获取无头登录Session |

**关键词**: `bitwarden`, `bw cli`, `bitwarden-cli`, `secret`

---

## 3. 配置中心与KV存储

### Consul

| 命令 | 说明 |
|------|------|
| `consul agent -dev -ui` | 启动开发模式（带UI） |
| `consul agent -server -bootstrap-expect=1 -data-dir=/tmp/consul` | 启动Server节点 |
| `consul kv put config/app/database "mysql://host:3306"` | 写入KV键值 |
| `consul kv get config/app/database` | 读取键值 |
| `consul kv delete config/app/database` | 删除键值 |
| `consul kv export config/` | 导出前缀下所有键 |
| `consul kv import @backup.json` | 导入JSON备份 |
| `consul members` | 查看集群成员 |
| `consul services register -name=web -address=127.0.0.1 -port=8080` | 注册服务 |

**关键词**: `consul`, `consul kv`, `service mesh`, `配置中心`

### etcd

| 命令 | 说明 |
|------|------|
| `etcdctl put /config/app/version "1.0.0"` | 写入键值 |
| `etcdctl get /config/app` | 读取键值 |
| `etcdctl del /config/app` | 删除键 |
| `etcdctl get --prefix /config/` | 前缀范围查询 |
| `etcdctl watch /config/app` | 监听键变化 |
| `etcdctl snapshot save backup.db` | 快照备份 |
| `etcdctl snapshot restore backup.db --data-dir=/var/lib/etcd` | 恢复快照 |
| `etcdctl lease grant 60` | 创建60秒TTL租约 |
| `etcdctl put --lease=xxx /config/session "data"` | 关联租约写入 |
| `ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 endpoint health` | API v3健康检查 |

**关键词**: `etcd`, `etcdctl`, `kv store`, `配置中心`

### Vault

| 命令 | 说明 |
|------|------|
| `vault server -config=config.hcl` | 启动Vault Server |
| `vault status` | 检查Vault状态 |
| `vault kv put secret/myapp API_KEY="xxx"` | 写入密钥（v2） |
| `vault kv get secret/myapp` | 读取密钥 |
| `vault kv get -field=API_KEY secret/myapp` | 仅读取特定字段 |
| `vault kv delete secret/myapp` | 删除密钥 |
| `vault kv list secret/` | 列出路径下所有键 |
| `vault auth enable userpass` | 启用用户名密码认证 |
| `vault login -method=userpass username=admin` | 用户密码登录 |
| `vault token create -policy=default` | 创建Token |
| `vault agent -config=agent.hcl -log-level=debug` | 启动Vault Agent（自动注入） |
| `vault secrets enable -path=aws aws` | 启用AWS动态密钥引擎 |
| `vault kv get -format=json secret/myapp | jq .data.data` | JSON格式化读取 |

**关键词**: `vault`, `vault kv`, `secret management`, `hashi`

---

## 4. 包管理器配置

### npm config

| 命令 | 说明 |
|------|------|
| `npm config set registry https://registry.npmmirror.com` | 设置镜像源 |
| `npm config get registry` | 查看当前registry |
| `npm config list --json` | 列出所有配置 |
| `npm config delete registry` | 删除配置项 |
| `npm config edit` | 打开编辑器编辑配置 |
| `npm config set package-lock true` | 启用package-lock |
| `npm config set save-exact true` | 保存精确版本号 |
| `npm config set fetch-retries 5` | 设置重试次数 |

**关键词**: `npm config`, `npm 配置`, `npm registry`

### yarn config

| 命令 | 说明 |
|------|------|
| `yarn config set registry https://registry.npmmirror.com` | 设置yarn镜像源 |
| `yarn config get registry` | 查看当前源 |
| `yarn config list` | 列出所有配置 |
| `yarn config set strict-ssl false` | 禁用严格SSL |
| `yarn config set network-timeout 120000` | 设置网络超时 |
| `yarn config set cache-folder /tmp/yarn-cache` | 设置缓存目录 |

**关键词**: `yarn config`, `yarn 配置`, `yarn registry`

### pip config

| 命令 | 说明 |
|------|------|
| `pip config list` | 列出pip配置 |
| `pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple` | 设置清华镜像 |
| `pip config set global.trusted-host pypi.tuna.tsinghua.edu.cn` | 添加可信主机 |
| `pip config set install.requires-python ">=3.8"` | 设置Python版本要求 |
| `pip config debug` | 调试配置来源 |

**关键词**: `pip config`, `pip 配置`, `pip mirror`

### apt

| 命令 | 说明 |
|------|------|
| `apt update && apt upgrade -y` | 更新并升级所有包 |
| `apt install nginx -y` | 安装软件包 |
| `apt remove nginx -y` | 卸载包（保留配置） |
| `apt purge nginx -y` | 彻底卸载（删除配置） |
| `apt search "^python3.*$"` | 搜索包 |
| `apt show nginx` | 查看包详情 |
| `apt list --upgradable` | 列出可升级包 |
| `apt autoremove -y` | 自动清理无用依赖 |
| `add-apt-repository ppa:deadsnakes/ppa && apt update && apt install python3.11` | 添加PPA源安装新版Python |

**关键词**: `apt`, `apt-get`, `debian`, `ubuntu`, `package`

### yum/dnf

| 命令 | 说明 |
|------|------|
| `yum update && yum upgrade -y` | 更新并升级 |
| `yum install nginx -y` | 安装包 |
| `yum remove nginx -y` | 卸载包 |
| `yum search nginx` | 搜索包 |
| `yum info nginx` | 查看包信息 |
| `yum list installed` | 列出已安装 |
| `yum deplist nginx` | 查看依赖关系 |
| `yum check-update` | 检查更新 |
| `dnf module reset nodejs && dnf module enable nodejs:18` | 启用Node.js 18模块流 |

**关键词**: `yum`, `dnf`, `rpm`, `centos`, `fedora`, `package`

### brew

| 命令 | 说明 |
|------|------|
| `brew install node@18` | 安装指定版本软件 |
| `brew uninstall node@18` | 卸载指定版本 |
| `brew list` | 列出已安装 |
| `brew search node` | 搜索包 |
| `brew info node` | 查看包详情 |
| `brew update && brew upgrade` | 更新brew及所有包 |
| `brew cleanup` | 清理旧版本和缓存 |
| `brew doctor` | 检查Homebrew健康状态 |
| `brew switch node 18.20.0` | 切换node版本（如果用brew安装） |
| `HOMEBREW_NO_INSTALLED_DEPENDENTS_CHECK=1 brew upgrade` | 跳过依赖检查升级 |

**关键词**: `brew`, `homebrew`, `macos`, `package`

---

## 5. 构建工具配置

### webpack

| 命令 | 说明 |
|------|------|
| `npx webpack --mode production` | 生产环境构建 |
| `npx webpack --mode development --watch` | 开发模式并监听 |
| `npx webpack --config webpack.prod.js` | 使用指定配置文件 |
| `npx webpack --entry ./src/index.js --output-path ./dist` | 指定入口和输出 |
| `npx webpack --env production` | 传递环境变量 |
| `npx webpack analyze` | 分析bundle（需插件） |
| `npx webpack --progress` | 显示构建进度 |
| `npx webpack --display-modules` | 显示模块来源 |

**关键词**: `webpack`, `webpack cli`, `bundler`, `构建`

### Vite

| 命令 | 说明 |
|------|------|
| `vite build` | 生产环境构建 |
| `vite build --mode staging` | 指定环境构建 |
| `vite build --outDir dist/static` | 指定输出目录 |
| `vite preview` | 预览生产构建 |
| `vite --port 5173` | 指定端口启动开发服务器 |
| `vite --host 0.0.0.0` | 允许外部访问 |
| `vite --cors` | 启用CORS |
| `vite --https` | 启用HTTPS |
| `vite inspect` | 审查Vite配置和插件 |

**关键词**: `vite`, `vite cli`, `构建`, `bundler`

### Parcel

| 命令 | 说明 |
|------|------|
| `parcel index.html` | 启动Parcel开发服务器 |
| `parcel build index.html --dist-dir dist` | 生产构建 |
| `parcel build index.html --no-source-maps` | 禁用sourcemap构建 |
| `parcel watch index.html` | 监听模式构建 |
| `parcel index.html --open` | 自动打开浏览器 |
| `parcel build index.html --target node` | Node.js环境构建 |
| `PARCEL_WORKERS=4 parcel build index.html` | 指定并行worker数 |

**关键词**: `parcel`, `parcel cli`, `零配置打包`

### esbuild

| 命令 | 说明 |
|------|------|
| `esbuild app.js --bundle --outfile=out.js` | 打包单个文件 |
| `esbuild app.js --bundle --outfile=out.js --sourcemap` | 启用sourcemap |
| `esbuild app.js --bundle --outfile=out.js --minify` | 压缩代码 |
| `esbuild app.js --bundle --outfile=out.js --target=es2020` | 指定ES目标版本 |
| `esbuild app.js --bundle --outfile=out.js --loader:.js=jsx` | 自定义loader |
| `esbuild app.js --bundle --outfile=out.js --external:npm:pkg` | 外部化npm包 |
| `esbuild app.js --bundle --outfile=out.js --define:process.env.NODE_ENV=\"production\"` | 全局替换 |
| `echo 'let x: number = 1; console.log(x)' | esbuild --bundle --outfile=out.js --loader=.ts=ts` | 管道构建 |
| `npx esbuild app.js --bundle --watch` | 监听模式 |
| `esbuild app.js --bundle --platform=node --outfile=out.js` | Node平台构建 |

**关键词**: `esbuild`, `bundle`, `构建`, `golang`

---

## 6. 综合实战命令

| 场景 | 命令 |
|------|------|
| 从.env启动Node应用 | `node -r dotenv/config server.js` |
| 使用1Password运行脚本 | `op run --env-file=.env -- node server.js` |
| Vault动态数据库凭证 | `vault kv get -field=password secret/db && mysql -u app -p` |
| SOPS加密更新配置 | `sops set prod/secrets.yaml API_KEY "newkey"` |
| age加密备份文件 | `age -p -o backup.tar.gz.age backup.tar.gz` |
| npm设置淘宝镜像 | `npm config set registry https://registry.npmmirror.com` |
| pip设置清华镜像 | `pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple` |
| etcd快照恢复 | `etcdctl snapshot restore backup.db --data-dir=/var/lib/etcd` |
| Consul服务注册 | `consul services register -name=web -port=8080` |
| Vite生产构建 | `vite build --mode production` |
| webpack分析 | `npx webpack --analyze` |
| esbuild快速打包 | `esbuild app.js --bundle --minify --outfile=dist/app.js` |
| brew安装指定版本 | `brew install node@18` |
| Vault Agent自动注入 | `vault agent -config=agent.hcl -log-level=info` |
| Bitwarden获取密码 | `bw get password "API Key" \| xclip` |

---

## 关键词索引

`config`, `env`, `secret`, `密钥`, `加密`, `vault`, `sops`, `consul`, `etcd`, `dotenv`, `direnv`, `envchain`, `1password`, `bitwarden`, `npm config`, `yarn config`, `pip config`, `apt`, `yum`, `brew`, `webpack`, `vite`, `parcel`, `esbuild`, `gpg`, `age`