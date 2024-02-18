from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Spacer
from reportlab.lib.units import inch
from order_model import ProductOrder
# Assuming ProductOrder is defined correctly in your order_model

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

# Setup document and margins
page_width, page_height = letter
left_margin, right_margin = inch * 0.75, inch * 0.75
content_width = page_width - (left_margin + right_margin)

doc = SimpleDocTemplate(pdf_file, pagesize=letter, leftMargin=left_margin, rightMargin=right_margin, topMargin=inch, bottomMargin=inch)
story = []

# Adjusting logo size
logo_width = content_width
logo_height = 150
logo = Image(logo_image_path, width=logo_width, height=logo_height)
story.append(logo)

# Preparing data for the table as before

column_widths = [content_width / 4 for _ in range(4)]
table = Table(data, colWidths=column_widths)

# Start with a basic style configuration
style_commands = [
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]

# Define light colors for a "gradient" effect
light_colors = [colors.lightblue, colors.lightgreen, colors.lightgrey, colors.lightpink]

# Append background color settings for each row
for i in range(1, len(data)):
    style_commands.append(('BACKGROUND', (0, i), (-1, i), light_colors[i % len(light_colors)]))

# Apply the style to the table
table.setStyle(TableStyle(style_commands))

story.append(Spacer(1, 12))  # Adjust space between logo and table as needed
story.append(table)

# Build the PDF
doc.build(story)

print(f"Order receipt with table and logo saved to {pdf_file}.")
