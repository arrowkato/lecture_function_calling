"""よくある四則演算のサンプル。
https://python.langchain.com/docs/how_to/tool_calling/#pydantic-class

tool callの日本語の解説。ただし、LangGraphで使うことを想定した解説
https://zenn.dev/pharmax/articles/1b351b730eef61
"""

import json

from langchain_core.messages import AIMessage, AnyMessage, HumanMessage, SystemMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


# これは、tool callingで呼び出す用の関数その1
# 関数名、引数、返り値、docstring を参照して、LLMがこの関数を使うべきかを決めるので、きちんと書くこと
@tool
def add(a: float | int, b: float | int) -> int:
    """Add two real number.

    Args:
        a: First real number
        b: Second real number
    """
    return a + b


# これは、tool callingで呼び出す用の関数その2
# 関数名、引数、返り値、docstring を参照して、LLMがこの関数を使うべきかを決めるので、きちんと書くこと
@tool
def multiply(a: float | int, b: float | int) -> int:
    """Multiply two real number.

    Args:
        a: First real number
        b: Second real number
    """
    return a * b


def _show_response(response: AnyMessage, prefix: str, delimiter: str = "-") -> None:
    response_dict = {
        "content": response.content,
        "additional_kwargs": response.additional_kwargs,
        "tool_calls": response.tool_calls if hasattr(response, "tool_calls") else None,
    }
    print(delimiter * 50)
    print(f"{prefix}\n{json.dumps(response_dict, indent=4, ensure_ascii=False,)}")
    print()
    print()


def _show_responses(
    responses: list[AnyMessage],
    prefix: str,
    delimiter: str = "-",
) -> None:
    print("=" * 50)
    for i, response in enumerate(responses):
        _show_response(response, prefix=f"{prefix} {i}", delimiter=delimiter)


def use_tool_call(question: str) -> None:
    # いつものLLMの定義
    llm = ChatOpenAI(model="gpt-4o", temperature=0.0)
    # step0 使う可能性のある関数(addとmultiply)を登録
    llm_with_tools = llm.bind_tools(tools=[add, multiply])

    msgs: list[AnyMessage] = [
        SystemMessage(content="あなたは、親切な数学教師です。"),
        HumanMessage(content=question),
    ]

    # step1, step2, step3
    # このresponseは、どの関数を使うべきかを返却しています。
    # addとmultiply の実行はまだ、というかLLM自体はコードの実行はできません。
    response_step3: AIMessage = llm_with_tools.invoke(input=msgs)

    # responseの中身を見てみる
    _show_response(response_step3, "step3 result")

    # 後でもう一回使うので、msgsに追加
    msgs.append(response_step3)

    _show_responses(msgs, "before step4", delimiter="-")

    # step4 アプリケーションは与えられた引数で関数を実行します
    for tool_call in response_step3.tool_calls:
        selected_tool = {"add": add, "multiply": multiply}[tool_call["name"].lower()]
        tool_msg = selected_tool.invoke(tool_call)  # add or multiplyの実行
        msgs.append(tool_msg)

    # このタイミングで、ブレークポイントを張って、msgsの中身を見てみましょう
    _show_responses(msgs, "after step4", delimiter="-")

    # step5 アプリケーションはAPIを呼び出して、プロンプトとコードが実行した結果を渡します。
    # step6 step5のを踏まえたLLMの応答を受け取ります。
    # # tool_callを使って、計算した結果を踏まえての最終結果
    response_step6: AIMessage = llm_with_tools.invoke(msgs)
    # step7 最終結果をユーザに表示します。
    # 必ずしもユーザに表示する必要は無いですが、何かしらに使うのが普通の挙動と思います。
    print("=" * 50)
    print(response_step6.content)

    _show_response(response=response_step6, prefix="final result detail")


if __name__ == "__main__":
    question1 = "929801.2 * 380.29  はいくつですか。"  # 353594098.348  桁数の少ない四則演算だとLLMは普通に答えるので
    question2 = "390.32 + 84.41 はいくつですか。"
    use_tool_call(question=question1)
    # use_tool_call(question=question2)
