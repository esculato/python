# Write your solution here

width = int(input("Width: "))
hash = ""

while width > 0:
    hash += "#"
    width -= 1

print(hash)