# Write your solution here

limit = int(input("Upper limit: "))
sum = 0
number = 0
numbers = "" 


while sum < limit:
    number += 1
    sum += number
    numbers += f"{number}"
    if sum < limit:
        numbers += " + " 

print(f"The consecutive sum: {numbers} = {sum}")
#print(f"Limit: {limit}")
