import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib
from pdfminer.high_level import extract_text
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
from PyPDF2 import PdfReader, PdfWriter

# Directories
os.makedirs('output_pdfs', exist_ok=True)
os.makedirs('output_csv', exist_ok=True)

# Step 1: Train the Model
def train_model():
    # Sample training data
    data = {
        'text': [
            'W2 Statement for the year', 'Paystub for employee', 'Renewal document for insurance', 'Tax Statement for 2023',
            'Employee W2 Form', 'Employee Paystub', 'Insurance Renewal', '1040 Tax Form'
        ],
        'label': ['W2', 'Paystubs', 'Renewal_Doc', 'Tax_Statement', 'W2', 'Paystubs', 'Renewal_Doc', 'Tax_Statement']
    }

    df = pd.DataFrame(data)

    # Train the model
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(df['text'], df['label'])

    # Save the model
    joblib.dump(model, 'pdf_classifier_model.pkl')

# Step 2: Load the Model
def load_model():
    return joblib.load('pdf_classifier_model.pkl')

# Step 3: Extract Text from a Page using pdfminer.six
def extract_text_from_page(pdf_path, page_num):
    """Extract text from a specific page of a PDF."""
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        page = reader.pages[page_num]
        text = page.extract_text()
    return text

# Step 4: Classify the Page
def classify_page(text, model):
    """Classify the page based on its text content."""
    prediction = model.predict([text])[0]
    confidence = max(model.predict_proba([text])[0])
    return prediction, confidence

# Step 5: Save Pages to PDF
def save_pages_to_pdf(pages, output_path):
    """Save a list of texts to a single PDF using reportlab."""
    c = canvas.Canvas(output_path, pagesize=letter)
    for text in pages:
        for i, line in enumerate(text.split('\n')):
            c.drawString(100, 750 - 15 * i, line)
        c.showPage()
    c.save()

# Step 6: Split PDF by Category and Create CSV
def split_pdf_by_category(input_pdf, output_prefix, model):
    categorized_pages = {'W2': [], 'Paystubs': [], 'Renewal_Doc': [], 'Tax_Statement': [], 'Other': []}
    csv_data = []
    
    reader = PdfReader(open(input_pdf, 'rb'))
    for page_num in range(len(reader.pages)):
        text = extract_text_from_page(input_pdf, page_num)
        if text:
            category, confidence = classify_page(text, model)
            categorized_pages[category].append(text)
            csv_data.append({
                'PDF Name': f'{output_prefix}_{category}.pdf',
                'Extracted Text': text,
                'Text as List': text.split('\n'),
                'Page Number': page_num,
                'Predicted Filename': category,
                'Confidence': confidence
            })
    
    for category, pages in categorized_pages.items():
        if pages:
            output_path = f'D:\Python Practice files\{output_prefix}_{category}.pdf'
            save_pages_to_pdf(pages, output_path)
    
    csv_df = pd.DataFrame(csv_data)
    csv_df.to_csv(f'D:\Python Practice files\{output_prefix}_extracted_data.csv', index=False)

# Main Execution
if __name__ == '__main__':
    # Train the model (only needs to be done once)
    train_model()

    # Load the trained model
    model = load_model()

    # Example usage
    input_pdf = 'loan_5648_Origination_File.pdf'
    output_prefix = 'loan_5648'
    split_pdf_by_category(input_pdf, output_prefix, model)
