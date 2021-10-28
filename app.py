import requests
from bs4 import BeautifulSoup

# this link for checking population of cities in united kingdom
url = 'https://worldpopulationreview.com/countries/cities/united-kingdom'
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')

# creating beautifulsoup object
datas = soup.find('tbody', {'class': 'jsx-1911055634'})

# printing data of cities and populations in there
for data in datas:
    title = data.find_all('td')
    print('city - ' + title[0].text, ' , '+'population - ' + title[1].text)
