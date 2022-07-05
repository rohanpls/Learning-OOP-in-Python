# Terminology in Inheritance:

# 1. Parent Class (Base class or Super Class): This class allows the reuse of its public properties in another class

# 2. Child class (Derived class or sub class): This class inherits or extends the parernt class. 

# * A child class has all public attributes of the parent class

# Syntax:

class ParentClass:
    # Attributes of parent class
    pass

class ChildClass(ParentClass):
    # Attributes of child class
    pass



# Example:

class programminglanguage:
    def __init__(self, creator, year):
        self.creator = creator
        self.year = year

    def details(self):
        print('Created by: ', self.creator)
        print('Year: ', self.year)

class Python(programminglanguage):
    def __init__(self,name, creator,year): # We will take some arguements
        self.name = name           
        programminglanguage.__init__(self, creator, year)  # Pass the values

    def info(self):
        print('Name: ', self.name)
        self.details()
    
lang1 = Python('Python', 'Guido van Rossum', 1991 )
lang1.info()