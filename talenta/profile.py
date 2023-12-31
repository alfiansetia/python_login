import requests

data = {
    'page': 1,
    'limit': 100,
    'chunk': 101,
    'search': '',
    'sort': '',
    'sortBy': ''
}
url =  'https://hr.talenta.co/api/web/my-info/personal-data?id=1716409'
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'Referer': 'https://hr.talenta.co/employee/address-book?id=A',
    'Cookie': "visid_incap_2148199=GL9TBHWkRhSIu61OUYSjRfpuXGUAAAAAQUIPAAAAAABlhInLXA9enuRAgCSWbVnX; locale=id; nlbi_2148199=2/P0QCD0jxinUbXOP00cfwAAAADoAfCM4Ekkd3VOfCTGErjW; PHPSESSID=22495b6a884bf1e1b43109a429ae19bb; _csrf=808ade590af67fd08b816b74a1b83c74f3b513113a7deb1aa7c5d9ceb3a3ba64a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22Tc66JxC_5usDqueGKqqap59ACZ8Tqw37%22%3B%7D; _session_token=b00304f4d4d7715a63f12293ccbf75a3c026a65239950fb8365e31cfdbd98ac5a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_session_token%22%3Bi%3A1%3Bs%3A32%3A%22wPT5nk8kCDTXxq8Nv0jcSasbZcyOqAKB%22%3B%7D; mp_cb42d2d2055e96ad5e5103b170def62f_mixpanel=%7B%22distinct_id%22%3A%20%2212104%22%2C%22%24device_id%22%3A%20%2218bf1119f93a47-05c81beb590dc6-26031051-1fa400-18bf1119f94740%22%2C%22%24user_id%22%3A%20%2212104%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Faccount.mekari.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22account.mekari.com%22%7D; incap_ses_1112_2148199=MzYYYppmCR1UFIjbRZ9uDx5CkGUAAAAAZa84fv0Dp4WyirFRn/VKyg=="
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print('Request failed with status code:', response.status_code)
