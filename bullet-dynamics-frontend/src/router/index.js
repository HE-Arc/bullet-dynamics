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
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: About
  },
  {
    path: '/simulator',
    name: 'Simulator',
    //
    component: Simulator
  },
  {
    path: '/login',
    name: 'Login',
    //
    component: Login
  },
  {
    path: '/lougout',
    name: 'Lougout',
    //
    component: Logout
  },
]

const router = new VueRouter({
  routes
})

export default router
