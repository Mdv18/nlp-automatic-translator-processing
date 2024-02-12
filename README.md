# NLPAutomaticTranslator

Ho sviluppato questo progetto come parte di un incarico universitario per creare un servizio di traduzione online. Utilizza un frontend costruito con **Vue.js** e **Bootstrap** per l'interfaccia utente, e un backend in **Flask** che gestisce le richieste di traduzione tramite **l'API DeepL**.

## Caratteristiche

- Traduzione di testo da una lingua all'altra utilizzando **l'API DeepL**.
- Selezione della lingua di origine e di destinazione attraverso menu a tendina.
- Interfaccia utente pulita e reattiva adatta a dispositivi desktop e mobili.
- Visualizzazione dei risultati della traduzione in tempo reale.

## Tecnologie Utilizzate

- **Frontend**: **Vue.js, Bootstrap** per il design e la reattività della pagina.
- **Backend**: **Flask** per gestire le richieste **API** e **CORS** per la comunicazione tra frontend e backend.
- **API di Traduzione**: **DeepL** per traduzioni di alta qualità.

## Installazione e Setup

Per eseguire il progetto in locale, segui i seguenti passi:

1. Clona il repository del progetto:
    ```sh
    git clone https://github.com/Mdv18/NLPAutomaticTranslator.git
    ```

2. Naviga nella directory del frontend e installa le dipendenze:
    ```sh
    cd NLPAutomaticTranslator/frontend
    npm install
    ```

3. Avvia il server di sviluppo del frontend:
    ```sh
    npm run serve
    ```

4. In una nuova finestra del terminale, naviga nella directory del backend e crea un ambiente virtuale:
    ```sh
    cd NLPAutomaticTranslator/backend
    python3 -m venv env
    ```

5. Attiva l'ambiente virtuale e installa le dipendenze del backend:
    ```sh
    source env/bin/activate  # Su Windows usa `env\Scripts\activate`
    pip install -r requirements.txt # Ricreo file dipendeze installate - pip freeze > requirements.txt

    ```

6. Avvia il server del backend:
    ```sh
    flask run
    ```

Ora, visita `http://localhost:8080` nel browser per visualizzare l'interfaccia **NLPAutomaticTranslator**.
