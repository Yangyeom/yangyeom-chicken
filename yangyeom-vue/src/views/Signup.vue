<template>
  <div class="signup" style="margin-top:200px">
      <SignupForm @signup-event="signup"/>
  </div>
</template>

<script>
import SignupForm from '@/components/SignupForm.vue'
import axios from 'axios'
import router from '../router'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.headers.common['X-REQUESTED-WITH'] = 'XMLHttpRequest'

export default {
    name: 'Signup',
    components: {
        SignupForm,
    },
    methods: {
        signup(credentials) {
            axios.post('http://127.0.0.1:8000/accounts/signup/', credentials)
                .then(response =>{
                    console.log(response)
                    if (response.status === 201){
                        axios.post('http://127.0.0.1:8000/api-token-auth/', credentials)
                            .then(response2 => {
                                console.log(response2)
                                const token = response2.data.token
                                this.$session.start()
                                this.$session.set('jwt', token)
                                this.$store.dispatch('login', token)
                                router.push('/rating')
                            })
                            .catch(error2 => {
                                console.log(error2)
                            })
                    }
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