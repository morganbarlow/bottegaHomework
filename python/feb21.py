class Shop:
  def __init__ (self, name, products):
    self.name = name
    self.products = products

  def (self,product):
    if product in self.products:
      return f'You purchased the {product}'
    else:
      return f'Sorry, {product} is out of stock'

    def __str__(self):
      return f'This is the store class with a name of {self.name} and these products: {self.products}'

    def __repr__(self):
      return f'Store Object: name= {self.name}, products = {self.products}'

class CandyStore(Store):
  def try_product(self, product):
    if product in self.products:
      return f'You tried on the {product}, they fit!'
    else:
      return f'Sorry, {product} is out of stock at {self.name}'

class Bakery(Store):
  def try_product(self, product):
    if product in self.products:
      return f'You tested the {product}, you like this one!'
    else:
      return f'Sorry, {product} is out of stock at {self.name}'

  # def __str__ (self):
  # def __repr__ (sef):


rocky_mt_chocolate = CandyStore('Rocky Mt. Chocolate', ['Candy apple','Chocolate strawberries','bon bon'])
lehi_bakery = Bakery('Lehi Bakery', ['square donut','bread','Jeans','Sweats'])
ulta = PerfumeStore('Ulta', ['Irmani','Daisy Made', 'Gucci', 'Fenty'])

print(nike.purchase_product('Rosches'))
print(str(nike))
print(repr(nike))
print(h_and_m.try_product('Jeans'))
print(h_and_m.try_product('Bag'))
print(ulta.try_product('Fenty'))