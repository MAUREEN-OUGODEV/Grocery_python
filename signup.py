class Signup:
    def __init__(self, name, email, phone_number, password):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.account_created = False

    def create_account(self):
         print("Account created successfully")
         self.account_created = True

    def login(self, email, password):
        if email == self.email and password == self.password:
            print("Logged in successfully") 
        else:
            print("Incorrect email or password")  

    def update_email(self, new_email):
           self.email = new_email
           print("Email updated successfully")

    def update_phone_number(self, new_number):
        self.phone_number = new_number 
        print("Phone number updated successfully") 

    def update_password(self, new_password):
        self.password = new_password
        print("Password updated successfully")

    def delete_account(self):
        self.account_created = False
        print("Account deleted successfully")         
                       
