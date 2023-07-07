# Write your solution here

word = input("Word: ")
x = 1
frame = ""

if len(word) % 2 ==  0:
    space1 = ((28 - len(word)) // 2) * " "
else:
    space1 = (((28 - len(word)) // 2) + 1) * " " 

space2 = ((28 - len(word)) // 2) * " "

middle = "*" + space1 + word + space2 + "*"

while x <= 30:
    frame += "*"
    x += 1

print(frame)
print(middle)
print(frame)

""" word = input("Word: ")
 
print("*" * 30)
spaces_at_start = (28 - len(word)) // 2
spaces_at_end = spaces_at_start
 
# If the word length is odd, one is added to the spaces at the end of the word
# to get all 30 characters filled
if len(word) % 2 != 0:
    spaces_at_end += 1
 
print("*" + spaces_at_start * " " + word + spaces_at_end * " " + "*")
print("*" * 30) """
 