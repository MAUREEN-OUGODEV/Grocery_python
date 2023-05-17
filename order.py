lass Order:
   
    def __init__(self, product_name, quantity, price):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        
    def add_item(self, product):
        self.product_name = product.name
        self.quantity += 1
        self.price += product.price
    
    def calculate_total_price(self):
        return self.quantity * self.price
