class Product:
    def __init__(self, price):
        self.price = price  # This will call the setter method to validate the price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

  
product = Product(10)

print(product.price)
