## 🚀 Live Demo  

🔗 **Try the AI Code Reviewer here:** [AI Code Reviewer](https://ai-code-reviewer-qhdhwqdnjtgi2c7x7rbtpn.streamlit.app/)  

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
```


## 📌 How the Code Works  

### 1️⃣ Google Gemini API Configuration  
- The application loads your **API key** from `.env`.  
- If the API key is missing, it **shows an error** and logs it for debugging.  

### 2️⃣ AI Model Initialization  
- The `gemini-2.0-flash-experiment` model is loaded with a **system prompt** to ensure structured responses.  
- The AI **expects Python code** and generates **bug reports + fixes**.  

### 3️⃣ Streamlit UI Setup  
- Users enter **Python code** in a text box.  
- They click **“🔍 Review Code”** to submit it.  
- The AI analyzes the code and **displays a structured review**.  

### 4️⃣ AI Processing & Response Handling  
- If the API **fails** or does not return a response, the app **logs the error** and shows a message.  
- If successful, the AI **returns two sections**:  
  - **Bug Report 🛠️** (Identified issues and explanations)  
  - **Fixed Code ✅** (Suggested corrections with improvements)  

### 5️⃣ Generating and Downloading Reports  
- Users can **download the AI review** as a `.txt` file for future reference.  
- The file is **time-stamped** to avoid overwriting old reports.  

### 6️⃣ Logging & Debugging Support  
- The app **logs API failures, user input errors, and processing issues** in `app.log`.  
- This helps **track issues** and improve the application over time.  

---

## 📌 API Key Security  

```md
- **DO NOT share your `GOOGLE_API_KEY`**.  
- Always **use a `.env` file** to keep it safe.  
- Add `.env` to **`.gitignore`** to prevent accidental uploads.

```

## 🤝 Contributing  

Contributions are welcome! Follow these steps to contribute:  

```sh
# Fork the repository  
# Create a new branch  
git checkout -b feature-branch  

# Commit your changes  
git commit -m "Added a new feature"  

# Push to your fork and submit a Pull Request  
git push origin feature-branch  
```
## 📜 License  
This project is **open-source** and available under the **MIT License**.  

---

## 📧 Contact  
For any queries, reach out via **[LinkedIn](https://www.linkedin.com/in/abhilash-surapuchetty-baa0a4267/)** or **GitHub Issues**.  


