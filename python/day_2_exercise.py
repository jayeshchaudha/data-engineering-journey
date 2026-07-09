'''
1. Create a list of 5 orders as a list of dictionaries
   Each order has: order_id, customer_name, city, amount, status

2. Write a function called clean_name(name) 
   that strips whitespace and converts to title case

3. Apply clean_name to every customer_name in your list

4. Print only orders where status == "delivered"

5. Calculate and print total revenue from delivered orders

6. Write the delivered orders to a file called 
   delivered_orders.txt using file handling

7. Wrap the file writing in a try/except block
'''


orders = [
    {"order_id": 1, "customer_name": "  rahul sharma", "city": "Mumbai", "amount": 4500, "status": "delivered"},
    {"order_id": 2, "customer_name": "priya  ", "city": "Delhi", "amount": 1200, "status": "pending"},
    {"order_id": 3, "customer_name": "  AMIT verma", "city": "Pune", "amount": 8900, "status": "delivered"},
    {"order_id": 4, "customer_name": "sneha", "city": "Mumbai", "amount": 2300, "status": "cancelled"},
    {"order_id": 5, "customer_name": "  vikas yadav  ", "city": "Pune", "amount": 5600, "status": "delivered"},
]
'''
2. Write a function called clean_name(name) 
   that strips whitespace and converts to title case
'''
def clean_name(name):
    return name.strip().title()

'''
3. Apply clean_name to every customer_name in your list
'''
cleaned_orders = []
for order in orders:
    new_order = order.copy()
    new_order["customer_name"] = clean_name(new_order["customer_name"])
    cleaned_orders.append(new_order)

#4. Print only orders where status == "delivered"
for order in orders:
    if order["status"] == "delivered":
        print(order)
# 5. Calculate and print total revenue from delivered orders
total_revenue = 0
for order in orders:
    if order["status"] == "delivered":
        total_revenue += order["amount"]
print(f"\nTotal Revenue from Delivered Orders: ₹{total_revenue}")

# 6. Write the delivered orders to a file called  delivered_orders.txt using file handling
try:
    with open("delivered_orders.txt", "w") as file:
        file.write("Delivered Orders Report\n")
        file.write("=======================\n")
        
        for order in orders:
            if order["status"] == "delivered":
                # Writing a clean string representation of each delivered order
                file.write(f"ID: {order['order_id']} | Name: {order['customer_name']} | Amount: ₹{order['amount']}\n")
                
    print("\n[Success] Delivered orders successfully written to 'delivered_orders.txt'")

except IOError as e:
    print(f"\n[Error] Could not write to file. Details: {e}")