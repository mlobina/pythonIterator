import requests
import json

link = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'


def download_file(link):
    file_name = link.split('/')[-1]
    resp = requests.get(link, allow_redirects=True)
    with open(file_name, 'wb') as file:
        file.write(resp.content)
    return file_name



def get_countries_data(file_name):
    with open(file_name, 'rb') as file:
        countries_data = json.load(file)
        return countries_data

def get_wiki_links(countries_data):
   for item in countries_data:
        country = item['name']['official']
        with open('coutries_wiki_links.txt', 'a') as file:
            file.write(f'{country} - "https://en.wikipedia.org/wiki/{country}""\n"')







