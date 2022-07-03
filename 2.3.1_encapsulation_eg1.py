# Under Encapsulation using two examples.

#The bad example

class User():

    def __init__(self, username, password):
        self.username = username
        self.password = password
        # This is dangerous because no encapsulation is protecting credentials of user.

    def login(self, userval, passwval):
        if ((self.username.lower() == userval.lower()) and (self.password == passwval)):
            return print("Login successful")
        else:
            return print("Invalid login")


obj1 = User('Androxus','pass99')

obj1.login('androxus', 'pass99')

obj1.login('Androxus', 'wrongpass')

obj1.password = 'wrongpass'

# And thus it's exploitable

obj1.login('Androxus', 'wrongpass')