"""よくある四則演算のサンプル。
https://python.langchain.com/docs/how_to/tool_calling/#pydantic-class
"""

import json

from langchain_core.messages import AIMessage, AnyMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


# これは、tool callingで呼び出す用の関数その1
def add(a: float | int, b: float | int) -> int:
    """Add two real number.

    Args:
        a: First real number
        b: Second real number
    """
    return a + b


# これは、tool callingで呼び出す用の関数その2
def multiply(a: float | int, b: float | int) -> int:
    """Multiply two real number.

    Args:
        a: First real number
        b: Second real number
    """
    return a * b


class CalculationResult(BaseModel):
    result: float = Field(..., description="calculation result")


def use_tool_call() -> None:
    llm = ChatOpenAI(model="gpt-4o", temperature=0.0)
    llm_with_tools = llm.bind_tools(tools=[add, multiply])
    system_msg = SystemMessage(content="あなたは、親切な数学教師です。")
    human_msg = HumanMessage(content="12*11.5 はいくつですか。")
    msgs: list[AnyMessage] = [system_msg, human_msg]

    response: AIMessage = llm_with_tools.invoke(input=msgs)
    # どの関数を使ったのかを確認
    print(json.dumps(response.additional_kwargs, indent=4, ensure_ascii=False))
    # 最終的な返答
    print("-------")
    print(response.content)


if __name__ == "__main__":
    use_tool_call()
