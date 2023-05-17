class Product:
    def __init__(self,product_name,product_price,quantity,category):
        self.product_name= product_name
        self.product_price = product_price
        self.quantity = quantity
        self.category = category
    def item_sold(self, already_sold):
        
        if already_sold > self.quantity:
            print("stocks almost over")
        else:
            
            self.quantity -= already_sold
            print(f"{already_sold} {self.product_price}")

    def adding_stock(self, add_quality):
        
        self.quantity += add_quality
        print(f"{add_quality} {self.product_name}")

    def total_sales(self):
       
        sales = self.price * (self.quantity)
        return sales    