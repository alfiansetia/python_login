import requests
import random
import string
from bs4 import BeautifulSoup
import json
import random


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

def generate_random_number(length):
    start = 10**(length-1)
    end = (10**length) - 1
    return random.randint(start, end)

def get_random_province():
    r=requests.get('https://join.jagoflutter.com/selectProv?_type=query')
    r.raise_for_status()
    dt = r.json()
    ran = random.randint(0,(len(dt['data'])-1))
    return dt['data'][ran]['id']

def get_random_city(province_id):
    r=requests.get('https://join.jagoflutter.com/selectRegenc/'+ str(province_id) +'?_type=query')
    r.raise_for_status()
    dt = r.json()
    ran = random.randint(0,(len(dt['data'])-1))
    return dt['data'][ran]['id']

i = 0
error = 0
state = True
while state:
    try:
        i = i+1
        with requests.Session() as sesi:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36'
            }
            url_login_page = 'https://join.jagoflutter.com/firebase'
            response = sesi.get(url_login_page, headers=headers)
            response.raise_for_status()
            # print(response.text)
            soup = BeautifulSoup(response.content, 'html.parser')
            code = soup.find_all('input', {'name': 'code'})[0].get('value')
            # code = ""
            url_pos = 'https://join.jagoflutter.com/api/checkout'
            ran = generate_random_string(10)
            ran2 = generate_random_string(5)
            ph = generate_random_number(10)
            phone = '8' + str(ph)
            name = str(ran2) + '_HEHE'
            email = str(ran) + '@gmail.com'
            prov = get_random_province()
            city = get_random_city(prov)
            data_pos = {
                'name': name,
                'email': email,
                'whatsapp': "08" + str(phone),
                'profesi': 'Guru',
                'discount_code': '',
                'payment_method': 'bank_transfer',
                'payment_va_name': 'bri',
                'package_id': 19,
                'batch_id': [],
                # 'event_id': random.choice([6,7,4,3,2]),
                'event_id': 7,
                'total_amount': 0,
                'coupon': '',
                'type': 'batch',
                'provinsi' : prov,
                'kota' : city,
                'code' : code,
            }
            p = sesi.post(url_pos, data=data_pos, headers=headers)
            p.raise_for_status()
            data = p.json()
            if p.status_code != 200:
                print('Error : ',data['message'])
                error = error+1
            else:
                error = 0
                print(f"{data['message']} {data['order']['transaction_number']} {email}")
            if error > 3:
                state = False
            # with open("output.txt", "w") as file:
            #     file.write(p.text)
            # try:
            #     p.text.index('Akun anda belum divalidasi')
            #     print(str(email) + ' ' + str(phone) + ' ke : ' +  str(i))
            # except:
            #     print('gagal')
        
    except KeyboardInterrupt:
        print('Stopped by user!')
        state = False
    except Exception as e :
        print('error : ', e)
        error = error+1
        if error > 3:
            state = False

