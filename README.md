# 1. 環境構築

## 1.1 VS Code + devcontainer を使う場合
docker はあらかじめインストールしておいてください。
VS Codeを使う場合は、[Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) の設定をしているので、通常通り開けば、uv でのライブラリのインストールまで自動で行います。


## 1.2 VS Code + devcontainer を使わない場合
### 1.2.1 コンテナを使う場合
[Docker in IntelliJ IDEA](https://www.jetbrains.com/help/idea/docker.html) を使う場合は、Dockerfile は
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

pythonのバージョンは3.9以降なら動きますが、動作確認をしているのが 3.12.6 なので、このバージョンをインストールしてください。
すでにインストール済みの場合、この手順は不要です。
```bash
uv python install $(cat .python-version)
```

**このリポジトリで使うライブラリのインストール**  
```bash
uv sync --dev
```

リポジトリ直下に `.venv` directoryができていればOKです。



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


# 3. このリポジトリで説明しないこと

Function Calling の説明をメインにしていますので、LangChain Expression Language(LCEL)の説明は省いています。
LCEL を使ったほうが、簡潔に書ける箇所もありますが、最低限の知識で Function Calling を使えるような構成にしています。

きちんと勉強したい人は、以下を参照してください。
- [LangChain 公式Doc](https://python.langchain.com/docs/concepts/lcel/)
- [LangChainとLangGraphによるRAG・AIエージェント［実践］入門 エンジニア選書](https://www.amazon.co.jp/dp/B0DK4YGYBL/)
- [つくりながら学ぶ！生成AIアプリ＆エージェント開発入門](https://www.amazon.co.jp/dp/B0D6VWX1T8)

