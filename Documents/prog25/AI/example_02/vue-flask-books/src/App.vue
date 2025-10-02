<template>
  <div class="container">
    <h1>Book Manager</h1>
    <BookManager />
  </div>
</template>

<script setup>
import BookManager from './components/BookManager.vue'
</script>

<style>
.container {
  max-width: 800px;
  margin: auto;
  padding: 20px;
  font-family: sans-serif;
}
</style>
