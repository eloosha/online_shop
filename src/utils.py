import json
import os

from src.main import Category, Product


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: list[dict]) -> list[Category]:
    categories = []

    for category in data:

        products = []

        for product in category["products"]:
            product_obj = Product(**product)
            products.append(product_obj)

        category_obj = Category(
            name=category["name"],
            description=category["description"],
            products=products,
        )

        categories.append(category_obj)

    return categories
