# This code defines a class Product that demonstrates the usage of protected attributes and methods.
# It represents a product with a name and a price, showcasing encapsulation principles.

class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # protected variable

    def get_price(self):
        return self._price

    def modify_price(self, new_price):
        if new_price > 0:
            self._precio = new_price
            print(f"The price of {self.name} is updated to ${new_price}")  
        else:
            print("The price must be greater than zero")

product = Product("Shirt", 25.99)

print(f"The price of  {product.name} is €{product.get_price()}")                                             

#Attempting to change the price directly (not recommended)
product._price = 19.99

# Change the price using the method
product.modify_price(15.99)

# Attempting to set an invalid price
product.modify_price(-5.0)