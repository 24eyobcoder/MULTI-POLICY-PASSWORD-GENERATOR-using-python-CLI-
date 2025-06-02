import random
#the input are given by the user
def custom_password():
    while True:
        char = input("enter a character: ")
        numb = int(input("enter a number:"))
        symbl = input("enter a symbol:")
        val=f'{char}{numb}{symbl}'
        shun=list(val)
        random.shuffle(shun)
        shuffled_text=''.join(shun)
        if len(shuffled_text) in range(8,64):
            break

    print(f'custom password is: {shuffled_text}')

