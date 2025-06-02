import random
from Cryptodome.Util.RFC1751 import wordlist

def nist_pwd(file_path='eff_large_wordlist.txt'):
    wordlists={}
    with open(file_path,'r') as f:
        for line in f:
            parts=line.strip().split()
            if len(parts) == 2:

                key, word=parts
                wordlists[key]=word
    return wordlists
def roll_dice():
    return ''.join(str(random.randint(1,6)) for i in range(5))

def generate_passphrase(wordlists,num_words=6, separator='-'):
    return separator.join(wordlists[roll_dice()] for _ in range(num_words))
if __name__=='__main__':
    try:
        wordlist=nist_pwd()
        passphrase=generate_passphrase(wordlist,num_words=5)
        print(f"Generated passphrase: {passphrase}")
    except FileNotFoundError:
        print("Error wordlist")


