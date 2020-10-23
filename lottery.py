import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
#reload(sys)
#sys.setdefaultencoding("utf-8")
r = requests.get("https://www.taiwanlottery.com.tw/index_new.aspx")
html_str = r.text
soup = BeautifulSoup(html_str, "html.parser")

#10 kinds of lottery

def bingobingo_1():
    target = soup.find_all('div', class_='ball_box01')
    lst = str()
    for i in target:
        lst += i.text + " "
    bin_1 = "".join(lst)
    return bin_1

    
def bingobingo_2():
    target = soup.find_all('div', class_='ball_red')
    lst = str()
    for i in target:
        lst += i.text + " "
    bin_2 = "".join(lst[:2])
    return bin_2

    
def bingobingo_3():
    target = soup.find_all('div', class_='ball_blue_BB1')
    lst  = str()
    for i in target:
        lst += i.text + " "
    bin_3 = "".join(lst[:2])
    return bin_3


def bingobingo_4():
    target = soup.find_all('div', class_='ball_blue_BB2')
    lst  = str()
    for i in target:
        lst += i.text + " "
    bin_4 = "".join(lst[:2])
    return bin_4


def win_win():
    target = soup.find_all('div', class_='ball_tx ball_blue')
    lst  = str()
    for i in target:
        lst += i.text + " "
    win = "".join(lst [:48])
    return "中獎號碼: " + win  


def powercolor_1():
    target = soup.find_all('div', class_='ball_tx ball_green')
    lst = str()
    for i in target:
        lst += i.text + " "
    pc_1 = lst[:24]
    return "中獎號碼: " + pc_1 + "\n"


def powercolor_2():
    target = soup.find_all('div', class_='ball_red')
    lst = str()
    for i in target:
        lst += i.text + " "
    pc_2 = lst[2:5]
    return "第二區： " + pc_2


def lottery38():
    target = soup.find_all('div', class_='ball_tx ball_green')
    lst = str()
    for i in target:
        lst += i.text + " "
    lot38 = "".join(lst [22:50])
    return "中獎號碼： " + lot38


def biglottery_1():
    target = soup.find_all('div', class_='ball_tx ball_yellow')
    lst = str()
    for i in target:
        lst += i.text + " "
    return str(lst [78:102]).strip()


def biglottery_2():
    target = soup.find_all('div', class_='ball_red')
    lst = str()
    for i in target:
        lst += i.text + " "
    return lst [7:9]


def lottery49():
    target = soup.find_all('div', class_='ball_tx ball_yellow')
    lst = str()
    for i in target:
        lst += i.text + " "
    lot49 = "".join(lst [80:102])  
    return "中獎號碼： " + lot49 


def todaylottery539():
    target = soup.find_all('div', class_='ball_tx ball_lemon')
    lst = str()
    for i in target:
        lst += i.text + " "
    lot539 = "".join(lst [:18])
    return "中獎號碼： " + lot539


def lottery39():
    target = soup.find_all('div', class_='ball_tx ball_lemon')
    lst = str()
    for i in target:
        lst += i.text + " "
    lot39 = "".join(lst[20:38])
    return "中獎號碼： " + lot39


def threestarlottery():
    target = soup.find_all('div', class_='ball_tx ball_purple')
    lst = str()
    for i in target:
        lst += i.text + " "
    threestar = "".join(lst [:6]) 
    return "中獎號碼：" + threestar


def fourstarlottery():
    target = soup.find_all('div', class_='ball_tx ball_purple')
    lst = str()
    for i in target:
        lst += i.text + " "
    fourstar = "".join(lst[6:15])
    return "中獎號碼： " + fourstar


def bingobingo():
    return "開出獎號： " + bingobingo_1() + "\n", "超級獎號: " + bingobingo_2() + "\n", "猜大小: " + bingobingo_3() + "\n", "猜單雙: " + bingobingo_4()



def biglottery():
    biglot_1 = "".join(biglottery_1())
    biglot_2 = "".join(biglottery_2())
    return "中獎號碼： " + biglot_1 + "\n", "特別號: " + biglot_2


def powercolor():
    return powercolor_1(), powercolor_2()


def main(window, font):
    def ask(content, result):
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
        result["text"] = "".join(all_lottery[statement])

    label = tk.Label(window, text = "請輸入彩卷種類")
    label["font"] = font 
    label.grid(row = 1, column = 1, pady = (130,20), padx = 140)
    content = ttk.Combobox(window, values=["大樂透", "威力彩", "賓果賓果", "雙贏彩", "三星彩", "四星彩", "今彩539", "38樂台彩", "39樂台彩", "49樂台彩"]) 
    content.grid(row = 2, column = 1, pady = 10, padx = 160)
    btn_exe = tk.Button(window, text='搜尋', width=5, height=1, bd=0, bg = "#D35400", fg = "white", command = lambda: ask(content, result))
    btn_exe["font"] = font 
    btn_exe.grid(row = 3, column = 1,  pady = 10, padx = 160)
    result = tk.Label(window, text = "")
    result["font"] = font  
    result.grid(row = 4, column = 1, pady = 10)

