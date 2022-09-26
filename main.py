import requests
from bs4 import BeautifulSoup
import json
import pandas as pd


page = 50

url = 'https://www.imdb.com/search/title/?title_type'
param = {
    'title_type': 'feature',
    "year": "2020-01-01,2022-12-31",
    'start':page
}
header ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}



res = requests.get(url,params=param,headers=header)
soup = BeautifulSoup(res.text,'html.parser')

im = soup.find('div','lister-list')
go = im.find_all('h3')

data_m = []

for judul in go:
    getIdMovie = judul.find('a')['href']
    getJudul = judul.find('a').text


    datalist = {
        'judul' : getJudul,
        'link' : getIdMovie
    }

    data_m.append(datalist)


    df = pd.DataFrame(data_m)
    df.to_excel('ex.xlsx',index=False)







