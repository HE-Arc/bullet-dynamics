import Vue from 'vue'
import VueRouter from 'vue-router'
import Simulator from '../views/Simulator.vue'
import Configuration from '../views/Configuration.vue'
import Login from '../views/Login.vue'
import Logout from '../views/Logout.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Configuration',
    component: Configuration,
    meta: {
      requiresLogin: true
    },    
  },
  {
    path: '/simulator',
    name: 'Simulator',
    component: Simulator,
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/logout',
    name: 'Logout',
    component: Logout
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
