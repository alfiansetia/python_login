import requests
import random
import string
import time

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

def generate_random_number(length):
    start = 10**(length-1)
    end = (10**length) - 1
    return random.randint(start, end)

calon = ['Calon 1 - [ SETYO HADI & SUGENG PRASETYO ]', 'Calon 2 - [ BAMBANG PUJIYANTO - CATUR SUGENG SUSANTO ]']
error =0
i = 0
state = True
while state:
    try:
        rand_calon = random.choice(calon)
        i = i+1
        data_pos = {
            'candidate': rand_calon
        }
        p = requests.post('https://pemilubupatigrobogan.reconet.co.id/vote.php', data=data_pos)
        p.raise_for_status()
        print(f"p: {p.status_code}, ke {i}, calon: {rand_calon}")
        error = 0
        # time.sleep(1)
    except KeyboardInterrupt:
        print('Stopped by user!')
        state = False
    except Exception as e:
         error = error+1
         if(error > 5):
             state = False
         print('Error : ' + str(e))
