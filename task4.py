n = int(input("Number of subjects: "))
grace_used = 0
all_pass = True
for i in range(n):
    marks = int(input("Marks for subject " + str(i + 1) + " (0-100): "))
    if marks < 0 or marks > 100:
        print("Invalid marks. Enter marks from 0 to 100.")
        all_pass = False
        continue
    original = marks
    if 35 <= marks < 40:
        needed = 40 - marks
        if grace_used + needed <= 5:
            marks += needed
            grace_used += needed
    if marks >= 40:
        print("Subject", i + 1, ":", original, "->", marks, "- PASS")
    else:
        print("Subject", i + 1, ":", original, "->", marks, "- FAIL")
        all_pass = False
print("Grace marks used:", grace_used)
if all_pass:
    print("Overall result: PASS")
else:
    print("Overall result: FAIL")