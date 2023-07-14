import requests
from bs4 import BeautifulSoup
import json

myStocks = ['.SPX', '.IXIC', '.AXJO', '.N225', '.GDAXI', '@GC.1', '@LCO.1', 'BTC.CB=', 'ETH.CM=']
stockData = []

def getData(symbol):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    url = f'https://www.cnbc.com/quotes/{symbol}'
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    stock = {
        'symbol': symbol,
        'price': soup.find('div', {'class': 'QuoteStrip-lastPriceStripContainer'}).find_all('span')[0].text,
        'change': soup.find('div', {'class': 'QuoteStrip-lastPriceStripContainer'}).find_all('span')[1].text
    }
    return stock

for item in myStocks:
    stockData.append(getData(item))
    print('Getting data from: ', item)

with open('stockdata.json', 'w') as file:
    json.dump(stockData, file)

print('The end.')