<!--
    para que esse script funcione, é preciso instalar:

    npm install -D vitest

-->

<script>

export default {

    data() {
        return {
            // lista de pessoas :-)
            pessoas: [],
            error: null
        };
    },

    methods: {
        getPessoas: function () {
            // chamada ao backend
            fetch('http://localhost:5000/listar_pessoas')
                .then(response => response.json()) // especificando que a resposta vai ser em json
                .then(json => {
                    //console.log(json);
                    if (json.resultado == 'ok') { // a API informa que deu certo a chamada?
                        this.pessoas = json.detalhes; // pega as pessoas ;-p
                    } else {
                        // informar o erro - assustar o usuário :-O
                        this.pessoas = [{"nome":json.detalhes, "telefone":"erro", "email":"erro"}]
                    }
                })
                .catch(error => {
                    this.error = error;
                });
        }
    }
}
</script>

<template>
    
    <div class="m-3">
        <button @click="getPessoas">Listar as pessoas</button>
    </div>

    <div class="m-3">

        <div v-if="pessoas.length"> <!-- tem alguém na lista? -->

            <!-- percorre a lista de pessoas: "for" na "div" WOOWW ;-p -->
            <div class="card" style="width: 18rem;" v-for="p in pessoas" :key="p.id">
                <div class="card-body">
                    <!-- para cada pessoa, exibe as informações -->
                    <strong>Nome: {{ p.nome }}</strong><br />
                    <small>Email: {{ p.email }}</small><br />
                    <small>Telefone: {{ p.telefone }}</small>
                </div>
            </div>
        </div>

        <p v-if="error">{{ error }}</p>
    </div>
</template >

<!--
    https://www.educative.io/answers/how-to-make-http-requests-in-vuejs-using-fetch-api
-->
