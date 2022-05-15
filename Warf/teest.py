import requests
from bs4 import BeautifulSoup


def par():
    URL = 'https://hobbygames.ru/nastolnie'    #ссылка
    Headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
    } #Маска
    resp = requests.get(URL, headers = Headers)
    soup = BeautifulSoup(resp.content, 'html.parser')
    boxs = soup.findAll('div', class_ = 'col-lg-4 col-md-6 col-sm-6 col-xs-12') #
    game = []
    for i in boxs:
        game.append({
            'price': i.find('span', class_ = 'price').get_text(strip = True),
            'name': i.find('a', class_ = 'name').get_text(strip = True),
            'link': i.find('a', class_ = 'name').get('href'),
            'coop': i.find('div', class_ = 'age__number').get_text(strip = True)
            })
    for j in game:
        print (f'\n Товар: {j["name"]}\n Новая цена: {j["price"]}\n Ссылка: {j["link"]}\n Кол-во человек: {j["coop"]}')
par()
