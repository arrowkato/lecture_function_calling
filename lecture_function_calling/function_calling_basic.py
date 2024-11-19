"""よくある四則演算のサンプル。
https://python.langchain.com/docs/how_to/tool_calling/#pydantic-class
"""

from langchain_core.messages import AIMessage, AnyMessage, HumanMessage, SystemMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


# これは、tool callingで呼び出す用の関数その1
@tool
def add(a: float | int, b: float | int) -> int:
    """Add two real number.

    Args:
        a: First real number
        b: Second real number
    """
    return a + b


# これは、tool callingで呼び出す用の関数その2
@tool
def multiply(a: float | int, b: float | int) -> int:
    """Multiply two real number.

    Args:
        a: First real number
        b: Second real number
    """
    return a * b


def use_tool_call() -> None:
    llm = ChatOpenAI(model="gpt-4o", temperature=0.0)
    llm_with_tools = llm.bind_tools(tools=[add, multiply])
    system_msg = SystemMessage(content="あなたは、親切な数学教師です。")
    human_msg = HumanMessage(content="12 * 1.5 + 4 はいくつですか。")
    msgs: list[AnyMessage] = [system_msg, human_msg]

    # このresponseは、どの関数を使うべきかを返却しています。addとmultiply の実行はまだ、というかLLM自体はコードの実行はできません。
    response: AIMessage = llm_with_tools.invoke(input=msgs)

    # 後でもう一回使うので、msgsに追加
    msgs.append(response)

    # response.tool_calls[0]["args"]
    for tool_call in response.tool_calls:
        selected_tool = {"add": add, "multiply": multiply}[tool_call["name"].lower()]
        tool_msg = selected_tool.invoke(tool_call)
        msgs.append(tool_msg)

    # このタイミングで、ブレークポイントとを張って、msgsの中身を見てみましょう

    # tool_callを使って、計算した結果を踏まえての最終結果
    final_response: AIMessage = llm_with_tools.invoke(msgs)
    print(final_response.content)


if __name__ == "__main__":
    use_tool_call()
