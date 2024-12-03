# 2. function calling の基本

## 2.1 用語

- OpenAI: [function calling](https://platform.openai.com/docs/guides/function-calling)
- Anthropic: [tool use](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)
- Google: [function calling](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling)
- LangChain: [tool calling](https://python.langchain.com/docs/how_to/tool_calling/)

目的は同じですが、各製品で表記揺れがあります。

講義では、LangChain の場合は、tool calling と呼ぶつもりですが、function calling と tool calling は同じものを指すと思ってください

## 2.2 function calling の概要

> Function calling は、2023 年 6 月に Chat Completions API に追加された機能です。簡単に言えば、 利用可能な関数を LLM に伝えておいて 、LLM に「関数を使いたい」という判断をさせる機能です(LLM が関数を実行するわけではなく、LLM は「関数を使いたい」という応答を返してくるだけです)

LangChain と LangGraph による RAG_AI エージェント実践入門 より引用

下図の step1, step2, step3 に当たります。

```mermaid
sequenceDiagram
    participant Your_code
    participant LLM

    activate Your_code
    Your_code->>LLM: step1 あなたのアプリケーションはプロンプトと<br/>LLMが呼び出せる関数の定義を使ってAPIを呼び出します
    deactivate Your_code
    activate LLM
    LLM->>LLM: step2 モデルはユーザに応答するか、<br/>1つ以上の関数を呼び出すかを決定します。
    LLM->>Your_code: step3 APIは、呼び出す関数とそれを呼び出す引数を指定して、<br/>アプリケーションに応答します。
    deactivate LLM
    activate Your_code
    Your_code->>Your_code: step4 アプリケーションは与えられた引数で<br/>関数を実行します
    Your_code->>LLM: step5 アプリケーションはAPIを呼び出し、<br/>プロンプトとコードが実行した関数呼び出しの結果を返します
    deactivate Your_code
    activate LLM
    deactivate LLM
```

https://platform.openai.com/docs/guides/function-calling#lifecycle の図を日本語に翻訳

png の図が良い人は、[こちら](./img/function-calling-diagram-ja.png)を参照してください。

## 2.3 サンプルコード

function_calling_basics.py をきちんと対応させて書くと下記です。

```mermaid
sequenceDiagram
    participant Your_code
    participant LLM

    activate Your_code
    Your_code->>Your_code: step0 使う可能性のある関数(addとmultiply)を登録します
    Your_code->>LLM: step1 あなたのアプリケーションはプロンプトと<br/>LLMが呼び出せる関数の定義を使ってAPIを呼び出します
    deactivate Your_code
    activate LLM
    LLM->>LLM: step2 モデルはユーザに応答するか、<br/>1つ以上の関数を呼び出すかを決定します。
    LLM->>Your_code: step3 APIは、呼び出す関数とそれを呼び出す引数を指定して、<br/>アプリケーションに応答します。
    deactivate LLM
    activate Your_code
    Your_code->>Your_code: step4 アプリケーションは与えられた引数で<br/>関数を実行します
    Your_code->>LLM: step5 アプリケーションはAPIを呼び出し、<br/>プロンプトとコードが実行した関数呼び出しの結果を渡します
    deactivate Your_code
    activate LLM
    LLM->>Your_code: step6 最終結果を受け取ります。
    deactivate LLM
    activate Your_code
    Your_code->>Your_code: step7 最終結果(final_response)をユーザに表示します。
    deactivate Your_code
```

# 2.4 実行

function_calling_basics.py を動かしてみてください。
ブレークポイントを貼りながら、LLM の返答を確認してみると理解が深まりやすいと思います。

# 参考文献

- https://platform.openai.com/docs/guides/function-calling
- https://zenn.dev/pharmax/articles/1b351b730eef61#tool%E3%81%AE%E4%BD%9C%E3%82%8A%E6%96%B9
- https://www.amazon.co.jp/dp/B0DK4YGYBL
