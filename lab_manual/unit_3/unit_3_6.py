'''6. Write a program to perform file and directory 
operations using os and sys modules.'''

import os
import sys
directory_name = os.path.dirname('D:\\4028_rajdeepsinh\\back-up\\backup_python\\unit_3')
print('directory name : ',directory_name)

file_name = os.path.isfile('D:\\4028_rajdeepsinh\\back-up\\backup_python\\unit_3\\unit_3_10.py')
print('file found : ',file_name)

base_name = os.path.basename('D:\\4028_rajdeepsinh\\back-up\\backup_python\\unit_3')
print('directory name : ',base_name)

absolute = os.path.isabs('D:\\4028_rajdeepsinh\\back-up\\backup_python\\unit_3')
print('is absolute path : ',absolute)

