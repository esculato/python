# Write your solution here

width = int(input("Width: "))
height = int(input("Height: "))

hash = ""

while width > 0:
    hash += "#"
    width -= 1

while height > 0:
    print(hash)
    height -= 1