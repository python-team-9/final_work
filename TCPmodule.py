
def m_recv(chat):
    all_data = ''
    while True:
        try:
            content = chat.recv(1024).decode()
            all_data += content
            if all_data[-1] == 'E':
                break

        except ConnectionError:
            print('连接错误')
            pass

    return all_data[:-1]
