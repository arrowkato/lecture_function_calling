


# 2.1 用語
- OpenAI: [function calling](https://platform.openai.com/docs/guides/function-calling)
- Anthropic: [tool use](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)
- Google: [function calling](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling)
- LangChain: [tool calling](https://python.langchain.com/docs/how_to/tool_calling/)

目的は同じですが、各製品で表記揺れがあります。

講義では、LangChainの場合は、tool callingと呼ぶつもりですが、function callingとtool callingは同じものを指すと思ってください

# 2.2 概要

> Function callingは、2023年6月にChat Completions APIに追加された機能です。簡単に言えば、 利用可能な関数を LLM に伝えておいて 、LLMに「関数を使いたい」という判断をさせる機能です(LLMが関数を実行するわけではなく、LLM は「関数を使いたい」という応答を返してくるだけです)

LangChainとLangGraphによるRAG_AIエージェント実践入門 より引用

下図のstep1に当たります。

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

pngの図が良い人は、[状態遷移](./img/function-calling-diagram-ja.png)を参照してください。



# 2.3 詳細
function_calling_basic.py を動かしてみてください。

# ref
- https://platform.openai.com/docs/guides/function-calling
- https://zenn.dev/pharmax/articles/1b351b730eef61#tool%E3%81%AE%E4%BD%9C%E3%82%8A%E6%96%B9
