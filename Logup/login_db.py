import sqlite3
import json
import socket

from TCPmodule import m_recv


def register(client, id, password, name, identity):
    jdata = [{'request': 'register', 'id': id, 'passwd': password, 'identity': identity, 'name': name}]
    client.send(json.dumps(jdata).encode())
    j_res = json.loads(m_recv(client))
    print(j_res)
    if j_res[0]['request_return'] == 'register':
        return j_res[0]['register_state']
    else:
        print('服务器返回数据出错！')
        return 'error'

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


    # sql = "select * from {} where id=\'{}\';".format(identity, id)
    # jdata = [{'request': 'getAccDetailSQL', 'sql': sql}]
    # client.send(json.dumps(jdata).encode())
    # jres = json.loads(m_recv(client))
    # print("jres[0]['num']", jres[0]['num'])
    # num = jres[0]['num']
    # if num > 0:
    #     print("该账号已存在")
    #     return '该账号已存在'
    # else:
    #     sql2 = "INSERT INTO {} VALUES(\'{}\',\'{}\',\'{}\');".format(identity, id, password, name)
    #     print("注册",sql2)
    #     jdata = [{'request': 'getAccDetailSQL', 'sql': sql2}]
    #     client.send(json.dumps(jdata).encode())
    #     jres = json.loads(m_recv(client))
    #     print("jres[0]['num']", jres[0]['num'])
    #     num = jres[0]['num']
    #     return '注册成功！'

    # sql2 = "insert into account.users values (\'{}\',\'{}\',\'{}\')".format(id, password, name)
    # print(sql)
    # jdata = [{'request': 'getJobDetailSQL', 'sql': sql2}]
    # client.send(json.dumps(jdata).encode())
    # jres = json.loads(m_recv(client))
    # res = jres[0]
    # # res = client.recv(1024).decode()
    # print(res)
    # if res['request_return'] == 'login':
    #     return res['login_state']
    # else:
    #     print('服务器返回数据出错！')
    #     return 'error'
    print("开发中")

def login(client, id, password, identity):

    jdata = [{'request': 'login', 'id': id, 'passwd': password, 'identity': identity}]
    client.send(json.dumps(jdata).encode())
    # 服务器返回登录状态信息
    # '用户未注册或账号错误'
    # '密码错误'
    # '登录成功'
    j_res = json.loads(m_recv(client))
    print('登录结果:j_res', j_res)
    if j_res[0]['login_state'] == '用户未注册或账号错误':
        info = []
        res = [j_res[0]['login_state'], info]
        print(res)
        if j_res[0]['request_return'] == 'login':
            return res
        else:
            print('服务器返回数据出错！')
            return 'error'

    elif j_res[0]['login_state'] == '密码错误':
        info = []
        res = [j_res[0]['login_state'], info]
        print(res)
        if j_res[0]['request_return'] == 'login':
            return res
        else:
            print('服务器返回数据出错！')
            return 'error'

    else:
        info = []
        info.append(j_res[1]['id'])
        info.append(j_res[1]['password'])
        info.append(j_res[1]['name'])
        res = [j_res[0]['login_state'], info]
        # res = client.recv(1024).decode()
        print(res)
        if j_res[0]['request_return'] == 'login':
            return res
        else:
            print('服务器返回数据出错！')
            return 'error'

    # sql = "select * from {} where id=\'{}\' and password=\'{}\';".format(identity, id, password)
    # jdata = [{'request': 'getAccDetailSQL', 'sql': sql}]
    # client.send(json.dumps(jdata).encode())
    # jres = json.loads(m_recv(client))
    # print("jres[0]['num']", jres[0]['num'])
    # num = jres[0]['num']
    # if num > 0:
    #     data = []
    #     data.append(jres[1]['id'])
    #     data.append(jres[1]['password'])
    #     data.append(jres[1]['name'])
    #     print("data", data)
    #     datas = ['登录成功',data]
    #     return datas
    # else:
    #     datas = ['用户未注册或账号错误']
    #     return datas


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


