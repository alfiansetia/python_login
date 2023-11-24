import requests
from bs4 import BeautifulSoup


with requests.Session() as sesi:
    url_login = 'https://account.mekari.com/users/sign_in?client_id=TAL-73645'
    # url_login = 'https://hr.talenta.co/users/sign_in'
    # url_emp = "https://hr.talenta.co/api/web/employee/directory/list-employee?page=1&limit=100&chunk=10&search=&sort=asc&sortBy=first_name"
    url_emp = "https://hr.talenta.co/api/web/dashboard"
    response = sesi.get(url_login)
    soup = BeautifulSoup(response.content, 'html.parser')
    csrf_token = soup.find_all('input', {'name': 'authenticity_token'})[0].get('value')
    # csrf_token = soup.find_all('meta', {'name': 'csrf-token'})[0].get('content')
    print(csrf_token)
    login_data = {
        'authenticity_token': csrf_token,
        # 'csrf_token': csrf_token,
        'user[email]': 'xxx@gmail.com',
        'user[password]': 'sss',
        'no-captcha-token' : '',
        'commit' : 'Sign in'
    }
    
    headers = {
        'Accept': 'application/json',
        'Cookie': '; '.join([f'{name}={value}' for name, value in sesi.cookies.items()]) 
    }
    p = sesi.post(url_login, data=login_data)
    q = sesi.get(url_emp, headers=headers)

    print(q.text)

# # Melakukan permintaan POST untuk login
# login_response = requests.post(url_login, data=login_data)

# # Tampilkan status respons dan konten
# print(login_response.status_code)
# print(login_response.content)
