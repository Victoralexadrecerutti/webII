<template>
  <div>
    <h2>List of Pessoas</h2>
    <ul>
      <li v-for="pessoa in pessoas" :key="pessoa.id">
        {{ pessoa.nome }} ({{ pessoa.idade }} years old, {{ pessoa.cidade }})
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      pessoas: []
    };
  },
  mounted() {
    this.fetchPessoas();
  },
  methods: {
    fetchPessoas() {
      axios.get('http://localhost:5000/pessoas')
        .then(response => {
          this.pessoas = response.data;
        })
        .catch(error => {
          console.error('There was an error fetching the pessoas:', error);
        });
    }
  }
};
</script>
