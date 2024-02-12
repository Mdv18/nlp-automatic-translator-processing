<template>
  <div id="app">
    <AppHeader/>
    <Translator/>
    <app-footer></app-footer>
  </div>
</template>

<script>
// Importo i componenti
import AppHeader from './components/AppHeader.vue';
import Translator from './components/Translator.vue';
import AppFooter from './components/AppFooter.vue';

export default {
  // Registro i componenti
  components: { 
    AppHeader,
    Translator, 
    AppFooter
  }
};
</script>
