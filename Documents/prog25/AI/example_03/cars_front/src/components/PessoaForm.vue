<template>
  <div>
    <h2>Create Pessoa</h2>
    <form @submit.prevent="createPessoa">
      <input v-model="nome" placeholder="Nome" required />
      <input v-model="idade" type="number" placeholder="Idade" required />
      <input v-model="cidade" placeholder="Cidade" required />
      <button type="submit">Create Pessoa</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      nome: '',
      idade: '',
      cidade: ''
    };
  },
  methods: {
    createPessoa() {
      axios.post('http://localhost:5000/pessoas', {
        nome: this.nome,
        idade: this.idade,
        cidade: this.cidade
      })
      .then(response => {
        alert('Pessoa created successfully');
        this.nome = '';
        this.idade = '';
        this.cidade = '';
      })
      .catch(error => {
        console.error('There was an error creating the Pessoa:', error);
      });
    }
  }
};
</script>
