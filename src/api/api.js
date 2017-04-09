import Vue from 'vue'
import axios from 'axios'

function installAxios(Vue, options) {
	if (installAxios.installed) return

	installAxios.installed = true

	Vue.mixin({
		created() {
			return this.$axios = axios;
		}
	})
}

if (typeof window !== 'undefined' && window.Vue) {
	// console.log("axios installed")
	window.Vue.use(installAxios)
}

export default installAxios