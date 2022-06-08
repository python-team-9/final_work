import socket
import pymysql
import json
import threading
from concurrent.futures import ThreadPoolExecutor
from dbutils.pooled_db import PooledDB
dblogin_config = {
    'host': '172.21.196.42',
    'port': 3306,
    'user': 'root',
    'passwd': 'Aa123456',
    'db': 'account',
    'charset': 'utf8',
    'maxconnections': 0,
    'mincached': 20,
    'maxcached': 0,
    'maxusage': None,
    'blocking': True
}

dbjobdetail_config = {
    'host': '172.21.196.42',
    'port': 3306,
    'user': 'root',
    'passwd': 'Aa123456',
    'db': 'jobOfferinformation',
    'charset': 'utf8',
    'maxconnections': 0,
    'mincached': 20,
    'maxcached': 0,
    'maxusage': None,
    'blocking': True
}

login_account = {}

class Command:
    _test = 'test'
    _quit = 'quit'
    _login = 'login'
    _register = 'register'
    _getJobDetail = 'getJobDetail'
    _getJobDetailSQL = 'getJobDetailSQL'
    _getAccDetailSQL = 'getAccDetailSQL'
    _getApplicant = 'getApplicant'
    _nextc = '下一个实现的命令'
    # 连接池
    jobDetail_pool = PooledDB(pymysql, **dbjobdetail_config)
    login_pool = PooledDB(pymysql, **dblogin_config)

    def __init__(self):
        pass

    @staticmethod
    def login(userid, passwd, identity, client):
        print('into login')
        return_num = 0
        conn = Command.login_pool.connection()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = 'select * from ' + identity + ' where id = %s'
        num = cursor.execute(sql,  userid)
        res_return = [{'request_return':'login', 'login_state':''}]
        print(num)
        if num == 0:
            print('wrong2')
            res_return[0]['login_state'] = '用户未注册或账号错误'
            jdata = json.dumps(res_return) + 'E'
            client.send(jdata.encode())
            return_num = 2

        res = cursor.fetchall()
        print(res)
        if res[0]['password'] != passwd:
            print('wrong1')
            res_return[0]['login_state'] = '密码错误'
            jdata = json.dumps(res_return) + 'E'
            client.send(jdata.encode())
            return_num = 1

        print('success', userid)
        t_is_login = login_account.get(userid)
        print('can you reach here')
        if t_is_login is not None:
            res_return[0]['login_state'] = '您已登录'
            res_return.append(res[0])
            jdata = json.dumps(res_return) + 'E'
            client.send(jdata.encode())
            content = [{'auto_msg':'您已在别处登录'}]
            jdata = json.dumps(content) + 'E'
            t_is_login.send(jdata.encode())
            t_is_login.close()
            login_account[userid] = client
        else:
            login_account[userid] = client
            res_return[0]['login_state'] = '登录成功'
            res_return.append(res[0])
            print(res)
            jdata = json.dumps(res_return)
            jdata += 'E'
            client.send(jdata.encode())

        conn.close()
        return return_num

    @staticmethod
    def register(client, id, pwd, name, identity):
        sql = 'select * from {} where id = {}'.format(identity, id)
        conn = Command.login_pool.connection()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        num = cursor.execute(sql)
        res_return = [{'request_return':'register', 'register_state':''}]
        print('in register')
        if num > 0:
            res_return[0]['register_state'] = '此账号已注册'
            jdata = json.dumps(res_return) + 'E'
            client.send(jdata.encode())
        else:
            sql = 'insert into {} values(%s, %s, %s)'.format(identity)
            cursor.execute(sql, (id, pwd, name))
            conn.commit()
            res_return[0]['register_state'] = '注册成功'
            jdata = json.dumps(res_return) + 'E'
            client.send(jdata.encode())

        cursor.close()
        conn.close()


    @staticmethod
    def get_job_detail(begin, client, cursor):
        print('into job', begin)
        max_num = 20 + begin
        sql = 'select * from jobOfferDetail limit %s'
        num = cursor.execute(sql, max_num)
        res = [{'num': num, 'request_return':'getJobDetail', 'err':''}]
        res.extend(cursor.fetchall())
        jdata = json.dumps(res) + 'E'
        client.send(jdata.encode())

    @staticmethod
    def get_job_detail_sql(sql, client, identity):
        print('job sql')
        conn = Command.jobDetail_pool.connection()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        num = cursor.execute(sql)
        op = sql.split(' ', 1)
        print(op[0])
        if op[0].lower() != 'select':
            conn.commit()

        cursor.close()
        conn.close()
        res = [{'num':num, 'request_return': 'getJobDetailSQL'}]
        # 权限控制暂时搁置

        res.extend(cursor.fetchall())
        print(res)
        jdata = json.dumps(res) + 'E'
        client.send(jdata.encode())

    @staticmethod
    def get_account_detail_sql(sql, client):
        print('account')
        conn = Command.login_pool.connection()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        num = cursor.execute(sql)
        op = sql.split(' ', 1)
        print(op[0])
        if op[0].lower() != 'select':
            conn.commit()

        cursor.close()
        conn.close()
        res = [{'num':num, 'request_return': 'getAccDetailSQL'}]
        res.extend(cursor.fetchall())
        jdata = json.dumps(res) + 'E'
        client.send(jdata.encode())

    @staticmethod
    def get_applicant(client, identity, company):
        print('applicant')
        sql = 'SELECT id, name, jobName, jobOfferid FROM ' \
              '(jobOfferinformation.jobOfferDetail natural join jobOfferinformation.resume natural join account.users )' \
              '  where jobCompany=%s'

        conn = Command.jobDetail_pool.connection()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        num = cursor.execute(sql, company)

        res_return = [{'request_return':'getApplicant', 'num':num}]
        res_return.extend(cursor.fetchall())
        jdata = json.dumps(res_return) + 'E'
        client.send(jdata.encode())




def server_fun(client):
    print('new client conn')
    is_login = False
    self_id = ''
    self_identity = ''
    while True:
        try:
            print('recv')
            msg = client.recv(1024)
            print('recv com', msg.decode())
            j_data = json.loads(msg)
            request = j_data[0]['request']
            print(j_data)

            if request == Command._test:
                content = '成功'
                client.send(content.encode())

            elif request == Command._quit:
                client.close()
                return

            elif request == Command._login:
                print('login')
                self_id = j_data[0]['id']
                self_identity = j_data[0]['identity']
                res = Command.login(j_data[0]['id'], j_data[0]['passwd'], j_data[0]['identity'], client)
                print(res)
                if res == 0:
                    is_login = True

            elif request == Command._register:
                print('register')
                Command.register(client, j_data[0]['id'], j_data[0]['passwd'], j_data[0]['name'], j_data[0]['identity'])

            elif request == Command._getJobDetail:
                print('getjob')
                if is_login:
                    print('jobjob')
                    Command.get_job_detail(j_data[0]['begin'], client)
                else:
                    print('unlogin')
                    content = [{'auto_message':'您还未登录'}]
                    client.send(json.dumps(content).encode())

            elif request == Command._getJobDetailSQL:
                print('gjs')
                if is_login:
                    Command.get_job_detail_sql(j_data[0]['sql'], client, self_identity)
                else:
                    print('unlogin')
                    content = [{'auto_message':'您还未登录'}]
                    client.send(json.dumps(content).encode())

            elif request == Command._getAccDetailSQL:
                print('ga')
                if is_login:
                    Command.get_account_detail_sql(j_data[0]['sql'], client)
                else:
                    print('unlogin')
                    content = [{'auto_message':'您还未登录'}]
                    client.send(json.dumps(content).encode())

            elif request == Command._getApplicant:
                print('get app')
                if is_login:
                    Command.get_applicant(client, j_data[0]['identity'], j_data[0]['company'])
                else:
                    print('unlogin')
                    content = [{'auto_message':'您还未登录'}]
                    client.send(json.dumps(content).encode())

        except ConnectionError:
            print('fail')
            del login_account[self_id]
            client.close()
            return


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1010
host = socket.gethostname()
print(host)
s.bind((host, port))
s.listen(100)

pool = ThreadPoolExecutor(max_workers=100)

while True:
    c, addr = s.accept()
    # msg = "成功连接"
    # c.send(msg.encode())
    future = pool.submit(server_fun, c)