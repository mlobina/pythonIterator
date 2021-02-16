import requests
import json
import os


link = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'

class SearchEngine:

    def __init__(self, link):
        self.link = link

    def download_file(self):

        file_name = self.link.split('/')[-1]
        resp = requests.get(self.link, allow_redirects=True)
        with open(file_name, 'wb') as file:
            file.write(resp.content)
            return file_name

    def get_countries_data(self, file_name):
        self.file_name = file_name
        with open(file_name, 'rb') as file:
            data = json.load(file)
            return data

searcher1 = SearchEngine(link)

data = searcher1.get_countries_data(searcher1.download_file())

class Iterator:

    def __init__(self, countries=data, start=-1):
        self.countries = countries
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < (len(self.countries)-1):
            self.start += 1
            country = self.countries[self.start]['name']['official']
            return country
        raise StopIteration

    def print_file(self):
        if os.path.isfile('countries_wiki_links.txt') == True:
            os.remove('countries_wiki_links.txt')
        else:
            pass
        for country in Iterator():
            with open('countries_wiki_links.txt', 'a') as file:
                file.write(f'{country} - "https://en.wikipedia.org/wiki/{country}", \n')


iterator1 = Iterator()

iterator1.print_file()
