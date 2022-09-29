from time import sleep
from unicodedata import name
from celery import shared_task
import requests
from bs4 import BeautifulSoup

from .models import CryptoCurrency


@shared_task
def crawl_currency():
    URL = 'https://coinmarketcap.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    webpage = requests.get(URL, headers=headers)
    soup = BeautifulSoup(webpage.text, 'lxml')

    get_table_row = soup.find_all('tr')

    count = 0
    for row in get_table_row:
        if count == 10:
            break
        ticker_name = row.find('p', attrs={
            'class': 'sc-1eb5slv-0 iworPT'
        })
        if ticker_name == None:
            continue
        else:
            current_row = row.select('td')
            splitter = str(count + 1)
            ticker = current_row[2].get_text().split(splitter)
            ticker_name = ticker[0]
            ticker_symbol = ticker[1]
            ticker_price = current_row[3].get_text()
            change_percent_1hr = current_row[4].get_text()
            change_percent_24hr = current_row[5].get_text()
            change_percent_7d = current_row[6].get_text()
            market_cap = current_row[7].get_text()
            volume = current_row[8].get_text()
            circulating_supply = current_row[9].get_text()
            data = {
                'price': ticker_price,
                'change_percentage_1h': change_percent_1hr,
                'change_percentage_2h': change_percent_24hr,
                'change_percentage_7d': change_percent_7d,
                'market_cap': market_cap,
                'volume': volume,
                'supply': circulating_supply
            }
        count += 1
        if not CryptoCurrency.objects.filter(name=ticker_name).exists():
            CryptoCurrency.objects.create(
                name=ticker_name,
                price=ticker_price,
                change_percentage_1h=change_percent_1hr,
                change_percentage_2h=change_percent_24hr,
                change_percentage_7d=change_percent_7d,
                market_cap=market_cap,
                volume=volume,
                supply=circulating_supply
            )
        else:
            CryptoCurrency.objects.filter(
                name=ticker_name,
            ).update(**data)
            print(data)
    sleep(5)


crawl_currency()


while True:
    crawl_currency()
    print('__Updating__')
    # sleep(5)
