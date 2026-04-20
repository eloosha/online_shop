from src.main import Category, Product


def test_product_init(my_product):
    assert my_product[0].name == "Арбуз"
    assert my_product[1].description == "оранжевый"
    assert my_product[2].price == 55
    assert my_product[3].quantity == 5


def test_category_init(my_category):
    assert my_category.name == "Фрукты"
    assert len(my_category._products) == 4
    assert my_category._products[0].name == "Арбуз"


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


def test_price_setter():
    my_product = Product("Яблоко", "красное", 45, 5)

    my_product.price = -1
    assert my_product.price == 45

    my_product.price = 0
    assert my_product.price == 45

    my_product.price = 50
    assert my_product.price == 50


def test_new_product():
    product_dict = {
        "name": "55 QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7,
    }

    my_new_product = Product.new_product(product_dict)
    assert my_new_product.name == "55 QLED 4K"
    assert my_new_product.description == "Фоновая подсветка"
    assert my_new_product.price == 123000.0
    assert my_new_product.quantity == 7


def test_products_getter(my_category):
    result = my_category.products

    assert result[0] == "Арбуз, 300 руб. Остаток: 10"
    assert result[1] == "Мандарин, 25 руб. Остаток: 25"


def test_add_product(my_category):
    new_product1 = Product("Арбуз", "зелено-красный", 500, 3)
    my_category.add_product(new_product1)

    assert my_category._products[0].price == 500
    assert my_category._products[0].quantity == 13
    assert len(my_category._products) == 4

    new_product2 = Product("Киви", "зеленый", 400, 10)
    my_category.add_product(new_product2)

    assert my_category._products[4].name == "Киви"
    assert my_category._products[4].description == "зеленый"
    assert my_category._products[4].price == 400
    assert my_category._products[4].quantity == 10
    assert len(my_category._products) == 5
