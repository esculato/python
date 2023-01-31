def isPhoneNumber(text):
    if len(text) != 11:
        return False # not phone number-sized
    for i in range(0, 1):
        if not text[i].isdecimal():
                return False # no area code
    if text[2] != '-':
        return False # missing dash
    for i in range (3, 10):
        if not text[i].isdecimal():
            return False # no  digits
    return True

# print(isPhoneNumber('06-12345687'))

message = 'Call me 06-12345678 tomorrow, or at 06-87654321'
foundNumber = False
for i in range (len(message)):
    chunk = message[i:i+11]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers.')
          
        
