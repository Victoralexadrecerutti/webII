import { createMemoryHistory, createRouter } from 'vue-router'

import HelloWorld from './components/HelloWorld.vue'
import Page2 from './components/Page2.vue'
import About from './components/About.vue'

const routes = [
  { path: '/', component: HelloWorld },
  { path: '/page2', component: Page2 },
  { path:'/about', component: About }
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router

// we wan to install:
// npm install vue-router@4
// https://router.vuejs.org/installation