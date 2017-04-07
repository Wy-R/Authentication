import Vue from 'vue'
import Router from 'vue-router'
import VueResource from 'vue-resource'
import VueCookie from 'vue-cookie'


// component
import Welcome from '@/components/Welcome'
import Hello from '@/components/Hello'
import Login from '@/components/Login'
import Reg from '@/components/Reg'

// import Axios from 'axios';

Vue.use(Router)
Vue.use(VueResource)
Vue.use(VueCookie)

export default new Router({
    routes: [{
        path: '/',
        name: 'Home',
        component: Welcome
    }, {
        path: '/login',
        name: 'Login',
        component: Login
    }, {
        path: '/hello',
        name: 'Hello',
        component: Hello
    }, {
        path: '/reg',
        name: 'Register',
        component: Reg
    }]
})