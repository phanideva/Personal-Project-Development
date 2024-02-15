from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from order_model import ProductOrder

# Assuming 'order' is an instance of ProductOrder with validated data
order_data = {
    "product_name": "Coffee Mug",
    "quantity": 2,
    "unit_price": 15.99
}
order = ProductOrder(**order_data)

# Specify the PDF file name
pdf_file = "order_receipt.pdf"

# Create a PDF
c = canvas.Canvas(pdf_file, pagesize=letter)
c.drawString(100, 750, f"Order Receipt")
c.drawString(100, 730, f"Product Name: {order.product_name}")
c.drawString(100, 710, f"Quantity: {order.quantity}")
c.drawString(100, 690, f"Unit Price: ${order.unit_price}")
c.drawString(100, 670, f"Total Cost: ${order.total_cost():.2f}")

c.save()

print(f"Order receipt saved to {pdf_file}.")
