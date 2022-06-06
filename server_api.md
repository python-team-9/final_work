服务器api 

​	使用json传输, 命令种类使用request标识

​	所有服务端返回的json数组第一个将含有 request_return 信息来标识这是对哪个请求的数据返回，

​	方便客户端多线程处理返回数据。一些没有请求而由服务器单方面发送的信息将为 'auto_msg' 信息，如同一用户在

​	别处登录后服务器给现在登录的客户端发送的 '您已在别处登录' 消息

​	

​	* 接收时不要使用下边例子的 client.recv(), 可以使用我写的 j_res = json.loads(m_recv(client)).

​	1.登录：login

​	例如：

```python
id='2020211754'
passwd = 'zy123456'
identity='users'
jdata = [{'request':'login', 'id':id, 'passwd':passwd, 'identity':identity}]
client.send(json.dumps(jdata).encode())
# 服务器返回登录状态json信息
	# '用户未注册或账号错误'
	# '密码错误'
	# '登录成功'
	# '您已登录'
# 其中您已登录状态会自动关闭上一个连接的客户端，留下最新建立连接的客户端
jres = json.loads(client.recv(1024).decode)
print(res)
# 控制台打印：[{'request_return': 'login', 'login_state': '登录成功'}]

# 同一用户多处登录，服务器给之前登录的客户端发送json消息[{'auto_msg':'您已在别处登录'}]并关闭连接
# 建议接收到[{'auto_msg':'您已在别处登录'}]之后客户端不再进行和服务器的通信而直接退出登录，不用发送quit请求
```

​	2.退出：quit

​	例如：

```python
# 客户端主动退出时向服务端发送quit请求，服务端正常关闭连接。
# 不发也行其实，不过走的是异常处理的路
jdata = [{'request':'quit'}]
client.send(json.dumps(jdata).encode())
```

​	3.获取职业信息：getJobDetail

​	例如：

```python
begin = 0
# 这个命令每次最多*多*返回20个职业详情的json数组，以及本次返回的职业详情具体数量
# 考虑到职业详情有可能更新，客户端刷新时不能只新返回数据而不管已经返回的数据
# begin代表已经返回的数据数量，这个命令是按数据库默认顺序返回数据的，每次调用返回前begin个之前已经返回过的数据
# 供客户端刷新，另外多返回最多20个新数据
jdata = [{'request':'getJobDetail','begin':begin}]
client.send(json.dumps(jdata).encode())
jres = json.loads(client.recv().decode())
begin += jres[0]['num']
for row in ''' jres剩余内容''':
    # 处理数据
# jres[0]:{'request_return':'getJobDetail', 'num':一个数字}
# 客户端将接受服务端信息的处理写到一个单独线程循环时，可根据每次循环接受的信息的'request_return'或'auto_msg'
# 进入相应的处理函数,这可以避免客户端被某一耗时长的请求阻塞，或用不正确的函数处理了返回的数据
# 例如
while True:
    res = json.loads(client.recv(4096).decode())
    if res[0].get('request_return') is None:
        if res[0].get('auto_msg') == '您已在别处登录'：
        	# do sth
    elif res[0].get('request_return') == 'login':
        # do sth
    ...
```

 4. 直接执行SQL：getJobDetailSQL

    例如

    ```python
    jdata = [{'request':'getJobDetailSQL', 'sql':'你的sql'}]
    client.send(json.dumps(jdata).encode())
    jres = json.loads(m_recv(client))
    # jres[0]:{'request_return':'getJobDetail', 'num':一个数字}
    # 之后跟num个数据
    ```





 5. 直接执行SQL：getAccDetailSQL

    例如

    ```python
    jdata = [{'request':'getAccDetailSQL', 'sql':'你的sql'}]
    client.send(json.dumps(jdata).encode())
    jres = json.loads(m_recv(client))
    # jres[0]:{'request_return':'getAccDetail', 'num':一个数字}
    # 之后跟num个数据
    ```

    