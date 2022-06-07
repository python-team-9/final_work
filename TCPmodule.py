
def m_recv(chat):
    all_data = ''
    time = 0
    max_wait = 10
    while True:
        if time > max_wait:
            print('等待超时')
            break

        try:
            content = chat.recv(1024).decode()
            all_data += content
            if len(all_data) > 0:
                if all_data[-1] == 'E':
                    break
            else:
                ++time
                continue

        except ConnectionError:
            print('连接错误')
            break

    return all_data[:-1]
