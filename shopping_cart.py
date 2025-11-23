orders = {"carbage": 4.00,
         "spinach": 3.00,
         "sausages": 4.00,
         "beef": 2.00,
         "pork": 3.00,
         "ice cream": 2.00,
         "potatoes": 3.00,
         "tomatoes": 2.00
}
cart =[]
total = 0

print("------ SHOPPING ORDERS -----")
for key, value in orders.items():
    print(f"{key:10}: ${value}")
print("-------------------------")

while True:
    order = input("Enter your order(q to quit): ").lower()
    if order == "q":
        break
    elif orders.get(order) is not None:
        cart.append(order)

print("----- YOUR ORDERS -----")
for things in cart:
    if len(cart) == 1:
        total += orders.get(things) 
        print(f"Your order is: {things}")
    else:
        total += orders.get(things)
        print(f"Your orders are: {things}")

print(f"Your total is: ${total}")
