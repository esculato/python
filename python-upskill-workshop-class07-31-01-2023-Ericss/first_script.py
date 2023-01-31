import utils.operations as operations
from utils.operations import addition
from utils.operations import substraction
## from operations import * <- uses more memory

from utils.files_operations import remove_file

print("This is my first script in Python")

'''
s1 = operations.addition(10,20)
print(s1)
s2 = operations.substraction(20,10)
print(s2)
'''

s1 = addition(10, 20)
print(s1)
s2 = substraction(20, 10)
print(s2)


print(__name__)