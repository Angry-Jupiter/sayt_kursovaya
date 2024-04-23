from LxmlSoup import LxmlSoup
import requests
import json

html = requests.get('https://papers.nips.cc/paper_files/paper/2022').text  # получаем html код сайта
soup = LxmlSoup(html)  # создаём экземпляр класса LxmlSoup


text_1 = soup.find_all("a", title ="paper title")

arr = []
for i, link in enumerate(text_1):
    url = 'https://papers.nips.cc' + link.get("href")
    name = link.text()
    html2 = requests.get(url).text
    soup2 = LxmlSoup(html2)
    text_2 = soup2.find_all("i")
    authors = text_2[0].text()
    a = {"url": url, "name":name, "authors": authors}
    arr.append(a)
    if i == 100:
          break

with open('./data.json', 'w') as file:
        json.dump(arr, file)

print('Data1 was parsed')

    