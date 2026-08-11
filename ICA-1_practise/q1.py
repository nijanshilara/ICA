item1 = input("Enter item1 name: ")
quantity1 = int(input("Enter item1 quantity: "))
price1 = float(input("Enter price per item: "))

item2 = input("Enter item2 name: ")
quantity2 = int(input("Enter item2 quantity: "))
price2 = float(input("Enter price per item: "))

item3 = input("Enter item3 name: ")
quantity3 = int(input("Enter item3 quantity: "))
price3 = float(input("Enter price per item: "))

total1 = quantity1 * price1
total2 = quantity2 * price2
total3 = quantity3 * price3

subtotal = total1 + total2 + total3

gst = subtotal * 0.05
grand_total = subtotal + gst

print("\t\tRESTAURANT BILL")
print("=" * 30)
print(f"Item 1: {item1} - Quantity: {quantity1} - Total: ${total1:.2f}")
print(f"Item 2: {item2} - Quantity: {quantity2} - Total: ${total2:.2f}")
print(f"Item 3: {item3} - Quantity: {quantity3} - Total: ${total3:.2f}")
print("-" * 30)
print(f"Subtotal: ${subtotal:.2f}")
print(f"GST (5%): ${gst:.2f}")
print(f"Grand Total: ${grand_total:.2f}")