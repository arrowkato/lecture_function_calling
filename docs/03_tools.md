# 3. tools
公式docの[tools](https://python.langchain.com/docs/integrations/tools/)を参照してください。
LangChainは成長が早いライブラリなので、[ソースコード](https://github.com/langchain-ai/langchain/tree/master/libs/community/langchain_community/tools) を見ると更に多くのtoolが実装されています。

> tool の入力はモデルによって生成されるように設計されており、出力はモデルに返されるように設計されています。

自分で定義した関数を tool calling で利用することもできますが、すでに実装された tool もあります。
微妙な実装のものもありますが、一度探してみるのがいいと思います。

search_tools.py では検索系のtoolのサンプルを書いています。


## 事前準備: tavily
search_tools.py では、tavilyを利用しています。tavilyの利用には、APIキーの取得が必要です。

[README.md](../README.md) の 2.3 Tavily を参照して、APIキーを取得してください。  
取得したAPIキーを .env ファイルの TAVILY_API_KEY に記入してください。  


# 参考文献
https://highreso.jp/edgehub/machinelearning/tavilysearchapi.html

