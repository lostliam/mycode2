import requests,re,os,warnings,random,string
from time import sleep
from csdata import *
warnings.filterwarnings("ignore")
proxies=''
CK=''
WEBSITE=os.getenv('WEBSITE')

# proxies={'http': '127.0.0.1:7890', 'https': '127.0.0.1:7890'}


def checkl(acc):
    data = {'email': acc, 'passwd': acc, 'code': '', }
    attempts = 0
    max_attempts=3
    while True:
        try:
            response = requests.post(WEBSITE + '/auth/login', headers=headers, data=data, proxies=proxies, verify=False,timeout=5)
            json_data = response.json()
            ret = json_data.get('ret', None)
            print(ret)
            if ret == 1:
                global CK
                CK= response.cookies
                return True
            else:
                return False
        except Exception as e:
            attempts += 1
            if attempts >= max_attempts:
                print('error', __name__)
                raise e
            else:
                sleep(2)

def checkvolume(acc):
    data = {'email': acc, 'passwd': acc, 'code': '', }
    attempts = 0
    max_attempts=3
    while True:
        try:
            response =requests.get(WEBSITE+'/user',cookies=CK,headers=headers,data=data,proxies=proxies,verify=False,timeout=5)
            pattern = r'<span class="counter">(.*?)</span>'
            matches = re.findall(pattern, response.text)
            if len(matches) >= 2:
                print(matches[0])
                print(matches[1])
                if int(matches[0]) >= 1 and float(matches[1]) >= 1.0:
                    print('can use')
                    return True
                else:
                    return False
        except Exception as e:
            attempts += 1
            if attempts >= max_attempts:
                print('error',__name__)
                raise e
            else:
                sleep(2)


def regnew(data):
    attempts = 0
    max_attempts=3
    while True:
        try:
            response = requests.post(WEBSITE + '/auth/register', headers=headers, data=data, proxies=proxies, verify=False,timeout=5)
            global CK
            CK= response.cookies
            return True
        except Exception as e:
            attempts += 1
            if attempts >= max_attempts:
                print('error', __name__)
                raise e
            else:
                sleep(2)

def buyitem(data):
    attempts = 0
    max_attempts=3
    while True:
        try:
            response = requests.post(WEBSITE + '/user/buy',cookies=CK, headers=headers, data=data, proxies=proxies, verify=False,timeout=5)
            return True
        except Exception as e:
            attempts += 1
            if attempts >= max_attempts:
                print('error', __name__)
                raise e
            else:
                sleep(2)

def checki():
    attempts = 0
    max_attempts=3
    while True:
        try:
            response = requests.post(WEBSITE + '/user/checkin',cookies=CK, headers=headers, proxies=proxies, verify=False,timeout=5)
            return True
        except Exception as e:
            attempts += 1
            if attempts >= max_attempts:
                print('error', __name__)
                raise e
            else:
                sleep(2)

def catch(mail):
    attempts = 0
    max_attempts=3
    while True:
        try:
            response = requests.get(WEBSITE+'/user', cookies=CK, headers=headers,proxies=proxies,verify=False,timeout=5)
            url = re.search(r'https://(.*?)clash=1', response.text).group()
            response = requests.get(url, headers=headers, proxies=proxies)
            with open('example.txt', 'w') as f:
                f.write(response.text)
            with open('test.txt', 'w') as f:
                f.write(mail)
            return True
        except Exception as e:
            attempts += 1
            if attempts >= max_attempts:
                print('error', __name__)
                raise e
            else:
                sleep(2)


def reg():
    mail = generate_random_id()
    data = {
        'email': mail,
        'name': mail,
        'passwd': mail,
        'repasswd': mail,
        'geetest_code': '111',
        'code': '',
        'geetest_challenge': '99de83c52927f403d186ccb7e9140964gi',
        'geetest_validate': 'f085c7b27d9111fac536fb7e1dba5396',
        'geetest_seccode': 'f085c7b27d9111fac536fb7e1dba5396|jordan',
    }
    sleep(2)
    regnew(data)
    sleep(2)
    checkl(mail)
    data1 = {
        'coupon': '',
        'shop': '1',
        'autorenew': '0',
        'disableothers': '1',
    }
    sleep(2)
    buyitem(data1)
    catch(mail)



with open('test.txt', 'r', encoding='gbk') as f:
    acc = str(f.readline())

if checkl(acc):
    sleep(2)
    if not checkvolume(acc):
        sleep(2)
        reg()
else:
    sleep(2)
    reg()


