# Declaring a class 'employee' with some properties

class employee:
    
    #Logically, if properties need to be unique for the object, you can initialize them without value
    # we will assign 'None' as default value

    eID = None   #Employee ID
    department = None  #Employee Department
    Salary = None  #Employee Salary

    # Please note, initializing property values is necessary and won't compile without it.

# Creating an object of class Employee

Lucas = employee()

# Assigning values to our unique object

Lucas.eID = 100
Lucas.department = "IT"
Lucas.Salary = '$90k'

# Printing properties
print('Employee ID = ', Lucas.eID)
print('Employee Department = ', Lucas.department)
print('Employee Salary = ', Lucas.Salary)

# Python allows to create properties outside class as well:

Lucas.title = 'Software Engineer'

print('Employee title: ', Lucas.title)

# Note: title property will be exclusive for Lucas. New objects will only have those properties
# that are defined in the class.