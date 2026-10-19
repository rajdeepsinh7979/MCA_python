'''10.Write a program to perform file pointer 
operations using seek and tell methods. '''

with open('text.txt','w') as f:
    f.write('hello\nhello')

with open('text.txt', 'r') as f:
    print("Initial file pointer position:", f.tell())
    
    print("Read 5 characters:", f.read(5))
    print("Position after reading 5 characters:", f.tell())
    
    f.seek(0)
    print("Position after seek(0):", f.tell())

