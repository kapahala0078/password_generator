import string
import random

print(''.join(random.choices(string.ascii_letters, k=8)))
#  ['R', 'n', 'J', 'T', 'k']

print(''.join(random.choices(string.ascii_letters + string.digits, k=8)))

print(''.join(random.choices(string.digits, k=4)))