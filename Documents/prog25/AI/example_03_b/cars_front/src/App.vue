<template>
  <div id="app">
    <h1>Carro and Pessoa Management</h1>
    <PessoaForm />
    <PessoaList />
    <CarroForm />
    <CarroList />
  </div>
</template>

<script>
import PessoaForm from './components/PessoaForm.vue';
import PessoaList from './components/PessoaList.vue';
import CarroForm from './components/CarroForm.vue';
import CarroList from './components/CarroList.vue';

export default {
  name: 'App',
  components: {
    PessoaForm,
    PessoaList,
    CarroForm,
    CarroList
  }
};
</script>

<style>
/* Add styles if needed */
</style>
