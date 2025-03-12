class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        self.items.append((item, price))

    def calculate_total(self):
        return sum(price for item, price in self.items)

# Usage
cart = ShoppingCart()
cart.add_item("Apple", 30)
cart.add_item("Milk", 50)
print(f"Total: {cart.calculate_total()}")
