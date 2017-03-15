<template>
	<div class="container">
		<h2>Reg</h2>
		<p>
			<label for="username">UserName</label>
			<input type="text" class="ipt" placeholder="请输入用户名" name="username" v-model="username">
		</p>
		<p>
			<label for="username">PassWord</label>
			<input type="text" class="ipt" placeholder="请输入密码" name="password" v-model="password">
		</p>
		<p><button class="btn" @click="loginIn">Login In</button></p>
		<p class="errormsg">{{msg}}</p>
	</div>
</template>

<script type="text/javascript">
	export default{
		name:"login",
		data(){
			return {
				username:'',
				password:'',
				apiUrl:'http://127.0.0.1:5000/reg',
				msg:""
			}
		},
		methods:{
			loginIn(){
				var info = {
					"username": this.username,
					"password": this.password
				}
				var _that = this
				this.$http.post(this.apiUrl, info, {
					headers:{
						'Content-Type': 'application/json; charset=UTF-8'
					}
				}).then((res)=>{
					if(res.body.errcode){
						_that.msg = res.body.msg
					}else{
						_that.$router.push({ path: 'login', query: { users: this.username }})
					}
				},(err)=>{
					console.warn(err.code)
				})

			}
		}
	}
</script>
<style type="text/css">
	.errormsg{
		color:red;
	}
</style>