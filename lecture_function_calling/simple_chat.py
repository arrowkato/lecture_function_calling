from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import AIMessage, AnyMessage, HumanMessage, SystemMessage
from langchain_google_vertexai import ChatVertexAI
from langchain_openai import ChatOpenAI

load_dotenv()


def chat_openai(messages: list[AnyMessage]) -> None:
    llm = ChatOpenAI(
        # モデル名は https://platform.openai.com/docs/models 参照
        model="gpt-4o-mini",
        # 0.2だと正しいけれども多様性が少なめ、0.5はバランスが良い、0.9だと多様性が高いけれども誤りが出てくる と言われています。
        temperature=0.5,
        # 出力時の最大トークン数。大体 *0.7倍した数値が出力日本語の文字数です。この場合、1400文字くらい
        max_tokens=2000,
    )
    ai_message: AIMessage = llm.invoke(input=messages)
    print(ai_message)  # AIMessageのメッセージ全体
    print(ai_message.content)  # LLMからの返答テキストは、contentに入っています。


def chat_openai_multi(messages: list[AnyMessage]) -> None:
    """ユーザーとLLMとのチャットを複数回やり取りする場合

    Args:
        messages (list[AnyMessage]): SystemMessage, HumanMessage, AIMessageが入りうるリスト
    """
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
    ai_message: AIMessage = llm.invoke(input=messages)
    print(ai_message.content)  # LLMからの返答その1

    # チャットシステムを作る場合は、以下のようにmessageをつなげてLLMに投げてください
    messages.append(ai_message)
    # ここではベタ打ちですが、chatシステムを作る場合は、ユーザーからの入力を受け取ります。
    messages.append(
        HumanMessage(
            content="私の好きなものを使って、今日の晩御飯のレシピを考えてください。"
        )
    )
    response = llm.invoke(messages)  # LLMに投げる
    print(response.content)  # LLMからの返答その2


def chat_anthropic(messages: list[AnyMessage]) -> None:
    llm = ChatAnthropic(
        # モデル名は、 https://docs.anthropic.com/en/docs/about-claude/models 参照
        model="claude-3-5-haiku-20241022",
        # https://docs.anthropic.com/en/docs/resources/glossary#temperature
        temperature=0.5,
        # 出力時の最大トークン数。多分 *0.7倍した数値が出力日本語の文字数です。この場合、1400文字くらい
        max_tokens_to_sample=2000,
    )
    ai_message: AIMessage = llm.invoke(input=messages)
    print(ai_message)
    print(ai_message.content)


def chat_gemini(messages: list[AnyMessage]) -> None:
    llm = ChatVertexAI(
        # モデル名は  https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models 参照のこと
        model="gemini-1.5-flash-002",
        # https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values#temperature
        temperature=0.5,
        # https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values#max-output-tokens
        # 1word=4token とあるが、おそらく英語の場合
        max_tokens=2000,
    )
    ai_message: AIMessage = llm.invoke(input=messages)
    print(ai_message)
    print(ai_message.content)


def main() -> None:
    system_msg = SystemMessage(content="あなたは親切なチャットアシスタントです。")
    human_msg = HumanMessage(content="こんにちは、私はめふんの塩漬けが好きです")
    msgs = [system_msg, human_msg]

    # 一番シンプルなチャット
    chat_openai([human_msg])  # HumanMessageのみ渡した場合
    chat_openai(msgs)  # .env 内の OPENAI_API_KEY にAPIキーを指定していること
    chat_anthropic(msgs)  # .env 内の ANTHROPIC_API_KEY にAPIキーを指定していること
    chat_gemini(msgs)  # Google Cloudに認証していること
    chat_openai_multi(msgs)


if __name__ == "__main__":
    main()
