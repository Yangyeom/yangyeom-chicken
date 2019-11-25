<template>
  <div class="signup">
      <h2>회원가입</h2>
      <SignupForm @signup-event="signup"/>
  </div>
</template>

<script>
import SignupForm from '@/components/SignupForm.vue'
import axios from 'axios'
// import router from '../router'

export default {
    name: 'Signup',
    components: {
        SignupForm,
    },
    methods: {
        signup(credentials) {
            axios.post('http://127.0.0.1:8000/api-token-auth/', credentials)
                .then(response =>{
                    console.log(response)

                    // const token = response.data.token
                    // this.$session.start()
                    // this.$session.set('jwt', token)
                    // // vuex actions 호출 -> dispatch
                    // this.$store.dispatch('login', token)
                    // router.push('/')
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