import os

#讀取資料
def openfile(filename):
    datas = []
    with open(filename, 'r') as f:
        for data in f:
            if '帳號,密碼\n' in data:
                continue
            username, password = data.strip().split(',')
            datas.append([username, password])
    return datas

#輸入帳號密碼
def input_data(datas):
    while True:
        username = input('請輸入帳號: ')
        if username == 'q':
            break
        if check(username, datas, 'u'):
            continue
        while True:
            password = input('請輸入密碼: ')
            if check(password, datas, 'p'):
                continue
            break
        datas.append([username, password])
    print(datas)
    return datas

#檢查帳號密碼
def check(word, datas, n):
    for data in datas:
        if word in data:
            if n == 'u':
                print('帳號已被使用,請重新輸入')
            if n == 'p':
                print('密碼已被使用,請重新輸入')
            return True

#寫入資料
def writefile(filename,datas):
    with open(filename, 'w') as f:
        f.write('帳號,密碼\n')
        for data in datas:
            f.write(data[0] + ',' + data[1] + '\n')


def main(filename):
    if os.path.isfile(filename):
        datas = openfile(filename)
    else:
        datas = []
    print(datas)
    datas = input_data(datas)
    writefile(filename,datas)

main('files.csv')