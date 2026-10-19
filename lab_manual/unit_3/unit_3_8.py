'''8. Write a program to demonstrate basic regular 
expression pattern matching. '''

import re

obj = re.compile(r'm\w\w')

str1 = 'hello mat this guy?'

result = obj.search(str1)

print(result.group())
