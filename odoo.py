import requests
from bs4 import BeautifulSoup

# URL halaman login
url_login_page = 'http://map.integrasi.online/web?db=MAP_LIVE'

# Lakukan permintaan GET untuk halaman login
response = requests.get(url_login_page)

# Parse HTML dari respons
soup = BeautifulSoup(response.content, 'html.parser')

# Cari elemen form dengan atribut name=csrf_token
# csrf_token = soup.find('input', {'name': 'csrf_token'}).get('value')
csrf_token = soup.find_all('input', {'name': 'csrf_token'})[0].get('value')

# print(csrf_token)

# Gunakan token CSRF dalam permintaan login
url_login = 'http://map.integrasi.online/web/login'
login_data = {
    'csrf_token': csrf_token,
    'db': 'MAP_LIVE',
    'login': '',
    'password': ''
}


with requests.Session() as sesi:
    p = sesi.post(url_login, data=login_data)
    print(p.text)

# # Melakukan permintaan POST untuk login
# login_response = requests.post(url_login, data=login_data)

# # Tampilkan status respons dan konten
# print(login_response.status_code)
# print(login_response.content)
