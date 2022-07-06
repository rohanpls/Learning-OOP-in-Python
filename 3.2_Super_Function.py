# super() function

# It is used while implementing inheritance. It's used in child class to refer to parent class without needing to name it explicitly. 

class Shape:   # Defining parent class

    value1 = 99  # property value
    def display(self):
        print("I'm from Shape class!")


class Rectangle(Shape):   #Defining Child class

    value1 = 100    # Can assign new value to inherited property
    def display(self):
        super().display()  # Calling parent class method display
        print("I'm from Rectangle Class!")

        print("Value 1 from Shape class: ", super().value1)  # We can still access value from parent class
        print("Value 1 from Rectangle Class: ", self.value1)  # Update property in child class
    
rect1 = Rectangle()
rect1.display()  # Calling Rectange class method display()