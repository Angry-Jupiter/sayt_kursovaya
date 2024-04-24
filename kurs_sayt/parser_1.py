from LxmlSoup import LxmlSoup
import requests
import json
import PyPDF2
from io import BytesIO

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
    authors = text_2[2].text()
    text_3 = soup2.find_all("a", class_ = "btn btn-primary btn-spacer")
    url2 = "https://proceedings.neurips.cc" + text_3[0].get("href")
    a = {"url": url, "name":name, "authors": authors, "url2": url2}

    response = requests.get(url2)

    if response.status_code == 200:
        file = BytesIO(response.content)
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
                text += page.extract_text() + "\n"

                print(text)  # Выводим текст
        else:
                print("Failed to retrieve PDF")


    html3 = requests.get(url2).text
    print(html3)
    arr.append(a)
    if i == 3:
          break

with open('./data.json', 'w') as file:
        json.dump(arr, file)

print('Data1 was parsed')

    