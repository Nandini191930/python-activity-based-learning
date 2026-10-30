n = int(input("Number of subjects: "))
subjects = []
old_scores = []
new_scores = []
for i in range(n):
    name = input("Subject name: ")
    old = float(input("Earlier exam score (%): "))
    new = float(input("Later exam score (%): "))
    if old < 0 or old > 100 or new < 0 or new > 100:
        print("Invalid score. Use values from 0 to 100.")
        continue
    subjects.append(name)
    old_scores.append(old)
    new_scores.append(new)
print("\\nPERFORMANCE REPORT")
for i in range(len(subjects)):
    change = new_scores[i] - old_scores[i]
    if change > 0:
        trend = "Improved"
    elif change < 0:
        trend = "Declined"
    else:
        trend = "Unchanged"
    weak = "YES" if new_scores[i] < 40 else "NO"
    print(subjects[i], "| Change:", round(change, 2),
          "| Trend:", trend, "| Weak subject:", weak)