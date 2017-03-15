<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Essential Links</h2>
    <h3>当前用户是：{{current_user}}</h3>
    <p  v-show="is_login"><button @click="logout()">Login Out</button></p>
    <p  v-show="!is_login"><router-link :to="{ path: 'login' }">Login</router-link></p>
  </div>
</template>

<script>
export default {
    name: 'hello',
    data () {
        return {
            msg: 'Welcome to Your Vue.js App',
            current_user:'',
            is_login:false
        }
    },
    computed:{
        token(){
            if(this.$cookie.get("access_token")){
                return this.$cookie.get("access_token")
            }else{
                return ''
            }
        }
    },
    created(){
        var _that = this;
        this.$http.get('http://localhost:5000/hello',{
            headers:{
                'Content-Type':'application/json',
                'Authorization': "JWT "+this.token
            }
        }).then((res)=>{
            // console.info(res)
            _that.current_user = res.body
            _that.is_login = true;
        },(err)=>{
            console.log("获取用户信息错误")
            _that.$router.push({ path: 'login'})
        })
        console.info("JWT "+this.token)
    },
    methods:{
        logout(){
            this.current_user = '当前用户未登录'
            this.is_login = false
            this.$cookie.delete('access_token')
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
