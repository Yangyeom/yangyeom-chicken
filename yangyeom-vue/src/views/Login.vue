<template>
  <div class="row d-flex justify-content-center w-100 p-3" style="height:500px">
    <div class="login" style="margin-top:200px">
      <LoginForm @login-event="login" />
    </div>
  </div>
</template>

<script>
  import LoginForm from '@/components/LoginForm.vue'
  import axios from 'axios'
  import router from '../router'

  export default {
    name: 'Login',
    components: {
      LoginForm,
    },
    methods: {
      login(credentials) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', credentials)
          .then(response => {
            console.log(response)

            const token = response.data.token
            this.$session.start()
            this.$session.set('jwt', token)
            // vuex actions 호출 -> dispatch
            this.$store.dispatch('login', token)
            router.push('/')
          })
          .catch(error => {
            console.log(error)
          })
      }
    }
  }
</script>

<style>

</style>