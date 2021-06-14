import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/list',
    name: 'List',
    component: () => import('@/views/List.vue')
  },
  {
    path: '/polar',
    name: 'Polar',
    component: () => import('@/views/Polar.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
