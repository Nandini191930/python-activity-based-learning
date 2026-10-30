months = int(input("Enter number of months: "))

month_names = []
units_list = []
bills = []

for i in range(months):
    print(f"\nMonth {i + 1}")
    month = input("Enter month name: ")
    units = float(input("Enter units consumed: "))

   
    if units <= 100:
        energy = units * 1.50
    elif units <= 200:
        energy = 100 * 1.50 + (units - 100) * 2.50
    elif units <= 300:
        energy = (100 * 1.50 + 100 * 2.50
                  + (units - 200) * 4.00)
    else:
        energy = (100 * 1.50 + 100 * 2.50
                  + 100 * 4.00 + (units - 300) * 6.00)

    fixed_charge = 100
    surcharge = energy  * 0.05

    if units < 100:
        rebate = energy * 0.02
    else:
        rebate = 0

    bill = energy + fixed_charge + surcharge - rebate

    month_names.append(month)
    units_list.append(units)
    bills.append(bill)

    print(f"Energy Charges: Rs. {energy:.2f}")
    print(f"Fixed Charges: Rs. {fixed_charge:.2f}")
    print(f"Surcharge: Rs. {surcharge:.2f}")