import requests
from bs4 import BeautifulSoup

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}


def get_page():
    print('get page')


def get_content():
    url = 'https://www.hklawsoc.org.hk/en/Serve-the-Public/The-Law-List/Firm-Detail?FirmId=19'

    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    content = bs.findAll('tr')
    print(content)


if __name__ == '__main__':
    get_content()