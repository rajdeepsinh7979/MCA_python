'''5. Write a program to implement single multilevel 
and multiple inheritance. '''

class university:
    def __init__(self):
        print('single inheritance parent class')

class student(university):
    def show2(self):
        print('single inheritance child class')

s=student()
s.show2()

print('=======================================================')
class a:
    def display(self):
        print('multilevel inheritance parent class')
class b(a):
    def display2(self):
        super().display()
        print('multilevel inheritance child class of a')
class c(b):
    def display3(self):
        super().display2()
        print('multilevel inheritance child class of a')

obj=c()
obj.display3()

print('=======================================================')
class a1:
    #def display(self):
    def __init__(self):
        print('multiple inheritance parent class 1')
class a2:
    #def display2(self):
    def __init__(self):
        print('multiple inheritance parent class 1')
class a3(a1,a2):
    def display3(self):
        #super().display()
        #super().display2()
        print('multiple inheritance child class of a1,a2')

a=a3()
a.display3()
