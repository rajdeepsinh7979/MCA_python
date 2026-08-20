''' 10.Write a program to extract specific information 
from a text file using regular expressions.  '''

import re

obj = re.compile(r'\d+')

str1 = 'hello this is rajdeepsinh. my number is 9998884444.'

result = obj.search(str1)

print(result.group())
