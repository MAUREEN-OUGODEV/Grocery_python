class Order:
   
    def __init(self,customer_id,product):
        self.customer_id = customer_id
        self.product = product
        #This attribute is a method for calculating total price of the products added
        self.total_price = self.calculate_total_price
    
    def add_product(self,product):
       self.product.append(product)
       self.total_price = self.calculate_total_price
    
    def remove_product(self,producr):
        self.product.remove(product)
        self.total_price = self.calculate_total_price
    
    def calculate_total_price(self)
           total_price = 0
        for item in self.items:
            total_price += item.price
        return total_price


