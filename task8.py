password = input("Enter a sample password: ")
errors = []
if len(password) < 8:
    errors.append("Must contain at least 8 characters.")
upper = False
lower = False
digit = False
special = False
for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    elif ch in "!@#$%":
        special = True
if not upper:
    errors.append("Add at least one uppercase letter.")
if not lower:
    errors.append("Add at least one lowercase letter.")
if not digit:
    errors.append("Add at least one digit.")
if not special:
    errors.append("Add at least one special character from !@#$%.")
if len(errors) == 0:
    print("Password satisfies the sample policy.")
else:
    print("Password does not satisfy the policy:")
    for error in errors:
        print("-", error)