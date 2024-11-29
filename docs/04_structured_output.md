# 4. structured output

https://python.langchain.com/docs/how_to/structured_output/

Q. 5 + 12 はいくつ
A. 5 + 12 = 17 です。


特に指定しない場合、LLMの返答は文になることが多いです。返答としてほしいのは、 `17` だけなど返答形式が決まっている場合は、with_structured_output() を使うと良いです。


## 4.1 pydantic

[Pydantic](https://docs.pydantic.dev/) は、Python で最も広く使用されているデータ検証ライブラリです。

データ検証の処理をいれることも出来ますが、LangChainだと、返り値に指定して、変数の種類を限定する目的で使われます。


## 4.2 typed dict
略。pydanticを知っていれはばそちらで対応できるので。
