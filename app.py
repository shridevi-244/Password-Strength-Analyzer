password = input("Enter Password: ")

score = 0

# Length Check
if len(password) >= 8:
    score += 1
else:
    print("Password should have at least 8 characters")

# Uppercase Check
if any(char.isupper() for char in password):
    score += 1
else:
    print("Add an uppercase letter")

# Lowercase Check
if any(char.islower() for char in password):
    score += 1
else:
    print("Add a lowercase letter")

# Number Check
if any(char.isdigit() for char in password):
    score += 1
else:
    print("Add a number")

# Special Character Check
special = "!@#$%^&*()"

if any(char in special for char in password):
    score += 1
else:
    print("Add a special character")

print("\nPassword Analysis:")

if score <= 2:
    print("Weak Password")
elif score <= 4:
    print("Medium Password")
else:
    print("Strong Password")