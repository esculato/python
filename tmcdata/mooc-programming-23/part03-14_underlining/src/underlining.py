# Write your solution here
string = input("Please type in a string: ")
line = ""
x = 0

while len(string) > 0:
    print(string)
    while len(string) > x:
        line += "-"
        x += 1
    print(line)
    string = input("Please type in a string: ")
    line = ""
    x = 0

#    while True:
#    string = input("Please type in a string: ")
#    if string == "":
#        break
#    print(string)
#    print(len(string) * "-")
 