import requests,re,os
from random import randint
from time import sleep
WEBSITE=os.getenv('WEBSITE')

mail=str(randint(100000000,9999999999))+'@qq.com'

data = '------WebKitFormBoundaryqhEFAFCsKLBfEqRY\r\nContent-Disposition: form-data; name="passwd"\r\n\r\n{}\r\n------WebKitFormBoundaryqhEFAFCsKLBfEqRY\r\nContent-Disposition: form-data; name="repasswd"\r\n\r\n{}\r\n------WebKitFormBoundaryqhEFAFCsKLBfEqRY\r\nContent-Disposition: form-data; name="geetest_code"\r\n\r\n111\r\n------WebKitFormBoundaryqhEFAFCsKLBfEqRY\r\nContent-Disposition: form-data; name="code"\r\n\r\n\r\n------WebKitFormBoundaryqhEFAFCsKLBfEqRY\r\nContent-Disposition: form-data; name="geetest_challenge"\r\n\r\n6d80c7a33d63e496e46fc5b2f4ae7dbeac\r\n------WebKitFormBoundaryqhEFAFCsKLBfEqRY\r\nContent-Disposition: form-data; name="geetest_validate"\r\n\r\naa38062903058b8013d7c27020a1107e\r\n------WebKitFormBoundaryqhEFAFCsKLBfEqRY\r\nContent-Disposition: form-data; name="geetest_seccode"\r\n\r\naa38062903058b8013d7c27020a1107e%7Cjordan\r\n------WebKitFormBoundaryqhEFAFCsKLBfEqRY\r\nContent-Disposition: form-data; name="email"\r\n\r\n{}\r\n------WebKitFormBoundaryqhEFAFCsKLBfEqRY\r\nContent-Disposition: form-data; name="name"\r\n\r\n{}\r\n------WebKitFormBoundaryqhEFAFCsKLBfEqRY--\r\n'.format(mail,mail,mail,mail)

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36 Edg/112.0.1722.64',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'email': mail,
    'passwd': mail,
    'code': '',
}

data1 = {
    'coupon': '',
    'shop': '1',
    'autorenew': '0',
    'disableothers': '1',
}


def post(url,headers,cookies='',data=''):
    attempts = 0
    max_attempts = 10
    while True:
        try:
            if cookies:
                response =requests.post(url,cookies=cookies,headers=headers,data=data )
            else:
                response = requests.post(url,  headers=headers, data=data )
                global CK
                CK= response.cookies
            #print(response.text.encode('utf-8').decode('unicode_escape'))
        except Exception as e:
            attempts += 1
            if attempts >= max_attempts:
                raise e
            else:
                sleep(2)    


def get(url,headers,cookies=''):
    attempts = 0
    max_attempts = 10
    while True:
        try:
            response =requests.get(url,cookies=cookies,headers=headers )
            url=re.search(r'https://(.*?)clash=1&extend=1',response.text).group()
            #print(response.text.encode('utf-8').decode('unicode_escape'))
            response = requests.get(url, headers=headers)
            with open('example.txt', 'w') as f:
                f.write(response.text)
        except Exception as e:
            attempts += 1
            if attempts >= max_attempts:
                raise e
            else:
                sleep(2)    



post(WEBSITE+'/auth/register',  headers=headers, data=data)
post(WEBSITE+'/auth/login',  headers=headers, data=data)
post(WEBSITE+'/user/buy', cookies=CK, headers=headers, data=data1)
post(WEBSITE+'/user/checkin', cookies=CK, headers=headers)
get(WEBSITE+'/user', cookies=CK, headers=headers)

