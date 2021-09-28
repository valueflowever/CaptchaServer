import requests
from tools import get_config, headers

config = get_config('config.ini')
api_key = config['2CaptchaConf']['api_key']  # 请替换成自己的TOKEN
google_key = config['2CaptchaConf']['google_key']
page_url = config['2CaptchaConf']['page_url']


def create_task():
    # url = f'http://2captcha.com/in.php?key={api_key}&' \
    #       'method=userrecaptcha&' \
    #       'invisible=1&' \
    #       'enterprise=1&' \
    #       f'googlekey={googlekey}&' \
    #       f'pageurl={pageurl}&' \
    #       f'json=1'
    url = f'http://2captcha.com/in.php?key={api_key}&' \
          'method=userrecaptcha&' \
          'version=v3&' \
          'min_score=0.3&' \
          f'googlekey={google_key}&' \
          f'pageurl={page_url}&' \
          f'json=1'
    resp = requests.post(url, headers=headers).json()
    request_id = resp['request']
    return request_id


def polling_task(request_id: int):
    url = f'http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}'
    response = requests.get(url)
    return response.content.decode('utf-8')[3:]
