import requests
import randomheaders
from bs4 import BeautifulSoup as soup


tp= ['https://www.walmart.com/ip/6-Pack-Scott-Rapid-Dissolving-Toilet-Paper-8-Rolls-Bath-Tissue/217279228?selected=true','https://www.walmart.com/ip/Angel-Soft-Toilet-Paper-24-Mega-Rolls-96-Regular-Rolls/341013821','https://www.walmart.com/ip/3-Pack-Scott-Rapid-Dissolving-Toilet-Paper-8-Rolls-Bath-Tissue/212484728?selected=true','https://www.walmart.com/ip/Huggies-Simply-Clean-Baby-Wipes-Unscented-704-Count/942573335?selected=true']
# print(source.status_code)
# page_soup = soup(tp1.text, "html.parser")
# tp = (page_soup.find_all('div', class_="prod-ProductOffer-oosMsg prod-PaddingTop--xxs"))
# # colors = page_soup.find_all('a', class_= True)
# # x=[]

def walmart_monitor (tp):
    for i in tp:
        print(i)
        r =requests.get(i,headers = randomheaders.LoadHeader()).text
        page_soup = soup(r, 'html.parser')
        tp = (page_soup.find_all('div', class_="prod-ProductOffer-oosMsg prod-PaddingTop--xxs"))
        for i in tp:
            if i.text == 'Out of stock':
                print('out of stock')
            else:
                return i

walmart_monitor(tp)
