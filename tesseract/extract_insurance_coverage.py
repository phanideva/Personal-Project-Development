import pandas as pd
import re

def extract_coverage_period(input_excel_path, output_excel_path):
    """
    Extracts the coverage period from the 'text' column and saves it in a new Excel file 
    with a single column 'COVERAGEPERIOD'.
    """
    # Load the Excel file
    df = pd.read_excel(input_excel_path)

    # Function to extract the date range after "Coverage Period:"
    def find_coverage_period(text):
        if pd.isnull(text):
            return None
        # Regex pattern to capture the date range after "Coverage Period:"
        pattern = r'\bCoverage\s*Period[:\-]?\s*([\d\/\-]+(?:\s*-\s*[\d\/\-]+)?)'
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1)
        return None
    
    def find_coverage_for(text):
        if pd.isnull(text):
            return None
        # Regex pattern to capture the date range after "Coverage Period:"
        pattern = r'\bCoverage\s*For[:\-]?\s*(\w+)'
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1)
        return None
    
    def find_plan_type(text):
        if pd.isnull(text):
            return None
        # Regex pattern to capture the date range after "Coverage Period:"
        pattern = r'\bPlan\s*Type[:\-]?\s*(\w+)'
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip("'")
        return None

    # Apply the function to the 'text' column and create a new DataFrame with only 'COVERAGEPERIOD' column
    coverage_periods = df['text'].apply(find_coverage_period)
    coverage_fors = df['text'].apply(find_coverage_for)
    plan_types = df['text'].apply(find_plan_type)
    new_df = pd.DataFrame({'COVERAGE PERIOD': coverage_periods, 'COVERAGE FOR': coverage_fors,
                           'PLAN TYPE': plan_types})

    # Save the new DataFrame to a new Excel file
    new_df.to_excel(output_excel_path, index=False, engine='openpyxl')
    print(f"Extracted coverage periods saved to {output_excel_path}")

# Example usage
if __name__ == '__main__':
    input_excel_path = r'D:\\extract_task\\output.xlsx'         # Path to the original output Excel file
    output_excel_path = r'D:\\extract_task\\updated_output.xlsx'  # Path to save the new Excel file with the 'coverage_period' column
    extract_coverage_period(input_excel_path, output_excel_path)
