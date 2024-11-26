# 5. 演習

## 5.1 wikipeadia 関連の toolの課題

search_tools.py で
- TavilySearchResults を使った場合と、
- WikipediaQueryRun + WikipediaAPIWrapper

を使った場合だと使用感がだいぶん違ったと思います。
これまで習得したことの演習として、Wikipediaでの検索でもTavilySearchResultsと似た挙動をするように実装してみましょう。



## 5.2 演習1
以下の仕様を満たす実装をしてみましょう。
まずは、簡単のため、ユーザが必ずwikipedia検索したいと思っている状況とします。

1. ユーザの入力から検索用のキーワードを取得
2. 取得したキーワードを半角スペースでつなげて、wikipediaで検索
3. 検索結果を元にして、最終的な返答を取得

structured_output と WikipediaQueryRunを使って実装してみましょう。

解答はexecise1.pyを参照してください。



