import json
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent


class ZillowSearchListing:
    def __init__(self, url):
        self.url = url
        ua = UserAgent()
        self.user_agent = ua.random
        self.accept_language = 'en-US,en;q=0.9'
        self.soup = self.create_soup()
        self.property_list = []
        self.link_list = []
        self.address_list = []
        self.price_list = []
        self.total_pages = 0
        self.results_per_page = 0
        self.total_results = 0
        # self.query_info()
        self.required_list_data()

    def create_soup(self):
        headers = {
            'User-Agent': self.user_agent,
            'Accept-Language': self.accept_language,
        }
        response = requests.get(url=self.url, headers=headers)
        response.raise_for_status()
        return bs(response.text, 'html.parser')

    def query_info(self):
        soup = self.soup
        data = json.loads(soup.find("script", attrs={
                          "data-zrr-shared-data-key": "mobileSearchPageStore"}).text.strip('<!->'))
        # data = json.loads(soup.select_one("script[data-zrr-shared-data-key]").contents[0].strip("!<>-"))
        self.total_pages = data['cat1']['searchList']['totalPages']
        self.results_per_page = data['cat1']['searchList']['resultsPerPage']
        self.total_results = data['cat1']['searchList']['totalResultCount']
        print(f"Your query have {self.total_pages} pages. Each page have almost {self.results_per_page} results."
              f" Total results are {self.total_results}.")

    def required_list_data(self):
        soup = self.soup
        # both ways it works 100%
        data = json.loads(soup.find("script", attrs={
                          "data-zrr-shared-data-key": "mobileSearchPageStore"}).text.strip('<!->'))
        # data = json.loads(soup.select_one("script[data-zrr-shared-data-key]").contents[0].strip("!<>-"))

        addr_list = self.address_list
        lin_list = self.link_list
        pri_list = self.price_list

        for i in data["cat1"]['searchResults']['listResults']:
            link = i['detailUrl']
            if 'https' not in link:
                lin_list.append('https://www.zillow.com/'+link)
                pri_list.append(i['units'][0]['price'].split('+')[0])
                building_name = i['buildingName']
                if building_name is None:
                    addr_list.append(f"{i['address']}")
                else:
                    addr_list.append(f"{building_name}, {i['address']}")
            else:
                lin_list.append(link)

                address = i['address']
                if 'bed' in address:
                    li = address.split(',')
                    set_address = ""
                    for j in li:
                        if 'bed' in j or 'sqft' in j or '$' in j:
                            pass
                        else:
                            set_address = set_address + j + ","
                    addr_list.append(set_address)
                else:
                    addr_list.append(address)

                price = i['price'].split('/')[0]
                if "+" in price:
                    pri_list.append(price.split('+')[0])
                else:
                    pri_list.append(price)
