from langchain_community.tools.wikipedia.tool import (
    WikipediaAPIWrapper,
    WikipediaQueryRun,
)
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent


@tool
def add(a: float | int, b: float | int) -> float:
    """Add two real number.

    Args:
        a: First real number
        b: Second real number
    """
    return a + b


@tool
def search_wikipedia(query: str) -> str:
    """search wikipedia

    Args:
        query (str): query for search wikipedia
    """
    wrapper = WikipediaAPIWrapper(
        lang="ja",
        top_k_results=3,
    )
    wikipedia = WikipediaQueryRun(api_wrapper=wrapper)

    response = wikipedia.invoke(query)
    return response


def use_tool_call(question: str) -> None:
    # プロンプトの定義
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "与えられたinputに従って適切な処理を呼び出してください",
            ),
            ("placeholder", "{messages}"),
        ]
    )

    # エージェントの作成
    agent = create_react_agent(
        model=ChatOpenAI(model="gpt-4o-mini"),
        tools=[add, search_wikipedia],
        state_modifier=prompt,
    )

    # エージェントの実行
    result = agent.invoke({"messages": [question]})
    print(result["messages"][-1].content)


if __name__ == "__main__":
    # question = "390.32 + 84.41 はいくつですか。"
    # question = "今日の晩御飯の献立を考えて"

    # 注:量子非隠蔽定理 の日本語記事は2024年にできており、gpt-4o-miniのcut offの2023年10月よりもあとの情報です。
    question = "量子非隠蔽定理について、小学生にもわかるように説明して"

    # question = "いまの総理大臣ってだれ?"
    use_tool_call(question=question)
