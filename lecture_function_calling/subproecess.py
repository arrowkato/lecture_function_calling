import subprocess
from subprocess import CompletedProcess

from langchain_core.messages import AIMessage, AnyMessage, HumanMessage, SystemMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


def call_ls_command() -> None:
    """ls -l コマンドを実行してその結果を取得"""
    result: CompletedProcess = subprocess.run(
        args=["ls", "-l"],
        capture_output=True,
        text=True,
    )

    # コマンドの実行結果の標準出力を表示
    print(result.stdout)


def call_golang_process(a: float, b: float) -> None:
    """goに処理をさせて結果を取得する

    add.goは足し算するだけの簡単なコードですが、Python以外のコード呼べることを示すためのサンプルです。
    """
    # $ go run /workspaces/lecture_function_calling/lecture_function_calling/add.go 7 23
    # をサブプロセスで実行
    result: CompletedProcess = subprocess.run(
        # PATHは通っているので、go はそのままでOK。実行ファイルは、カレントディレクトリによるので、フルパスで指定するのが無難
        args=[
            "go",
            "run",
            # コンテナ内の絶対パスを指定しています。コンテナを使っていない場合はローカル環境に応じて変更してください
            "/workspaces/lecture_function_calling/lecture_function_calling/add.go",
            str(a),
            str(b),
        ],
        capture_output=True,
        text=True,
        # cwd="/workspaces/lecture_function_calling/lecture_function_calling", # カレントディレクトリを指定する場合
    )

    # コマンドの実行結果の標準出力を表示
    print(result.stdout)


@tool  # この @tool デコレータは必須
def add(a: float, b: float) -> float:
    """Add two real number.

    Args:
        a: First real number
        b: Second real number
    """

    # 普通はこんなことしないですが、他の言語の再利用できるってことです。
    result: CompletedProcess = subprocess.run(
        # PATHは通っているので、go はそのままでOK。実行ファイルは、カレントディレクトリによるので、フルパスで指定するのが無難
        args=[
            "go",
            "run",
            "/workspaces/lecture_function_calling/lecture_function_calling/add.go",
            str(a),
            str(b),
        ],
        capture_output=True,
        text=True,
    )
    return float(result.stdout.strip())


def use_tool_call_with_golang(msgs: list[AnyMessage]) -> None:
    """goで作成した足し算のコードを呼び出す"""
    llm = ChatOpenAI(model="gpt-4o", temperature=0.0)
    llm_with_tools = llm.bind_tools(tools=[add])
    # メッセージ作成
    response: AIMessage = llm_with_tools.invoke(input=msgs)

    result = add.invoke(response.tool_calls[0]["args"])
    print(result)


if __name__ == "__main__":
    # shellの ls -l コマンドを実行
    # call_ls_command()

    # 7 + 23 を golangで加算する
    # call_golang_process(7, 23)

    # 1274826.348 + 191.5 をgolangで加算させる。
    # ユーザには、自然言語で "1274826.348 + 191.5 はいくつですか" を入力させる想定
    msgs: list[AnyMessage] = [
        SystemMessage(content="あなたは、加算のみできる電卓です"),
        HumanMessage(content="1274826.348 + 191.5 はいくつですか"),
    ]
    use_tool_call_with_golang(msgs)
