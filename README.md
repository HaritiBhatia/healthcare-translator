# Healthcare Translator - Flask

A web-based healthcare translation app built with Flask that provides real-time multilingual translation.

## Features
- **Speech-to-Text**: Convert spoken input into a text transcript.
- **Translation**: Translate text using OpenAI API.
- **Text-to-Speech**: Play translated text as speech.
- **Mobile-Friendly**: Responsive design.

## Setup & Deployment

### Setup Locally
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/healthcare-translator-flask.git
   cd healthcare-translator-flask
   ```
2. Create a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Set OpenAI API Key in `.env`:
   ```sh
   OPENAI_API_KEY=your_openai_api_key_here
   ```
4. Run the Flask app:
   ```sh
   python app.py
   ```

### Deploy on Render
1. Push the code to GitHub.
2. Create a new **Render** web service.
3. Set the **Build Command** to:
   ```sh
   pip install -r requirements.txt
   ```
4. Set **Environment Variables**:
   - `GEMINI_API_KEY`
5. Deploy and use the app!

