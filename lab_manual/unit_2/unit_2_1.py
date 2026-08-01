marks = int(input('enter the marks : '))

if(marks>0 and marks<45):
    print('you are fail.')
else:
    print('you are pass.')
    
if(marks >= 90 and marks < 100 ):
    print('your grade is A.')
elif(marks >= 75 and marks < 90 ):
    print('your grade is B.')
elif(marks >= 65 and marks < 75 ):
    print('your grade is c.')
elif(marks >= 45 and marks < 65 ):
    print('your grade is d.')
elif(marks >= 0 and marks < 45 ):
    print('your grade is e.')
else:
    print('enter a valid choice.')

    
    
