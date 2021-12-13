import requests
import datetime
import random


now = datetime.datetime.now()
waktu_sekarang = now.strftime("%Y-%m-%d %H:%M")
alamat = [
        "Bekasi, RT.003RW.005 Kav C3, RT.003RW.005, Kali Baru, Medan Satria, Bekasi City, West Java 17132, Indonesia",
        "Bizpark 3, Blok C No. 9, Jl. Sultan Agung No.Km 28,5, RT.003/RW.005, Kali Baru, Medan Satria, Bekasi City, West Java 17>]

url_login = "https://vast-viovera.co.id"
url_home = "https://vast-viovera.co.id/home"
url_log ="https://vast-viovera.co.id/laporan/log-absensi"
url_absen = "https://vast-viovera.co.id/mobile/insert_data"

karyawan = {
                'id' : '1541',
                'nama' : 'Abdul Hai',
                'induk' : '60814062'
        },{
                'id' : '1609',
                'nama' : 'Alfian Setiawan',
                'induk' : '60218224'
        },{
                'id' : '3089',
                'nama' : 'indra',
                'induk' : '50519262'
        }

form_absen = {
        'geoloc_status' : True,
        'geoloc_response' : 'success',
        'proc_val' : 'mobile_checkin',
        'currdb' : 'vioveradb',
        'comp_id' : '1082',
        'no_induk' : '60218224',
        'geoloc_addr' : random.choice(alamat),
        #'dateString' : '2021-12-13 18:05',
        'dateString' : waktu_sekarang
}

form_login = {
        'imeino' : '',
        'app_id' : 0,
        'username' : '60218224@map',
        'password' : 'as123224',
        'btn_submit' : 'Login',
        'is_ajax': 1,
}

form_log = {
        'proc_val' : 'proc_log',
        'txt_tgl_awal' : '13-12-2021',
        'txt_no_induk_s' : '1609',
        'txt_tgl_akhir' : '13-12-2021',
        'cmb_dep' : '0',
        'txt_name_s' : '1609',
        'btn_submit' : '',
}
print("\n==========ABSEN ILLEGAL ALFINETWORK==============\n")

with requests.Session() as sesi:
        p = sesi.post(url_login, data=form_login)
        print("Behasil Login Bos...")
#       r = sesi.get(url_home)
#       r = sesi.post(url_log, data=form_log)
#       r = sesi.post(url_absen, dat=form_absen)
        print("================MENU=============================")
        print("1. Absen")
        print("2. Log Absen")
        print("=================================================")
        pilih = int(input("Pilihan : "))

        if(pilih == 1):
                ulang = int(input("Berapa kali : "))
                if(int(ulang) > 0 ):
                        for x in range(int(ulang)):
                                ab = sesi.post(url_absen, data=form_absen)
                                print(waktu_sekarang)
                                print(ab.text)
        elif(pilih == 2):
                log = sesi.post(url_log, data=form_log)
                print(log.text)
        else:
                print('Pilihan Salah!')
print("\n==========PROGRAM SELESAI===================\n")
