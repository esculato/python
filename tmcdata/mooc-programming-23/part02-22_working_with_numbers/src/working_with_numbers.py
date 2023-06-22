# Write your solution here

print("Please type in integer numbers. Type in 0 to finish.")

count = 0
sum = 0
positive = 0
negative = 0

while True:
    number = int(input("Number: "))
    if number == 0:
        break
    count += 1
    sum += number
    mean = sum / count
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1

print("... the program asks for numbers")
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")