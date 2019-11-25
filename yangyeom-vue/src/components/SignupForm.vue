<template>
  <div id="app">
  <div class="container">
    <form>
      <div class="row">
        <div class="col-xs-12 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3">
          <!-- Exercise 1 -->
          <!-- Create a Signup Form where you retrieve the following Information -->
          <!-- Full Name (First Name + Last Name) -->
          <!-- Mail -->
          <!-- Password -->
          <!-- Store Data? Yes/No -->
          <h1>Signup</h1>
          <hr>
          <div class="form-group">
            <label for="firstName">아이디</label>
            <input type="text" id="firstName" class="form-control" v-model="userData.firstName">
          </div>
          <div class="form-group">
            <label for="password">비밀번호</label>
            <input type="password" id="password" class="form-control" v-model="userData.password">
            <p>
              {{ userData.password }}
            </p>
          </div>
          <div class="form-group">
            <label for="password">비밀번호 재확인</label>
            <input type="password" id="password" class="form-control" v-model="userData.password">
            <p>
              {{ userData.password }}
            </p>
          </div>
        </div>
      </div>
      <hr>
      <div class="row">
        <div class="col-xs-12 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3">
          <button class="btn btn-primary" @click.prevent="submitted">Submit!
          </button>
        </div>
      </div>
    </form>
  </div>
</div>

</template>

<script>
export default {
    name: 'SignupForm',
    data(){
        return {
            userData: {
                firstName: '',
                lastName: '',
                email: '',
                password: ''
            },
            storeData: 'Yes',
            isSubmitted: false
        }
    },
    methods: {
    submitted() {
      this.isSubmitted = true;
    }
  }
}
</script>

<style>

</style>