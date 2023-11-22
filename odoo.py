import requests
from bs4 import BeautifulSoup

with requests.Session() as sesi:
    url_login_page = 'http://map.integrasi.online/web?db=MAP_LIVE'
    response = sesi.get(url_login_page)
    soup = BeautifulSoup(response.content, 'html.parser')
    csrf_token = soup.find_all('input', {'name': 'csrf_token'})[0].get('value')
    url_login = 'http://map.integrasi.online/web/login'
    login_data = {
        'csrf_token': csrf_token,
        'db': 'MAP_LIVE',
        'login': 'alfian.setia100@gmail.com',
        'password': '123456'
    }
    p = sesi.post(url_login, data=login_data)

    q = sesi.get('http://map.integrasi.online/web#action=411&model=product.template&view_type=kanban&menu_id=241')
    soup1 = BeautifulSoup(q.content, 'html.parser')
    print(q.text)

# # Melakukan permintaan POST untuk login
# login_response = requests.post(url_login, data=login_data)

# # Tampilkan status respons dan konten
# print(login_response.status_code)
# print(login_response.content)
