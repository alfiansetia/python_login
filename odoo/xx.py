import requests
from bs4 import BeautifulSoup

from dotenv import load_dotenv
import os

load_dotenv()
email = os.getenv("email")
passw = os.getenv("pass_odoo")

with requests.Session() as sesi:
    url_login_page = 'http://map.integrasi.online:8069/web?db=MAP_LIVE'
    response = sesi.get(url_login_page)
    soup = BeautifulSoup(response.content, 'html.parser')
    csrf_token = soup.find_all('input', {'name': 'csrf_token'})[0].get('value')
    url_login = 'http://map.integrasi.online:8069/web/login'
    login_data = {
        'csrf_token': csrf_token,
        'db': 'MAP_LIVE',
        'login': email,
        'password': passw
    }
    p = sesi.post(url_login, data=login_data)
    print(p.cookies)

    # q = sesi.get('http://map.integrasi.online/web#action=411&model=product.template&view_type=kanban&menu_id=241')
    # soup1 = BeautifulSoup(q.content, 'html.parser')
    # print(q.text)

# # Melakukan permintaan POST untuk login
# login_response = requests.post(url_login, data=login_data)

# # Tampilkan status respons dan konten
# print(login_response.status_code)
# print(login_response.content)
