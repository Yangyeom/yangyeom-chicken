<template>
  <div class="container">
    <form @submit.prevent="signup">
        <h1>Signup</h1>
        <hr>
        <div class="form-group text-center">
          <label for="username">아이디</label>
          <input type="text" id="username" class="form-control" v-model="credentials.username">
        </div>
        <div class="form-group text-center">
          <label for="password">비밀번호</label>
          <input type="password" id="password" class="form-control" v-model="credentials.password">
        </div>
        <div class="form-group text-center">
          <label for="password2">비밀번호 재확인</label>
          <input type="password" id="password2" class="form-control" v-model="password2">
        </div>
      <hr>
      <button class="btn btn-primary" type="submit">회원가입</button>
    </form>
  </div>

</template>

<script>
  export default {
    name: 'SignupForm',
    data() {
      return {
        credentials: {},
        password2: ''
      }
    },
    methods: {
        signup(){
            if(this.credentials.password === this.password2){
              this.password2 = ''
              this.$emit('signup-event', this.credentials)
              this.credentials = {}
            } else {
              this.credentials.password = '',
              this.password2 = ''
            }
        }
    }
  }
</script>

<style>
</style>