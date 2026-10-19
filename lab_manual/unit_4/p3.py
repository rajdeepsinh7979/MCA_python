# 3. Write a program to illustrate instance variables and class variables.

class Student:
    collage_name = "MU"

    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name
    
    def printinfo(self):
        print('rollno. is ',self.rollno)
        print('name is ',self.name)
        print('college is ',Student.collage_name)

s1=Student(101,'rajdeepsinh')
s1.printinfo()
s2=Student(102,'test')
s2.printinfo()
