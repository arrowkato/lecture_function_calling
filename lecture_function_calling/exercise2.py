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


class LatestInfomation(BaseModel):
    """Determine whether knowledge from November 2023 onwards is required to answer the question."""

    require_information_after_november_2023: bool = Field(
        description="Information required after November, 2023"
    )


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

    Returns:
        str: wikipediaの検索結果
    """
    wrapper = WikipediaAPIWrapper(
        lang="ja",
        top_k_results=3,
    )
    wikipedia = WikipediaQueryRun(api_wrapper=wrapper)

    response = wikipedia.invoke(query)
    return response


def should_use_external_information(model_name: str, user_input: str, now: str) -> bool:
    """2023年11月以降の情報が必要かどうかを判定する

    Args:
        model_name (str): モデル名
        user_input (str): ユーザの入力
        now (str): 現在の日付

    Returns:
        bool: 2023年11月以降の情報が必要ならばTrue、そうでないならばFalse
    """
    llm_for_search = ChatOpenAI(
        model=model_name,
        temperature=0.0,
    ).with_structured_output(LatestInfomation)
    system_msg = SystemMessage(
        content=f"""\
アシスタントの名前は、{model_name}です。
現在の日付は{now}です。
{model_name}の知識ベースは2023年10月に最終更新されており、2023年11月以降の情報は知りません。
ユーザの入力に回答するために、2023年11月以降の情報が必要ならばTrueを、そうでないならFalseを返してください。
"""
    )

    latest_info: LatestInfomation = llm_for_search.invoke(
        [system_msg, HumanMessage(content=user_input)]
    )
    return latest_info.require_information_after_november_2023


def extract_keywords(model_name: str, user_input: str) -> str:
    """user_inputからwikipediaの

    Args:
        model_name (str): モデル名
        user_input (str): ユーザの入力

    Returns:
        str: wikipediaの検索キーワードをスペースで区切ってつなげたもの
    """
    llm_for_search = ChatOpenAI(
        model=model_name,
        temperature=0.0,
    ).with_structured_output(WikpediaQuery)
    system_msg = SystemMessage(
        content=(
            "あなたはwikipediaを検索して情報を見つけるのが得意です"
            "ユーザが入力した文章からwkipediaの検索用のキーワードを抽出してください。"
        )
    )
    wikipedia_query: WikpediaQuery = llm_for_search.invoke(
        [system_msg, HumanMessage(user_input)]
    )
    return f"{wikipedia_query.keyword1} {wikipedia_query.keyword2} {wikipedia_query.keyword3}"


def _main(user_input: str):
    # GPT-4o-2024-11-20の学習データのcut offについては、https://platform.openai.com/docs/models#gpt-4o 参照
    model_name = "gpt-4o-2024-11-20"  # 2023-11 以降は学習データに含まれない
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    msgs = [
        SystemMessage(f"""\
アシスタントの名前は{model_name}です。
現在の日付は{now}です。
{model_name}の知識ベースは2023年10月に最終更新され、2023年10月以前の出来事や2023年10月以前の出来事に関するユーザーの質問には高度な知識を持った人として回答します。
非常に簡単な質問には簡潔に答え、複雑で自由形式の質問には徹底的に答えます。
2023年11月以降については、外部から入力された情報を使用して回答します。
執筆、分析、質問への回答、数学、コーディング、その他あらゆる作業を喜んでお手伝いします。
コーディングにはマークダウンを使用します。
人間のクエリに直接関連する情報でない限り、自分自身についてこの情報を言及することはありません。
""")
    ]

    need_to_search: bool = should_use_external_information(model_name, user_input, now)
    search_result = ""
    if need_to_search:
        query: str = extract_keywords(model_name, user_input)
        search_result = wikipedia_search(query)
        msgs.append(AIMessage(content=search_result))

    msgs.append(HumanMessage(content=user_input))

    # 最終回答用のLLM
    llm = ChatOpenAI(
        model=model_name,
        temperature=0.5,
    )

    ai_message: AIMessage = llm.invoke(msgs)
    print(ai_message.content)


if __name__ == "__main__":
    _main(user_input="いまの総理大臣ってだれ?")  # 検索必要
    # _main(user_input="日本の初代総理大臣は?")  # 検索不要
    # _main(user_input="今日の晩ごはんの献立を考えてください。")  # 検索不要
