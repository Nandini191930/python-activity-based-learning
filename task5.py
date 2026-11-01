attended = 60
conducted = 90
target = 75
if conducted <= 0 or attended < 0 or attended > conducted:
    print("Invalid attendance")
else:
    print("Current attendance:", round(attended / conducted * 100, 2), "%")
    count = 0
    while (attended + count) / (conducted + count) * 100 < target:
        count += 1
    print("Future classes if all are attended:", count)
    future = 1
    while True:
        future_attended = (future // 5) * 4 + min(future % 5, 4)
        percentage = (attended + future_attended) / (conducted + future) * 100
        if percentage >= target:
            break
        future += 1
    print("Future classes in 4-out-of-5 scenario:", future)