"""ref: https://python.langchain.com/docs/how_to/structured_output/

Q. 5 + 12 はいくつ
A. 5 + 7 = 12 です。

ほしいのは、 12 だけというときに、with_structured_output() を使うと、良いです。

"""

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
from langchain_google_vertexai import ChatVertexAI
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

load_dotenv()


# Pydantic
class CaliculationResult(BaseModel):
    """The result of the calculation"""

    result: int = Field(description="The result of the calculation")
    # 変数の数は2つ以上あってもいいです。


def openai_structured_outputs() -> None:
    llm = ChatOpenAI(model="gpt-4o").with_structured_output(CaliculationResult)

    human_msg = HumanMessage("3掛ける12引く5は?")
    response: CaliculationResult = llm.invoke([human_msg])
    # response自体が、 CaliculationResult なので、そこに定義したもののみ返却される
    print(response.result)


def anthropic_structured_outputs() -> None:
    llm = ChatAnthropic(model="claude-3-5-sonnet-20241022").with_structured_output(
        schema=CaliculationResult
    )

    human_msg = HumanMessage("3掛ける12引く5は?")

    response: CaliculationResult = llm.invoke([human_msg])
    # response自体が、 CaliculationResult なので、そこに定義したもののみ返却される
    print(response.result)


def gemini_structured_outputs() -> None:
    llm = ChatVertexAI(model="gemini-1.5-pro-002").with_structured_output(
        schema=CaliculationResult
    )

    human_msg = HumanMessage("3掛ける12引く5は?")

    response: CaliculationResult = llm.invoke([human_msg])
    # response自体が、 CaliculationResult なので、そこに定義したもののみ返却される
    print(response.result)


if __name__ == "__main__":
    # openai_structured_outputs()
    # anthropic_structured_outputs()
    gemini_structured_outputs()
