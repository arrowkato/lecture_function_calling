
# 1. 環境構築

## 1.1 VS Code + devcontainer を使う場合
docker はあらかじめインストールしておいてください。
VS Codeを使う場合は、[Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) の設定をしているので、通常通り開けば、uv でのライブラリのインストールまで自動で行います。


## 1.2 VS Code + devcontainer を使わない場合
### 1.2.1 コンテナを使う場合
[Docker in IntelliJ IDEA](https://www.jetbrains.com/help/idea/docker.html) を使う場合は、Dockerfile に以下のように記述してください。

.devcontainer/Dockerfile をビルドして使ってください。


**このリポジトリで使うライブラリのインストール**  
```bash
uv sync --dev
```
リポジトリ直下に`.venv` directoryができていればOKです。

### 1.2.2 コンテナを使わない場合

**uv自体のインストール**  
[uvの公式doc](https://docs.astral.sh/uv/getting-started/installation/) 参照です。

**pythonのインストール**  
uv はパッケージマネージャーですが、pythonをインストールもできます。

多分pythonのバージョンは3.9以降なら動きますが、動作確認をしているのが3.12.6なので、このバージョンをインストールしてください。
すでにインストール済みの場合、この手順は不要です。
```bash
uv python install $(cat .python-version)
```

**このリポジトリで使うライブラリのインストール**  
```bash
uv sync --dev
```

リポジトリ直下に`.venv` directoryができていればOKです。



# 2. APIキー等の設定
OpenAI, Anthropic、tavily を利用にあたって、APIキーが必要になります。
(Anthropic は Bedrock model garden 経由での利用も出来ますが、今回は割愛しています。)

## 2.1 OpenAIとAnthropicのAPIキー
```bash
cp .env.sample .env
```
.env ファイルに OpenAI と AnthropicのAPIキーを記入してください。


## 2.2 Google Cloud へのアクセス
```bash
# <PROJECT_ID> は、Google Cloud Platform のプロジェクトIDに置き換えてください。
export CLOUDSDK_CORE_PROJECT=<PROJECT_ID>
# コマンドを打つと、URLが出てくるので、認証して、パスワードっぽい長い文字列をコピペしてください
gcloud auth application-default login
```

## 2.3 Tavily

1. https://tavily.com/ にアクセス。
2. Sign up をクリック
3. Googleアカウント or GitHubアカウントでアカウント作成する(必要なら)
4. ログインする
5. https://app.tavily.com/home にアクセスして、`tfly-` から始まるAPIキーを取得してください。


Free プランなら、 1,000 API credits / month まで無料です。https://tavily.com/ より
