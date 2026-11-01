students = ["Anu", "Balu", "Chitra"]
subjects = ["Python", "Maths", "English"]
marks = [[85, 78, 90], [70, 65, 72], [45, 40, 55]]
totals = []
for i in range(len(students)):
    total = sum(marks[i])
    totals.append(total)
    print(students[i], "Total:", total,
          "Average:", round(total / len(subjects), 2))
top = totals.index(max(totals))
print("Top performer:", students[top])
low = []
for j in range(len(subjects)):
    column_total = 0
    for i in range(len(students)):
        column_total += marks[i][j]
    average = column_total / len(students)
    print(subjects[j], "Average:", round(average, 2))
    if average < 50:
        low.append(subjects[j])
print("Low-average subjects:", low)