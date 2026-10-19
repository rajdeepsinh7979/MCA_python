'''8. Write a program to demonstrate encapsulation 
and abstraction using classes. '''

from abc import ABC, abstractmethod


class a(ABC):
    @abstractmethod
    def news(self):
        pass

class b(a):
    def news(self):
        print('hello')

b1=b()
b1.news()
        
