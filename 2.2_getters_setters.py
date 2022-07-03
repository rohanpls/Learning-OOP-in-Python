# In order to allow controlled access to properties from outsite the class,
# getter and setter methods are used.

# A getter method, as you can guess, allows reading / getting property valuers
# getValue()

# A setter method, as you can guess, allows modifying / setting property values
# setValue()

# Example:

class Employee():
    def __init__(self, name,Id = None):
        self.__name = name
        self.__Id = Id
    def getBothValues(self):
        return self.__name, self.__Id
    def setValueID(self, Id1):
        self.__Id = Id1

obj1 = Employee('Grohk')
print('Reading both values: ', obj1.getBothValues())

obj1.setValueID(50)
print('Both values now: ', obj1.getBothValues())