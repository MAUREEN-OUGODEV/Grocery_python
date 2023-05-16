class Customer:
     def __init__(self,name,email,password,phone_number,id_number,address):
        self.name=name
        self.email=email
        self.password=password
        self.phone_number=phone_number
        self.id_number=id_number
        self.address=address

    def name(self):
        return f"Name:{self.name}"

    def email():
        return f"Email: {self.email}"  

    def password():
        return f"Password: {self.password}"     

    def phone_number():
        return f"Phone number: {self.phone_number}" 

    def id_number():
        return f"Business id:  {self.id_number}" 

    def address():
        return f"Adress:{self.address}"  


class Products :
    def __init__(self,name,category,price,description):
        self.name=name
        self.category=category
        self.price=price
        self.description=description

    def add_to_cart(self,cart):
        cart.append(self)

    def remove_from_cart():
        cart.remove(self)
     
    def total_cost():
        return self.price *quantity
     