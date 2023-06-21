# Write your solution here

year = int(input("Year: "))
intyear = year

while True:
    year += 1
    if year % 4 == 0:
        if year % 100 != 0:
            break
        elif year % 100 == 0 and year % 400 == 0:
            break
        elif year % 100 != 0 and year % 400 == 0:
            break

print(f"The next leap year after {intyear} is {year}")

