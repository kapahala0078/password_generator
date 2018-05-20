import string
import random

# 実行する際のモードを入力
# alphabet or digits or both
mode = "both"
# 大文字小文字の選択
# alphabet or digits or both
ul = "both"

for i in range(100):
    if mode is "alphabet":
        if ul is "upper":
            print(''.join(random.choices(string.ascii_letters, k=8)).upper())
        elif ul is "lower":
            print(''.join(random.choices(string.ascii_letters, k=8)).lower())
        elif ul is "both":
            print(''.join(random.choices(string.ascii_letters, k=8)))
    elif mode is "digits":
        print(''.join(random.choices(string.digits, k=4)))
    elif mode is "both":
        if ul is "upper":
            print(''.join(random.choices(string.ascii_letters + string.digits, k=8)).upper())
        elif ul is "lower":
            print(''.join(random.choices(string.ascii_letters + string.digits, k=8)).lower())
        elif ul is "both":
            print(''.join(random.choices(string.ascii_letters + string.digits, k=8)))      
    else:
        print("error")

def function_name(x, y):
    # ここに処理を書く
    return x*y
