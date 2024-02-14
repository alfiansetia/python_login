import requests
from prettytable import PrettyTable
import json
import os

def format_number(number):
    if number >= 1000:
        formatted_number = '{:.0f}k'.format(number / 1000)
    else:
        formatted_number = str(number)
    return formatted_number

def calculate_percentage(value, total):
    if total == 0:
        return 0
    percentage = (value / total) * 100
    return "{:.2f}%".format(percentage)


def get_data(id = ''):
    url = 'https://us-central1-kp24-fd486.cloudfunctions.net/hierarchy2'
    headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
    }
    data = {
            "data": {
                "id": id
            }
        }
    os.system('cls')
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        dt_json = response.json()
        table = PrettyTable()
        table.field_names = ["KODE", "NAME", "1", "2", "3"]
        table.align["NAME"] = "l"
        name_lokasi = ''
        data_name = dt_json['result']['names']
        array_kota = ['PROV : ', 'KAB : ', 'KEC : ', 'DESA : ', 'DUS : ']
        j=0
        if(len(data_name) < 1):
            print('LOKASI : ALL PROV')
        else:
            for x in data_name:
                print(array_kota[j] + x)
                j+=1
        print('\n')
        i = 1
        total_pas1 = 0
        total_pas2 = 0
        total_pas3 = 0
        for dt in dt_json['result']['aggregated']:
            id_lokasi = dt
            name = dt_json['result']['aggregated'][dt][0]['name']
            if(len(data_name) > 3):
                name = 'TPS' + str(name)
            pas1 = int(dt_json['result']['aggregated'][dt][0]['pas1'])
            pas2 = int(dt_json['result']['aggregated'][dt][0]['pas2'])
            pas3 = int(dt_json['result']['aggregated'][dt][0]['pas3'])
            total_suara = pas1+pas2+pas3
            i += 1
            total_pas1 += pas1
            total_pas2 += pas2
            total_pas3 += pas3
            table.add_row(
                [
                    id_lokasi,
                    name,
                    calculate_percentage(pas1, total_suara),
                    calculate_percentage(pas2, total_suara),
                    calculate_percentage(pas3, total_suara),
                ],
            )
        total_data = total_pas1+total_pas2+total_pas3
        table.add_row(
            [
                "#",
                "TOTAL",
                calculate_percentage(total_pas1,total_data),
                calculate_percentage(total_pas2,total_data),
                calculate_percentage(total_pas3,total_data),
            ],
        )
        print(table)
    else:
        print('Request failed with status code:', response.status_code)


while True:
    user_input = input("Masukkan ID (enter untuk kembali, x untuk keluar): ")
    
    if user_input == "x":
        print("Terima kasih! Keluar dari program.")
        break
    
    try:
        user_id = str(user_input)
        get_data(user_id)
    except ValueError:
        print("Error: Masukkan ID dalam bentuk angka.")