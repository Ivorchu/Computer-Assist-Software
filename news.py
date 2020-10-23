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
    text = tk.Text(window, width=80, fg='blue', font=font, padx = 5, pady = 5) 
    for i in range(total_rows): 
        for j in range(total_columns): 
            text.grid(row=3, column=0) 
            text.insert(END, lst[i][j])
            text.insert(END, '\n')
    entry = tk.Entry(window, width = 80)
    entry.grid(row = 1, column = 0, pady = 5, padx = (5, 220))   
    btn_exe = tk.Button(window, text='搜尋', width=5, height=1, bd=0, bg = "#D35400", fg = "white", anchor = "center", command = search)
    btn_exe["font"] = font 
    btn_exe.grid(row = 2, column = 0, pady = 5, padx = (0, 220))


def search():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions") 
    options.add_experimental_option("detach", True) 
    driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe", options=options)
    driver.get(url+'search/word/2/'+entry.get())



