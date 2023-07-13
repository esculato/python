# Write your solution here

string = input("Please type in a string: ")
first = string[0]
x = 1

while string[0] != string[:x]:
    print(string[:x])
    x = x + 1