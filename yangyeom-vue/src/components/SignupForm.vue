<template>
  <!-- <div class="container">
    <form @submit.prevent="signup">
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
  </div> -->
  <div class="container">
    <div class="d-flex justify-content-center h-100">
      <div class="card">
        <div class="card-header">
          <h3>회원가입</h3>
        </div>
        <form @submit.prevent="signup">
          <div class="card-body">
            <div class="input-group form-group">
              <div class="input-group-prepend">
                <span class="input-group-text"><i class="fas fa-user"></i></span>
              </div>
              <input type="text" id="username"  placeholder="ID" class="form-control" v-model="credentials.username"><br>
            </div>
            <div class="input-group form-group">
              <div class="input-group-prepend">
                <span class="input-group-text"><i class="fas fa-key"></i></span>
              </div>
              <input type="password" id="password" placeholder="password" class="form-control" v-model="credentials.password"><br>
            </div>
            <div class="input-group form-group">
              <div class="input-group-prepend">
                <span class="input-group-text"><i class="fas fa-key"></i></span>
              </div>
              <input type="password" id="password2" placeholder="password" class="form-control" v-model="password2"><br>
            </div>
          </div>
          <div class="card-footer">
            <div class="form-group">
              <input type="submit" value="Sign Up" class="btn float-center login_btn">
            </div>
          </div>
        </form>
      </div>
    </div>
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
      signup() {
        if (this.credentials.password === this.password2) {
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