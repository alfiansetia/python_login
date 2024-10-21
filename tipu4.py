import requests
import re

r = requests.get('https://cheveapps-x0-x1xxx.vercel.app/token.js')
text = r.text

url_pattern = re.compile(r"url: '([^']+otp\.php)'")
match = url_pattern.search(text)

if match:
    url = match.group(1)
    print("URL ditemukan:", url)
else:
    print("URL tidak ditemukan.")
