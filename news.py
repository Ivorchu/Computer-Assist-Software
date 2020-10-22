#coding: utf-8
from tkinter import *
from bs4 import BeautifulSoup
import requests
import tkinter as tk
from selenium import webdriver

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
    text = tk.Text(window, width=80, fg='blue', font=font)
    for i in range(total_rows): 
        for j in range(total_columns): 
            text.grid(row=i, column=j) 
            text.insert(END, lst[i][j])
            text.insert(END, '\n')
    entry = tk.Entry(window)
    entry.grid(row = 0, column = 1, pady = 5) 
    btn_exe = tk.Button(window, text='Search', width=5, height=1, bd=0, bg = "#D35400", fg = "white", anchor = "w", command = search)
    btn_exe["font"] = font 
    btn_exe.grid(row = 1, column = 1, pady = 5)
    

def search():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions") 
    options.add_experimental_option("detach", True) 
    driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe", options=options)
    driver.get(url+'search/word/2/'+entry.get())



