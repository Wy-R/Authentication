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
后端用 **Flask** 实现的时候，因为 **Flask** 自带有 ``request.get_json()`` 的方法，那么在前端调用接口的时候传过去的必须是 json 的数据。所以必须是在【options】这个属性里面需要带上 Content-Type 这个属性

部分的 **python** 代码如下：

```
	@app.route('/login', methods=['POST'])
	def login_in():
		username  = request.get_json()['username]
		password = request.get_json()['password']
```

类似这样接收数据【未总结完】




