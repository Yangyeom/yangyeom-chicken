import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueSession from 'vue-session'
import store from './store'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

Vue.use(VueSession)
Vue.config.productionTip = false
Vue.prototype.$EventBus = new Vue()

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
