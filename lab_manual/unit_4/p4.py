''' 4. Write a program to demonstrate instance 
methods class methods and static methods.'''

class Student:
    def instmethod(self):
        print('This is instance method.')
        
    @classmethod
    def clsmethod(cls):
        print('This is class method.')

    @staticmethod
    def stmethod():
        print('This is static method.')
        
s1=Student()
s1.instmethod()

Student.clsmethod()

s1.stmethod()
