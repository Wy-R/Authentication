# Authentication

> An example of user authentication with Vue + Flask_JWT


#### 主要实现

注册成功之后跳转到登录页面登录成功之后，flask-jwt鉴权成功返回一个``access_token``，然后跳转到``/hello`` 的页面，上面会显示当前登录信息

#### 关于 Vuejs 登录注册的问题【占位】

前端用 **Vue-resource** 实现的话

```
	this.$http.post('/someUrl', [body], [options]).then(successCallback, errorCallback);
``` 

这是标准的调用格式

即 部分代码如下：

```
	this.$http.post(apiUrl, data, 
	{
		headers:{
			'Content-Type': 'application/json; charset=UTF-8'
		}
	})
	.then((res)=>{
		//do something..
	},(err)=>{
		// error code here...
	})
```
新demo使用 **Axios** 来实现的

因为这个是个插件，所以在文件中不能全局使用 ``use`` 引入，
目前的做法是 **在每个需要使用的文件中import 该插件**，雨鞋麻烦

还有一种方式是用 webpack 提供的这种方式来在全局使用，也不方便

```
	new webpack.ProvidePlugin({
		axios: "axios
	})
```

【更新下】

用 Vue.use(plugin) 的方式来引入 **axios**

**方式1 -->**  组件注入的形式

```
	Vue.mixin({
		created() {
			return this.$axios = axios;
		}
	})
```
**方式2 -->** 针对 Vue 的prototype 的方式，通过 defineProperties 创建实例方法

```
	Object.defineProperties(Vue.prototype,{
		$axios:{
			get(){
				return getAxios
			}
		}
	})
```

这两种方式都可以通过 **Vue.use** 的方式在所有文件中直接引用 axios

 
后端用 **Flask** 实现的时候，因为 **Flask** 自带有 ``request.get_json()`` 的方法，那么在前端调用接口的时候传过去的必须是 json 的数据。所以必须是在【options】这个属性里面需要带上 Content-Type 这个属性

部分的 **python** 代码如下：

```
	@app.route('/login', methods=['POST'])
	def login_in():
		username  = request.get_json()['username']
		password = request.get_json()['password']
```

接收完数据之后，查询数据库，如果用户名已经存在，则返回 errcode，然后


#### 样式

上次写的没有样式，so...这次加点样式，demo样式是基于material desgin 的[MuseUI](https://museui.github.io)

样式使用 [SCSS](http://sass-lang.com/) 编写

在 **Vue** 中引入 SCSS 文件类似这样：

```
<style lang="scss">
@import "../assets/common.scss";
.login-page{
	@include add-padding(30px,0px,30px,0px);

	.login-btn{
		@include add-margin(30px,0px,30px,0px)
	}
}
</style>
``` 

#### Vue 

##### 动态修改头部标题 
在组件里面监听路由的变化，实现头部title跟随路由变化

```
watch:{
       "$route"(){
           this.Title = this.$route.name
       }
   }
```

监听 **route** 的变化，然后每次变化之后修改 **Title** 的值

##### 动态修改标签栏

```
router.beforeEach((to, from, next) => {
	/**
	 * to -> 跳转的路由的信息  name meta path ...etc
	 * from -> 当前路由的信息
	 */
	document.title = to.name || document.title
})
```

 

在路由变化之前修改下导航栏的文字

#### Webpack 配置

用 ``vue-cli`` 生成的文件之后，``cnpm run build`` 生成的 **dist** 文件发现每次 **index.html** 文件引入的文件是``/static/js/app.bf48482c0e962b5ec97b.js`` 这种路径的，这个路径是错的，每次都需要手动修改把这个**/** 去掉

看了下 配置 build.js 中build 的配置是：

```
rm(path.join(config.build.assetsRoot, config.build.assetsSubDirectory)
```

所以找到  **config/index.js** 中的文件，里面大致分为**build** 之后的配置和 **dev** 环境的配置。类似

```
 build: {
        env: require('./prod.env'),
        index: path.resolve(__dirname, '../dist/index.html'),
        assetsRoot: path.resolve(__dirname, '../dist'),
        assetsSubDirectory: 'static',
        assetsPublicPath: '/',
    },
    dev: {
	    //...
    }
```

最后发现其实它将**publicPath** 也加进去了，我们只需要将**publicPath** 置空即可




