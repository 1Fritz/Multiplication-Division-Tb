
# The Heading
print("  WELCOME TO CATUC POS")
print("_____________________________________")

# Create an empty dictionary
items = {}

# Enter items
while True:

    name = input("\nWhat item would you like to buy? ")

    quantity = int(input("Enter quantity: "))

    price = float(input("Enter unit price: "))

    # Store item details
    items[name] = {
        "quantity": quantity,
        "price": price
    }

    choice = input("\nWould you like to buy another item? (yes/no): ")

    if choice.lower() == "no":
        break

# Calculate total expenditure
total_bill = 0
total_items = 0

for name in items:
    total = items[name]["quantity"] * items[name]["price"]

    total_bill = total_bill + total
    total_items = total_items + items[name]["quantity"]

# Apply discounts

if total_bill > 10000:
    discount = 30

elif total_items > 4 and total_bill > 4000:
    discount = 15

elif total_bill > 5000:
    discount = 10
else :
    discount = 0    

# Calculate final bill
discount_amount = total_bill * discount / 100
final_bill = total_bill - discount_amount

# Display receipt
print("\n==============================================")
print("           CATUC POS")
print("           SALES RECEIPT")
print("==============================================")

print("S/N\tITEM\t\tQTY\tPRICE\tTOTAL")
print("----------------------------------------------")

sn = 1

for name in items:

    quantity = items[name]["quantity"]
    price = items[name]["price"]
    total = quantity * price

    print(f"{sn}\t{name}\t\t{quantity}\t{price}\t{total}")

    sn = sn + 1

print("----------------------------------------------")

print(f"Total Expenditure: {total_bill} FCFA")
print(f"Discount: {discount}%")
print(f"Discount Amount: {discount_amount}FCFA")

print("----------------------------------------------")
print(f"FINAL BILL: {final_bill}FCFA")

print("==============================================")
print("       THANK YOU FOR SHOPPING WITH US!")
print("==============================================")
