import re

text = 'Mi phone number is 123456, the zipcode is 11011 and my favorite number is 13'
result = re.findall('[0-9]+', text)
print('/'*100)
print(result)

print('/'*100)

import collections

numbers = [1,1,2,2,3,34,5,6]
counter = collections.Counter(numbers)
print(counter)

print('/'*100)

