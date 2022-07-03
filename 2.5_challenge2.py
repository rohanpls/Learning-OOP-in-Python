# Encapsulation Challenge 2

# Implement the complete Student class by completing following tasks

Challenge2 = """Implement the following properties as private:
    name
    rollNumber

Include the following methods to get and set the private properties above:

    getName()
    setName()
    getRollNumber()
    setRollNumber()

Implement this class according to the rules of encapsulation.
"""

# Note: Do not use initializers to initialize the properties. Use the set methods to do so.
# If the setter is not defined properly, the corresponding getter will also generate an error even if the getter is defined properly.

SampleCode="""class Student:
    def setName(self):
        pass

    def getName(self):
        pass

    def setRollNumber(self):
        pass

    def getRollNumber(self):
        pass
    """

class Student:
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber

obj1 = Student()

obj1.setName('Hughie')
print(obj1.getName())

obj1.setRollNumber(10)
print(obj1.getRollNumber())