import { createRouter, createWebHistory } from 'vue-router'

import Inicio from '../pages/Inicio.vue'
import Identificar from '../pages/Identificar.vue'
import Catalogo from '../pages/Catalogo.vue'
import Sobre from '../pages/Sobre.vue'
import Contato from '../pages/Contato.vue'

const routes = [
  {
    path: '/',
    component: Inicio
  },
  {
    path: '/identificar',
    component: Identificar
  },
  {
    path: '/catalogo',
    component: Catalogo
  },
  {
    path: '/sobre',
    component: Sobre
  },
  {
    path: '/contato',
    component: Contato
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router