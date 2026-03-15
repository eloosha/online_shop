from src.main import Category, Product


def test_product_init(my_product):
    assert my_product[0].name == "Арбуз"
    assert my_product[1].description == "оранжевый"
    assert my_product[2].price == 55
    assert my_product[3].quantity == 5


def test_category_init(my_category):
    assert my_category.name == "Фрукты"
    assert len(my_category.products) == 4
    assert my_category.products[0].name == "Арбуз"


def test_counter_one(my_category):
    assert Category.category_count == 1
    assert Category.products_count == 4


def test_counter_multiple():
    product_apple = Product("Яблоко", "красное", 45, 5)
    category_fruits = Category("Фрукты", "обычные", [product_apple])

    assert Category.category_count == 1
    assert Category.products_count == 1

    product_tomato = Product("Помидор", "красный", 35, 8)
    category_fruits = Category("Овощи", "стандартные", [product_tomato])

    assert Category.category_count == 2
    assert Category.products_count == 2


def test_counter_with_multiple_products():
    product_apple = Product("Яблоко", "красное", 45, 5)
    product_banana = Product("Банан", "желтый", 65, 2)
    product_orange = Product("Апельсин", "оранжевый", 55, 6)

    category = Category(
        "Фрукты", "спелые", [product_apple, product_banana, product_orange]
    )

    assert Category.category_count == 1
    assert Category.products_count == 3
