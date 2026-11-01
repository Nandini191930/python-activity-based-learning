marks = [38, 45, 39, 72]
pass_mark = 40
valid = True
for mark in marks:
    if mark < 0 or mark > 100:
        valid = False
if not valid:
    print("Invalid marks")
else:
    deficits = []
    for mark in marks:
        if mark < pass_mark:
            deficits.append(pass_mark - mark)
    if sum(deficits) <= 5 and max(deficits + [0]) <= 5:
        for i in range(len(marks)):
            if marks[i] < pass_mark:
                marks[i] = pass_mark
        print("Grace marks applied:", sum(deficits))
    else:
        print("Grace policy cannot cover shortage")
    print("Final marks:", marks)
    passed = True
    for mark in marks:
        if mark < pass_mark:
            passed = False
    if passed:
        print("Result: PASS")
    else:
        print("Result: FAIL")