# Write your solution here

word = "" 
words = ""

while True:
    prevword = word
    word = input("Please type in a word: ")
    if word == prevword:
        break
    else:
        words += word + " "

print(f"{words}")