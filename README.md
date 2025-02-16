# 🤖 AI Code Reviewer

### 🚀 A Streamlit-based AI-powered Python Code Reviewer using Google Gemini API

## 🌟 Features:
✅ **AI-Powered Code Review** – Detects bugs and suggests fixes  
✅ **Downloadable Report** – Users can download the AI-generated bug report  
✅ **Logging & Error Handling** – Keeps track of issues for debugging  
✅ **Streamlit UI** – Simple and interactive web-based interface  

---

## 📌 Installation Guide  

1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/yourusername/AI-Code-Reviewer.git
cd AI-Code-Reviewer
2️⃣ **Clone the Repository**  

sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # (On Windows, use `venv\Scripts\activate`)
3️⃣ Install Dependencies

sh
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up API Key
Create a .env file in the project folder and add:

ini
Copy
Edit
GOOGLE_API_KEY=your_google_gemini_api_key
5️⃣ Run the Application

sh
Copy
Edit
streamlit run app.py
📌 How It Works
Enter Python code in the input box
Click the "🔍 Review Code" button
AI generates a Bug Report & Fixed Code
Download the generated report
🤝 Contributing
Feel free to fork the repo and submit pull requests!