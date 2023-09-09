import requests,re,os,warnings,random,string
from time import sleep


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


def generate_random_id():
    digits = ''.join(random.choices(string.digits, k=9))
    num_letters = random.randint(2, 5)
    letters = ''.join(random.choices(string.ascii_letters, k=num_letters))
    if random.choice([True, False]):
        random_id = letters + digits
    else:
        random_id = digits + letters
    return random_id+'@qq.com'

