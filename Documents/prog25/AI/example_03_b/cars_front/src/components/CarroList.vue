<template>
  <div>
    <h2>List of Carros</h2>
    <ul>
      <li v-for="carro in carros" :key="carro.id">
        {{ carro.fabricante }} {{ carro.modelo }} ({{ carro.ano }}), Owned by {{ carro.dono_nome }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      carros: []
    };
  },
  mounted() {
    this.fetchCarros();
  },
  methods: {
    fetchCarros() {
      axios.get('http://localhost:5000/carros')
        .then(response => {
          this.carros = response.data;
        })
        .catch(error => {
          console.error('There was an error fetching the carros:', error);
        });
    }
  }
};
</script>
