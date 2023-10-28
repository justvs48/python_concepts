from bs4 import BeautifulSoup
import requests
url ='https://www.tutorialspoint.com/index.htm'
resp=requests.get(url)
print(resp.status_code,"\n")
soup=BeautifulSoup(resp.text, "html.parser")
print(soup.title)
for link in soup.find_all('img'):
    print(link.get('src'))

