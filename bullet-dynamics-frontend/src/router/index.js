import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Simulator from '../views/Simulator.vue'
import Login from '../views/Login.vue'
import Logout from '../views/Logout.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: About,
  },
  {
    path: '/simulator',
    name: 'Simulator',
    //
    component: Simulator,
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/login',
    name: 'Login',
    //
    component: Login
  },
  {
    path: '/logout',
    name: 'Logout',
    //
    component: Logout
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
