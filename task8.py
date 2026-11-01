password = "PassWord11"
errors = []
if len(password) < 8:
    errors.append("Use at least 8 characters")
upper = lower = digit = special = False
allowed_special = "!@#$%^&*"
for ch in password:
    if ch >= "A" and ch <= "Z":
        upper = True
    elif ch >= "a" and ch <= "z":
        lower = True
    elif ch >= "0" and ch <= "9":
        digit = True
    elif ch in allowed_special:
        special = True
if not upper:
    errors.append("Add an uppercase letter")
if not lower:
    errors.append("Add a lowercase letter")
if not digit:
    errors.append("Add a digit")
if not special:
    errors.append("Add a special character")
for i in range(len(password) - 1):
    if password[i] == password[i + 1]:
        errors.append("No consecutive repeated characters")
        break
if "password" in password.lower():
    errors.append("The word password is prohibited")
if len(errors) == 0:
    print("Password is valid")
else:
    print("Password is invalid")
    for error in errors:
        print("-", error)