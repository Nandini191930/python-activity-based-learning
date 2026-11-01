monthly_units = [80, 120, 260]
bills = []
for units in monthly_units:
    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = 100 * 2 + (units - 100) * 3
    else:
        energy = 100 * 2 + 100 * 3 + (units - 200) * 5
    bill = energy + 50 + energy * 0.05
    if units <= 100:
        bill -= 20
    bills.append(bill)
print("MONTHLY ELECTRICITY BILLS")
for i in range(len(bills)):
    print("Month", i + 1, "Units:", monthly_units[i],
          "Bill: Rs.", round(bills[i], 2))
print("MONTH-TO-MONTH COMPARISON")
for i in range(1, len(bills)):
    if bills[i - 1] > 0:
        increase = (bills[i] - bills[i - 1]) / bills[i - 1] * 100
        print("Month", i + 1, "increase:", round(increase, 2), "%")
        if increase > 50:
            print("Unusual increase detected")
        else:
            print("No unusual increase")