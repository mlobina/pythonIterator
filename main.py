import requests
import json
import os


link = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'

class SearchEngine:

    def __init__(self, link):
        self.link = link

    def download_file(self, link):
        link = self.link
        file_name = link.split('/')[-1]
        resp = requests.get(link, allow_redirects=True)
        with open(file_name, 'wb') as file:
            file.write(resp.content)
            return file_name

    def get_countries_data(self, file_name):
        self.file_name = file_name
        with open(file_name, 'rb') as file:
            countries_data = json.load(file)
            return countries_data

    def get_wiki_links(self, countries_data):
        self.countries_data = countries_data

        if os.path.isfile('countries_wiki_links.txt') == True:
            os.remove('countries_wiki_links.txt')
        else:
            pass
        for item in countries_data:
            country = item['name']['official']
            with open('countries_wiki_links.txt', 'a') as file:
                file.write(f'{country} - "https://en.wikipedia.org/wiki/{country}", \n')


    def main(self):
        self.get_wiki_links(self.get_countries_data(self.download_file(link)))

wiki_searcher = SearchEngine(link)

wiki_searcher.main()

