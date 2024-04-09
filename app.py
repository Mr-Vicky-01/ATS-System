import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
import re
import ast

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_repsonse(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

#Prompt Template

input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

## streamlit app
st.title("Applicant Tracking System (ATS)")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response_string=get_gemini_repsonse(input_prompt)
       
        # Extract JD match percentage
        jd_match = int(re.search(r'"JD Match":"(\d+)%?"', response_string).group(1))

        # Extract missing keywords
        missing_keywords = re.search(r'"MissingKeywords":(.*?)]', response_string).group(1) + ']'
        missing_keywords = eval(missing_keywords)  # Convert string representation of list to actual list

        # Extract profile summary
        profile_summary = re.search(r'"Profile Summary":"(.*?)"', response_string).group(1)

        # Streamlit app
        st.title("Resume Evaluation Result")
        st.write("JD Match:", f"{str(jd_match)}%")
        st.write("Missing Keywords:", missing_keywords)
        st.write("Profile Summary:", profile_summary)

        # If JD match percentage is more than 80%, display balloons
        if jd_match >= 80:
            st.balloons()
