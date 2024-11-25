# API keyの指定

ChatOpenAIを使うときは、裏でOpenAIのAPIをつかているので、API keyが必要です。
```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5,
    api_key="sk-1234567890abcdef1234567890abcdef"
)
```

https://github.com/langchain-ai/langchain/blob/a83357dc5ab5fcbed8c2dd7606e9ce763e48d194/libs/partners/openai/langchain_openai/chat_models/base.py#L399 より
```
api_key: Optional[str]
  OpenAI API key. If not passed in will be read from env var OPENAI_API_KEY.
```
です。

API keyは、秘匿情報なので、ソースコードには書かないようにしてください。
毎度、shellで、export OPENAI_API_KEY=sk-1234567890abcdef1234567890abcdef などとして、API keyを環境変数にセットするのも手間なので、[python-dotenv](https://pypi.org/project/python-dotenv/)を使うと楽です。

# .env ファイルの読み込み
```shell
pip install python-dotenv
```

```python
from dotenv import load_dotenv
load_dotenv() # .env ファイルに定義している環境変数を読み込む
```
