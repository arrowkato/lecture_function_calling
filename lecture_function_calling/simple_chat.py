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
    # モデル名は https://platform.openai.com/docs/models 参照
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
    ai_message: AIMessage = llm.invoke(input=messages)
    print(ai_message)
    print(ai_message.content)


def chat_anthropic(messages: list[AnyMessage]) -> None:
    # モデル名は、 https://docs.anthropic.com/en/docs/about-claude/models 参照
    llm = ChatAnthropic(model="claude-3-5-haiku-20241022", temperature=0.5)
    ai_message: AIMessage = llm.invoke(input=messages)
    print(ai_message)
    print(ai_message.content)


def chat_gemini(messages: list[AnyMessage]) -> None:
    llm = ChatVertexAI(model="gemini-1.5-flash-001", temperature=0.5)
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
