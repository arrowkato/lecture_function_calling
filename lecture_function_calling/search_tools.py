from dotenv import load_dotenv
from langchain_community.tools import (
    DuckDuckGoSearchResults,
    DuckDuckGoSearchRun,
    TavilySearchResults,
    WikipediaQueryRun,
)
from langchain_community.utilities import (
    DuckDuckGoSearchAPIWrapper,
    WikipediaAPIWrapper,
)

load_dotenv()


def duckduckgo_search_in_english(query: str) -> None:
    search = DuckDuckGoSearchResults()
    result: DuckDuckGoSearchResults = search.invoke(query)
    print(result)


def duckduckgo_search_in_japanese(query: str) -> None:
    search = DuckDuckGoSearchRun()
    # https://pypi.org/project/duckduckgo-search/#regions
    wrapper = DuckDuckGoSearchAPIWrapper(region="jp-jp", max_results=1)
    search = DuckDuckGoSearchResults(
        api_wrapper=wrapper, source="news", output_format="list"
    )
    # execute the search
    result = search.invoke(query)
    print(result)


def wikipedia_search(query: str) -> None:
    """wikipediaの検索

    Args:
        query (str): 基本的にキーワードをスペース区切りで入れてください。文章をいれるとヒットしないことがあります。
    """
    wrapper = WikipediaAPIWrapper(
        lang="ja",
        top_k_results=3,
    )
    wikipedia = WikipediaQueryRun(api_wrapper=wrapper)

    response: str = wikipedia.invoke(query)
    print(response)


def tavily_search(query: str) -> None:
    """tavilyを使った検索

    Args:
        query (str): クエリ
    """
    search = TavilySearchResults(
        max_results=3,
        search_depth="advanced",
        # include_answer=True,
        # include_raw_content=True,
        # include_images=True,
        # include_domains=[...],
        # exclude_domains=[...],
        # name="...",            # overwrite default tool name
        # description="...",     # overwrite default tool description
        # args_schema=...,       # overwrite default args_schema: BaseModel
    )
    result: list[dict] = search.invoke(input={"query": query})
    print(result)


if __name__ == "__main__":
    query = "いまの総理大臣ってだれ?"
    # duckduckgo_search_in_english("What is LLM in the context of machine learning?")
    # duckduckgo_search_in_japanese()
    # wikipedia_search(query)
    tavily_search(query)
