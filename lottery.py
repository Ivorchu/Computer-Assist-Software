import requests
#coding:UTF-8
from bs4 import BeautifulSoup
import tkinter as tk
import sys

#reload(sys)
#sys.setdefaultencoding("utf-8")

r = requests.get("http://www.taiwanlottery.com.tw/")
html_str = r.text
soup = BeautifulSoup(html_str, "html.parser")

#10 kinds of lottery


def bingobingo_1():
    target = soup.find_all('div', class_='ball_box01')
    lst = []
    for i in target:
        lst.append(i) 
    #return("賓果賓果BingoBingo \n" + "開出獎號: " + lst )
    return lst

    
    # 超級獎號
def bingobingo_2():
    target = soup.find_all('div', class_='ball_red')
    lst = []
    for i in target:
        lst.append(i) 
    #return("超級獎號: " + lst [:2])
    return lst[:2]

    
def bingobingo_3():
    # 猜大小
    target = soup.find_all('div', class_='ball_blue_BB1')
    lst  = []
    for i in target:
        lst.append(i) 
    #return("猜大小: " + lst [:2])
    return lst [:2]


def bingobingo_4():
    # 猜單雙
    target = soup.find_all('div', class_='ball_blue_BB2')
    lst  = []
    for i in target:
        lst.append(i) 
    #return("猜單雙: " + lst [:2])
    return lst [:2]


def win_win():
    target = soup.find_all('div', class_='ball_tx ball_blue')
    lst  = []
    for i in target:
        lst.append(i) 
    #return("雙贏彩 \n" + "開出順序: " + lst [:36] + "\n" + "大小順序: " + lst [36:])
    return lst [:36], lst [36:]


def powercolor_1():
    target = soup.find_all('div', class_='ball_tx ball_green')
    lst = []
    for i in target:
        lst.append(i) 
    #return("威力彩 \n" + "開出順序: " + lst [:18] + "\n" + "大小順序: " + lst [18:36])
    return lst [:18], lst [18:36]


def powercolor_2():
    target = soup.find_all('div', class_='ball_red')
    lst = []
    for i in target:
        lst.append(i) 
    #return("第二區: " + lst [2:4])
    return lst [2:4]


def lottery38():
    target = soup.find_all('div', class_='ball_tx ball_green')
    lst = []
    for i in target:
        lst.append(i) 
    #return("38樂台彩 \n" + "開出順序: " + lst [36:54] + "\n" + "大小順序: " + lst [54:72])
    return lst [36:54], lst [54:72] 


def biglottery_1():
    target = soup.find_all('div', class_='ball_tx ball_yellow')
    lst = []
    for i in target:
        lst.append(i) 
    #return("大樂透 \n" + "開出順序: " + lst [60:78] + "\n" + "大小順序: " + lst [78:96])
    return lst [60:78], lst [78:96]


    # 特別號
def biglottery_2():
    target = soup.find_all('div', class_='ball_red')
    lst = []
    for i in target:
        lst.append(i) 
    #return("特別號:" + lst [4:7])
    return lst [4:7]


def lottery49():
    target = soup.find_all('div', class_='ball_tx ball_yellow')
    lst = []
    for i in target:
        lst.append(i) 
    #return("49樂台彩 \n" + "開出順序: " + lst [96:114] + "\n" + "大小順序: " + lst [114:132])
    return lst [96:114], lst [114:132]


def todaylottery539():
    target = soup.find_all('div', class_='ball_tx ball_lemon')
    lst = []
    for i in target:
        lst.append(i) 
    #return("今彩539 \n" + "開出順序: " + lst [:15] + "\n" + "大小順序: " + lst [15:30])
    return lst [:15], lst [15:30]


def lottery39():
    target = soup.find_all('div', class_='ball_tx ball_lemon')
    lst = []
    for i in target:
        lst.append(i) 
    #return("39樂台彩 \n" + "開出順序: " + lst [30:45] + "\n" +"大小順序: " + lst [45:63])
    return lst [30:45], lst [45:63]


def threestarlottery():
    target = soup.find_all('div', class_='ball_tx ball_purple')
    lst = []
    for i in target:
        lst.append(i) 
    #return("三星彩\n" + "中獎號碼: " + lst [:6])
    return lst [:6]


def fourstarlottery():
    target = soup.find_all('div', class_='ball_tx ball_purple')
    lst = str()
    for i in target:
        lst += i.text + " "
    #return("四星彩 \n" + "中獎號碼: " + lst [6:15])
    return lst[6:15]


def bingobingo():
    return bingobingo_1(), bingobingo_2(), bingobingo_3(), bingobingo_4()



def biglottery():
    return biglottery_1(), biglottery_2()


def powercolor():
    return powercolor_1(), powercolor_2()


def main(window, font):
    def ask(content):
        statement = content.get()
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
        "四星彩": fourstarlottery()
        } 
        label1 = tk.Label(window, text = all_lottery[statement])
        label1.grid(row = 1, column = 1, pady = (150, 10))
        content.grid(row = 2, column = 1, pady = (10, 10)) 

       
    # text = tk.Label(text = "Enter lottery", anchor = "center")
    #entry1 = tk.Entry(window)
    content = tk.Entry(window)
    content.grid(row = 2, column = 1, pady = (160, 10), padx = 160) 
    btn_exe = tk.Button(window, text='Search', width=5, height=1, bd=0, bg = "#D35400", fg = "white", anchor = "w", command = lambda: ask(content))
    btn_exe["font"] = font 
    btn_exe.grid(row = 3, column = 1, pady = (10, 160), padx = 160) 

powercolor()
