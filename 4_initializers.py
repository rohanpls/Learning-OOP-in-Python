# Initializer is used to initialize an object of a class.

# Initilization method is similiar to how function works but has pre-defined name: __init__

# Note: Double underscores mean it's a special method and python interpreter will treat as a special case

# The reason it's special is because it does have a return type.

class employee:
    def __init__(self, idvalue, departmentvalue, salaryvalue):
        self.eID = idvalue
        self.department = departmentvalue
        self.salary = salaryvalue

# So basically now you can pass arguements while initilizing the object to assign values directly

# The previous way: 

# Lucas.eID = 100
# Lucas.department = "IT"
# Lucas.Salary = '$90k'

# Now you can create a object like this:

Diana = employee(97, 'Accounting', '$75k')

# See how convenient that was?

print('Employee ID: ', Diana.eID)
print('Employee Department: ', Diana.department)
print('Employee Salary: ', Diana.salary)