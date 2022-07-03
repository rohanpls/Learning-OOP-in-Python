# Create a program which has a class "squaresum"

# It initializes with 3 values and returns the sum of the squares of each numbers.

# Example: input of 2,3,4 returns the value 29

class squaresum():
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def calcsqsum(self):
        return (self.x * self.x) + (self.y * self.y) + (self.z * self.z)

test1 = squaresum(2,3,4)

print(test1.calcsqsum())