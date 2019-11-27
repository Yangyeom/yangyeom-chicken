<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup"
        aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div>
          <router-link to="/" class="nav-item">Home</router-link> |
        </div>
        <div v-if="!isAuthenticated">
          <router-link to="/signup" class="nav-item">회원가입</router-link> |
          <router-link to="/login" class="nav-item">로그인</router-link>
        </div>
        <div v-else>
          <a @click.prevent="logout" href="" class="nav-item"> 로그아웃</a> |
          <a @click.prevent="payment" href="" class="nav-item ">결제</a> |
          <a @click.prevent="payment" href="" class="nav-item ">추천 받기</a> |
        </div>
      </div>
    </nav>
    <router-view />
  </div>
</template>
<script>
  import router from './router'
  import axios from 'axios'
  import {
    mapGetters
  } from 'vuex'
  export default {
    name: 'App',
    computed: {
      ...mapGetters([
        'options',
        'user'
      ])
    },
    data() {
      return {
        isAuthenticated: this.$session.has('jwt')
      }
    },
    methods: {
      logout() {
        this.$session.destroy()
        this.$store.dispatch('logout')
        router.push('/login')
      },
      payment() {
        axios.get(`http://127.0.0.1:8000/payments/pay/${this.user}/`)
          .then(response => {
            let win = window.open(response.data['next_redirect_pc_url'], '_blank');
            win.focus();
          })
          .catch(error => {
            console.log(error)
          })
      }
    },
    updated() {
      this.isAuthenticated = this.$session.has('jwt')
    }
  }
</script>
<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  #nav {
    padding: 30px;
  }

  #nav a {
    font-weight: bold;
    color: #2c3e50;
  }

  #nav a.router-link-exact-active {
    color: #42b983;
  }
</style>