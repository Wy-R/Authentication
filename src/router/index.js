import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import Login from '@/components/Login'
import Reg from '@/components/Reg'
import VueResource from 'vue-resource'
import VueCookie from 'vue-cookie'



Vue.use(Router)
Vue.use(VueResource)
Vue.use(VueCookie)


export default new Router({
    routes: [{
        path: '/',
        name: 'reg',
        component: Reg
    }, {
        path: '/login',
        name: 'login',
        component: Login
    }, {
        path: '/hello',
        name: 'hello',
        component: Hello
    }, {
        path: '/reg',
        name: 'reg',
        component: Reg
    }]
})