applicants = [
    ("Anu", [85, 90, 80], 92, 250000),
    ("Balu", [78, 82, 80], 88, 280000),
    ("Chitra", [95, 55, 90], 96, 200000),
    ("Deepak", [88, 86, 84], 84, 220000)
]
eligible = []
for name, marks, attendance, income in applicants:
    percentage = sum(marks) / 3
    if percentage >= 75 and min(marks) >= 60 and attendance >= 85 and income <= 300000:
        eligible.append((name, percentage, attendance))
    else:
        print(name, "is not eligible")
eligible.sort(key=lambda x: (x[1], x[2]), reverse=True)
print("SCHOLARSHIP MERIT LIST")
for rank, record in enumerate(eligible, 1):
    print(rank, record[0], round(record[1], 2), "Attendance:", record[2])