# Now let's get to interaction between properties and other objects

# There are three types of methods in Python:
# 1. instance methods
# 2. class methods
# 3. static methods

# We will focus on instance methods 

# methods are basically functions of a class which perform some operations and may or may not return values

# Return statement makes it possible to get a value from the method / function

class Employee:
    type = "Permanent"

    def __init__(self, idvalue, namevalue, departmentvalue, salaryvalue):
        self.eID = idvalue
        self.name = namevalue
        self.department = departmentvalue
        self.monthlysalary = salaryvalue

    # Self arguement in methods only need to be passed during method defination and not when it's called
    def tax(self):
        return (self.monthlysalary * 0.2)

    def salaryPerDay(self):
        return (self.monthlysalary / 30)

employee98 = Employee(98, 'Casper', 'Human Resources', 40000)

print('Employee ID: ', employee98.eID)
print('Employee Name: ', employee98.name)
print('Employee Department: ', employee98.department)
print('Employee Monthly Salary: ', employee98.monthlysalary)

# Now we can use the methods to get specific values when needed

print('Employee Tax: ', employee98.tax())
print('Employee Salary Per day: ', employee98.salaryPerDay())
