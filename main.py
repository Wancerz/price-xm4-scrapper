import requests
from bs4 import BeautifulSoup
import time
import json
# url_list = ["https://www.amazon.pl/Sony-WH-1000XM4-bezprzewodowe-sluchawki-sterowanie/dp/B08C7KCJF5/ref=asc_df_B08C7KCJF5/?tag=plshogostdde-21&linkCode=df0&hvadid=504516820791&hvpos=&hvnetw=g&hvrand=17379220845896933618&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061067&hvtargid=pla-936807621760&psc=1",
#             "https://www.amazon.pl/Sony-WH-1000XM4-bezprzewodowe-sluchawki-sterowanie/dp/B091CQH6VT/ref=asc_df_B08C7KCJF5/?tag=plshogostdde-21&linkCode=df0&hvadid=504516820791&hvpos=&hvnetw=g&hvrand=17379220845896933618&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061067&hvtargid=pla-936807621760&th=1",
#             "https://www.amazon.pl/Sony-WH-1000XM4-bezprzewodowe-sluchawki-sterowanie/dp/B08C7KG5LP/ref=asc_df_B08C7KCJF5/?tag=plshogostdde-21&linkCode=df0&hvadid=504516820791&hvpos=&hvnetw=g&hvrand=17379220845896933618&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061067&hvtargid=pla-936807621760&th=1",
#             ]
url_list = {"media_expert":{"media_black_xm4":"https://www.mediaexpert.pl/telewizory-i-rtv/sluchawki/wszystkie-sluchawki/sluchawki-nauszne-sony-wh-1000xm4b-czarny",
                            "media_blue_xm4" :"https://www.mediaexpert.pl/telewizory-i-rtv/sluchawki/wszystkie-sluchawki/sluchawki-bluetooth-sony-wh1000xm4l-ce7-anc-nauszne-granatowe",
                            "media_black_xm5":"https://www.mediaexpert.pl/telewizory-i-rtv/sluchawki/wszystkie-sluchawki/sluchawki-bluetooth-sony-wh1000xm5b-ce7-anc-nauszne-czarne",
                            "media_white_xm5":"https://www.mediaexpert.pl/telewizory-i-rtv/sluchawki/wszystkie-sluchawki/sluchawki-bluetooth-sony-wh1000xm5s-ce7-anc-nauszne-srebrne"}
            # "euro_rtv_agd":["https://www.mediaexpert.pl/telewizory-i-rtv/sluchawki/wszystkie-sluchawki/sluchawki-bluetooth-sony-wh1000xm5b-ce7-anc-nauszne-czarne",
            #                 "https://www.mediaexpert.pl/telewizory-i-rtv/sluchawki/wszystkie-sluchawki/sluchawki-bluetooth-sony-wh1000xm5s-ce7-anc-nauszne-srebrne"]
}

with open("./price.json") as file:
    temp_dict = file.read()
    price = json.loads(temp_dict)
print(price)
price_temporary = {}


def get_price(shop_name, link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')

    if shop_name == 'media_expert':
        blog_titles = soup.find('div', attrs={ "class":"main-price is-big"})
        return blog_titles.text[0:-5]
    if shop_name == 'rtv_euro_agd':
        return


HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'})

for shop in url_list: 
    print(shop)

    for link in url_list[shop]:

        # price_temporary[return_value[0]] = return_value[1] 
        print(link)
        price_temporary[link] = int(get_price(shop, url_list[shop][link]).replace("\u202f", ""))


# response = requests.get("https://www.euro.com.pl/sluchawki/sony-sluchawki-bt-nc-wh1000xm4b-ce7-czarne.bhtml",headers=HEADERS,timeout=60)
# soup = BeautifulSoup(response.content, 'html.parser')
# # print(soup)
# blog_titles = soup.find('div', attrs={ "class":"product-price selenium-price-normal"})
# print(blog_titles.text)
# print(price_temporary)




