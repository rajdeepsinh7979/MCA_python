'''9. Write a program to use re module functions 
such as match, search and find all. '''

import re

obj = re.compile(r'm\w\w')

str1 = 'hello mat this guy ?'
str2 = 'mat this guy ?'
str3 = 'hello mat this man ?'

result = obj.search(str1)
result1 = obj.match(str2)
result2 = obj.findall(str3)

print('using search method : ',result.group())
print('using match method : ',result1.group())
print('using findall method : ',result2)
