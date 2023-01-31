import re

message = 'Call me 06-12345678 tomorrow, or at 06-87654321'
        
phoneNumRegex = re.compile(r'\d\d-\d\d\d\d\d\d\d\d')
print(phoneNumRegex.findall(message))


