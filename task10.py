menu = ["idli", "dosa", "juice"]
prices = [30, 50, 25]
stock = [20, 20, 20]
total_sales = 0
orders = int(input("Number of orders: "))
for i in range(orders):
    item = input("Item (idli/dosa/juice): ").lower()
    quantity = int(input("Quantity: "))
    if item in menu and quantity > 0:
        index = menu.index(item)
        if quantity <= stock[index]:
            bill = prices[index] * quantity
            stock[index] -= quantity
            total_sales += bill
            print("Order accepted. Bill: n", bill)
        else:
            print("Order rejected: insufficient stock.")
    else:
        print("Order rejected: invalid item or quantity.")
print("\\nDaily sales: n", total_sales)
print("Remaining stock:")
for i in range(len(menu)):
    print(menu[i], ":", stock[i])