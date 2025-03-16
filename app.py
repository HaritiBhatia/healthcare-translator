import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
import os
import re
from dotenv import load_dotenv


load_dotenv()

# ✅ Google Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("🚨 ERROR: Google Gemini API Key not found! Check your .env file.")
else:
    print(f"✅ Google Gemini API Key Loaded.")

genai.configure(api_key=GEMINI_API_KEY)


MODEL_NAME = "models/gemini-1.5-pro-latest"

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

        
        if not text or not re.match("^[a-zA-Z0-9\s.,!?'-]+$", text):
            print("🚨 ERROR: Invalid text input detected.")
            return jsonify({"error": "Invalid input provided."}), 400

        if not target_lang or not re.match("^[a-zA-Z-]+$", target_lang):
            print("🚨 ERROR: Invalid language code.")
            return jsonify({"error": "Invalid target language."}), 400

        print(f"📝 Translating: '{text}' → '{target_lang}' using Google Gemini AI...")

      
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(f"Translate this to {target_lang}: {text}")

        translation = response.text if response.text else "Translation failed."

       
        print(f"✅ Translation completed.")

        return jsonify({"translation": translation})

    except Exception as e:
        print("🚨 Translation API Error:", str(e))
        return jsonify({"error": "An error occurred while processing your request."}), 500
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
