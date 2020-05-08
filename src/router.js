import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Login from './views/Login'
import store from './store'

Vue.use(Router)

const routeGuard = async (to, from, next) => {
  const goTo = `?goTo=${to.fullPath}`

  try {
    if (store.getters.isLoggedIn) {
      next()
    } else {
      next('/login' + goTo)
    }
  } catch (error) {
    console.log(error)
    next('/login')
  }
}

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      component: Home,
      beforeEnter: routeGuard,
      children: [
        {
          path: '',
          name: 'interaction-screen',
          component: () => import('@/components/InteractionScreen')
        },
        {
          path: '/settings',
          name: 'settings',
          component: () => import('@/views/Settings')
        },
        {
          path: '/profile',
          name: 'profile',
          component: () => import('@/views/Profile')
        },
        {
          path: '/about',
          name: 'about-us',
          component: () => import('@/components/About')
        },
        {
          path: '/help',
          name: 'helpline',
          component: () => import('@/components/About')
        },
        {
          path: '/privacy-policy',
          name: 'privacy',
          component: () => import('@/components/PrivacyPolicy')
        },
        {
          path: '/terms',
          name: 'terms',
          component: () => import('@/components/Terms')
        }
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    }
  ]
})
