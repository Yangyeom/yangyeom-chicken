<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <div v-if="!isAuthenticated">
        <router-link to="/signup">회원가입</router-link> |
        <router-link to="/login">로그인</router-link>
      </div>
      <div v-else>
        <a @click.prevent="logout" href="">로그아웃</a> | 
        <a @click.prevent="payment" href="">결제</a> |
        <a href="">영화 추천 받기</a>
      </div>
    </div>
    <router-view/>
  </div>
</template>
<script>
import router from './router'
import axios from 'axios'
export default {
  name: 'App',
  data(){
    return {
      isAuthenticated: this.$session.has('jwt')
    }
  },
  methods: {
    logout(){
      this.$session.destroy()
      this.$store.dispatch('logout')
      router.push('/login')
    },
    payment(){
      axios.get('http://127.0.0.1:8000/payments/pay/')
        .then(response => {
          console.log(response)
          axios.get(response.data)
            .then(response2 => {
              console.log(response2)
            })
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
