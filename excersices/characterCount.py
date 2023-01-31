import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {} # 'r': 5

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

rjtext = pprint.pformat(count)
print(rjtext)
