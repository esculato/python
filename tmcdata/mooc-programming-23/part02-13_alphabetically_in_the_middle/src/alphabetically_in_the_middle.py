# Write your solution here

letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

if letter1 < letter2 and letter1 < letter3:
    if letter2 < letter3:
        print(f"The letter in the middle is {letter2}")
    elif letter3 < letter2:
        print(f"The letter in the middle is {letter3}")

if letter2 < letter3 and letter2 < letter1:
    if letter3 < letter1:
        print(f"The letter in the middle is {letter3}")
    elif letter1 < letter3:
        print(f"The letter in the middle is {letter1}")  

if letter3 < letter1 and letter3 < letter2:
    if letter1 < letter2:
        print(f"The letter in the middle is {letter1}")
    elif letter2 < letter1:
        print(f"The letter in the middle is {letter2}")  

# letter1 = input("1st letter: ")
# letter2 = input("2nd letter: ")
# letter3 = input("3rd letter: ")
 
# if letter1 > letter2 and letter1 > letter3:
#     if letter2 > letter3:
#         middle = letter2
#     else:
#         middle = letter3
# elif letter2 > letter3:
#     if letter3 > letter1:
#         middle = letter3
#     else:
#         middle = letter1
# else:
#     if letter2 > letter1:
#         middle = letter2
#     else:
#         middle = letter1
 
# print("The letter in the middle is " + middle)


