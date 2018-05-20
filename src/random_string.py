import string
import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(''.join(random.choices(string.ascii_letters, k=8)))
#  ['R', 'n', 'J', 'T', 'k']
# 