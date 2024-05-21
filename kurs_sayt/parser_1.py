from LxmlSoup import LxmlSoup
import requests
import json
import pandas as pd
import PyPDF2
from io import BytesIO
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle


def predict_article_quality(article_text):    

    with open('tokenizer.pkl', 'rb') as handle:        
        tokenizer = pickle.load(handle)
    model = load_model('model.h5')
    seq = tokenizer.texts_to_sequences([article_text])
    max_len = 500    
    pad_seq = pad_sequences(seq, maxlen=max_len)
    prediction = model.predict(pad_seq)    
    if prediction[0][0] >= 0.5:
        return '1'    
    else:
        return '0'

html = requests.get('https://papers.nips.cc/paper_files/paper/2022').text 
soup = LxmlSoup(html)  


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
    name2 = name.replace(' ', '+')
    url3 = "https://scholar.google.com/scholar?hl=ru&as_sdt=0%2C5&q=" + name2 + "="
    a = {"url": url, "name":name, "authors": authors, "url2": url3, "name2": name2}

    response = requests.get(url2)

    q_control = 0

    if response.status_code == 200:
        file = BytesIO(response.content)
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
                text += page.extract_text() + "\n"
                q_control = predict_article_quality(text)
                a = {"url": url, "name":name, "authors": authors, "isGood": 1, "name2": name2}
                

    arr.append(a)
    if i == 50:
          break

with open('./data.json', 'w') as file:
        json.dump(arr, file)

print('Data1 was parsed')

    