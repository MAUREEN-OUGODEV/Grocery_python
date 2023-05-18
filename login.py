class Login:
   def __init__(self,correct_username,correct_password):
       self.correct_username=correct_username
       self.correct_password=correct_password


   def successful(self,username,password):
       if username==self.correct_username and self.correct_password:
           print("The process was successful")
       else:
           print("The process was unsuccessful")