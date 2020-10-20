#coding:UTF-8
import requests
from bs4 import BeautifulSoup
import tkinter as tk

r = requests.get("http://www.taiwanlottery.com.tw/")
html_str = r.text
soup = BeautifulSoup(html_str, "html.parser")

#10 kinds of lottery

def bingobingo():
    bingobingo_1()
    bingobingo_2()
    bingobingo_3()
    bingobingo_4()
    return 0;


def bingobingo_1():
    target = soup.find_all('div', class_='ball_box01')
    list = ""
    for i in target:
        list += i.text
    return("賓果賓果BingoBingo \n" + "開出獎號: " + list)

    
    # 超級獎號
def bingobingo_2():
    target = soup.find_all('div', class_='ball_red')
    list = ""
    for i in target:
        list += i.text
    return("超級獎號: " + list[:2])

    
def bingobingo_3():
    # 猜大小
    target = soup.find_all('div', class_='ball_blue_BB1')
    list = ""
    for i in target:
        list += i.text
    return("猜大小: " + list[:2])


def bingobingo_4():
    # 猜單雙
    target = soup.find_all('div', class_='ball_blue_BB2')
    list = ""
    for i in target:
        list += i.text
    return("猜單雙: " + list[:2])


def win_win():
    target = soup.find_all('div', class_='ball_tx ball_blue')
    list = ""
    for i in target:
        list += i.text
    return("雙贏彩 \n" + "開出順序: " + list[:36] + "\n" + "大小順序: " + list[36:])


def powercolor():
    powercolor_1()    
    powercolor_2()


def powercolor_1():
    target = soup.find_all('div', class_='ball_tx ball_green')
    list = ""
    for i in target:
        list += i.text
    return("威力彩 \n" + "開出順序: " + list[:18] + "\n" + "大小順序: " + list[18:36])
    

def powercolor_2():
    target = soup.find_all('div', class_='ball_red')
    list = ""
    for i in target:
        list += i.text
    return("第二區: " + list[2:4])


def lottery38():
    target = soup.find_all('div', class_='ball_tx ball_green')
    list = ""
    for i in target:
        list += i.text
    return("38樂台彩 \n" + "開出順序: " + list[36:54] + "\n" + "大小順序: " + list[54:72])


def biglottery():
    biglottery_1()
    biglottery_2()

def biglottery_1():
    target = soup.find_all('div', class_='ball_tx ball_yellow')
    list = ""
    for i in target:
        list += i.text
    return("大樂透 \n" + "開出順序: " + list[60:78] + "\n" + "大小順序: " + list[78:96])
    

    # 特別號
def biglottery_2():
    target = soup.find_all('div', class_='ball_red')
    list = ""
    for i in target:
        list += i.text
    return("特別號:" + list[4:7])


def lottery49():
    target = soup.find_all('div', class_='ball_tx ball_yellow')
    list = ""
    for i in target:
        list += i.text
    return("49樂台彩 \n" + "開出順序: " + list[96:114] + "\n" + "大小順序: " + list[114:132])


def todaylottery539():
    target = soup.find_all('div', class_='ball_tx ball_lemon')
    list = ""
    for i in target:
        list += i.text
    return("今彩539 \n" + "開出順序: " + list[:15] + "\n" + "大小順序: " + list[15:30])

def lottery39():
    target = soup.find_all('div', class_='ball_tx ball_lemon')
    list = ""
    for i in target:
        list += i.text
    return("39樂台彩 \n" + "開出順序: " + list[30:45] + "\n" +"大小順序: " + list[45:63])


def threestarlottery():
    target = soup.find_all('div', class_='ball_tx ball_purple')
    list = ""
    for i in target:
        list += i.text +" "
    return("三星彩\n" + "中獎號碼: " + list[:6])


def fourstarlottery():
    target = soup.find_all('div', class_='ball_tx ball_purple')
    list = ""
    for i in target:
        list += i.text + " "
    return("四星彩 \n" + "中獎號碼: " + list[6:15])


def main(window, font):
    def ask():
        all_lottery = {
        "賓果賓果": bingobingo(),
        "雙贏彩": win_win(),
        "威力彩": powercolor(),
        "38樂台彩": lottery38(),
        "大樂透": biglottery(),
        "49樂台彩": lottery49(),
        "今彩539": todaylottery539(),
        "39樂台彩": lottery39(),
        "三星彩": threestarlottery(),
        "四星彩": fourstarlottery(),
        } 
        all_lottery[statement]

       
    # text = tk.Label(text = "Enter lottery", anchor = "center")
    var = tk.StringVar()
    #entry1 = tk.Entry(window)
    content = tk.Entry(window, textvariable = var)
    content.grid(row = 1, column = 1, pady = (150, 10), padx = 160) 
    statement = var.get()
    btn_exe = tk.Button(window, text='Search', width=5, height=1, bd=0, bg = "#D35400", fg = "white", anchor = "w", command = ask)
    btn_exe["font"] = font 
    btn_exe.grid(row = 2, column = 1, pady = (10, 150), padx = 160) 


