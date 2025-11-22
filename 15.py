tax_rate = 0.05
subtotal = 0.0
dicta={"Americano":65,"Cappacino":80,"Mojjito":90,"Chocolate MilkShake":80,"Matcha":60}
print("Welcome To Our Cafe")
a=input("Enter Your Name:")
print("Menu:")
print("Americano-65 Cappacino- 80|Mojjito-₹90|Chocolate MilkShake-₹80|Matcha-60")
print("Type item and quantity.")
print("Press Enter to finish.")
for item,price in dicta.items():
    print({str(item)},":",{float(price)})

while True:
    b=input("Order>>")
    if not b:
        break
    else:
        item,quantity=b.split()
        qua=int(quantity)
        if item in dicta and qua> 0:
            price=dicta[item]
            cost=price*qua
            subtotal+=cost
        else:
            print("Item not found or quantity is invalid. Try again.")
if subtotal == 0.0:
    print("\n--- No items ordered. Thank you! ---")
tax_amount = subtotal * tax_rate
grand_total = subtotal + tax_amount
print("\n" + "=" * 20)
print("**FINAL BILL**")
print("-" * 20)
print("Subtotal:"   + f"₹{float(subtotal)}")
print(f"Tax({float(tax_rate * 100)}%):" + f"₹{float(tax_amount)}")
print("-" * 20)
print("GRAND TOTAL:" + f"   ₹{float(grand_total)}")
print("=" * 20)            

