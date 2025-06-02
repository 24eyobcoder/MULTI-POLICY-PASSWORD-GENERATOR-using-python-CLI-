import random
import string

# Step 1: Generate a random password
def generate_password(length=12):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(all_chars) for _ in range(length))

# Step 2: Load weak password list into a set
def load_weak_passwords(path='weak_password.txt'):
    try:
        with open(path, 'r') as file:
            return {line.strip().lower() for line in file}
    except FileNotFoundError:
        print("❌ Weak password list not found.")
        return set()

# Step 3: Check ISO 27001 complexity
def is_iso27001_compliant(password):
    if len(password) < 12 or len(password) > 64:
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c in string.punctuation for c in password):
        return False
    return True

# Step 4: Combine all in strong password generator
def generate_strong_password(weak_passwords, length=12):
    while True:
        pwd = generate_password(length)
        if pwd.lower() not in weak_passwords and is_iso27001_compliant(pwd):
            return pwd

