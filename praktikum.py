import requests
import json
from prettytable import PrettyTable

url_all_data = "https://kuliah.sttdb.ac.id/mahasiswa/api/praktikum.php"
url_detail_praktikum = "https://kuliah.sttdb.ac.id/mahasiswa/api/praktikan.php"

form_data = {
    "username": "nim",
    "password": "nim",
}
jarkom = 201
pemr = 205

while True:
    try:
        print("Jarkom : 201, Pemrograman Terstruktur : 205")
        num = int(input("Masukkan ID Praktikum: "))
        if num > 0:
            break
        else:
            print("Angka harus lebih besar dari nol.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang valid.")

print("Loading.....")

with requests.Session() as sesi:
    # login = sesi.post(
    #     url=url_login,
    #     data=form_data,
    # )
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
