import requests
from bs4 import BeautifulSoup

# this link for checking population of cities in united kingdom
url = 'https://worldpopulationreview.com/countries/cities/united-kingdom'
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')

# creating beautifulsoup object
datas = soup.find('tbody', {'class': 'jsx-1911055634'})

print(datas.text)