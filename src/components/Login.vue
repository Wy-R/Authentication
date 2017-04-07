<template>
	<div class="login-page">
		<mu-text-field label="用户名" hintText="请输入用户名" type="text" labelFloat v-model="username"/><br/>
		<mu-text-field label="密码" hintText="请输入密码" type="password" labelFloat v-model="password"/><br/>
		<p class="err-msg">{{msg}}</p>
		<mu-raised-button label="LOGIN IN" class="demo-raised-button login-btn" primary @click="loginIn"/>
	</div>
	
</template>

<script type="text/javascript">	
	import axios from 'axios';
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
				// this.$http.post(this.apiUrl, info, {
				// 	headers:{
				// 		'Content-Type': 'application/json; charset=UTF-8'
				// 	}
				// }).then((res)=>{
				// 	console.info(res)
				// 	if(res.body.access_token==undefined){
				// 		this.msg = "获取用户信息失败，请重新登录"
				// 	}else{
				// 		_that.$cookie.set('access_token', res.body.access_token);
				// 		_that.$router.push({ path: 'hello'})
				// 	}
					
				// },(err)=>{
				// 	this.msg = "用户名或者密码错误"
				// })
				axios.post(this.apiUrl, info,{
					headers:{
						'Content-Type': 'application/json; charset=UTF-8'
					}
				})
				.then((res)=>{
					console.log("ok",res)
					if(res.data.errcode){
						this.msg = '用户名或者密码错误'
						return false;
					}
					/**token 存储到 cookie 中**/
					this.$cookie.set('access_token', res.data.access_token);
					/** 全局更新当前用户名  */
					this.$store.commit('loginState',{
						'current_user': this.username
					})
					this.$router.push({ path: 'hello'})
				})
				.catch(function (error) {
				    // console.log(error);
				    this.msg = '用户名或者密码错误'
				});
			}
		}
	}
</script>
<style lang="scss">
@import "../assets/common.scss";
.login-page{
	@include add-padding(30px,0px,30px,0px);

	.login-btn{
		@include add-margin(30px,0px,30px,0px)
	}
	.err-msg{
		color:$red;
	}
}
</style>