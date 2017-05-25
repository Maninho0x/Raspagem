import requests 
from bs4 import BeautifulSoup 

tituloAnime = [] 


response = requests.get ("https://myanimelist.net/topanime.php?type=airing") 

if response.status_code == 200:
  bsoup = BeautifulSoup(response.content, "html.parser")

  charts = bsoup.findAll("div", class_="detail")

for row in charts:
    tituloAnime.append(row.find('a').get_text())
    

for x in range(0, 50):
    print (x+1, tituloAnime[x].strip()) 

else:
    print ("A requisicao falhou!") 
