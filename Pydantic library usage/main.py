from order_model import ProductOrder
from pydantic import ValidationError

# Simulated user input (replace this with actual user input in a real scenario)
user_input = {
    "product_name": "Coffee Mug",
    "quantity": 2,
    "unit_price": 15.99
}

try:
    # Validate user input and create a ProductOrder instance
    order = ProductOrder(**user_input)
    print(f"Order Validated: {order}")
    print(f"Total Cost: ${order.total_cost():.2f}")
except ValidationError as e:
    print(f"Error in order data: {e}")

