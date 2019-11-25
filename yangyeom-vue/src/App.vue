<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <div v-if="!isAuthenticated">
        <router-link to="/login">Login</router-link>
      </div>
      <div v-else>
        <a @click.prevent="logout" href="">Logout</a>
      </div>
    </div>
    <router-view/>
  </div>
</template>
<script>
import router from './router'
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
