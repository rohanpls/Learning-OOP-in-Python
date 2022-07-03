# Access Modifiers in Python are as follows:

# 1. Public Attributes 
# 2. Private Attributes: 
#   2.1 Private Properties 
#   2.2 Private Methods

# 1. Public attributes are those that can access inside the class and outside the class

class Employee:

    def __init__(self, eID, salary):
            #These values are public 
        self.ID = eID
        self.salary = salary

    def showID(self):
        print("ID:", self.ID)


Charles = Employee(75, 25000)
Charles.showID()

# Since properties are public, we can directly access and print them 

print(Charles.salary)

# 2.1 Private Attributes - Properties
class Employee:

    def __init__(self, eID, salary):
        self.ID = eID
        self.__salary = salary  # salary is a private property
    def getSalary(self):
        print('Salary: ', self.__salary)

Mark = Employee(77, 30000)
print("ID: ", Mark.ID)  # Public Property
# print("Salary: ", Mark.__salary)        ----> This will thow an error
Mark.getSalary() 

# 2.2 Private attributes - Methods

class Employee:

    def __init__(self, eID, salary):
        self.ID = eID
        self.__salary = salary  # salary is a private property
    def getSalary(self):
        print('Salary: ', self.__salary)
    def __getID(self):
        print('ID: ',self.ID)

Donna = Employee(76, 30000)
Donna.getSalary()  # Public method
# Donna.__getID()   --------->  This will throw error because method is private and cannot be accessed by outside