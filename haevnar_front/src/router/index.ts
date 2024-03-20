import { createRouter, createWebHistory } from 'vue-router'
import WelcomeView from '@/views/WelcomeView.vue'
import AlliancesView from '@/views/AlliancesView.vue'
import EventsView from '@/views/EventsView.vue'
import RegistrationAllianceView from '@/views/RegistrationAllianceView.vue'
import AdminView from '@/views/AdminView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: WelcomeView
    },
    {
      path: '/alliances',
      name: 'alliances',
      component: AlliancesView
    },
    {
      path: '/events',
      name: 'events',
      component: EventsView
    },
    {
      path: '/registration',
      name: 'registration',
      component: RegistrationAllianceView
    },
    {
      path: '/admin',
      name: 'admin',
      component: AdminView
    },
  ]
})

export default router
