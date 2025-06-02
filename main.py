from NIST_pwd import generate_passphrase, nist_pwd
from rand_pwd import random_strong
from custom import custom_password
from ISO_27001 import generate_strong_password
from ISO_27001 import load_weak_passwords
# to chosse between menus from the given list

def main():
    while True:
        print("\n=== Menu ===")
        print("1.run function custom")
        print("2.random strong password")
        print("3.run function iso_27001")
        print("4.run function nist")
        print("5.Exit")
        choice=input("enter your choice in [1-5]")

        if choice == '1':
            custom_password()
        elif choice == '2':
            random_strong()
        elif choice =='3':
            weak_passwords = load_weak_passwords()
            secure_password = generate_strong_password(weak_passwords, length=16)
            print("✅ Generated ISO 27001-compliant password:", secure_password)
        elif choice=='4':
            try:
                wordlist = nist_pwd()  # Load wordlist file
                passphrase = generate_passphrase(wordlist, num_words=5)
                print("Generated NIST passphrase:", passphrase)
            except FileNotFoundError:
                print("Error: 'eff_large_wordlist.txt' file not found.")
        elif choice == '5':
            print("Exiting goodbye!")
            break
        else:
            print("invalid choice,please select 1,2,3 or 4.")
        input("\n press enter to return menu...")

#calling the main function
main()





