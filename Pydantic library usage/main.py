from order_model import ProductOrder
from pydantic import ValidationError

# Simulated user input (replace this with actual user input in a real scenario)
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

def process_order(order_data):
    try:
        # Validate user input and create a ProductOrder instance
        order = ProductOrder(**order_data)
        print(f"Order Validated: {order}")
        print(f"Product: {order.product_name}, Quantity: {order.quantity}, Unit Price: ${order.unit_price}, Total Cost: ${order.total_cost():.2f}")
    except ValidationError as e:
        print(f"Error in order data: {e}")

for user_input in user_inputs:
    process_order(user_input)
