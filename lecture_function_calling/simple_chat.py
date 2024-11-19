import langchain
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import AIMessage, AnyMessage, HumanMessage, SystemMessage
from langchain_google_vertexai import ChatVertexAI
from langchain_openai import ChatOpenAI

model = ChatAnthropic(model="claude-3-opus-20240229")


langchain.debug = True
load_dotenv()


def chat_openai(messages: list[AnyMessage]) -> None:
    llm = ChatOpenAI(
        # モデル名は https://platform.openai.com/docs/models 参照
        model="gpt-4o-mini",
        # 0.2だと正しいけれども多様性が少なめ、0.5はバランスが良い、0.9だと多様性が高いけれども誤りが出てくる と言われています。
        temperature=0.5,
        # 出力時の最大トークン数。大体 *0.7倍した数値が出力日本語の文字数です。この場合、140文字くらい
        max_tokens=200,
    )
    ai_message: AIMessage = llm.invoke(input=messages)
    print(ai_message)
    print(ai_message.content)


def chat_anthropic(messages: list[AnyMessage]) -> None:
    llm = ChatAnthropic(
        # モデル名は、 https://docs.anthropic.com/en/docs/about-claude/models 参照
        model="claude-3-5-haiku-20241022",
        # https://docs.anthropic.com/en/docs/resources/glossary#temperature
        temperature=0.5,
        # 出力時の最大トークン数。多分 *0.7倍した数値が出力日本語の文字数です。この場合、140文字くらい
        max_tokens_to_sample=200,
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
        max_tokens=200,
    )
    ai_message: AIMessage = llm.invoke(input=messages)
    print(ai_message)
    print(ai_message.content)


def main() -> None:
    system_msg = SystemMessage(content="あなたは親切なチャットアシスタントです。")
    human_msg = HumanMessage(content="こんにちは")
    msgs = [system_msg, human_msg]

    chat_openai(msgs)
    chat_anthropic(msgs)
    chat_gemini(msgs)


if __name__ == "__main__":
    main()
