# Write your solution here

string = input("Please type in a string: ")
index = 1

while index <= len(string):
    number = index * -1
    print(string[number])
    index += 1

#OR 

#input_string = input("Please type in a string: ")
#index = -1
#while index >= -len(input_string):
#    print(input_string[index])
#    index -= 1