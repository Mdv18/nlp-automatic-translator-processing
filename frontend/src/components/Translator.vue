<template>
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
      </div>
      <div class="text-box">
        <textarea v-model="translatedText" placeholder="Translation" readonly></textarea>
      </div>
    </div>

    <button @click="translateText" class="translate-button">Translate</button>
  </div>
</template>

<script>
export default {
  name: 'TranslatorComponent',
data() {
  return {
    textToTranslate: '',
    translatedText: '',
    selectedSourceLanguage: 'IT', // pre-seleziono una lingua 
    selectedTargetLanguage: 'EN-US', // pre-seleziono una lingua di destinazione
    languages: [
      { name: 'Inglese (US)', code: 'EN-US' },
      { name: 'Italiano', code: 'IT' },
      { name: 'Spagnolo', code: 'ES' },
      { name: 'Francese', code: 'FR' }
      // posso aggiungere altre lingue
    ]
  };
},

methods: {
  translateText() {
    // Includo le lingue di origine e destinazione nel corpo della richiesta
    const payload = {
      text: this.textToTranslate,
      source_lang: this.selectedSourceLanguage, // Lingua di origine selezionata
      target_lang: this.selectedTargetLanguage  // Lingua di destinazione selezionata
    };

    //console.log(JSON.stringify(payload)); // Aggiungo questa riga per il debug
    
    fetch('http://localhost:5001/translate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload)
    })
    .then(response => {
      if (!response.ok) {
        throw new Error(`Errore dal server con stato: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      if (data.translated_text) {
        this.translatedText = data.translated_text;
      } else {
        console.error('Risposta inaspettata dal server:', JSON.stringify(data)); // debug
        this.translatedText = 'Risposta inaspettata dal server';
      }
    })
    .catch(error => {
      console.error('Errore:', error); // debug
      this.translatedText = 'Errore nella traduzione';
    });
  }
}

}
</script>

<style>
/* Applico uno stile alla mia applicazione */
body, html {
  height: 100%; 
  margin: 0;
  display: flex; 
  justify-content: center; 
  align-items: center; 
  background: #f5f7f8 !important; 
}

.translator-container {
  width: 100%; 
  max-width: 900px; 
  margin: 0 auto; 
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); 
  background: #ffffff; 
  padding: 20px; 
  border-radius: 8px; 
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
  background-color: #36558F;
  color: #ffffff;
  border-radius: 5px;
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
</style>