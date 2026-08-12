import pract1 as pr

print('operations : ')
print('1. addition')
print('2. subtraction')
print('3. multiplication')
print('4. division')

choice=int(input('enter you choice :'))
a= int(input('enter the number 1 : '))
b= int(input('enter the number 2 : '))

if choice == 1:
    print('addition is ',pr.add(a,b))
elif choice == 2:
    print('subtraction is ',pr.sub(a,b))
elif choice == 3:
    print('multiplication is ',pr.mul(a,b))
elif choice == 4:
    print('division is ',pr.div(a,b))
else:
    print("enter the valid choice.")
