import os
import json
from pdf2image import convert_from_path
import pytesseract
import pandas as pd

def pdf_to_images(pdf_path, output_folder=r'D:\\extract_task\\images'):
    """
    Convert each page of a PDF to images and save them in the output folder.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    images = convert_from_path(pdf_path)
    image_filenames = []
    for i, image in enumerate(images):
        image_filename = f"{output_folder}/{os.path.splitext(os.path.basename(pdf_path))[0]}_{i+1:03d}.jpg"
        image.save(image_filename, 'JPEG')
        image_filenames.append(image_filename)
    
    return image_filenames

def extract_text_from_images(image_filenames, json_output_path=r'D:\\extract_task\\extracted_data.json'):
    """
    Extract text from a list of image files and save it to a JSON file.
    """
    extracted_data = []
    for image_path in image_filenames:
        text = pytesseract.image_to_string(image_path, lang='eng')
        filename = os.path.splitext(os.path.basename(image_path))[0]
        text_list = text.split('\n')
        text_string = ' '.join([line.strip() for line in text_list if line.strip()]) 
        extracted_data.append({
            'filename': filename,
            'text': text_string,
            'text_list': text_list
        })

    with open(json_output_path, 'w', encoding='utf-8') as f:
        json.dump(extracted_data, f, ensure_ascii=False, indent=4)
    
    print(f"Extracted data saved to {json_output_path}")
    return extracted_data

def json_to_csv_or_excel(json_path, output_path=r'D:\\extract_task\\output.xlsx', file_type='excel'):
    """
    Convert extracted JSON data to a CSV or Excel file.
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    df = pd.DataFrame(data)
    
    if file_type == 'csv':
        df.to_csv(output_path, index=False)
        print(f"Data saved to {output_path}")
    else:
        df.to_excel(output_path, index=False, engine='openpyxl')
        print(f"Data saved to {output_path}")

def main(pdf_path, output_folder=r'D:\\extract_task\\images', json_output_path=r'D:\\extract_task\\extracted_data.json', output_excel_path=r'D:\\extract_task\\output.xlsx'):
    """
    Main function to process the PDF, extract text, and save to an Excel file.
    """
    # Step 1: Convert PDF to images
    print("Converting PDF to images...")
    image_filenames = pdf_to_images(pdf_path, output_folder)
    
    # Step 2: Extract text from images and save to JSON
    print("Extracting text from images...")
    extract_text_from_images(image_filenames, json_output_path)
    
    # Step 3: Convert JSON to Excel
    print("Saving extracted data to Excel...")
    json_to_csv_or_excel(json_output_path, output_excel_path, file_type='excel')

if __name__ == '__main__':
    # Replace 'sample.pdf' with your PDF file path
    pdf_path = r'D:\\extract_task\\Summary of Benefits and Coverage Completed Example.pdf'
    main(pdf_path)
