<template>
  <div>
    <h2>Create Carro</h2>
    <form @submit.prevent="createCarro">
      <input v-model="fabricante" placeholder="Fabricante" required />
      <input v-model="modelo" placeholder="Modelo" required />
      <input v-model="ano" type="number" placeholder="Ano" required />
      <select v-model="dono_id" required>
        <option disabled value="">Select Pessoa (Owner)</option>
        <option v-for="pessoa in pessoas" :key="pessoa.id" :value="pessoa.id">
          {{ pessoa.nome }}
        </option>
      </select>
      <button type="submit">Create Carro</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      fabricante: '',
      modelo: '',
      ano: '',
      dono_id: '',
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
          console.error('Error fetching pessoas:', error);
        });
    },
    createCarro() {
      axios.post('http://localhost:5000/carros', {
        fabricante: this.fabricante,
        modelo: this.modelo,
        ano: this.ano,
        dono_id: this.dono_id
      })
      .then(response => {
        alert('Carro created successfully');
        this.fabricante = '';
        this.modelo = '';
        this.ano = '';
        this.dono_id = '';
      })
      .catch(error => {
        console.error('There was an error creating the Carro:', error);
      });
    }
  }
};
</script>
