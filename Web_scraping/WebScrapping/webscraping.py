import requests, openpyxl
from bs4 import BeautifulSoup

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Top Rated Movies'
sheet.append(['Rank', 'Score', 'Movie Name', 'Synopsis'])

try:
    source = requests.get('https://editorial.rottentomatoes.com/guide/best-movies-2022/')
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')

    movies = soup.find('div', class_='articleContentBody').find_all('div', class_='row countdown-item')

    for movie in movies:
        name = movie.find('h2').a.text
        rank = movie.find('div', class_='countdown-index').text
        score = movie.find('span', class_='tMeterScore').text
        synopsis = movie.find('div', class_='info synopsis').text.strip('Synopsis: ').strip('[More]')
        sheet.append([rank, score, name, synopsis])

except Exception as e:
    print(e)

print('Done!')
excel.save('Rottentomatoes Ratings.xlsx')


