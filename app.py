import streamlit as st
from PyPDF2 import PdfReader
from groq import Groq
from dotenv import load_dotenv
import os
import json

# Page configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Custom UI
st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)

# Load environment variables
load_dotenv()

# Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Title
st.markdown(
    '<div class="main-title">📄 AI Resume Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Upload your resume and get AI-powered feedback</div>',
    unsafe_allow_html=True
)

# Upload resume
uploaded_file = st.file_uploader(
    "📤 Upload your Resume",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("✅ Resume uploaded successfully!")

    # Extract text
    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    # Display extracted text
    st.subheader("📄 Extracted Resume Text")

    st.text_area(
        "Resume Content",
        text,
        height=300
    )

    # Analyze button
    if st.button("🔍 Analyze Resume"):

        with st.spinner("🤖 AI is analyzing your resume..."):

            prompt = f"""
Analyze the following resume and return the result ONLY as valid JSON.

Use exactly this format:

{{
    "ats_score": 75,
    "strengths": [
        "Strength 1",
        "Strength 2",
        "Strength 3"
    ],
    "weaknesses": [
        "Weakness 1",
        "Weakness 2",
        "Weakness 3"
    ],
    "improvement_suggestions": [
        "Suggestion 1",
        "Suggestion 2",
        "Suggestion 3"
    ],
    "missing_skills": [
        "Skill 1",
        "Skill 2",
        "Skill 3"
    ]
}}

Rules:
- ats_score must be a number between 0 and 100.
- Give 3 to 5 strengths.
- Give 3 to 5 weaknesses.
- Give 3 to 5 improvement suggestions.
- Give 3 to 5 missing skills.
- Do not add markdown.
- Do not add explanations outside the JSON.

Resume:
{text}
"""

            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.2
            )

            analysis = response.choices[0].message.content

            try:
                result = json.loads(analysis)

                # ATS Score
                st.subheader("📊 ATS Score")

                score = result["ats_score"]

                if score >= 80:
                    score_message = "Excellent ATS compatibility"
                elif score >= 60:
                    score_message = "Good, but can be improved"
                else:
                    score_message = "Needs improvement"

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        label="Estimated ATS Score",
                        value=f"{score} / 100"
                    )

                with col2:
                    st.info(score_message)

                # Strengths
                st.subheader("💪 Strengths")

                for strength in result["strengths"]:
                    st.write(f"✅ {strength}")

                # Weaknesses
                st.subheader("⚠️ Weaknesses")

                for weakness in result["weaknesses"]:
                    st.write(f"🔸 {weakness}")

                # Suggestions
                st.subheader("💡 Improvement Suggestions")

                for suggestion in result["improvement_suggestions"]:
                    st.write(f"➡️ {suggestion}")

                # Missing Skills
                st.subheader("🧠 Missing Skills")

                for skill in result["missing_skills"]:
                    st.write(f"📌 {skill}")

            except json.JSONDecodeError:
                st.error("❌ AI returned an invalid response.")
                st.write(analysis)