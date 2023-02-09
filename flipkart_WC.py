import requests
from bs4 import BeautifulSoup
import pandas as pd

name=[]
price=[]
description=[]
reviews=[]



def get_data(url):
    for i in range(1,10):
        url_=url+str(i)
        r= requests.get(url_)

        soup=BeautifulSoup(r.text,'html.parser')


        box=soup.find('div',class_="_1YokD2 _3Mn1Gg")

        div_=box.find_all('div',class_='_4rR01T')


        for i in div_:
            a=i.text
            name.append(a)
        


        price_=box.find_all('div',class_='_30jeq3 _1_WHN1')

        for i in price_:
            b=i.text
            price.append(b)
        


        description_=box.find_all('ul',class_='_1xgFaf')

        for i in description_:
            c=i.text
            description.append(c)
        


        reviews_=box.find_all('div',class_='_3LWZlK')

        for i in reviews_:
            d=i.text
            reviews.append(d)
        
    # if len(reviews)!=len(name):



    # print(name)
    # print(len(description))
    # print(len(reviews))
    # print(len(name))

get_data("https://www.flipkart.com/search?q=mobile+under+10000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_9_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_9_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobile+under+10000%7CMobiles&requestId=b580910a-09bd-446d-bbb7-04a4c9968634&page=")

df={"Product_name":name,"Price":price,"Description":description,"Reviews":reviews}
df=pd.DataFrame.from_dict(df,orient='index')
df=df.transpose()
df.to_csv('Flipkart_pages_2.csv')


