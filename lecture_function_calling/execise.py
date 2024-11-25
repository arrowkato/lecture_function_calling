from datetime import datetime

from dotenv import load_dotenv
from langchain_community.tools import (
    WikipediaQueryRun,
)
from langchain_community.utilities import (
    WikipediaAPIWrapper,
)
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

load_dotenv()


class WikpediaQuery(BaseModel):
    """Query for wikipedia search"""

    keyword1: str = Field(description="The first keyword to search")
    keyword2: str | None = Field(description="The second keyword to search")
    keyword3: str | None = Field(description="The third keyword to search")

    # こっちでもいいです。ただし数は制限できないことに注意
    # keywords: list[str] = Field(description="The keywords to search")


def wikipedia_search(query: str) -> str:
    """wikipediaの検索

    Args:
        query (str): 基本的にキーワードをスペース区切りで入れてください。文章をいれるとヒットしないことがあります。
    """
    wrapper = WikipediaAPIWrapper(
        lang="ja",
        top_k_results=3,
    )
    wikipedia = WikipediaQueryRun(api_wrapper=wrapper)

    response = wikipedia.invoke(query)
    return response


def _main():
    user_query = "総理大臣ってだれ?"

    model_name = "gpt-4o"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    system_msg = SystemMessage(f"""\
アシスタントの名前は{model_name}です。
現在の日付は{now}です。
{model_name}の知識ベースは2023年10月に最終更新され、2023年10月以前の出来事や2023年10月以前の出来事に関するユーザーの質問には高度な知識を持った人として回答します。
非常に簡単な質問には簡潔に答え、複雑で自由形式の質問には徹底的に答えます。
2023年11月以降については、外部から入力された情報を使用して回答します。
執筆、分析、質問への回答、数学、コーディング、その他あらゆる作業を喜んでお手伝いします。
コーディングにはマークダウンを使用します。
人間のクエリに直接関連する情報でない限り、自分自身についてこの情報を言及することはありません。
""")

    llm_for_search = ChatOpenAI(
        model=model_name,
        temperature=0.5,
    ).with_structured_output(WikpediaQuery)
    wikipedia_query: WikpediaQuery = llm_for_search.invoke([system_msg, user_query])

    # wikipedia検索
    result_of_wikipedia_search = wikipedia_search(
        f"{wikipedia_query.keyword1} {wikipedia_query.keyword2} {wikipedia_query.keyword3}"
    )

    # 最終回答用のLLM
    llm = ChatOpenAI(
        model=model_name,
        temperature=0.5,
    )

    ai_message: AIMessage = llm.invoke(
        input=[
            system_msg,
            # 検索結果を詰める
            AIMessage(content=result_of_wikipedia_search),
            # 元々のユーザーのクエリ
            HumanMessage(content=user_query),
        ]
    )
    # print(ai_message)
    print(ai_message.content)


if __name__ == "__main__":
    _main()
