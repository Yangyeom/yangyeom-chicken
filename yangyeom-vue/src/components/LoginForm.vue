<template>
  <div class="container">
    <!-- 
      form에 이벤트 리스너 달아서,
      1) 사용자 입력 값 출력
      2) /api-token-auth/로 요청 보내서 토큰 값 출력
    -->
    <form @submit.prevent="login">
        <label for="username">username: </label>
        <input v-model="credentials.username" type="text" id="username"><br>
        <label for="password">password: </label>
        <input v-model="credentials.password" type="password" id="password"><br>
        <button class="btn btn-primary" type="submit">로그인</button>
    </form>

  </div>
</template>

<script>
export default {
    name: 'LoginForm',
    data(){
        return {
            credentials: {}
        }
    },
    methods:{
        login(){
            this.$emit('login-event', this.credentials)
            this.credentials = {}
        }
    }
}
</script>

<style>

</style>