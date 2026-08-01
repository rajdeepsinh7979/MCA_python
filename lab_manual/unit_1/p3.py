a = int(input("enter the number 1 :"))
b= int(input("enter the number 2 :"))

add = a+b
sub=a-b
mul=a*b
div=a/b

print("addition is ",add)
print("subtraction is ",sub)
print("multiplication is ",mul)
print("division is ",div)


print()

print("***********Now reational operator***********")

if( a<b and a>10):
    print("a is in the range")
else:
    print("a is not in range")

print()
print("equals ? ",a==b)
print("not equals ? ",a!=b)
print("a is greater? ", a>b)
print("a is lesser? ",a<b)
print("b is greater? ", a<b)
print("b is lesser? ",a>b)

print()

if(a<b and a>5):
    print("a is in the range")
elif(b>50 or b<40):
    print("b is in the range")
else:
    print("numbers are invalid")

li = [10,20,30,40]

if(not(a<b)):
    print("a i bigger")
else:
    print("b is bigger")
    
