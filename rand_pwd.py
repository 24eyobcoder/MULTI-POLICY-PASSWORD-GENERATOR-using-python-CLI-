import random
import string

def random_strong():
    while True:
        letter=string.ascii_letters
        digit=string.digits
        symbol=string.punctuation
        all_chars=letter+digit+symbol
        password = ''.join(random.choice(all_chars) for _ in range(15))
        if len(password)>14:
            break
    print(f"Random-character password: {password}")


