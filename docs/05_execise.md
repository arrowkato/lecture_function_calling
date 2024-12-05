# 5. 演習

## 5.1 wikipeadia 関連の toolの課題

search_tools.py で
- TavilySearchResults を使った場合と、
- WikipediaQueryRun + WikipediaAPIWrapper

を使った場合だと使用感がだいぶん違ったと思います。
これまで習得したことの演習として、Wikipediaでの検索で、適切な検索結果を得て、それをもとに最終的な回答を得るプログラムを作成してみましょう。



## 5.2 演習1
以下の仕様を満たす実装をしてみましょう。
まずは、簡単のため、ユーザが **必ず** wikipedia検索したいと思っている状況とします。

user_query = "いまの総理大臣ってだれ?"


1. ユーザの入力から検索用のキーワードを取得
2. 取得したキーワードを半角スペースでつなげて、wikipediaで検索
3. 検索結果を元にして、最終的な返答を取得

with_structured_output と WikipediaQueryRunを使って実装してみましょう。

また、[GPT-4o](https://platform.openai.com/docs/models/gpt-4o#gpt-4o) の説明によると、
Knowledge cutoff は 2023年 10月とあるので、2023年11月以降の知識はないことに注意してください。

Claude, Geminiを使っている場合は、cut offの日付けは下記を参照してください。
- [Claude 3.5 の cut off](https://docs.anthropic.com/en/docs/about-claude/models#model-comparison-table)
- [Gemini 1.5 Pro の cut off](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models#gemini-1.5-pro)


解答はexecise1.pyを参照してください。

## 5.3 演習2

さらに以下の仕様を満たす実装をしてみましょう。
ユーザは必ずしもwikipediaの情報を必要するわけではないので、LLMのcut offよりあとの情報が必要な場合は、wikipediaで関連項目を検索し、そうでない場合は、wikipediaを使わずにLLMのみで回答するようにしましょう

1. ユーザの入力からcut offよりあとの情報が必要/不要を判定する
2. 必要ならば、ユーザの入力から検索用のキーワードを取得
3. 必要ならば、取得したキーワードを半角スペースでつなげて、wikipediaで検索
4. 必要ならば、 検索結果を元にして、最終的な返答を取得
5. 不要ならば、特に検索せずに回答する

structured_output と WikipediaQueryRunを使って実装してみましょう。

解答はexecise2.pyを参照してください。


## 5.3 演習2の別解 LangGraphを使った場合
exercise2-2.py参照です。
よしなに使い分けていることがわかると思います。
