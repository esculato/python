'''
This is my first script
'''
from my_pkg.my_sub_pkg01.module01 import (
    get_even_numbers
)
from my_pkg.my_sub_pkg01 import module02
number_cats = 10
number2 = number_cats / 1
age = input('Enter the age: ')
print("Hello", "from my first script in python", sep=',')
print(get_even_numbers(limit_number=100))
module02.say_hello()
