from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
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

# Specify the PDF file name
pdf_file = "order_receipt.pdf"

# Create a PDF
c = canvas.Canvas(pdf_file, pagesize=letter)
y_position = 750  # Starting Y position

# Header
c.drawString(100, y_position, "Order Receipt")
y_position -= 20  # Adjust position for the next line

for user_input in user_inputs:
    try:
        order = ProductOrder(**user_input)
        c.drawString(100, y_position, f"Product Name: {order.product_name}")
        y_position -= 20
        c.drawString(100, y_position, f"Quantity: {order.quantity}")
        y_position -= 20
        c.drawString(100, y_position, f"Unit Price: ${order.unit_price}")
        y_position -= 20
        c.drawString(100, y_position, f"Total Cost: ${order.total_cost():.2f}")
        y_position -= 40  # Add extra space before the next product
    except ValidationError as e:
        print(f"Error in order data for {user_input['product_name']}: {e}")
        y_position -= 20  # Adjust position even in case of error

c.save()

print(f"Order receipt saved to {pdf_file}.")
