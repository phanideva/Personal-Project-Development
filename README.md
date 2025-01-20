# Personal-Project-Development

![Owner](https://github.com/phanideva/Personal-Project-Development): Phani Deva  
_A collection of personal development projects in AI, ML, Django, and more._

## 📄 Description

This repository contains a variety of personal projects focused on data science, machine learning, deep learning, web development, and automation. The projects serve as a learning ground and practical application of various technologies.

---

## 📁 Project Structure

Here's an overview of the key projects and folders in this repository:
```graphql
├── .github/workflows # GitHub actions for CI/CD automation 
├── AI and ML practice # Machine Learning and AI scripts and models 
├── Health App # Health-related application in Django 
├── MLmodels # Machine Learning models for loan pricing, etc. 
├── Pydantic library usage # Scripts for data validation using Pydantic 
├── aws_operations # AWS scripts for S3 operations, etc. 
├── chess_game # Chess game implementation 
├── data/MNIST/raw # MNIST dataset for DL projects
├── dave_game # Dave game look a like implementation
├── degrees # Shortest path algorithm implementation 
├── django_project # Full-stack web app using Django 
├── finance_project # Django finance management application 
├── pytesseract_ocr_extract # OCR implementation using Tesseract 
├── snake_game # Classic snake game implementation 
├── test_project # Unit testing scripts using pytest 
├── tictactoe # TicTacToe game using Python 
├── venv # Virtual environment │ 
├── EDA_analysis.ipynb # Exploratory Data Analysis (EDA) 
├── financial_usecase.ipynb # Financial analysis use cases 
├── requirements.txt # Project dependencies 
└── README.md # Project documentation
```
---

## 🚀 Installation

Follow these steps to set up the project on your local machine:

### **Clone the repository**
```bash
git clone https://github.com/phanideva/Personal-Project-Development.git
cd Personal-Project-Development
```

### **Set up the environment***
#### Install Python virtual environment and dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
pip install -r requirements.txt
```
### **To Run Django Project***
#### Navigate to the django_project folder and run:
```bash
cd django_project
python manage.py runserver
```

📦Dependencies
This repository requires the following major dependencies:

    Python 3.8+
    Django - Web framework for building full-stack applications
    PyTorch - Deep learning framework
    NumPy & Pandas - Data manipulation libraries
    Matplotlib & Seaborn - Data visualization libraries
    Pytesseract - OCR implementation
    AWS Boto3 - AWS service integration
    
Install all dependencies using:
```bash
pip install -r requirements.txt
```
🧪 Running Tests
Unit tests can be run using the following command:
```bash
pytest tests/
```
💡 Features
    🧠 AI and Machine Learning models (Loan pricing, OCR, etc.)
    🏥 Health and finance-related applications
    🎮 Fun games like Chess, Snake, and TicTacToe
    📄 Document extraction and OCR solutions
    📊 Exploratory Data Analysis (EDA) on financial datasets
    🌐 Full-stack Django applications (further end to end example can be found in django_react_project repository)

🛠️ Technologies Used
The following technologies are used in this repository:
    Programming Languages: Python, JavaScript (for frontend Django apps)
    Frameworks: Django, Flask
    Libraries: NumPy, Pandas, PyTorch, OpenCV, Pydantic
    Tools: AWS S3, Docker, GitHub Actions (CI/CD)

🤝 Contributing
Contributions are welcome! If you would like to improve the project, follow these steps:
    Fork the repository.
    Create a new feature branch (git checkout -b feature-branch-name).
    Commit your changes (git commit -m "Add some feature").
    Push to the branch (git push origin feature-branch-name).
    Open a Pull Request.

📬 Contact
If you have any questions or suggestions, feel free to contact:

    GitHub: phanideva
    Email: phanisaisri@gmail.com
