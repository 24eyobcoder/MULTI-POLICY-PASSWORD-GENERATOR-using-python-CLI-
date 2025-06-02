# multi-policy-password-generator
# 🔐 Multi-Policy Password Generator

A terminal-based Python password tool that supports:

- ✅ Random password generation
- ✏️ Custom user-defined passwords
- 🛡 ISO 27001-compliant secure passwords
- 🧠 NIST-style passphrases (using EFF wordlist)

## 📦 Features

- Validates against weak/common passwords
- Fully CLI-based with menu interface
- Uses separate modules for clarity
- Easy to extend with other password policies

## 📁 Password Policies

| Policy      | Description                                                                 |
|-------------|-----------------------------------------------------------------------------|
| Random      | Secure 15-character password with letters, digits, and symbols              |
| Custom      | User chooses components of the password                                     |
| ISO 27001   | Enforces security rules: length, character mix, weak word filtering         |
| NIST        | Generates passphrase from the EFF's diceware-style wordlist                 |

## 🛠 Usage

### Clone the repo:

```bash
git clone https://github.com/yourusername/multi-policy-password-generator.git
cd multi-policy-password-generator
python main.py
