#coding: utf-8
from tkinter import *
from bs4 import BeautifulSoup
import requests
import tkinter as tk

url = 'https://udn.com/news/breaknews/'

def refreshNews(window, font):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    lst = []
    news = soup.find_all('div', class_='story-list__text')
    for data in news:
        if data.select_one('a').get('title') != None:
            lst.append((data.select_one('a').getText(), 'udn.com' + data.select_one('a').get('href') + '\n'))

    total_rows = len(lst) 
    total_columns = len(lst[0])
    e = tk.Text(window, width=80, fg='blue', font=font)
    for i in range(total_rows): 
        for j in range(total_columns): 
            e.grid(row=i, column=j) 
            e.insert(END, lst[i][j])
            e.insert(END, '\n')



