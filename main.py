from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.sathyabama.ac.in/")
soup = BeautifulSoup(response.text,"html.parser")

news = soup.find_all(class_="content-wrp")

#<div class="content-wrp">
for heading in news:
     print(heading.find(class_="title").getText().strip()) 
     print(heading.find(class_="date").getText().strip())
     link = heading.find(class_="view-more-right").find(name="a").get("href")
     print("https://www.sathyabama.ac.in/"+link)
     print("")
     
