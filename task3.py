n = int(input("Number of different items: "))
items = []
subtotal = 0
rates = {"groceries": 0.05, "electronics": 0.18, "clothing": 0.12}
for i in range(n):
    print("\nItem", i + 1)
    name = input("Product name: ")
    category = input("Category (groceries/electronics/clothing): ").lower()
    price = float(input("Unit price: "))
    quantity = int(input("Quantity: "))
    if category not in rates or price < 0 or quantity <= 0:
        print("Invalid item; please restart with valid details.")
        break
    line_total = price * quantity
    subtotal += line_total
    items.append((name, category, line_total))
else:
    discount = subtotal * 0.10 if subtotal >= 2000 else 0
    discounted_total = subtotal - discount
    tax = 0
    print("\nITEMIZED BILL")
    for item in items:
        share = item[2] / subtotal if subtotal > 0 else 0
        discounted_line = share * discounted_total
        item_tax = discounted_line * rates[item[1]]
        tax += item_tax
        print(item[0], ":", round(item[2], 2),
              "Tax:", round(item_tax, 2))
    print("Subtotal: $", round(subtotal, 2))
    print("Discount: $", round(discount, 2))
    print("Tax: $", round(tax, 2))
    print("Final total: $", round(discounted_total + tax, 2))