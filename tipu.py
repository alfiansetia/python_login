import requests
import json

url_reg = "https://www.toko-mall.org/base/user_reg.ashx"

# while True:
#     try:
#         print("Jarkom : 201, Pemrograman Terstruktur : 205")
#         num = int(input("Masukkan ID Praktikum: "))
#         if num > 0:
#             break
#         else:
#             print("Angka harus lebih besar dari nol.")
#     except ValueError:
#         print("Input tidak valid. Harap masukkan angka yang valid.")

# print("Loading.....")

with requests.Session() as sesi:
    user_name = 'kontol'
    for i in range(1, 1000000):
        form = {
            "user_name": user_name+str('_')+str(i),
            "mobile": "",
            "password": "kontol",
            "confirmPwd": "kontol",
            "invitation": "100214322",
            "areacode": "+86",
            "verify_code": ""
        }
        header = {
            'User-Agent' : "PostmanRuntime/7.35.0",
            'Accept': 'application/json',
        }
        proxy = {
            'http': 'http://192.168.4.225:3128',
            'https': 'http://192.168.4.225:3128'
        }
        try:
            data = sesi.post(
                url=url_reg,
                json=form,
                headers=header,
                proxies=proxy
            )
            parsed_data = json.loads(data.text)
            print(parsed_data['D'])
        except Exception as e:
            print('Error program : ' + str(e))



