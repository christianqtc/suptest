import requests
from bs4 import BeautifulSoup as bs

session = requests.Session()

url = "https://www.supremenewyork.com/shop/all"
item_search = 'Expedition'
item_color = 'Black'

def get_links():
    list_of_links = []
    response = session.get(url)

    starts_links = ("/shop/all", "/shop/cart", "/shop/new")

    soup = bs(response.text, "html.parser")

    for links in soup.find_all("a", href=True):
        if links['href'].startswith('/shop/'):
            if not links['href'].startswith(starts_links):
                list_of_links.append('https://www.supremenewyork.com' + links['href'])
                print("Links found: ", links['href'])
    print(list_of_links)
    return list_of_links

def get_items():
    list_of_links1 = get_links()
    for url2 in list_of_links1:
        response = session.get(url2)
        soup = bs(response.text, "html.parser")
        item_title_lower = soup.find("title").string.lower()
        print(item_title_lower)
        if item_search.lower() and item_color.lower() in item_title_lower:
            found_link = url2
            print(found_link + ": FOUND")
            break
        else:
            print('Not found.')
'''
def add_to_cart():
'''


get_items()
