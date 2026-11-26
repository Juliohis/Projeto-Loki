
<script setup>
import { ref, onMounted, watch } from 'vue'
const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:5000'

const resultados = ref([])
const buscando = ref(false)
const opcoes = ref({
  generos: [],
  estilos: [],
  visoes: []
})

const selecionados = ref({
  genero: [],
  estilo_de_jogo: [],
  visao: []
})

const carregando = ref(true)
const erro = ref('')

async function carregarOpcoes() {
  try {
    const resposta = await fetch(`${API_URL}/api/opcoes`)

    if (!resposta.ok) {
      throw new Error('Não foi possível carregar as opções.')
    }

    opcoes.value = await resposta.json()
  } catch (erroApi) {
    erro.value = erroApi.message
  } finally {
    carregando.value = false
  }
}

onMounted(carregarOpcoes)
async function carregarEstilos() {
  const parametros = new URLSearchParams()

  selecionados.value.genero.forEach(genero => {
    parametros.append('genero', genero)
  })

  selecionados.value.visao.forEach(visao => {
    parametros.append('visao', visao)
  })
  
  const resposta = await fetch(
    `${API_URL}/api/estilos?${parametros.toString()}`
  )

  opcoes.value.estilos = await resposta.json()

  selecionados.value.estilo_de_jogo = []
}

watch(
  [
    () => selecionados.value.genero,
    () => selecionados.value.visao
  ],
  carregarEstilos
)
async function buscarJogos() {
 console.log('Botão de busca acionado!')

  buscando.value = true

  try {
    const resposta = await fetch(`${API_URL}/api/buscar`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(selecionados.value)
    })

    if (!resposta.ok) {
      throw new Error('Erro ao buscar jogos.')
    }

    resultados.value = await resposta.json()

  } catch (erroApi) {
    erro.value = erroApi.message
  } finally {
    buscando.value = false
  }
}
</script>

<template>
  <main>
    <h1>Identificar jogo</h1>
    <p>Selecione as características do jogo que procura.</p>

    <p v-if="carregando">Carregando opções...</p>
    <p v-else-if="erro">{{ erro }}</p>

    <template v-else>
      <section>
        <h2>Gênero</h2>
        <label v-for="opcao in opcoes.generos" :key="opcao">
          <input
            type="checkbox"
            :value="opcao"
            v-model="selecionados.genero"
          />
          {{ opcao }}
        </label>
      </section>

      <section>
        <h2>Visão</h2>
        <label v-for="opcao in opcoes.visoes" :key="opcao">
          <input
            type="checkbox"
            :value="opcao"
            v-model="selecionados.visao"
          />
          {{ opcao }}
        </label>
      </section>

      <section>
        <h2>Estilo de jogo</h2>
        <label v-for="opcao in opcoes.estilos" :key="opcao">
          <input
            type="checkbox"
            :value="opcao"
            v-model="selecionados.estilo_de_jogo"
          />
          {{ opcao }}
        </label>
      </section>

      <button @click="buscarJogos" :disabled="buscando">
        {{ buscando ? 'Buscando...' : 'Buscar jogos' }}
      </button>
      <section v-if="resultados.length > 0">
  <h2>Resultados encontrados</h2>

  <article v-for="jogo in resultados" :key="jogo.id">
    <h3>{{ jogo.nome }}</h3>
    <p>Caminho da capa: {{ jogo.capa }}</p>
    <p>{{ jogo.ano }}</p>
    <p>{{ jogo.descricao }}</p>
    <img
      :src="`${API_URL}/${jogo.capa}`"
      :alt="'Capa de ' + jogo.nome"
    />
  </article>
</section>

<p v-else>Selecione os filtros e busque um jogo.</p>

    </template>
  </main>
</template>
