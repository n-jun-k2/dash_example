# Python開発環境

### ディレクトリ構成

```bash
```

### .envの作成

| item name | overview | default |
|---|---|---|
| PYTHONDONTWRITEBYTECODE | pythonのキャッシュバイナリ作成フラグ（1の場合、作成しない) | 1 |
| REDIS_PORT | redisコンテナのポート指定 | 6379 |

### 構築方法

```bash
user@desktop:/pyenv# make requirements
user@desktop:/pyenv# docker-compose up -d dash
```

### パッケージ追加
[/tools/pip-tools/requirements.in](/tools/pip-tools/requirements.in)に必要なパッケージを記載後、以下のコマンドを実行.

```
user@desktop:/pyenv# make requirements
```