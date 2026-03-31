import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('../components/Index.vue')
    },
    {
      
      name: 'BookDetails',
      path: '/BookDetails',
      component: () => import('../components/BookDetails.vue')
    },
    {
      path: '/BookPanel',
      name: 'BookPanel',
      component: () => import('../components/BookPanel.vue')
    },
    {
      
      name: 'UpsertBook',
      path: '/upsertBook',
      component: () => import('../components/UpsertForm.vue')
    },

  ]
})

export default router
