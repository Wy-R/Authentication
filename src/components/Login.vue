<template>
	<div class="container">
		<h2>Login</h2>
		<p>
			<label for="username">UserName</label>
			<input type="text" class="ipt" placeholder="请输入用户名" name="username" v-model="username">
		</p>
		<p>
			<label for="username">PassWord</label>
			<input type="text" class="ipt" placeholder="请输入密码" name="password" v-model="password">
		</p>
		<p class="msg">{{msg}}</p>
		<p><button class="btn" @click="loginIn">Login In</button></p>
	</div>
	
</template>

<script type="text/javascript">
	export default{
		name:"login",
		data(){
			return {
				username:this.$route.query.users,
				password:'',
				apiUrl:'http://127.0.0.1:5000/auth',
				msg:""
			}
		},
		methods:{
			loginIn(){
				var info = {
					"username": this.username,
					"password": this.password
				}
				var _that = this;
				this.$http.post(this.apiUrl, info, {
					headers:{
						'Content-Type': 'application/json; charset=UTF-8'
					}
				}).then((res)=>{
					console.info(res)
					if(res.body.access_token==undefined){
						this.msg = "获取用户信息失败，请重新登录"
					}else{
						_that.$cookie.set('access_token', res.body.access_token);
						_that.$router.push({ path: 'hello'})
					}
					
				},(err)=>{
					this.msg = "用户名或者密码错误"
				})
			}
		}

	}
</script>
<style type="text/css">
	.msg{
		color:red;
	}
</style>