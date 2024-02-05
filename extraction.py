#import PyPDF2
#from PyPDF2 import PdfReader
#import re
#import pandas as pd
#
#def extract_info_from_first_table(pdf_path):
#    with open(pdf_path, 'rb') as file:
#        reader = PdfReader(file)
#        # Assuming the required information is in the first page
#        text = reader.pages[0].extract_text()
#
#    # Extract year from the 1st main heading
#    year_match = re.search(r'(\d{4}) W-2 and EARNINGS SUMMARY', text)
#    year = year_match.group(1) if year_match else "UnknownYear"
#
#    # Define your patterns here based on your PDF structure.
#    # This is a simplified example. You would need to refine these based on your actual PDF content.
#    patterns = {
#        'EmployeeNameAndAddress': r' Employer’s name, address, and ZIP code (.*?)ZIP',
#        'WagesTipsOtherComp': r'Wages,?\s+tips,?\s+other\s+compensation.*?(\$[\d,]+.\d{2})',
#        'FederalIncomeTaxWithheld': r'Federal income tax withheld (\d+)',
#        'SocialSecurityWages': r'Social security wages (\d+)',
#        'SocialSecurityTaxWithheld': r'Social security tax withheld (\d+)',
#        'MedicareWagesAndTips': r'Medicare wages and tips (\d+)',
#        'MedicareTaxWithheld': r'Medicare tax withheld (\d+)',
#        'State': r'State (\w+)',
#        'EmployersStateIDNo': r'Employer’s state ID no. (\d+)',
#        'StateWagesTips': r'State wages, tips, etc. (\d+)',
#        'StateIncomeTax': r'State income tax (\d+)',
#    }
#
#
#    extracted_info = {}
#    for key, pattern in patterns.items():
#        match = re.search(pattern, text, re.DOTALL)  # re.DOTALL to make . match newline
#        extracted_info[key] = match.group(1).strip() if match else ''
#
#    return extracted_info, year
#
#def write_info_to_csv(info, year, csv_path):
#    df = pd.DataFrame([info])
#    df.columns = [
#        'Employee Name and Address', 'Wages, Tips, Other Comp.', 'Federal Income Tax Withheld',
#        'Social Security Wages', 'Social Security Tax Withheld', 'Medicare Wages and Tips',
#        'Medicare Tax Withheld', 'State', 'Employer’s State ID No.', 'State Wages, Tips, Etc.',
#        'State Income Tax'
#    ]
#    df.to_csv(f"{year} W-2 and EARNINGS SUMMARY.csv", index=False)
#
## Path to your PDF
#pdf_path = 'D:\\Python Practice files\\Statement for 2023.pdf'
#csv_path = 'D:\\Python Practice files'
## Extract information
#info, year = extract_info_from_first_table(pdf_path)
#
## Write to CSV
#write_info_to_csv(info, year, csv_path)

#from pdfminer.high_level import extract_pages
#from pdfminer.layout import LTTextBoxHorizontal
#import re
#import pandas as pd
#
#def extract_info_from_first_table(pdf_path):
#    texts_with_coords = []  # List to hold text and its coordinates
#
#    for page_layout in extract_pages(pdf_path):
#        for element in page_layout:
#            if isinstance(element, LTTextBoxHorizontal):
#                for text_line in element:
#                    texts_with_coords.append({
#                        "text": text_line.get_text().strip(),
#                        "bbox": element.bbox
#                    })
#        break  # Assuming all relevant data is on the first page
#
#    return texts_with_coords
#
#def process_extracted_data(texts_with_coords):
#
#    data = {
#        'EmployeeNameAndAddress': r' Employer’s name, address, and ZIP code (.*?)ZIP',
#        'WagesTipsOtherComp': r'Wages, tips, other comp. (\d+)',
#        'FederalIncomeTaxWithheld': r'Federal income tax withheld (\d+)',
#        'SocialSecurityWages': r'Social security wages (\d+)',
#        'SocialSecurityTaxWithheld': r'Social security tax withheld (\d+)',
#        'MedicareWagesAndTips': r'Medicare wages and tips (\d+)',
#        'MedicareTaxWithheld': r'Medicare tax withheld (\d+)',
#        'State': r'State (\w+)',
#        'EmployersStateIDNo': r'Employer’s state ID no. (\d+)',
#        'StateWagesTips': r'State wages, tips, etc. (\d+)',
#        'StateIncomeTax': r'State income tax (\d+)',
#    }
#    return data
#
#def write_info_to_csv(info, csv_path):
#    year = info.pop('Year', 'UnknownYear')
#    df = pd.DataFrame([info], columns=info.keys())
#    df.to_csv(f"{csv_path}/{year} W-2 and EARNINGS SUMMARY.csv", index=False)
#
## Paths
#pdf_path = 'D:\\Python Practice files\\Statement for 2023.pdf'
#csv_path = 'D:\\Python Practice files'
#
## Extract information
#texts_with_coords = extract_info_from_first_table(pdf_path)
#info = process_extracted_data(texts_with_coords)
#
## Write to CSV
#write_info_to_csv(info, csv_path)

#import re
#from pdfminer.high_level import extract_pages
#from pdfminer.layout import LTTextBoxHorizontal
#import pandas as pd
#
#def extract_info_from_first_table(pdf_path):
#    # Initialize an empty string to hold all extracted text
#    full_text = ""
#    
#    # Extract text from the first page of the PDF
#    for page_layout in extract_pages(pdf_path):
#        for element in page_layout:
#            if isinstance(element, LTTextBoxHorizontal):
#                full_text += element.get_text()
#        break  # Only process the first page
#
#    # Define the regex patterns for each field
#
#    data_patterns = {
#    'EmployeeNameAndAddress': r'\d*\s*Employer’s name, address, and ZIP code\s*:\s*(.*?)\s*ZIP',
#    'WagesTipsOtherComp': r'Wages,?\s+tips,?\s+other\s+compensation.*?(\$[\d,]+.\d{2})',
#    'FederalIncomeTaxWithheld': r'\d*\s*Federal income tax withheld\s*:\s*(.+)',
#    'SocialSecurityWages': r'\d*\s*Social security wages\s*:\s*(.+)',
#    'SocialSecurityTaxWithheld': r'\d*\s*Social security tax withheld\s*:\s*(.+)',
#    'MedicareWagesAndTips': r'\d*\s*Medicare wages and tips\s*:\s*(.+)',
#    'MedicareTaxWithheld': r'\d*\s*Medicare tax withheld\s*:\s*(.+)',
#    'State': r'\d*\s*State\s*:\s*(.+)',
#    'EmployersStateIDNo': r'\d*\s*Employer’s state ID no\.\s*:\s*(.+)',
#    'StateWagesTips': r'\d*\s*State wages, tips, etc\.\s*:\s*(.+)',
#    'StateIncomeTax': r'\d*\s*State income tax\s*:\s*(.+)',
#}
#
#
#
#    # Initialize a dictionary to hold the extracted data
#    extracted_data = {}
#
#    # Apply each regex pattern to the full_text and store the results
#    for key, pattern in data_patterns.items():
#        match = re.search(pattern, full_text, re.DOTALL)  # Use re.DOTALL to make '.' match newline characters as well
#        extracted_data[key] = match.group(1).strip() if match else 'Not Found'
#
#    return extracted_data
#
#def write_info_to_csv(info, csv_path):
#    df = pd.DataFrame([info], columns=info.keys())
#    df.to_csv(csv_path, index=False)
#
#pdf_path = 'D:\\Python Practice files\\Statement for 2023.pdf'
#csv_path = 'D:\\Python Practice files\\Statement for 2023.csv'
#
## Extract information
#info = extract_info_from_first_table(pdf_path)
#
## Write to CSV
#write_info_to_csv(info, csv_path)


from pdfminer.high_level import extract_text
import re
import pandas as pd

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)
# Define a dictionary with the regex patterns for each field
patterns = {
    'WagesTipsOtherComp': r'Wages, tips, other comp\.\s*(\d+,\d+\.\d+)',
    'FederalIncomeTaxWithheld': r'Federal income tax withheld\s*(\d+,\d+\.\d+)',
    'SocialSecurityWages': r'Social security wages\s*(\d+,\d+\.\d+)',
    'SocialSecurityTaxWithheld': r'Social security tax withheld\s*(\d+,\d+\.\d+)',
    'MedicareWagesAndTips': r'Medicare wages and tips\s*(\d+,\d+\.\d+)',
    'MedicareTaxWithheld': r'Medicare tax withheld\s*(\d+,\d+\.\d+)',
    # Add additional fields as needed
}

# Function to extract all fields using defined patterns
def extract_fields_from_text(text, patterns):
    extracted_values = {}
    for field, pattern in patterns.items():
        match = re.search(pattern, text.replace('\n', ''))
        if match:
            # Remove commas from the matched values and convert to float
            extracted_values[field] = float(match.group(1).replace(',', ''))
        else:
            extracted_values[field] = None  # or some default value
    return extracted_values


# Function to write extracted data to CSV
def write_to_csv(data, csv_path):
    df = pd.DataFrame([data])
    df.to_csv(csv_path, index=False)
# PDF path (use the path where the PDF is stored)
pdf_path = 'D:\\Python Practice files\\Statement for 2023.pdf'
csv_path = 'D:\\Python Practice files\\Statement for 2023.csv'

# Extract text from PDF
text = extract_text_from_pdf(pdf_path)

# Extract fields from text
extracted_values = extract_fields_from_text(text, patterns)

# Write to CSV
write_to_csv(extracted_values, csv_path)




