import requests
from bs4 import BeautifulSoup

# this link for checking population of cities in united kingdom
url = 'https://worldpopulationreview.com/countries/cities/united-kingdom'
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')

# creating beautifulsoup object
soup_data = soup.find('tbody', {'class': 'jsx-1911055634'})

# storing data into file
output_file = open('UK.txt', 'w')


# printing data of cities and populations in there
def find_all_datas():
    for sdata in soup_data:
        title = sdata.find_all('td')
        print('city - ' + title[0].text, ' , ' + 'population - ' + title[1].text)
        output_file.write('city - ' + title[0].text + ' , ' + 'population - ' + title[1].text + '\n\n')


# for find population in cities
def search_population(city_name):
    for data in soup_data:
        city = data.find_all('td')[0].text
        population = data.find_all('td')[1].text
        if any(s.lower() in city.lower() for s in city_name):
            print(city, ',' + 'population -' + ' ' + population)


# creating objects

# can add city name in list for find population
sort = ['london', 'liverpool']

# get all data from website
search_population(sort)

# used for search population in cities
find_all_datas()
