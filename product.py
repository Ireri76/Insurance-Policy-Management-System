# product.py
class Product:
    def __init__(self, product_id, name, kes, availability=True):
        self.product_id = product_id
        self.name = name
        self.price = kes  # Store the price as Kenya shillings
        self.availability = availability  # Product can be 'available' or 'suspended'

    def update_price(self, new_price):
        self.price = new_price
        print(f"Product {self.name} price updated to kes {self.price}")

    def suspend_product(self):
        self.availability = False
        print(f"Product {self.name} is suspended.")

    def activate_product(self):
        self.availability = True
        print(f"Product {self.name} is now available.")
    
    def display_details(self):
        status = 'Available' if self.availability else 'Suspended'
        print(f"Product ID: {self.product_id}, Name: {self.name}, Price: kes {self.price}, Status: {status}")
