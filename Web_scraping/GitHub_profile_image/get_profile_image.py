import requests
from bs4 import BeautifulSoup as bs

github_user = input('Github user profile: ')
url = f'https://github.com/{github_user}'
req = requests.get(url)
soup = bs(req.content, 'html.parser')
profile_image = soup.find('img', {'alt': 'Avatar'})['src']
print(profile_image)