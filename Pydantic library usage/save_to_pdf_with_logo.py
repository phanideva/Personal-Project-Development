from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Spacer
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

# Specify the PDF file name and the logo image path
pdf_file = "order_receipt_with_table_and_logo.pdf"
logo_image_path = "D:\Python Practice files\PDCo_logo.png"  # Update this path to your logo image

doc = SimpleDocTemplate(pdf_file, pagesize=letter)
story = []

# Add logo
logo = Image(logo_image_path, width=100, height=50)  # Adjust width and height as needed
story.append(logo)
story.append(Spacer(1, 12))  # Add some space between the logo and the table

# Create a table with the data
table = Table(data)

# Add style to the table
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
])
table.setStyle(style)

# Add table to the story
story.append(table)

# Build the PDF
doc.build(story)

print(f"Order receipt with table and logo saved to {pdf_file}.")
