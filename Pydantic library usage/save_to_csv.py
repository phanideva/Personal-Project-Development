import csv
from order_model import ProductOrder

# Simulated user input for multiple products
user_inputs = [
    {
        "product_name": "Coffee Mug",
        "quantity": 2,
        "unit_price": 15.99
    },
    {
        "product_name": "T-Shirt",
        "quantity": 1,
        "unit_price": 25.50
    },
    {
        "product_name": "Notebook",
        "quantity": 4,
        "unit_price": 6.99
    }
]

# Specify the CSV file name
csv_file = "order_summary.csv"

# Field names in the CSV
fields = ['Product Name', 'Quantity', 'Unit Price', 'Total Cost']

# Write to CSV
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    
    for user_input in user_inputs:
        try:
            order = ProductOrder(**user_input)
            writer.writerow({
                'Product Name': order.product_name,
                'Quantity': order.quantity,
                'Unit Price': order.unit_price,
                'Total Cost': order.total_cost()
            })
        except ValidationError as e:
            print(f"Error in order data for {user_input['product_name']}: {e}")

print(f"Order summary saved to {csv_file}.")
