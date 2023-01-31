def spam():
    global eggs
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0
    
eggs = 42
spam()
print(eggs)
