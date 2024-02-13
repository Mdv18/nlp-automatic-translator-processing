<template>
  <div class="">
    <div class="page-container">
    <div class="translator-container">
      <div class="language-selectors">
        <select v-model="selectedSourceLanguage">
          <option v-for="lang in languages" :key="lang.code" :value="lang.code">{{ lang.name }}</option>
        </select>

        <div class="language-switch-icon">⇄</div>

        <select v-model="selectedTargetLanguage">
          <option v-for="lang in languages" :key="lang.code" :value="lang.code">{{ lang.name }}</option>
        </select>
      </div>

    <div class="translation-boxes">
      <div class="text-box">
        <textarea v-model="textToTranslate" placeholder="Type to translate."></textarea>
        <div>Caratteri inseriti: {{ textToTranslate.length }}</div>
      </div>
      <div class="text-box">
        <textarea v-model="translatedText" placeholder="Translation" readonly></textarea>
        <div>Caratteri tradotti: {{ translatedText.length }}</div>
      </div>
    </div>

    <button @click="translateText" class="translate-button">Translate</button>
    </div>
    </div>

    <div class="analysis-container">
      <div v-if="analisiSentimenti.length">
        <h5>Analisi del Sentimento:</h5>
          <ul>
            <li v-for="(risultato, index) in analisiSentimenti" :key="index" :style="{ color: getColor(risultato.sentimento) }">
              "{{ risultato.testo }}" - {{ getSentimentoLabel(risultato.sentimento) }}
            </li>
          </ul>
      </div>

      <div v-if="analisiTesto.tokens.length || analisiTesto.entities.length">
        <h5>Analisi Testo:</h5>
          <div>
            <p v-for="(token, index) in analisiTesto.tokens" :key="`token-${index}`" class="analisi-tag" :class="`pos-${token.pos}`">
            {{ token.word }} <span>({{ token.pos }})</span>
            </p>
            <p v-for="(entity, index) in analisiTesto.entities" :key="`entity-${index}`" class="analisi-tag" :class="`ner-${entity.type}`">
            {{ entity.text }} <span>({{ entity.type }})</span>
            </p>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TranslatorComponent',
  data() {
    return {
      textToTranslate: '',
      translatedText: '',
      selectedSourceLanguage: 'IT',
      selectedTargetLanguage: 'EN-US',
      languages: [
        { name: 'Inglese (US)', code: 'EN-US' },
        { name: 'Italiano', code: 'IT' },
        { name: 'Spagnolo', code: 'ES' },
        { name: 'Francese', code: 'FR' },
      ],
      analisiSentimenti: [],
      analisiTesto: {
        tokens: [],
        entities: []
      },
    };
  },
  methods: {
    translateText() {
      const payload = {
        text: this.textToTranslate,
        source_lang: this.selectedSourceLanguage,
        target_lang: this.selectedTargetLanguage,
      };
      
      fetch('http://localhost:5001/translate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      })
      .then(response => response.json()) // prendo risposta e converto
      .then(data => { // prendo dato convertito 
        this.translatedText = data.translated_text || 'Errore nella traduzione';
        
        // array vuoto come valore di default se dati ricevuti somo vuoti
        this.analisiSentimenti = data.sentimenti || [];
        this.analisiTesto.tokens = data.tokens || [];
        this.analisiTesto.entities = data.entities || [];
      })
      .catch(error => {
        console.error('Errore:', error);
        this.translatedText = 'Errore nella traduzione';
      });
    },

    // determino in base a valore sentimento colore
    getColor(sentimento) {
      return sentimento < 1 ? 'red' : sentimento > 1 ? 'green' : 'gray';
    },
    // determino in base a valore sentimento titolo
    getSentimentoLabel(sentimento) {
      return sentimento < 1 ? 'Negativo' : sentimento > 1 ? 'Positivo' : 'Neutro';
    },
  },
}
</script>

<style>
body, html {
  display: grid;
  height: 100%; 
  margin: 0;
  display: flex; 
  justify-content: center; 
  align-items: center; 
  background: #e7ecef !important; 
}
 
.translator-layout {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  margin: 0 auto;
  max-width: 1240px;
  padding: 40px; 
}

.translator-container, .analysis-container {
  flex: 1;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  background: #ffffff;
  padding: 20px;
  border-radius: 40px;
  min-width: 300px;
  max-width: 1240px;
  margin: 20px;
} 

.translator-layout {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  margin: 0 auto;
  max-width: 1240px;
}

/* Display per Mobile */
@media (max-width: 768px) {
  .translator-layout {
    flex-direction: column;
  }
  .translator-container, .analysis-container {
    margin: 10px;
    max-width: none;
  }
}

.page-container {
    display: flex;
    justify-content: center;
    align-items: center;
    /*height: 100vh;*/
    padding: 20px;
}

.translator-container {
  width: 100%; 
  max-width: 800px; 
  margin: 0 auto; 
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); 
  background: #ffffff; 
  padding: 20px; 
  border-radius: 36px;
  margin: 14px;
}

.language-selectors {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.language-switch-icon {
  display: flex;
  align-items: center;
  font-size: 24px;
}

.translation-boxes {
  display: flex;
  gap: 20px;
}

.text-box {
  flex: 1;
}

.text-box textarea {
  width: 100%;
  padding: 10px;
  height: 150px;
  border: 1px solid #ccc;
  border-radius: 5px;
  resize: none;
}

.translate-button {
  display: block;
  width: 100%;
  padding: 10px 20px;
  margin-top: 20px;
  border: none;
  background-color: #00a6fb;
  color: #ffffff;
  border-radius: 20px;
  font-size: 18px;
  font-weight: 300;
  cursor: pointer;
}

.translate-button:hover {
  background-color: #16233B;
}

select {
  padding: 10px;
  border-radius: 5px;
  background: #ffffff;
  border: 1px solid rgba(0,0,0,.05);
}

/* Stile per POS */
.pos-NOUN { background-color: #B4C5E4; }
.pos-VERB { background-color: #90e0ef; }
.pos-ADJ { background-color: #00b4d8; }
.pos-ADV { background-color: #0077b6; }
.pos-PRON { background-color: #caf0f8; }
.pos-CONJ { background-color: #f0f3bd; }
.pos-DET { background-color: #fde2e4; }
.pos-PREP { background-color: #ffc6ff; }
.pos-AUX { background-color: #ffcccb; }
.pos-PROPN { background-color: #ffa07a; }
.pos-CCONJ { background-color: #fafad2; }

/* Stile per NER */
.ner-PERSON { background-color: #ffadad; }
.ner-LOCATION { background-color: #ffd6a5; }
.ner-ORG { background-color: #fdffb6; }
.ner-DATE { background-color: #caffbf; }
.ner-TIME { background-color: #9bf6ff; }
.ner-MONEY { background-color: #a0c4ff; }
.ner-PRODUCT { background-color: #bdb2ff; }

.analisi-tag {
  display: inline-block;
  margin: 5px;
  padding: 5px;
  border-radius: 15px;
  font-size: 0.7em;
  cursor: pointer;
  transition: background-color 0.3s;
}
</style>