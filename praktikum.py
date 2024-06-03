import requests
import json
from prettytable import PrettyTable
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup


load_dotenv()
nim = os.getenv("NIM")

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
clear_console()
url_all_data = "https://kuliah.sttdb.ac.id/mahasiswa/api/praktikum.php"
url_detail_praktikum = "https://kuliah.sttdb.ac.id/mahasiswa/api/praktikan.php"
url_html_data = "https://kuliah.sttdb.ac.id/mahasiswa/event/praktikum/"
url_login = "https://kuliah.sttdb.ac.id/proses.php"

form_data = {
    "username": nim,
    "password": nim,
    "login": ''
}
jarkom = 201
pemr = 205
text_gagal = "Maaf Sesi Anda Habis, Silahkan Login Kembali!"
data = []
with requests.Session() as sesi:
    login = sesi.post(
        url=url_login,
        data=form_data,
    )
    # try:
    html = sesi.get(url_html_data)
    with open("output.txt", "w") as file:
        file.write(html.text)

    try:
        html.text.index(text_gagal)
        print(text_gagal)
    except:
        soup = BeautifulSoup(html.text, 'html.parser')
        list_praktikan_elements = soup.find_all(class_="list_praktikan")
        data = [{"id": element['data-id'], "mk": element['data-mk']} for element in list_praktikan_elements]

def get_data(num):
    clear_console()
    with requests.Session() as sesi:
        data = sesi.post(
            url=url_detail_praktikum,
            data={
                "id_praktikum": num,
            },
        )
        parsed_data = json.loads(data.text)
        # print(parsed_data)
        i = 1
        if len(parsed_data["data"]) > 0:
            table = PrettyTable()
            table.field_names = ["NIM", "NAME", "BAYAR", "MK", "kode"]
            table.align["NAME"] = "l"
            table.align["MK"] = "l"
            count_bayar = 0
            count_belum = 0
            for dt in parsed_data["data"]:
                i += 1
                if dt["status_bayar"] == "sudah":
                    count_bayar += 1
                elif dt["status_bayar"] == "belum":
                    count_belum += 1
                table.add_row(
                    [
                        dt["nim"],
                        dt["nama"],
                        dt["status_bayar"],
                        dt["nama_mk"],
                        dt["kode"],
                    ],
                )
            table.add_row(
                ["", "", "", "", ""],
                divider=True,
            )
            table.add_row(
                ["TOTAL", len(parsed_data["data"]), "", "", ""],
                divider=True,
            )
            table.add_row(
                ["BAYAR", count_bayar, "", "", ""],
                divider=True,
            )
            table.add_row(
                ["BELUM", count_belum, "", "", ""],
                divider=True,
            )
            print(table)
        else:
            print("Data Not Found!")
    print('\n')
    
state = True
while (len(data) > 0 and state):
    try:
        table_list = PrettyTable()
        table_list.field_names = ["NO", "MK"]
        table_list.align["MK"] = "l"
        for i, dt in enumerate(data):
            table_list.add_row(
                    [
                        int(i)+1,
                        dt["mk"],
                    ],
                )
        print(table_list)
        num = int(input("Masukkan Nomor (0 Keluar): "))
        if(num == 0):
            print('Bye!')
            state = False
        else :
            if num > 0 and num <= len(data):
                get_data(data[num-1]['id'])
            else:
                print("Angka harus lebih besar dari nol dan kurang dari " + str(len(data)+1))
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang valid.")
    except:
        state = False
