from tools import get_config, headers
import requests
import time

config = get_config('config.ini')
TOKEN = config['yesCaptchaConf']['token']  # 请替换成自己的TOKEN
REFERER = config['yesCaptchaConf']['referer']
BASE_URL = config['yesCaptchaConf']['base_url']
SITE_KEY = config['yesCaptchaConf']['site_key']  # 请替换成自己的SITE_KEY


def create_task():
    url = f"{BASE_URL}/v3/recaptcha/create?token={TOKEN}&siteKey={SITE_KEY}&siteReferer={REFERER}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('taskId')


def polling_task(task_id):
    url = f"{BASE_URL}/v3/recaptcha/status?token={TOKEN}&taskId={task_id}"
    count = 0
    while count < 120:
        try:
            response = requests.get(url)
            print(response.content)
            if response.status_code == 200:
                data = response.json()
                status = data.get('data', {}).get('status')
                if status == 'Success':
                    return data.get('data', {}).get('response')
        except requests.RequestException as e:
            print('polling task failed', e)
        finally:
            count += 1
            time.sleep(1)
