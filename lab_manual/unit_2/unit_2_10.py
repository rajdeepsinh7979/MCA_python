'''10.Write a program to generate a sequence of 
numbers using generator functions and yield 
keyword. '''

def func1(n):
    while n>0:
        yield n
        n-=1

for i in func1(5):
    print(i)
