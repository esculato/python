while True:
    print('How many cats do you have?')
    numCats = input()
    try:
        if int(numCats) >= 4:
            print('Thats a lot of cats.')
            break
        elif int(numCats) <0:
            print('You cannot have negative cats!')
        else:
            print('That is not that many cats.')
            break
    except ValueError:
        print('You did not enter a number.')
    
        
