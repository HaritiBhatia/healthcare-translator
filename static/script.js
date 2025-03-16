const startButton = document.getElementById("start-recording");
const transcriptElement = document.getElementById("transcript");
const translateButton = document.getElementById("translate");
const translatedTextElement = document.getElementById("translated-text");
const speakButton = document.getElementById("speak");
const languageSelect = document.getElementById("language");

// ✅ Speech-to-Text (Web Speech API)
startButton.addEventListener("click", () => {
    try {
        const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        recognition.lang = "en-US";
        recognition.start();

        recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript;
            transcriptElement.innerText = transcript;
        };

        recognition.onerror = (event) => {
            console.error("🚨 Speech Recognition Error:", event.error);
            alert("Speech recognition failed. Please try again.");
        };
    } catch (error) {
        console.error("🚨 Speech API Error:", error);
        alert("Speech recognition is not supported in your browser.");
    }
});

// ✅ Translation Request
translateButton.addEventListener("click", async () => {
    const text = transcriptElement.innerText;
    const targetLang = languageSelect.value;

    if (!text) {
        alert("No text to translate!");
        return;
    }

    try {
        const response = await fetch("/translate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text, targetLang }),
        });

        const data = await response.json();

        if (data.error) {
            alert("Translation failed: " + data.error);
            return;
        }

        translatedTextElement.innerText = data.translation;
    } catch (error) {
        console.error("🚨 Translation API Error:", error);
        alert("Translation service is currently unavailable.");
    }
});

// ✅ Text-to-Speech (TTS)
speakButton.addEventListener("click", () => {
    const translatedText = translatedTextElement.innerText;

    if (!translatedText) {
        alert("No translated text to speak!");
        return;
    }

    const utterance = new SpeechSynthesisUtterance(translatedText);
    speechSynthesis.speak(utterance);
});
