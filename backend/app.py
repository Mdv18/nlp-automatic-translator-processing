from flask import Flask, request, jsonify
from flask_cors import CORS
import deepl
import stanza

stanza.download('en') # scarico modello inglese
nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,ner,sentiment') # processo dati

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}}) # Abilito CORS

# Imposto API DeepL
translator = deepl.Translator("fa823044-2278-0dab-95e4-3810429b3659:fx")


def analizza_testo(testo):
    doc = nlp(testo)
    tokens = []
    entities = []
    
    for sentence in doc.sentences: # Itera
        for token in sentence.tokens:
            if token.words[0].pos != "PUNCT": # per ogni token ignoro punteggiatura
                # aggiungo un dizionario all'elenco tokens 
                tokens.append({'word': token.text, 'pos': token.words[0].pos})
    
    for ent in doc.ents:
        entities.append({'text': ent.text, 'type': ent.type}) # tipo di entità
    
    sentimenti = [{'testo': sentence.text, 'sentimento': sentence.sentiment} for sentence in doc.sentences]
    # Restituisce un dizionario degli elenchi creati
    return {'tokens': tokens, 'entities': entities, 'sentimenti': sentimenti}

@app.route('/')
def home():
    return "Benvenuto al servizio di traduzione e NLP!"

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text_to_translate = data.get('text')
    target_lang = data.get('target_lang', 'IT')
    
    try:
        translated_result = translator.translate_text(text_to_translate, target_lang=target_lang)
        translated_text = translated_result.text
        analisi = analizza_testo(text_to_translate)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    return jsonify({
        'translated_text': translated_text,
        **analisi
    })

if __name__ == '__main__':
    app.run(debug=True)
