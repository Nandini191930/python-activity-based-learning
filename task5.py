attended = int(input("Classes attended: "))
total = int(input("Total classes conducted: "))
threshold = float(input("Required attendance percentage: "))
if attended < 0 or total < 0 or attended > total:
    print("Invalid attendance counts.")
elif threshold <= 0 or threshold > 100:
    print("Threshold must be greater than 0 and at most 100.")
else:
    current = attended / total * 100 if total > 0 else 0
    extra = 0
    while (attended + extra) / (total + extra) * 100 < threshold:
        extra += 1
    print("Current attendance:", round(current, 2), "%")
    print("Consecutive classes to attend:", extra)
    print("Attendance after recovery:",
          round((attended + extra) / (total + extra) * 100, 2), "%")