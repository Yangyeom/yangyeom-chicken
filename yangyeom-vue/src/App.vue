<template>
  <!-- Navigation -->
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark fixed-top" id="mainNav" style="background-color:black">
      <div class="container">
        <router-link to="/" class="navbar-brand js-scroll-trigger">Coke</router-link>
        <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse"
          data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false"
          aria-label="Toggle navigation">
          메뉴
          <i class="fas fa-bars"></i>
        </button>
        <div v-if="!isAuthenticated" class="collapse navbar-collapse" id="navbarResponsive">
              <ul class="navbar-nav text-uppercase ml-auto">
              <li class="nav-item">
                <a><router-link class="nav-link js-scroll-trigger" to="/signup">회원가입</router-link></a>
              </li>
              <li class="nav-item">
                <a><router-link class="nav-link js-scroll-trigger" to="/login">로그인</router-link></a>
              </li>
              </ul>
            </div>
            <div v-else class="collapse navbar-collapse" id="navbarResponsive">
              <ul class="navbar-nav text-uppercase ml-auto">
              <li class="nav-item">
                <a @click.prevent="logout" class="nav-link js-scroll-trigger" href="#contact">로그아웃</a>
              </li>
              <li class="nav-item">
                <a @click.prevent="payment" class="nav-link js-scroll-trigger" href="#contact">결제</a>
              </li>
              <li class="nav-item">
                <a @click.prevent="" class="nav-link js-scroll-trigger" href="#contact">추천 받기</a>
              </li>
              </ul>
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
    components: {

    },
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