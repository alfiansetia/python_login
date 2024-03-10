import requests
import json
from prettytable import PrettyTable
from dotenv import load_dotenv
import os

load_dotenv()
email = os.getenv("email")
passw = os.getenv("passw")

url_login = "https://motis.djka.dephub.go.id/validate"
url_cek = "https://motis.djka.dephub.go.id/daftar/check-quota"

form_data = {
    "username": email,
    "password": passw,
}

form_cek = {
    "tripType" : "ROUNDTRIP",
    "arrivalId" : 6,
    "departureId" : 2,
    "arrivalDate" : "17/04/2024",
    "departureDate" : "06/04/2024"
}
kata ="Login gagal"

with requests.Session() as sesi:
    login = sesi.post(
        url=url_login,
        data=form_data,
    )
    # print(login.text)
    try:
        login.text.index(kata)
        #   if(hasil.text.index(kata)):
        print("Respon Gagal")
        # print(login.text.index(kata))
    except:
        data = sesi.post(
            url=url_cek,
            data=form_cek
        )
        parsed_data = json.loads(data.text)
        print(parsed_data)
    #       print(kata+' ke  '+str(i))
    #       else:
    # else:
    #         #print('Respon Berhasil')
    #         print("Respon Else")
    
    
