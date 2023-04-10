import requests

url_post = 'https://api-order.eriksanjaya.com/trx-order'

for x in range(10):
    p = requests.post(url=url_post, data={
        'nama' : 'I Love YOU1 ' + str(x),
        'email' : 'i.love.you1' + str(x) + '@gmail.com',
        'hp' : '62856969691' + str(x+1),
        'hostname' : 'ilove1' + str(x) + '.you',
        'produk' : 'bundle-d',
        'owner' : 'erik'
    })
    print(p.text)