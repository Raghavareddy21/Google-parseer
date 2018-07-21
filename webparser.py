from bs4 import BeautifulSoup
import requests
search=raw_input("Enter the link:")
base = "http://www.google.de"
url = "http://www.google.de/search?q="+ search
response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")
for item in soup.select(".r a"):
    print(item.text)
for next_page in soup.select(".fl"):
    res = requests.get(base + next_page.get('href'))
    soup = BeautifulSoup(res.text,"lxml")
    for item in soup.select(".r a"):
        print(item.text)