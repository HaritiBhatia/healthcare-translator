import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
import os
import re
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

# ✅ Set API Key Manually (since Render doesn’t use .env files)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("🚨 ERROR: Google Gemini API Key not found! Check your Render environment settings.")
else:
    print("✅ Google Gemini API Key Loaded.")

# ✅ Configure API Key
genai.configure(api_key=GEMINI_API_KEY)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate_text():
    try:
        print("🔹 Received POST request to /translate")

        data = request.json
        text = data.get("text", "").strip()
        target_lang = data.get("targetLang", "").strip()

       
        if not text or not re.match(r"^[a-zA-Z0-9\s.,!?'-]+$", text):
            print("🚨 ERROR: Invalid input detected.")
            return jsonify({"error": "Invalid input."}), 400

        if not target_lang or not re.match(r"^[a-zA-Z-]+$", target_lang):
            print("🚨 ERROR: Invalid target language.")
            return jsonify({"error": "Invalid target language."}), 400

        print(f"📝 Translating Medical Text Securely: '{text}' → '{target_lang}'")

        
        model_name = "models/gemini-1.5-flash-latest"

        medical_prompt = f"""
        You are a professional medical translator. 
        Ensure that medical terminology is correctly translated into {target_lang} without loss of meaning:
        
        "{text}"
        """

        model = genai.GenerativeModel(model_name)
        response = model.generate_content(medical_prompt)

        translation = response.text if response.text else "Translation failed."

        print("✅ Secure Medical Translation Completed.")
        return jsonify({"translation": translation})

    except Exception as e:
        print("🚨 Translation API Error:", str(e))
        return jsonify({"error": "An error occurred while processing your request."}), 500


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
