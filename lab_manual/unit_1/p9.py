'''9. Write a program to define and use user-defined 
functions with different types of arguments. '''

#positional argument
def display(rollno):
    print(rollno)

#default argument
def display1(rollno=4028):
    print(rollno)

#variable length argument
def display2(*str1):
    print('variable length argument ',str1)

#keyword argument
def display3(age,name):
    print('age : ',age)
    print('name : ',name)
    
display(7030)
display1()
display2('marwadi','university')
display3(age=18,name='raj')

