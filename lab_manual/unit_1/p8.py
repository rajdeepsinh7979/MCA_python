""". Write a program to explain mutable and 
immutable objects in Python. """

def message(x):
    
    return x
    
list1 = [10,20,30,40]
list2=[]

list2= message(list1)

if(len(list2) == 5):
    print("mutable")
else:
    print("immutable")
     
if(len(list2) >= 0):
    print("mutable")
else:
    print("immutable")
    
print(list2)    
