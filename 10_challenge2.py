# Implement class 'Student' with 4 properties and 2 methods and all of these should be public.

# 4 properties: name, phy, chem, bio
# 2 methods: totalObtained and percentage

#It takes input of name and marks from student and calculate total marks obtained and the percentage from total marks as 300

class Student():
    def __init__(self, name,phy,chem,bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio
    def totalObtained(self):
        return self.phy + self.chem + self.bio
    def percentage(self):
        percent = ((self.phy + self.chem + self.bio)/300) * 100
        return percent

student1 = Student('Augustus', 80, 90, 100)
print('Total Obtained: ', student1.totalObtained())
print('Percentage: ', student1.percentage())