from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
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

# Prepare data for the table
data = [['Product Name', 'Quantity', 'Unit Price', 'Total Cost']]
for user_input in user_inputs:
    order = ProductOrder(**user_input)
    data.append([order.product_name, order.quantity, f"${order.unit_price}", f"${order.total_cost():.2f}"])

# Specify the PDF file name
pdf_file = "order_receipt_with_table.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter)

# Create a table with the data
table = Table(data)

# Add style to the table
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),  # Header row background color
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header row text color
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Align all cells to the center
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header row font
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Header row bottom padding
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Data rows background color
    ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Grid color and size
])

table.setStyle(style)

# Build the PDF
doc.build([table])

print(f"Order receipt with table saved to {pdf_file}.")
