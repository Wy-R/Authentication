import Vue from 'vue'
import {
	install
} from './api.js'

console.log("install", install)

var axios = {}

// export default class axios {
// 	// static install: () => void;
// }

function init() {
	process.env.NODE_ENV !== 'production' && assert(
		install.installed,
		`Vue.use()...something`
	)
}

if (typeof window !== 'undefined' && window.vue) {
	window.Vue.use(axios)
}

// export default Axios