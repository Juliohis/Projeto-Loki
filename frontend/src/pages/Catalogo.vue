
<script setup>
import { ref, onMounted } from 'vue'
const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:5000'

const jogos = ref([])
const carregando = ref(true)
const erro = ref('')

async function carregarJogos() {
  try {
    const resposta = await fetch(`${API_URL}/api/jogos`)

    if (!resposta.ok) {
      throw new Error('Não foi possível carregar o catálogo.')
    }

    jogos.value = await resposta.json()

  } catch (erroApi) {
    erro.value = erroApi.message
  } finally {
    carregando.value = false
  }
}

onMounted(carregarJogos)
</script>

<template>
  <main>
    <h1>Catálogo de jogos</h1>

    <p>
      Explore nossa coleção de jogos de Super Nintendo.
    </p>

    <p v-if="carregando">Carregando jogos...</p>
    <p v-else-if="erro">{{ erro }}</p>

    <section v-else>
      <h2>Todos os jogos</h2>
      <p>{{ jogos.length }} jogos disponíveis no catálogo.</p>

      <div class="catalogo">
        <article v-for="jogo in jogos" :key="jogo.id">
          <img
            :src="`${API_URL}/${jogo.capa}`"
            :alt="'Capa de ' + jogo.nome"
          />

          <h3>{{ jogo.nome }}</h3>
          <p>{{ jogo.ano }}</p>
        </article>
      </div>
    </section>
  </main>
</template>
