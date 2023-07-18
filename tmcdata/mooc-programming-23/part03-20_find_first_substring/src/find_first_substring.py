# Write your solution here

word = input("Please type in a word: ")
char = input("Please type in a character: ")
first = word.find(char)
second = first + 3

if len(word) - first >= 3:
    print(word[first:second])
else:
    print("")

""" word = input("Please type in a word: ")
character = input("Please type in a character: ")
 
index = word.find(character)
if index!=-1 and len(word)>=index+3:
    print(word[index:index+3]) """
 