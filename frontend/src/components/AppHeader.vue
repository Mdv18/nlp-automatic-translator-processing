<template>
    <header class="header">
      <h2>NLPAutomaticTranslator</h2>
      <h5>traduzioni veloci, precise e sicure</h5>
      <button class="button">Version 0.0.18</button>
    </header>
  </template>
  
  <script>
  export default {
    name: 'AppHeader'
  };
  </script>
  
  <style scoped>
  .header {
    background-color: #16233B;
    padding: 2rem;
    color: #ffffff;
    text-align: center;
    border-radius: 20px;
    margin-bottom: 50px;
  }
  .button {
    background-color: #0052cc;
    color: white;
    border: none;
    margin-top: 20px;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    cursor: pointer;
  }
  </style>
  