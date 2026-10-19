'''9. Write a program to read and write data into a 
file using different file modes. '''


data=['101','rajdeepsinh']

with open('mdata.txt','w') as f:
    f.writelines(data)
with open('mdata.txt','r') as f:
    print(f.read())
