"""インスタンスごとに変数を格納する書き方。pydanticのみ見てください。"""

from dataclasses import dataclass

from pydantic import BaseModel, Field


# これは、クラス変数になります。
class Item:
    id: int
    name: str
    price: float


# インスタンス変数に格納する方法
class Product:
    def __init__(self, id: int, name: str, price: float) -> None:
        self.id = id
        self.name = name
        self.price = price


# dataclassを使うと、インスタンス変数に格納することができます
@dataclass
class Merchandise:
    id: int
    name: str
    price: float


# Pydanticで書くとこうなります。特に、Field()で説明を追加できることが後々役に立ちます。
class Goods(BaseModel):
    id: int = Field(..., description="The ID of the product")
    name: str = Field(..., description="The name of the product")
    price: float = Field(..., description="The price of the product. USD")


if __name__ == "__main__":
    # item = Item(id=1, name="Banana", price=2.0) # これはエラーになります。
    product = Product(id=2, name="Apple", price=1.0)
    merchandise = Merchandise(id=3, name="Cherry", price=3.0)
    goods = Goods(id=4, name="Date", price=4.0)

    # print(item)
    print(product)
    print(merchandise)
    print(goods)
