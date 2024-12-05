# 4. structured output

https://python.langchain.com/docs/how_to/structured_output/

Q1. 5 + 12 はいくつ
A1. 17
Q2. さらに4を加算すると最終的にいくつ?
A2. 21 です。

特に指定しない場合、LLMの返答は文になることが多いです。
例えば、A1 は、`5 + 12 = 17 です` という回答になる場合があります。
A1での返答としてほしいのは、 `17` のみのように返答形式が決まっている場合は、with_structured_output() を使うと良いです。

注:
方法として、System Promptで`返答は数値のみにしてください` と記載すればうまくいく場合もあります。
ただし、返答するものが複数あるなど複雑な場合、成功率は低くなります。


## 4.1 pydantic

[Pydantic](https://docs.pydantic.dev/) は、Python で最も広く使用されているデータ検証ライブラリです。

データ検証の処理をいれることも出来ますが、LangChainだと、返り値に指定して、変数の種類を限定する目的で使われます。


## 4.2 typed dict
略。pydanticを知っていれはばそちらで対応できるので。
