products = [
    ("Notebook", 5, 60, "other"),
    ("Shirt", 2, 500, "clothing"),
    ("Headphones", 1, 1800, "electronics")
]
subtotal = 0
for name, qty, price, category in products:
    subtotal += qty * price
discount = 0
if subtotal >= 2000:
    discount = min(subtotal * 0.10, 500)
rate = discount / subtotal if subtotal > 0 else 0
total_tax = 0
print("ITEMIZED BILL")
for name, qty, price, category in products:
    amount = qty * price * (1 - rate)
    if category == "electronics":
        tax_rate = 0.18
    elif category == "clothing":
        tax_rate = 0.05
    else:
        tax_rate = 0.12
    tax = amount * tax_rate
    total_tax += tax
    print(name, "Qty:", qty, "Tax:", round(tax, 2))
print("Subtotal:", subtotal)
print("Discount:", round(discount, 2))
print("Tax:", round(total_tax, 2))
print("Final bill:", round(subtotal - discount + total_tax, 2))