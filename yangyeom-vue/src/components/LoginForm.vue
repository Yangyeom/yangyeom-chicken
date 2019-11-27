<template>
  <div class="container">
	<div class="d-flex justify-content-center h-100">
		<div class="card">
			<div class="card-header">
				<h3>로그인</h3>
			</div>
				<form @submit.prevent="login">
			<div class="card-body">
					<div class="input-group form-group">
						<div class="input-group-prepend">
							<span class="input-group-text"><i class="fas fa-user"></i></span>
						</div> 
            <input v-model="credentials.username" placeholder="ID" type="text" id="username"><br>
					</div>
					<div class="input-group form-group">
						<div class="input-group-prepend">
							<span class="input-group-text"><i class="fas fa-key"></i></span>
						</div>
        <input v-model="credentials.password" placeholder="password" type="password" id="password"><br>
					</div>
			</div>
			<div class="card-footer">
          <div class="form-group">
						<input type="submit" value="Login" class="btn float-center login_btn">
					</div>
			</div>
			</form>
		</div>
	</div>
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