import sqlite3
import json
import socket


def register(userid,password,ismanager):
    # identity_db = 'identity.db'
    # conn = sqlite3.connect(identity_db)
    #
    # cur = conn.cursor()
    # # sql语句
    # sql = "insert into users values (?,?,?)"
    # data = (userid,password,ismanager)
    # # 执行sql语句
    # cur.execute(sql,data)
    # # 提交数据，否则无法同步之数据库
    # conn.commit()
    # # 关闭
    # cur.close()
    # conn.close()
    print("开发中")

def login(client, id,password,identity):

    jdata = [{'request': 'login', 'id': id, 'passwd': password, 'identity': identity}]
    client.send(json.dumps(jdata).encode())
    # 服务器返回登录状态信息
    # '用户未注册或账号错误'
    # '密码错误'
    # '登录成功'
    res = client.recv(1024).decode()
    print(res)
    return res

    # identity_db = 'identity.db'
    # conn = sqlite3.connect(identity_db)
    #
    # cur = conn.cursor()
    # sql = "SELECT count(*) FROM users WHERE userid=? AND password=? AND manager=?"
    # cur.execute(sql,(userid,password,ismanager))
    # res = cur.fetchall()[0][0]
    # conn.commit()
    # # 关闭
    # cur.close()
    # conn.close()


