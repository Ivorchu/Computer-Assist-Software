#coding: utf-8
from tkinter import *
from bs4 import BeautifulSoup
import requests

url = 'https://udn.com/news/breaknews/'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
lst = []

class Newstable:
    def __init__(self, root):
        for i in range(total_rows): 
            for j in range(total_columns): 
                  
                self.e = Entry(root, width=20, fg='blue', font=('Arial',16,'bold')) 
                  
                self.e.grid(row=i, column=j) 
                self.e.insert(END, lst[i][j])

news = soup.find_all('div', class_='story-list__text')
for data in news:
    if data.select_one('a').get('title') != None:
        lst.append((data.select_one('a').getText(), 'udn.com' + data.select_one('a').get('href')))
