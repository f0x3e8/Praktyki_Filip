class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def total_value(self):
        return self.price * self.qty

    def is_available(self):
        if self.qty > 0:
            return True
        else:
            return False

    def sell(self, amount):
        if self.qty <= 0 or amount > self.qty:
            return False
        else:
            self.qty -= amount

    def inventory_value(inventory):
        all = 0
        for i in inventory:
            all += i.total_value()
        return all

    def available_products(inventory):
        available = []
        for i in inventory:
            if i.is_available():
                available.append(i.name)
        return available

    def low_stock(inventory, threshold):
        low_stock = []
        for i in inventory:
            if i.qty < threshold:
                low_stock.append(i.name)
        return low_stock

    def most_valuable(inventory):
        best_total = inventory[0].total_value()
        best_name = inventory[0].name
        for i in inventory:
            if i.total_value() > best_total:
                best_total = i.total_value()
                best_name = i.name
        return best_name

    def find_by_name(inventory, name):
        for i in inventory:
            if i.name == name:
                return i
            else:
                return None

inventory = [
    Product("chleb", 5, 12),
    Product("mleko", 3, 0),
    Product("masło", 9, 3),
    Product("ser", 24, 7),
]

print(Product.inventory_value(inventory))          # 255
print(Product.low_stock(inventory, 5))             # ["mleko", "mas?o"]
print(Product.most_valuable(inventory))       # ser

bread = Product.find_by_name(inventory, "chleb")
bread.sell(2)
print(bread.qty)                           # 10
print(Product.inventory_value(inventory))          # 245