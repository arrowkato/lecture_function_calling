# 4. structured output

https://python.langchain.com/docs/how_to/structured_output/

Q. 5 + 12 はいくつ
A. 5 + 7 = 12 です。

ほしいのは、 12 だけというときに、with_structured_output() を使うと、良いです。


## 4.1 pydantic

[Pydantic](https://docs.pydantic.dev/) は、Python で最も広く使用されているデータ検証ライブラリです。

データ検証の処理をいれることも出来ますが、LangChainだと、返り値に指定して、変数の種類を限定する目的で使われます。


## 4.2 typed dict
略。pydanticを知っていれ対応できるので。
