<template>
    <footer class="footer">
      <div class="container">
        <div class="logo">
          <!-- Aggiungo l'immagine del logo -->
          <img src="@/assets/NLPAutomaticTranslator-logo.png" alt="Logo Traduttore Online" class="footer-logo">
        </div>
        <div class="links">
          <a href="#!" class="footer-link">Home</a>
          <a href="#!" class="footer-link">About</a>
          <a href="#!" class="footer-link">Contact</a>
          <a href="#!" class="footer-link">Privacy Policy</a>
        </div>
        <div class="credits">
          <p>© {{ currentYear }} <b>NLPAutomaticTranslator</b>. Tutti i diritti riservati.</p>
        </div>
      </div>
    </footer>
  </template>
  
  <script>
  export default {
    name: 'AppFooter',
    data() {
      return {
        // Aggiungo l'anno con il costruttore Date e getFullYear
        currentYear: new Date().getFullYear()
      }
    }
  };
  </script>
  
  
  <style scoped>
  /* Stile locale per il componente cosi da non sovrascrivere altri stili */
  .footer {
    background-color: #f5f5f5;
    padding: 20px 0;
    text-align: center;
  }
  
  .logo {
    text-align: center;
    margin-bottom: 20px;
  }
  
  .links {
    margin-bottom: 20px;
  }
  
  .footer-link {
    margin: 0 15px;
    color: #007bff;
    text-decoration: none;
  }
  
  .footer-link:hover {
    text-decoration: underline;
  }
  
  .footer-logo {
    max-width: 250px;
  }
  </style>
  