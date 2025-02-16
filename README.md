# 🤖 AI Code Reviewer  

🚀 A Streamlit-based AI-powered Python Code Reviewer using Google Gemini API  

## 🌟 Overview  

AI Code Reviewer is a web-based tool that helps developers **identify bugs, inefficiencies, and errors** in their Python code using **Google Gemini AI**. It provides **detailed feedback** along with **suggested fixes** and allows users to **download AI-generated reports**.  

---

## 🌟 Features  

✅ **AI-Powered Code Review** – Automatically detects issues and suggests fixes  
✅ **Downloadable Reports** – Users can save the AI-generated bug report  
✅ **Logging & Error Handling** – Tracks errors and logs debugging info  
✅ **Secure API Key Management** – Uses `.env` file to protect credentials  
✅ **Simple Streamlit UI** – Interactive and easy to use  
✅ **Works on Any System** – Supports Windows, Mac, and Linux  

---

## 📌 Installation Guide  

Follow these steps to set up and run the AI Code Reviewer:  

```sh
# 1️⃣ Clone the Repository  
git clone https://github.com/AbhilashSurapuchetty/AI-Code-Reviewer.git
cd AI-Code-Reviewer

# 2️⃣ Create a Virtual Environment  
python -m venv venv  

# Activate the virtual environment  
source venv/bin/activate  # (Windows: venv\Scripts\activate)

# 3️⃣ Install Dependencies  
pip install -r requirements.txt

# 4️⃣ Set Up API Key  
echo "GOOGLE_API_KEY=your_google_gemini_api_key" > .env (Linux)
In Windows visit google AI studio create your own API Key
Save that API Key as GOOGLE_API_KEY = Key in a .env file.

# 5️⃣ Run the Application  
streamlit run app.py
