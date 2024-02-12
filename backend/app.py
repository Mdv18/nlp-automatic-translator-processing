from flask import Flask, request, jsonify
from flask_cors import CORS
import deepl

app = Flask(__name__)
CORS(app, resources={r"/translate": {"origins": "http://localhost:8080"}})  # Abilito CORS solo per l'endpoint '/translate' e dall'URL del frontend

# Inserisco chiave API di DeepL configurata
translator = deepl.Translator("fa823044-2278-0dab-95e4-3810429b3659:fx")

@app.route('/')
def home():
    return "Benvenuto al servizio di traduzione!"

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text_to_translate = data.get('text')
    target_lang = data.get('target_lang', 'IT')  # Fallback a 'IT' se non specificato
    print(f"Traducendo in {target_lang}: '{text_to_translate}'")  # Debug

    # Chiamo la funzione di traduzione con il testo da tradurre e la lingua di destinazione specificata
    try:
        result = translator.translate_text(text_to_translate, target_lang=target_lang)
        translated_text = result.text
    except Exception as e:
        print(f"Errore durante la traduzione: {e}")
        return jsonify({'error': 'Si è verificato un errore durante la traduzione'}), 500
    
    # Restituisco il testo tradotto in formato JSON se la traduzione è avvenuta con successo.
    return jsonify(translated_text=translated_text)


if __name__ == '__main__':
    app.run(debug=True)