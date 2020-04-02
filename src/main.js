import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
import vuetify from './plugins/vuetify'
import helpers from './plugins/helpers'
import Notifications from 'vue-notification'

Vue.config.productionTip = false
Vue.prototype.$appName = 'Claire AI'
const $eventBus = new Vue()
Vue.prototype.$eventBus = $eventBus
Vue.use(Notifications)

const plugin = {
  install () {
    Vue.prototype.$helpers = helpers
  }
}
Vue.use(plugin)

const vm = new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')

export { vm }
