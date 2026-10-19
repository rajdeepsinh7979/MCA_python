'''5. Write a program to implement single multilevel 
and multiple inheritance. '''

print('---------------single inheritance---------------')
class abc:
    def __init__(self):
        print('single inheritance class')

class xyz(abc):
    def show(self):
        print('single inheritance object')

a=xyz()
a.show()

print('----------------multilevel inheritance-------------------')

class yuvraj:
    def abc(self):
        print('abc object')
        
class zala(yuvraj):
    def xyz(self):
        super().abc()
        print('xyz object')
        
class sinh(zala):
    def dfg(self):
        super().xyz()
        print('dfg object')
        
b=sinh()
b.dfg()

print('------------------multiple inheritance--------------------')
class a1:
    def __init__(self):
        super().__init__()
        print('mu')
class a2(a1):
    def __init__(self):
        super().__init__()
        print('college')
class a3(a2):
    def display1(self):
        print('mu and college')
c=a3()
c.display1()
