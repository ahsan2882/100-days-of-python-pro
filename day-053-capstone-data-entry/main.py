from zillow_search_listing import ZillowSearchListing
from google_form import GoogleForm

zlow_url = 'https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D' \
           '%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A' \
           '-122.56362048510742%2C%22east%22%3A-122.30303851489258%2C%22south%22%3A37.69560228625891%2C' \
           '%22north%22%3A37.85489581746635%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C' \
           '%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A' \
           '%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D' \
           '%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A' \
           '%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22' \
           '%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D' \
           '%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C' \
           '%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'


url_list = []
for url_num in range(1, 18):
    if url_num != 1:
        change_url = f"{zlow_url[:48]}{url_num}_p/{zlow_url[48:92]}22currentPage%22%3A{url_num}%{zlow_url[92:]}"
        url_list.append(change_url)
    else:
        url_list.append(zlow_url)

complete_pages_price_list = []
complete_pages_link_list = []
complete_pages_address_list = []
page_ = 1
for url in url_list:
    z = ZillowSearchListing(url)
    print(page_)
    for price in z.price_list:
        complete_pages_price_list.append(price)
    for address in z.address_list:
        complete_pages_address_list.append(address)
    for link in z.link_list:
        complete_pages_link_list.append(link)
    page_ += 1
print("START SENDING")
g = GoogleForm()
g.update_form(complete_pages_address_list,
              complete_pages_price_list, complete_pages_link_list)
