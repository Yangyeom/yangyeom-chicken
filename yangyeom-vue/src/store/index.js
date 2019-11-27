import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth' // auth 모듈 추가
import VueAwesomeSwiper from 'vue-awesome-swiper'

Vue.use(Vuex)
Vue.use(VueAwesomeSwiper)


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