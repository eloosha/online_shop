

class Product:
  name: str
  description: str
  price: float
  quantity: int

  def __init__(self, name: str, description: str, price: float, quantity: int):
    self.name = name
    self.description = description
    self.price = price
    self.quantity = quantity

  def __str__(self):
    return f'Продукт: {self.name}({self.description}), {self.price} руб., количество: {self.quantity}'

  def __repr__(self):
    return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"

class Category:
  name: str
  description: str
  products: list
  category_count = 0
  products_count = 0

  def __init__(self, name: str, description: str, products: list[Product]):
      self.name = name
      self.description = description
      self.products = products

      Category.category_count += 1
      Category.products_count += len(products)

  def __str__(self):
    return f'Категория: {self.name}({self.description}), продукты: {self.products})'
