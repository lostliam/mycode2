import requests,re,os
from random import randint
WEBSITE=os.getenv('WEBSITE')
headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryqhEFAFCsKLBfEqRY',
    'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64',
    'x-requested-with': 'XMLHttpRequest',
}

mail=str(randint(100000000,9999999999))+'@qq.com'

data = '------WebKitFormBoundaryqhEFAFCsKLBfEqRY\r\nContent-Disposition: form-data; name="passwd"\r\n\r\n{}\r\n------WebKitFormBoundaryqhEFAFCsKLBfEqRY\r\nContent-Disposition: form-data; name="repasswd"\r\n\r\n{}\r\n------WebKitFormBoundaryqhEFAFCsKLBfEqRY\r\nContent-Disposition: form-data; name="geetest_code"\r\n\r\n111\r\n------WebKitFormBoundaryqhEFAFCsKLBfEqRY\r\nContent-Disposition: form-data; name="code"\r\n\r\n\r\n------WebKitFormBoundaryqhEFAFCsKLBfEqRY\r\nContent-Disposition: form-data; name="geetest_challenge"\r\n\r\n6d80c7a33d63e496e46fc5b2f4ae7dbeac\r\n------WebKitFormBoundaryqhEFAFCsKLBfEqRY\r\nContent-Disposition: form-data; name="geetest_validate"\r\n\r\naa38062903058b8013d7c27020a1107e\r\n------WebKitFormBoundaryqhEFAFCsKLBfEqRY\r\nContent-Disposition: form-data; name="geetest_seccode"\r\n\r\naa38062903058b8013d7c27020a1107e%7Cjordan\r\n------WebKitFormBoundaryqhEFAFCsKLBfEqRY\r\nContent-Disposition: form-data; name="email"\r\n\r\n{}\r\n------WebKitFormBoundaryqhEFAFCsKLBfEqRY\r\nContent-Disposition: form-data; name="name"\r\n\r\n{}\r\n------WebKitFormBoundaryqhEFAFCsKLBfEqRY--\r\n'.format(mail,mail,mail,mail)

response = requests.post(WEBSITE+'/auth/register',  headers=headers, data=data)
# print(response.text.encode('utf-8').decode('unicode_escape'))
# print(mail)


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

response = requests.post(WEBSITE+'/auth/login',headers=headers, data=data)
# print(response.text.encode('utf-8').decode('unicode_escape'))
cookies=response.cookies


data = {
    'coupon': '',
    'shop': '1',
    'autorenew': '0',
    'disableothers': '1',
}

response = requests.post(WEBSITE+'/user/buy', cookies=cookies, headers=headers, data=data)
# print(response.text.encode('utf-8').decode('unicode_escape'))
response = requests.post(WEBSITE+'/user/checkin', cookies=cookies, headers=headers)
# print(response.text.encode('utf-8').decode('unicode_escape'))

response = requests.get(WEBSITE+'/user', cookies=cookies, headers=headers)
url=re.search(r'https://(.*?)clash=1&extend=1',response.text).group()

response = requests.get(url, headers=headers)
# print(response.text)

with open('example.txt', 'w') as f:
    f.write(response.text)