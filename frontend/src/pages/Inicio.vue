
<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

function iniciarIdentificacao() {
  router.push('/identificar')
}
</script>

<template>
  <main>
    <h1>Projeto Loki</h1>

    <p>
      Descubra qual jogo de Super Nintendo você está procurando.
    </p>

    <button @click="iniciarIdentificacao">
      Começar identificação
    </button>
  </main>
</template>
