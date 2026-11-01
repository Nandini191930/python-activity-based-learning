timetable = [
    ("Python", "Monday", 9, 10, "R101"),
    ("Maths", "Monday", 9, 11, "R102"),
    ("English", "Monday", 11, 12, "R103"),
    ("Physics", "Tuesday", 10, 11, "R101")
]
conflicts = 0
for i in range(len(timetable)):
    for j in range(i + 1, len(timetable)):
        course1, day1, start1, end1, room1 = timetable[i]
        course2, day2, start2, end2, room2 = timetable[j]
        if day1 == day2 and start1 < end2 and start2 < end1:
            print("Conflict:", course1, "and", course2, "on", day1)
            conflicts += 1
if conflicts == 0:
    print("Timetable is valid")
else:
    print("Total conflicts:", conflicts)
    print("Timetable is not valid")