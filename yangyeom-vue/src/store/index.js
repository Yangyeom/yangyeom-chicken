import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth' // auth 모듈 추가
import VueGlide from 'vue-glide-js'
import 'vue-glide-js/dist/vue-glide.css'

Vue.use(Vuex)
Vue.use(VueGlide)

export default new Vuex.Store({
  // state: {
  // },
  // mutations: {
  // },
  // actions: {
  // },
  modules: {
    auth // 모듈 추가
  }
})