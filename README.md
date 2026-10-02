# 📄 AI Resume Analyzer

An AI-powered Resume Analyzer that reads a PDF resume and provides useful feedback using Artificial Intelligence.

## 🚀 Features

* 📤 Upload Resume in PDF format
* 📄 Extract text from PDF
* 📊 Estimate ATS Score
* 💪 Analyze Resume Strengths
* ⚠️ Identify Resume Weaknesses
* 💡 Provide Improvement Suggestions
* 🧠 Suggest Missing Skills

## 🛠️ Technologies Used

* Python
* Streamlit
* Groq API
* PyPDF2
* python-dotenv

## 📁 Project Structure

```text
AI_Resume_Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Open the project folder

```bash
cd AI_Resume_Analyzer
```

### 3. Create virtual environment

```bash
python -m venv venv
```

### 4. Activate virtual environment

Windows PowerShell:

```bash
venv\Scripts\activate
```

### 5. Install required libraries

```bash
pip install -r requirements.txt
```

## 🔑 Groq API Key Setup

Create a `.env` file in the project folder:

```text
GROQ_API_KEY=your_groq_api_key_here
```

Do not share or upload your real API key publicly.

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in the browser.

## 📊 Example Output

The application provides:

* ATS Score
* Strengths
* Weaknesses
* Improvement Suggestions
* Missing Skills

## 🎯 Project Objective

The main objective of this project is to understand:

* PDF text extraction
* Prompt Engineering
* AI-based Resume Analysis
* ATS Score Estimation
* Building a web application using Streamlit

## 🔮 Future Improvements

* Job description matching
* Resume keyword analysis
* Resume formatting suggestions
* Downloadable analysis report
* More accurate ATS analysis

## 👩‍💻 Author

B.Tech Final Year Student
