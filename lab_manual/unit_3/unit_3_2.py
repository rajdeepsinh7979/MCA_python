import math

print('Standard import')
print(math.sqrt(25))

from math import factorial
print('from package import')
print(factorial(5))

import math as mt
print('using as keyword : ')
print(mt.ceil(5.3))

from math import *
m=math
print('using as keyword')
print(m.floor(5.3))
