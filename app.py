import streamlit as st
import google.generativeai as genai
import os
import logging
from dotenv import load_dotenv
import time
from datetime import datetime

# Load API Key from environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Ensure API Key is available before configuring the AI model
if not API_KEY:
    st.error("❌ API Key is missing! Please check your `.env` file.")
else:
    try:
        genai.configure(api_key=API_KEY)
    except Exception as e:
        st.error(f"⚠️ Error configuring API: {e}")
        logging.error(f"API configuration failed: {e}")

# Set up logging to track errors and activity
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Initialize the AI model for code reviewing
try:
    model = genai.GenerativeModel(
        'gemini-2.0-flash-exp',
        system_instruction="""You are an AI-powered Python Code Reviewer. Your task is to analyze Python code submitted by the user, detect any potential bugs, and provide a fixed version of the code. 
        Ensure your response follows this structure:

        **Bug Report:**
        - Identify issues or inefficiencies in the code.
        - Clearly explain each problem.

        **Fixed Code:**
        - Provide a corrected version of the code.
        - Ensure it follows best practices and optimizations.

        Additional Rules:
        - If the input is not Python code, respond in a friendly manner, suggesting that the tool is designed for Python.
        - Keep responses concise and to the point.
        """
    )
except Exception as e:
    st.error(f"⚠️ Failed to initialize AI model.")
    logging.error(f"Model initialization error: {e}")

# Streamlit UI setup
st.title("🤖 AI Code Reviewer")
st.write("Submit your Python code for AI-powered bug detection and fixes!")

# Text input area for users to enter their Python code
code = st.text_area("Enter your Python code:", height=200)

# Function to generate a downloadable review report
def generate_report(code, review):
    """
    Generates a text file containing the AI's review of the submitted Python code.
    The file is named using a timestamp to avoid overwriting previous reports.

    Parameters:
        code (str): The Python code submitted by the user.
        review (str): The AI-generated review of the code.

    Returns:
        str: The filename of the generated report.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"code_review_{timestamp}.txt"
    
    report_content = f"""AI Code Review Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Submitted Code:
--------------------
{code}

AI Feedback:
--------------------
{review}
"""

    try:
        with open(filename, "w") as file:
            file.write(report_content)
        return filename
    except Exception as e:
        logging.error(f"Error generating report: {e}")
        return None

# Submit button - Triggers AI code review
if st.button("🔍 Review Code"):
    if code.strip() == "":
        st.warning("⚠️ Please enter some code before submitting!")
    else:
        with st.spinner("Analyzing your code... Please wait."):
            time.sleep(1.5)  # Simulating processing time for a better user experience
            try:
                # Construct the prompt to send to the AI model
                prompt = f"Review the following Python code:\n\n{code}"
                response = model.generate_content(prompt)

                # Ensure the response is valid before displaying it
                if response and hasattr(response, 'text'):
                    st.subheader("🛠️ AI Feedback:")
                    st.write(response.text)

                    # Generate and offer a downloadable review report
                    report_filename = generate_report(code, response.text)
                    if report_filename:
                        with open(report_filename, "rb") as file:
                            st.download_button(
                                label="📥 Download Code Review Report",
                                data=file,
                                file_name=report_filename,
                                mime="text/plain",
                                key="download-button"
                            )
                    else:
                        st.error("⚠️ Error generating report file.")
                else:
                    st.error("⚠️ No response received from AI model!")

            except Exception as e:
                st.error(f"🚨 Error processing your request: {e}")
                logging.error(f"Processing error: {e}")