class Product:
    def __init__(self, product_id, product_name, quantity, price, category):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.category = category

    def add_product(self):
        self.quantity += 1
        print("Product added successfully!")

    def search(self, product):
        if self.product_name == product and self.quantity > 0:
            return "Product Found"
        return "Product Not Found"

    def update(self, new_price):
        self.price = new_price
        print("Price updated successfully!")

    def delete(self):
        id = int(input("Enter product id to remove: "))

        if id == self.product_id:
            if self.quantity > 0:
                self.quantity -= 1
                print("Product removed successfully!")
            else:
                print("Out of stock")
        else:
            print("Invalid Product ID")

    def details(self):
        print("\nProduct ID :", self.product_id)
        print("Product Name :", self.product_name)
        print("Price :", self.price)
        print("Category :", self.category)
        print("Quantity :", self.quantity)


pr = Product(101, 'Dabur Babul', 25, 250, 'toothpaste')

pr.details()
print(pr.search('Dabur Babul'))

pr.update(300)
pr.details()