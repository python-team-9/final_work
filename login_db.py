import sqlite3



def register(userid,password,ismanager):
    identity_db = 'identity.db'
    conn = sqlite3.connect(identity_db)

    cur = conn.cursor()
    # sql语句
    sql = "insert into users values (?,?,?)"
    data = (userid,password,ismanager)
    # 执行sql语句
    cur.execute(sql,data)
    # 提交数据，否则无法同步之数据库
    conn.commit()
    # 关闭
    cur.close()
    conn.close()

def login(userid,password,ismanager):
    identity_db = 'identity.db'
    conn = sqlite3.connect(identity_db)

    cur = conn.cursor()
    sql = "SELECT count(*) FROM users WHERE userid=? AND password=? AND manager=?"
    cur.execute(sql,(userid,password,ismanager))
    res = cur.fetchall()[0][0]
    conn.commit()
    # 关闭
    cur.close()
    conn.close()
    return res




