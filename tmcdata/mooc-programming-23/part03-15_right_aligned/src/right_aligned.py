# Write your solution here

string = input("Please type in a string: ")
line = 20 - len(string)
star = ""
x = 1

while x <= line:
    star += "*"
    x += 1

print(star + string)

""" word = input("Please type in a string: ")
 
aligned = (20 - len(word)) * "*" + word
 
print(aligned) """