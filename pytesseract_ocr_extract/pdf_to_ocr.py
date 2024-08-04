import fitz  # PyMuPDF
import pytesseract
import pandas as pd
from PIL import Image, ImageEnhance, ImageFilter
import os

def pdf_to_images(pdf_path, output_folder, zoom_x=2.0, zoom_y=2.0):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    doc = fitz.open(pdf_path)
    image_paths = []
    for i in range(len(doc)):
        page = doc.load_page(i)
        matrix = fitz.Matrix(zoom_x, zoom_y)  # Increase resolution
        pix = page.get_pixmap(matrix=matrix)
        image_path = os.path.join(output_folder, f'page_{i+1}.png')
        pix.save(image_path)
        image_paths.append(image_path)
    return image_paths

def preprocess_image(image_path):
    image = Image.open(image_path)
    # Enhance the image for better OCR accuracy
    image = image.convert('L')  # Convert to grayscale
    image = image.filter(ImageFilter.SHARPEN)  # Apply sharpen filter
    image = ImageEnhance.Contrast(image).enhance(2)  # Increase contrast
    return image

def image_to_text(image):
    # OCR configuration to get all text lines
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(image, config=custom_config)
    return text

def extract_text_from_pdf(pdf_path, output_csv):
    output_folder = 'D:\Python Practice files\images'
    image_paths = pdf_to_images(pdf_path, output_folder)
    
    data = []
    for image_path in image_paths:
        image = preprocess_image(image_path)
        text = image_to_text(image)
        # Combine lines into a single string separated by spaces
        combined_text = ' '.join(text.splitlines())
        document_name = os.path.basename(image_path)
        data.append({'document_name': document_name, 'text': combined_text})
    
    df = pd.DataFrame(data)
    df.to_csv(output_csv, index=False)


if __name__ == "__main__":
    pdf_path = 'D:\Python Practice files\docs\Transcripts of bachelors degree.pdf'  # Replace with the path to your PDF file
    output_csv = 'D:\Python Practice files\output.csv'  # The name of the output CSV file
    
    extract_text_from_pdf(pdf_path, output_csv)
    print(f"Text extracted and saved to {output_csv}")
