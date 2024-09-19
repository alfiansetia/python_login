import requests
from bs4 import BeautifulSoup

import os
import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

while True:
    with requests.Session() as sesi:
        url_login_page = 'https://dashboard.pusataplikasi.com/register'
        response = sesi.get(url_login_page)
        soup = BeautifulSoup(response.content, 'html.parser')
        csrf_token = soup.find_all('input', {'name': '_token'})[0].get('value')
        url_regis = 'https://dashboard.pusataplikasi.com/register'
        # print(csrf_token)
        ran = generate_random_string(10)
        email = str(ran) + '.' + str(ran) + '@gmail.com'
        regis_data = {
            '_token': csrf_token,
            'level': random.randint(1,5),
            'wilpro': 100054,
            'wilkab': 191126,
            'wilkec': 101710,
            'wilkel': 101712,
            'name': 'Aku Anak Sehat',
            'email': email,
            'password': email,
            'password_confirmation': email,
        }
        p = sesi.post(url_regis, data=regis_data)
        try:
            p.text.index('Home | DASHBOARD')
            print(email)
            # print('success')
        except:
            print('gagal')