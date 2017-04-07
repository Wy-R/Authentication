import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)

const store = new Vuex.Store({
	state: {
		is_login: false,
		current_user: ''
	},
	mutations: {
		loginState: (state, payload) => {
			state.is_login = payload.is_login
		},
		current_userInfo: (state, payload) => {
			state.current_user = payload.current_user
		}
	}
})

export default store