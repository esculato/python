# Write your solution here

string = input("Please type in a string: ")
x = 1
print(string[:x])

while string[:x] != string:
    x = x + 1
    print(string[:x])

# string = input("Please type in a string: ")
 
# length = 1
# while length <= len(string):
#     print(string[0:length])
#     length += 1
 