
while True:
    pin = int(input("PIN: "))
    if pin == 4321:
        if attempt == 1:
            print("Correct! It only took you one single attempt!")
            break
        else:
            print(f"Correct! It took you {attempt} attempts")
            break
    else:
        attempt += 1
        print("Wrong")