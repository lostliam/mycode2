import requests,re,os
from random import randint
from time import sleep
import warnings,random,string
warnings.filterwarnings("ignore")

WEBSITE=os.getenv('WEBSITE')

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36 Edg/113.0.1774.35',
    'x-requested-with': 'XMLHttpRequest',
}


with open('example.txt', 'r',encoding='gbk') as f:
    str=str(f.readline()[1:])
    acc=re.search(r'(.*?)@qq.com',str).group()

datac = {
    'email': acc,
    'passwd': acc,
    'code': '',
}

# proxies={'http': '127.0.0.1:7890', 'https': '127.0.0.1:7890'}
proxies=''

def generate_random_id():
    digits = ''.join(random.choices(string.digits, k=9))
    num_letters = random.randint(2, 5)
    letters = ''.join(random.choices(string.ascii_letters, k=num_letters))

    # Randomly choose the position of letters
    if random.choice([True, False]):
        random_id = letters + digits
    else:
        random_id = digits + letters

    return random_id+'@qq.com'

mail=generate_random_id()

def post(url,headers,cookies='',data='',proxies=''):
    attempts = 0
    max_attempts = 10
    while True:
        try:
            if cookies:
                response =requests.post(url,cookies=cookies,headers=headers,data=data,proxies=proxies)
            else:
                response = requests.post(url,  headers=headers, data=data,proxies=proxies)
                global CK
                CK= response.cookies
            #print(response.text.encode('utf-8').decode('unicode_escape'))
            break
        except Exception as e:
            attempts += 1
            if attempts >= max_attempts:
                raise e
            else:
                sleep(2)    

def get(url,headers,cookies='',proxies=''):
    attempts = 0
    max_attempts = 10
    while True:
        try:
            response =requests.get(url,cookies=cookies,headers=headers,proxies=proxies)
            url=re.search(r'https://(.*?)clash=1',response.text).group()
            # print(response.text.encode('utf-8').decode('unicode_escape'))
            response = requests.get(url, headers=headers,proxies=proxies)
            with open('example.txt', 'w') as f:
                f.write('#'+mail)
                f.write(response.text)
            break
        except Exception as e:
            attempts += 1
            if attempts >= max_attempts:
                raise e
            else:
                sleep(2)    



def register():
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
    data1 = {
        'email': mail,
        'passwd': mail,
        'code': '',
    }
    data2 = {
        'coupon': '',
        'shop': '1',
        'autorenew': '0',
        'disableothers': '1',
    }
    post(WEBSITE+'/auth/register',  headers=headers, data=data,proxies=proxies)
    post(WEBSITE+'/auth/login',  headers=headers, data=data1,proxies=proxies)
    post(WEBSITE+'/user/buy', cookies=CK, headers=headers, data=data2,proxies=proxies)
    post(WEBSITE+'/user/checkin', cookies=CK, headers=headers,proxies=proxies)
    get(WEBSITE+'/user', cookies=CK, headers=headers,proxies=proxies)

def getc(url,headers,cookies='',proxies=''):
    attempts = 0
    max_attempts = 10
    while True:
        try:
            response =requests.get(url,cookies=cookies,headers=headers,proxies=proxies)
            pattern = r'<span class="counter">(.*?)</span>'
            matches = re.findall(pattern, response.text)
            if len(matches) >= 2:
                print(matches[0])
                print(matches[1])
                if int(matches[0])>=1 and float(matches[1]) >=1.0:
                    print('can use')
                    break
                else:
                    register()
                    break
        except Exception as e:
            attempts += 1
            if attempts >= max_attempts:
                print('login error')
                register()
                raise e
            else:
                sleep(2)

post(WEBSITE+'/auth/login',  headers=headers, data=datac,proxies=proxies)

getc(WEBSITE+'/user', cookies=CK, headers=headers,proxies=proxies)