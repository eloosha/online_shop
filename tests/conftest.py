import pytest
from src.main import Product
from src.main import Category


@pytest.fixture()
def my_product():
    product1 = Product('Арбуз', 'зелено-красный', 300, 10)
    product2 = Product('Мандарин', 'оранжевый', 25, 25)
    product3 = Product('Яблоко', 'зеленое', 55, 15)
    product4 = Product('Банан', 'желтый', 45, 5)
    return [product1, product2, product3, product4]


@pytest.fixture()
def my_category(my_product):
    return Category('Фрукты', 'классические', my_product)

@pytest.fixture(autouse=True)
def reset_counters():
  Category.category_count = 0
  Category.products_count = 0
