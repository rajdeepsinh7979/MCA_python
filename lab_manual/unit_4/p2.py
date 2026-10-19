# 2. Write a program to demonstrate constructor and destructor usage.

class student():
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
        
    def message(self):
        print("rollno is ",self.rollno)
        print("name is ",self.name)
        
    def __del__(self):
        print('resources destructed.')
        
s = student(10,'rajdeepsinh')
s.message()

del s
