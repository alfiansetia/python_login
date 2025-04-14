import requests
from bs4 import BeautifulSoup
import json
from prettytable import PrettyTable

def get_stations():
    r = requests.post('https://booking.kai.id/api/stations2')
    return r.json()
    

url = 'https://booking.kai.id'
url_step2 = 'https://booking.kai.id/passengerdata'
url_step3 = 'https://booking.kai.id/passengercontrol'
param = {
    'origination': 'KNN',
    'flexdatalist-origination': 'KRADENAN',
    'destination': 'SMT',
    'flexdatalist-destination': 'SEMARANG TAWANG BANK JATENG',
    'tanggal': '28-Februari-2025',
    'adult': 1,
    'infant': 0,
    'submit': 'Cari & Pesan Tiket',
}
# 'origination': 'SMT',
#     'flexdatalist-origination': 'SEMARANG TAWANG BANK JATENG',
#     'destination': 'BKS',
#     'flexdatalist-destination': 'BEKASI',
#     'tanggal': '7-April-2025',
#     'adult': 3,
#     'infant': 0,
#     'submit': 'Cari & Pesan Tiket',
print(f"Tiket Tgl : {param['tanggal']}")
print(f"Asal : {param['flexdatalist-origination']}")
print(f"Tujuan : {param['flexdatalist-destination']}")

table = PrettyTable()
table.field_names = ['NO', "Nama Kereta", "Kelas", "Habis"]

with requests.Session() as sesi:
    r= sesi.get(url, params=param)
    # with open("kai.html", "w") as file:
    #     file.write(r.text)
    # print(r.status_code)
    # with open("kai.html", "r", encoding="utf-8") as f:
    #     html_content = f.read()
    html_content = r.text
    soup = BeautifulSoup(html_content, "html.parser")

    kereta_list = soup.find_all("div", class_="data-block list-kereta")

    i=1
    data_kereta = []
    for kereta in kereta_list:
        link_element = kereta.find("a", class_="habis")
        
        data = {
            '_token' : soup.find('meta', {'name': 'csrf-token'})['content'],
            'nama_kereta' : kereta.find("div", class_="name").get_text(strip=True),
            'kelas_kereta' : kereta.find("div", class_="{kelas kereta}").get_text(strip=True),
            'habis' : "Habis" if link_element else "Tersedia",
            
            'tripdate' :kereta.find("input", {"name": "tripdate"})["value"],
            'depart_date' :kereta.find("input", {"name": "depart_date"})["value"],
            'tanggal_sampai' :kereta.find("input", {"name": "tanggal_sampai"})["value"],
            'asal' :kereta.find("input", {"name": "asal"})["value"],
            'tujuan' :kereta.find("input", {"name": "tujuan"})["value"],
            'kodeasal' :kereta.find("input", {"name": "kodeasal"})["value"],
            'kodetujuan' :kereta.find("input", {"name": "kodetujuan"})["value"],
            'timestart' :kereta.find("input", {"name": "timestart"})["value"],
            'timeend' :kereta.find("input", {"name": "timeend"})["value"],
            'nokereta' :kereta.find("input", {"name": "nokereta"})["value"],
            'kereta' :kereta.find("input", {"name": "kereta"})["value"],
            'kelas' :kereta.find("input", {"name": "kelas"})["value"],
            'kelas_gerbong' :kereta.find("input", {"name": "kelas_gerbong"})["value"],
            'subkelas' :kereta.find("input", {"name": "subkelas"})["value"],
            'dewasa' :kereta.find("input", {"name": "dewasa"})["value"],
            'infant' :kereta.find("input", {"name": "infant"})["value"],
            'harga' :kereta.find("input", {"name": "harga"})["value"],
            'trip_id' :kereta.find("input", {"name": "trip_id"})["value"],
            'wagonclassid' :kereta.find("input", {"name": "wagonclassid"})["value"],
            'orgid' :kereta.find("input", {"name": "orgid"})["value"],
            'desid' :kereta.find("input", {"name": "desid"})["value"],
            'propscheduleid' :kereta.find("input", {"name": "propscheduleid"})["value"],
        }
        data_kereta.append(data)
        # print(data)
        # Tambahkan data ke tabel
        table.add_row([i, data['nama_kereta'], data['kelas_kereta'], data['habis']])
        i= i+1

    print(table)
    pilih = int(input('Pilih Nomor : '))
    step2 = sesi.post(url_step2, data=data_kereta[pilih-1])
    with open("kai2.html", "w") as file:
        file.write(step2.text)


    # print(get_stations())


