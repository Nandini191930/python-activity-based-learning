n = int(input("Number of applicants: "))
eligible = []
for i in range(n):
    print("\\nApplicant", i + 1)
    name = input("Name: ")
    marks = float(input("Aggregate marks (%): "))
    attendance = float(input("Attendance (%): "))
    income = float(input("Annual family income (n): "))
    if marks >= 75 and attendance >= 85 and income <= 250000:
        eligible.append((name, marks, attendance))
    else:
        print(name, "is not eligible.")
eligible.sort(key=lambda item: (item[1], item[2]), reverse=True)
print("\nScholarship shortlist:")
if len(eligible) == 0:
    print("No eligible applicants.")
else:
    for rank, applicant in enumerate(eligible, start=1):
     print(rank, applicant[0], "- Marks:", applicant[1], "\nAttendance:", applicant[2])
