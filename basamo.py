import requests
from prettytable import PrettyTable
from bs4 import BeautifulSoup
import time

def get_link():
    url = 'https://pulangbasamo.com/'
    r = requests.get(url)
    html_content = r.text
    soup = BeautifulSoup(html_content, "html.parser")
    buttons = soup.find_all("a", class_="elementor-button")

    for button in buttons:
        if button.find("span", class_="elementor-button-text") and button.find("span", class_="elementor-button-text").text.strip() == "DAFTAR TUJUAN PADANG":
            link = button["href"]
            print("Link tombol DAFTAR TUJUAN PADANG:", link)
            break

state= True
while(state):
    try:
        get_link()
        time.sleep(5)
    except KeyboardInterrupt:
        state : False
    except:
        state:False
        # 
