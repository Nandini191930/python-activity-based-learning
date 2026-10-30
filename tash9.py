students = int(input("Number of students: "))
subjects_count = int(input("Number of subjects: "))
subject_names = []
for j in range(subjects_count):
    subject_names.append(input("Subject name: "))
names = []
marks_matrix = []
for i in range(students):
    name = input("Student name: ")
    row = []
    for j in range(subjects_count):
        mark = float(input("Marks in " + subject_names[j] + ": "))
        row.append(mark)
    names.append(name)
    marks_matrix.append(row)
totals = []
for i in range(students):
    total = sum(marks_matrix[i])
    totals.append(total)
    print(names[i], "total:", total)
if students > 0:
    top_index = totals.index(max(totals))
    print("Top performer:", names[top_index])
for j in range(subjects_count):
    column_total = 0
    for i in range(students):
        column_total += marks_matrix[i][j]
    average = column_total / students if students > 0 else 0
    print(subject_names[j], "average:", round(average, 2))