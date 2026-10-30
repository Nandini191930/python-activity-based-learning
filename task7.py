n = int(input("Number of classes: "))
classes = []
for i in range(n):
    print("Class", i + 1)
    course = input("Course name: ")
    day = input("Day: ").lower()
    start = int(input("Start time in minutes after midnight: "))
    end = int(input("End time in minutes after midnight: "))
    if start < 0 or end > 1440 or start >= end:
        print("Invalid time interval; class skipped.")
    else:
        classes.append((course, day, start, end))
found = False
for i in range(len(classes)):
    for j in range(i + 1, len(classes)):
        a = classes[i]
        b = classes[j]
        if a[1] == b[1] and a[2] < b[3] and b[2] < a[3]:
            print("Conflict:", a[0], "and", b[0], "on", a[1])
            found = True
if not found:
    print("No timetable conflicts found.")