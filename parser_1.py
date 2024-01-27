from LxmlSoup import LxmlSoup
import requests

html = requests.get('https://papers.nips.cc/paper_files/paper/2022').text  # получаем html код сайта
soup = LxmlSoup(html)  # создаём экземпляр класса LxmlSoup


text_1 = soup.find_all("a", title ="paper title")

arr = []
for i, link in enumerate(text_1):
    url = link.get("href")
    name = link.text()
    a = [url, name]
    arr.append(a)

# html1 = requests.get(arr[0][0]).text  # получаем html код сайта
# soup1 = LxmlSoup(html1)  # создаём экземпляр класса LxmlSoup
# print(html1)
    