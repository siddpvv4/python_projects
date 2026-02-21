# Password Strength Checker

password = input("Enter your password: ")

score = 0
special_chars = "!@#$%^&*()_+-="

# Check length
if len(password) >= 8:
    score += 1

# Check for number
for ch in password:
    if ch.isdigit():
        score += 1
        break

# Check for uppercase letter
for ch in password:
    if ch.isupper():
        score += 1
        break

# Check for special character
for ch in password:
    if ch in special_chars:
        score += 1
        break


# Print result
if score <= 1:
    print("Weak Password 😐")
elif score == 2 or score == 3:
    print("Medium Password 🙂")
else:
    print("Strong Password 💪")