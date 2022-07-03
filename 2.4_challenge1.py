# Encapsulation Challenge 1

# You are given a partially completed code of a Rectangle class in the editor. 
# Implement the class by completing the tasks below.

# 1. Implement a constructor to initialize the values of two private properties: length and width.

# 2. Implement a method, area(), in the Rectangle class that returns the product of length and width. See the formula below:

# Area=length×width

# 3. Implement a method, perimeter(), in the Rectangle class that returns two times the sum of length and width. See the formula below:

# Perimeter=2×(length+width)

#Treat this variable as a multi-line comment
GivenCode = """class Rectangle:
    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass
"""


class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        area = self.__length * self.__width
        return area

    def perimeter(self):
        perimeter = 2 * (self.__length + self.__width)
        return perimeter

rect1 = Rectangle(5,10)

print('Area: ', rect1.area())
print('Perimeter: ', rect1.perimeter())

