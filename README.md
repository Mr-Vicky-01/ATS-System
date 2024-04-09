![image](https://github.com/Mr-Vicky-01/YT-Video-Summarizer/assets/143078285/962938a2-c064-44bb-9388-690353a12d49)

## Overview
This project is an Applicant Tracking System (ATS) that evaluates resumes based on a provided job description. It utilizes Google's GenerativeAI model "gemini-pro" to match resumes with job descriptions, assign a percentage match, identify missing keywords, and provide a profile summary.

## Usage
To use the ATS:
1. Paste the job description into the designated text area.
2. Upload your resume in PDF format.
3. Click on "Submit" to get the evaluation results.
4. The system will display the JD match percentage, missing keywords, and a profile summary.

## Requirements
- `python 3`
- `streamlit`
- `google.generativeai`
- `PyPDF2`
- `dotenv`

Install the dependencies using:
```bash
pip install streamlit google.generativeai PyPDF2 python-dotenv
```

## Project Structure
- ats_system.py: Main script containing the ATS functionality.
- GeminiPro_model: Model directory containing the GenerativeAI model "gemini-pro".

## Running the Project

To run the project:
```bash
streamlit run app.py
```

## Screen Shots

![image](https://github.com/Mr-Vicky-01/YT-Video-Summarizer/assets/143078285/0d3f0520-f6ff-4465-b5a2-32cd89c8b9f7)
![image](https://github.com/Mr-Vicky-01/YT-Video-Summarizer/assets/143078285/7a27e9d3-2020-4729-be10-8e1dedea9599)

## Link

[click here](https://huggingface.co/spaces/Mr-Vicky-01/ATS-System)
