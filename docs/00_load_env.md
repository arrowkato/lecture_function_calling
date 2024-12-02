# 0. OpenAI等のAPIキーの設定方法
## 0.1 API key の指定

ChatOpenAI を使うときは、裏で OpenAI の API をつかているので、API key が必要です。

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5,
    api_key="sk-1234567890abcdef1234567890abcdef"
)
```

[関連コード](https://github.com/langchain-ai/langchain/blob/a83357dc5ab5fcbed8c2dd7606e9ce763e48d194/libs/partners/openai/langchain_openai/chat_models/base.py#L399) より

```python
api_key: Optional[str]
  OpenAI API key. If not passed in will be read from env var OPENAI_API_KEY.
```

です。

API key は、秘匿情報なので、ソースコードには書かないようにしてください。
毎度、shell で、`export OPENAI_API_KEY=sk-1234567890abcdef1234567890abcdef` などとして、API key を環境変数にセットするのも手間です。[python-dotenv](https://pypi.org/project/python-dotenv/)を使うと楽です。

---

# 0.2 .env ファイルの読み込み

python-dotenv のインストール。
```shell
pip install python-dotenv
```
`uv sync --dev` を使っている場合は、すでにインストール済みです。

使い方

```python
from dotenv import load_dotenv
load_dotenv() # .env ファイルに定義している環境変数を読み込む
```
