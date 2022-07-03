# Create a class named Calculator. 

# Initializer for values num1 and num2
# add() returns sum, subtract() returns num1 from num2.
# multiply() returns product, divide() returns num2 by num1

class Calculator():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num2 - self.num1
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num2 / self.num1

object1 = Calculator(5,20)

print(object1.add())
print(object1.subtract())
print(object1.multiply())
print(object1.divide())