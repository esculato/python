#! python3

import re, pyperclip

# Create a regex for PO description
POdescriptionRegex = re.compile(r'''
# Separate PO description LP10589MS-P1462 S02345, LP10589 MS-P1462 S02345, MS-P1462 S02345

LP # first part VF
\w{8} # number part VF
-
\w\w\w\w\w
\s\w\d\d\d\d\d           # sitenumber

''', re.VERBOSE)

# Create a regex for email adresses
emailRegex  = re.compile(r''''
# some.+_thing@(d\25}))?.something.com

[a-zA-Z0-9_.+]+    # name part
@                # @ symbol
[a-zA-Z0-9_.+]+    # domain name part
''', re.VERBOSE)

# Get the text of the clipboard
text = pyperclip.paste()

# Get: Extract the podescription/email from this text
extractedPOdescr = POdescriptionRegex.findall(text)

allPOs = []
for Podescription in extractedPOdescr:
    allPOs.append(Podescription[0])
    
#extractedEmail = emailRegex.findall(text)

print(extractedPOdescr)
print(allPOs)
# print(extractedEmail)

# TODO: Copy the extraced email/phone to the clipboard
results = '\n'.join(allPOs)
pyperclip.copy(results)

