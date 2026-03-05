import re

def check_password_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if re.search("[a-z]", password):
        score += 1

    if re.search("[A-Z]", password):
        score += 1

    if re.search("[0-9]", password):
        score += 1

    if re.search("[@#$%^&*!]", password):
        score += 1

    if score <= 2:
        return "Weak Password"
    elif score == 3 or score == 4:
        return "Medium Strength Password"
    else:
        return "Strong Password"


password = input("Enter a password: ")

strength = check_password_strength(password)

print("\nPassword Strength:", strength)