import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueSession from 'vue-session'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

Vue.use(VueSession)
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
