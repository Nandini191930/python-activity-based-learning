items = ["Idli", "Dosa", "Juice"]
prices = [30, 50, 25]
stock = [20, 15, 10]
orders = [("Idli", 4), ("Dosa", 3), ("Juice", 12), ("Pizza", 2)]
sales = 0
for item, quantity in orders:
    if item in items:
        i = items.index(item)
        if quantity <= 0:
            print("Invalid quantity:", item)
        elif quantity > stock[i]:
            print("Rejected:", item, "- insufficient stock")
        else:
            amount = prices[i] * quantity
            stock[i] -= quantity
            sales += amount
            print(item, "x", quantity, "Bill: Rs.", amount)
    else:
        print("Rejected - item unavailable:", item)
print("Daily sales: Rs.", sales)
print("Remaining stock:")
for i in range(len(items)):
    print(items[i], stock[i])