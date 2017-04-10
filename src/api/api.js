import Vue from 'vue'
import axios from 'axios'

var getAxios = function(){
	return axios;
}

function installAxios(Vue, options) {
	if (installAxios.installed) return

	installAxios.installed = true

	if(!axios){
		console.error("Please install axios")
	}

	/** 组件注入的方式 **/
	Vue.mixin({
		created() {
			return this.$axios = axios;
		}
	})
	// 调用方式直接是  this.$axios -->  返回 axios 插件

	/** or  添加实例的方法**/
	Object.defineProperties(Vue.prototype,{
		$axios:{
			get(){
				return getAxios
			}
		}
	})
	
}

if (typeof window !== 'undefined' && window.Vue) {
	// console.log("axios installed")
	window.Vue.use(installAxios)
}

export default installAxios