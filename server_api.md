服务器api 

​	使用json传输, 命令种类使用request标识

​	1.登录：login

​	例如：

```python
id='2020211754'
passwd = 'zy123456'
identity='users'
jdata = [{'request':'login', 'id':id, 'passwd':passwd, 'identity':identity}]
client.send(json.dumps(jdata).encode())
# 服务器返回登录状态信息
	# '用户未注册或账号错误'
	# '密码错误'
	# '登录成功'
res = client.recv(1024).decode
```

​		