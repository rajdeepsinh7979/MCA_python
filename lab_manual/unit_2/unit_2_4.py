num = int(input('enter the numer : '))
summ=0

while(num>0):
    digit = num%10
    summ=summ+digit
    num=num//10
    
print(summ)
