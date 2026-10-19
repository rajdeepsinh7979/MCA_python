'''6. Write a program to demonstrate method 
overriding and polymorphism. '''

class a:
    def msg(self,rollno):
        print('roll no.: ',rollno);

class b(a):
    def msg(self,rollno):
        super().msg(4028)
        print('roll no.[1]: ',rollno)


b2=b()
b2.msg(1020)
