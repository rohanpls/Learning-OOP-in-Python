# What are Instance and class variables?
#
# Instance variables are those which are defined outside the intializer function. 
#
# - This can be used for properties that need to be shared among objects without 
#   needing to define it everytime.
#
#
# Class Variables are those which are defined inside the intializer function. 
#
#  - These variables need to be defined when objects are intialized or you will get an error
#
#
# Here is our example class:

class Employee:
    type = 'Permanent'   #This would be the instance variable
    # You can assign string, int, bool, list, dict, any python variable you want.

    # It cannot be taken as an arguement but can be changed indivudually later

    def __init__(self, namevalue, departmentvalue, salaryvalue):
        # Our Class variables as you already know: 
        self.name = namevalue
        self.department = departmentvalue
        self.salary = salaryvalue

#Let's create one object with the class we just made

employee99 = Employee('Lucas', 'IT', '$90k')

# Check the printed values

print("Employee Name: ", employee99.name)
print("Employee Department: ", employee99.department)
print("Employee Salary: ", employee99.salary)
print("Employment Type: ", employee99.type)

# Everything checks out

# Every object made through this class will have type = 'Permanent'

print('\n')

# Let's say we have another employee

employee97 = Employee('Diana', 'Accounting', '$75k')

# They would have 'Permanent' employment type because of instance variable

# But let's say this one specific employee is on Contract

employee97.type = 'Contract'

# (Yes python allows defining like this)

# Now let's see result

print("Employee Name: ", employee97.name)
print("Employee Department: ", employee97.department)
print("Employee Salary: ", employee97.salary)
print("Employment Type: ", employee97.type)

# As you can see, every object of class employee will be considered as 'Permanent'
# unless specifically defined

# !Note: In a situation where instance variable is a list
# !do not append to a instance List unless intended because it will append values to the instance
# !itself which would result in same values for every object of that class
# !Python will not throw an error for this.
