<template>
  <div class="hello-page">
    <h1>{{ msg }}</h1>
    <h3>当前用户是：{{current_user}}</h3>
    <mu-raised-button label="LOGIN OUT" v-show="is_login" class="demo-raised-button loginout-btn" primary @click="logout"/>
    <mu-raised-button label="LOGIN IN" v-show="!is_login" class="demo-raised-button login-btn" primary @click="loginIn"/>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'hello',
    data () {
        return {
            msg: 'Welcome to Here',
        }
    },
    computed:{
        token(){
            if(this.$cookie.get("access_token")){
                return this.$cookie.get("access_token")
            }else{
                return ''
            }
        },
        is_login(){
            return this.$store.state.is_login
        },
        current_user(){
            return this.$store.state.current_user
        }
    },
    created(){
        // var _that = this;
        // this.$http.get('http://localhost:5000/hello',{
        //     headers:{
        //         'Content-Type':'application/json',
        //         'Authorization': "JWT "+this.token
        //     }
        // }).then((res)=>{
        //     // console.info(res)
            // this.current_user = res.body
            // // this.is_login = true;
            // this.$store.commit("loginState",{
            //     "is_login": true
            // })
        // },(err)=>{
        //     console.log("获取用户信息错误")
        //     this.$router.push({ path: 'login'})
        // })
        // console.warn(axios)
        axios.get('http://localhost:5000/hello',{
            headers:{
                'Content-Type':'application/json',
                'Authorization': "JWT "+this.token
            }
        })
        .then((res)=>{
            console.info(res)
            this.$store.commit("current_userInfo",{
                'current_user': res.data
            })
            this.$store.commit("loginState",{
                "is_login": true
            })
        })
        .catch((err)=>{
            this.$router.push({ path: 'login'})
        })
        console.info("JWT "+this.token)
    },
    methods:{
        logout(){
            // this.current_user = '当前用户未登录'
            // this.is_login = false
            // this.$cookie.delete('access_token')
            this.$store.commit("current_userInfo",{
                'current_user': '当前未登录'
            })
            this.$store.commit("loginState",{
                'is_login':false
            })
            this.$cookie.delete('access_token')
        },
        loginIn(){
            console.log("获取用户信息错误")
            this.$router.push({ path: 'login'})
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
@import "../assets/common.scss";
.hello-page{
    @include add-padding(50px,10px,10px,10px);
    h1{
        color:$lightBlue;
    }
    h3{
        color:$lightBlue;
        @include add-padding(0px,10px,10px,30px)
    }
    p{
        text-align:left;
        @include add-padding(0px,10px,10px,30px);
        font-size:20px;
    }
    .loginout-btn{
        background-color:$lightPink
    }
}
</style>
