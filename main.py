import requests
from bs4 import BeautifulSoup
from json_functions import json_functions
from mail import mail

class SHOP:
    def __init__(self) -> None:
        
        self.price_temporary = self.get_price_temporary()
        self.price = json_functions().open_json("price")
        if self.price_temporary != self.price:
            mail().send_mail(self.price,self.price_temporary)
        pass

    #scrapping prices from the shops
    def get_price(self,shop_name,link):

        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')

        if shop_name == 'media_expert':
            blog_titles = soup.find('div', attrs={ "class":"main-price is-big"})
            # print(blog_titles)
            if blog_titles is None:
                blog_titles = soup.find('div', attrs={ "class":"main-price for-action-price is-big"})
            return blog_titles.text[0:-5]
        if shop_name == 'rtv_euro_agd':
            return

    #load prices from json 
    def get_price_temporary(self,):
        self.price_temporary = {}
        self.url_list = json_functions().open_json("url")
        for self.shop in self.url_list: 
            print(self.shop)

            for self.link in self.url_list[self.shop]:
                print(self.link)
                self.price_temporary[self.link] = int(self.get_price(self.shop, self.url_list[self.shop][self.link]).replace("\u202f", "")) 
                print(self.price_temporary)
        return self.price_temporary




p1 = SHOP()

