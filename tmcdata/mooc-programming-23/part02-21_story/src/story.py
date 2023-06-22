# Write your solution here

word = "" 
words = ""
attempt = 0

while True:
    prevword = word
    word = input("Please type in a word: ")
    attempt += 1
    if word == "end":
        break
    elif word == prevword:
        if attempt > 1:
            break
    else:
        words += word + " "


print(f"{words}")