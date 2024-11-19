# 番外編 langchainを使わずに、画像に写っている物体を検出して、ImageFeaturesクラスの形式で取り出す
import base64
import json

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()


class Step(BaseModel):
    explanation: str
    output: str


class MathReasoning(BaseModel):
    steps: list[Step]
    final_answer: str


def sample() -> None:
    """openai公式サンプル
    https://platform.openai.com/docs/guides/structured-outputs?lang=python
    """
    client = OpenAI()

    completion = client.beta.chat.completions.parse(
        model="gpt-4o",  # https://platform.openai.com/docs/guides/structured-outputs#supported-models
        messages=[
            {
                "role": "system",
                "content": "You are a helpful math tutor. Guide the user through the solution step by step.",
            },
            {"role": "user", "content": "how can I solve 8x + 7 = -23"},
        ],
        response_format=MathReasoning,  # MathReasoning クラスの形式で返答
    )

    math_reasoning = completion.choices[0].message

    # If the model refuses to respond, you will get a refusal message
    if math_reasoning.refusal:
        print(math_reasoning.refusal)
    else:
        print(math_reasoning.parsed)


class ImageFeatures(BaseModel):
    main_object: str
    sub_object1: str
    sub_object2: str
    sub_object3: str
    background: str
    situation: str
    main_color: str


def encode_image(image_path: str):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def detect_objects(image_path: str) -> str:
    """image_pathの画像ファイルに写っている物体を検出します。

    どのような種類のものを検出するかは、ImageFeatures 参照です。

    Args:
        image_path (str): 検出対象の画像のパス

    Returns:
        str: parse済みのjson
    """
    client = OpenAI()

    base64_image = encode_image(image_path)

    response = client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "あなたは正直者です。見えたものをそのまま表現します",
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "画像に写っているものを列挙して下さい"},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{base64_image}"},
                    },
                ],
            },
        ],
        temperature=0.0,
        response_format=ImageFeatures,  # IamgeFeastures クラスの形式で返答
    )

    # 確認の為に表示 消してOK
    print(response.choices[0].message.content)
    content = json.loads(response.choices[0].message.content)
    parsed_json = json.dumps(content, indent=4, ensure_ascii=False)
    print(parsed_json)
    print(response.choices[0].message.content)

    return parsed_json


if __name__ == "__main__":
    # sample()
    image_path = "<your_imaeg_path>"  # 画像を配置して下さい。
    detect_objects(image_path)
