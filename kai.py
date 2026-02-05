import requests
from bs4 import BeautifulSoup
import json
from prettytable import PrettyTable

def get_stations():
    r = requests.post('https://booking.kai.id/api/stations2')
    return r.json()
    

stations = {
    'BKS': 'BEKASI',
    'SMT': 'SEMARANG TAWANG BANK JATENG',
    'SMC': 'SEMARANG PONCOL',
    'KNN': 'KRADENAN',
    'NBO': 'NGROMBO',
}

# Nama-nama bulan dalam Bahasa Indonesia
bulan_indo = {
    1: 'Januari', 
    2: 'Februari', 
    3: 'Maret', 
    4: 'April',
    5: 'Mei', 
    6: 'Juni', 
    7: 'Juli', 
    8: 'Agustus',
    9: 'September', 
    10: 'Oktober', 
    11: 'November', 
    12: 'Desember'
}

# Tampilkan pilihan stasiun
print("\nPilih Stasiun Asal:")
station_keys = list(stations.keys())
for idx, key in enumerate(station_keys, 1):
    print(f"{idx}. {stations[key]} ({key})")
pilih_asal = int(input("Pilih Nomor Stasiun Asal: "))
asal_key = station_keys[pilih_asal - 1]

print("\nPilih Stasiun Tujuan:")
for idx, key in enumerate(station_keys, 1):
    print(f"{idx}. {stations[key]} ({key})")
pilih_tujuan = int(input("Pilih Nomor Stasiun Tujuan: "))
tujuan_key = station_keys[pilih_tujuan - 1]

print("\nPilih Tanggal Keberangkatan")
tgl_input = input('Masukkan Tanggal (ddmmyyyy): ').strip()

# Parsing ddmmyyyy
tgl = tgl_input[0:2]
bln_num = int(tgl_input[2:4])
thn = tgl_input[4:8]

# Pastikan format tanggal 2 digit jika < 10 (opsional, tergantung API KAI)
# Di kai.id biasanya formatnya d-B-Y (misal 19-Maret-2026)
tanggal_query = f"{int(tgl)}-{bulan_indo[bln_num]}-{thn}"

url = 'https://booking.kai.id'
url_step2 = 'https://booking.kai.id/passengerdata'
url_step3 = 'https://booking.kai.id/passengercontrol'
param = {
    'origination': asal_key,
    'flexdatalist-origination': stations[asal_key],
    'destination': tujuan_key,
    'flexdatalist-destination': stations[tujuan_key],
    'tanggal': tanggal_query,
    'adult': 1,
    'infant': 0,
    'submit': 'Cari & Pesan Tiket',
}
print(f"Tiket Tgl : {param['tanggal']}")
print(f"Asal : {param['flexdatalist-origination']}")
print(f"Tujuan : {param['flexdatalist-destination']}")
print(f"Tanggal Input : {tgl}-{bulan_indo[bln_num]}-{thn}")

table = PrettyTable()
table.field_names = ['NO', "Nama Kereta", "Kelas", "Habis", "Harga"]

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
        # Format harga dengan titik (thousand separator)
        harga_raw = int(data['harga'])
        harga_formatted = f"{harga_raw:,}".replace(",", ".")
        
        # Tambahkan data ke tabel
        table.add_row([i, data['nama_kereta'], data['kelas_kereta'], data['habis'], f"Rp {harga_formatted}"])
        i= i+1
    if(len(data_kereta) == 0):
        print("Tidak ada kereta tersedia")
    else:
        print(table)
        # pilih = int(input('Pilih Nomor : '))
        # step2 = sesi.post(url_step2, data=data_kereta[pilih-1])
        # with open("kai2.html", "w") as file:
        #     file.write(step2.text)


    # print(get_stations())


