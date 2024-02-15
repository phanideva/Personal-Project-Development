import csv
from order_model import ProductOrder

# Assuming 'order' is an instance of ProductOrder with validated data
order_data = {
    "product_name": "Coffee Mug",
    "quantity": 2,
    "unit_price": 15.99
}
order = ProductOrder(**order_data)

# Specify the CSV file name
csv_file = "order_summary.csv"

# Field names in the CSV
fields = ['Product Name', 'Quantity', 'Unit Price', 'Total Cost']

# Write to CSV
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    writer.writeheader()
    writer.writerow({
        'Product Name': order.product_name,
        'Quantity': order.quantity,
        'Unit Price': order.unit_price,
        'Total Cost': order.total_cost()
    })

print(f"Order summary saved to {csv_file}.")
