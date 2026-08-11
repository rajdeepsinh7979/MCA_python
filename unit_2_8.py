''' Write a program to illustrate variable scope 
using local global and nonlocal variables. '''

name = 'rajdeepsinh'

print('value before global variable change : ',name)

def func1():
    global name
    name = 'rajbha'
    rollno = 4028
    print('value after global variable change : ',name)
    
    def func2():
        nonlocal rollno
        rollno = 7030
        div = 'A'
        print('nonlocal variable after change : ',rollno)
        print('local variable div : ',div)
    func2()
func1()
