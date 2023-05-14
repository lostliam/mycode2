import requests,re,os
from random import randint
from time import sleep
import warnings 
warnings.filterwarnings("ignore")

WEBSITE=os.getenv('WEBSITE')
mail=str(randint(100000000,9999999999))+'@qq.com'


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
# proxies={'http': '127.0.0.1:7890', 'https': '127.0.0.1:7890'}
proxies=''
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
            #print(response.text.encode('utf-8').decode('unicode_escape'))
            response = requests.get(url, headers=headers,proxies=proxies)
            with open('example.txt', 'w') as f:
                f.write(response.text)
            break
        except Exception as e:
            attempts += 1
            if attempts >= max_attempts:
                raise e
            else:
                sleep(2)    



post(WEBSITE+'/auth/register',  headers=headers, data=data,proxies=proxies)
post(WEBSITE+'/auth/login',  headers=headers, data=data1,proxies=proxies)
post(WEBSITE+'/user/buy', cookies=CK, headers=headers, data=data2,proxies=proxies)
post(WEBSITE+'/user/checkin', cookies=CK, headers=headers,proxies=proxies)
get(WEBSITE+'/user', cookies=CK, headers=headers,proxies=proxies)

