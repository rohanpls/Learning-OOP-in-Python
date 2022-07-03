# Under Encapsulation using two examples.

#The good example

class User():
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    
    def login(self, user, passw):
        if ((self.__username == user) and (self.__password == passw)):
            print('Login success!')
        else:
            print('Invalid Login')

obj1 = User('Frigo','StrongPass123')

#Check if login works
obj1.login('Frigo','StrongPass123')

# obj1.__password   # AttributeError: 'User' object has no attribute '__password'

# And thus this will do nothing at all:
obj1.__password = "Pass123"  

obj1.login('Frigo','Pass123')

#Invalid login

#And thus no one can change the value directly from main code

#Only way to do that would be through getters or setters