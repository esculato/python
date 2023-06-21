# Write your solution here

person1 = input("Person 1: ")
age1    = int(input("Age: "))
person2 = input("Person 2: ")
age2    = int(input("Age: "))

if age1 > age2:
    print("The elder is", person1)
elif age1 < age2:
    print("The elder is", person2)
else:
    print(person1, "and", person2, "are the same age")