<!--
    https://www.koderhq.com/tutorial/vue/http-fetch/
    https://serversideup.net/sending-post-put-and-patch-requests-with-fetch-api-and-vuejs/
-->

<!--

    instalar:

    npm install axios vue-axios


-->


<template>
    <div id="div_form_incluir">
        <form @submit.prevent="incluirPessoa" id="meuformulario">
            <p>
                Nome: <input type=" text" id="nome" v-model="dados.nome">
            </p>
            <p>
                Email: <input type="email" id="email" v-model="dados.email">
            </p>
            <p>
                Telefone: <input type="text" id="telefone" v-model="dados.telefone">
            </p>
            <button>Incluir!</button>
        </form>
        <input v-model="mensagem">
    </div>
</template>
  
<style>
#div_form_incluir {
    background-color: lightgray;
}
</style>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            dados: {
                nome: 'João da Silva Oliveira',
                email: 'josilvaliv@gmail.com',
                telefone: '47 91234 5678'
            },
            mensagem: "",
        }
    },
    methods: {
        incluirPessoa() {
            // faz a solicitação http, enviando dados
            axios.post('http://localhost:5000/incluir_pessoa', this.dados)
                .then(response => {
                    //console.log(response); // descomente essa linha se quiser ver a resposta no console
                    // resposta ok?
                    if (response.data.resultado == 'ok') {
                        // informa sucesso na operação
                        this.mensagem = "Pessoa incluída com sucesso!";
                        // limpa os campos
                        this.nome = "";
                        this.email = "";
                        this.telefone = "";
                    } else {
                        // exibe mensagem de erro se houve erro na resposta
                        this.mensagem = response.data.detalhes;
                    }
                })
                // se houve erro na chamada
                .catch(error => {
                    this.mensagem = "Erro na chamada: " + error;
                });
        }
    }
};
</script>