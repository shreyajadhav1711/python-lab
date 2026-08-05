print("====== Grocery Calculator ======")

num_items = int(input("\nHow many items do you want to enter? "))

grand_total = 0

print("\n----- Bill -----")

for i in range(1, num_items + 1):
    item = input(f"\nEnter item {i}: ")
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))

    total = price * qty
    grand_total += total

    print(item, "=", total)

# Apply Discount
if grand_total > 5000:
    discount = grand_total * 0.20
    discount_percent = 20
elif grand_total > 2000:
    discount = grand_total * 0.10
    discount_percent = 10
elif grand_total >= 1000:
    discount = grand_total * 0.05
    discount_percent = 5
else:
    discount = 0
    discount_percent = 0

final_bill = grand_total - discount

print("\n------------------------")
print("Total Bill =", grand_total)
print("Discount =", discount_percent, "%")
print("Discount Amount =", discount)
print("Final Bill =", final_bill)