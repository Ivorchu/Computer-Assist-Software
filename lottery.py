#coding:UTF-8
import requests
from bs4 import BeautifulSoup


r = requests.get("http://www.taiwanlottery.com.tw/")
html_str = r.text
soup = BeautifulSoup(html_str, "html.parser")

#10 kinds of lottery

def bingobingo():
    target = soup.find_all('div', class_='ball_box01')
    print("賓果賓果BingoBingo")
    list = ""
    for i in target:
        list += i.text
    print("開出獎號: " + list)
    # 超級獎號
    target = soup.find_all('div', class_='ball_red')
    list = ""
    for i in target:
        list += i.text
    print("超級獎號: " + list[:2])
    # 猜大小
    target = soup.find_all('div', class_='ball_blue_BB1')
    list = ""
    for i in target:
        list += i.text
    print("猜大小: " + list[:2])
    # 猜單雙
    target = soup.find_all('div', class_='ball_blue_BB2')
    list = ""
    for i in target:
        list += i.text
    print("猜單雙: " + list[:2])
    print()

def win_win():
    target = soup.find_all('div', class_='ball_tx ball_blue')
    print("雙贏彩")
    list = ""
    for i in target:
        list += i.text
    print("開出順序: " + list[:36])
    print("大小順序: " + list[36:])
    print()


def powercolor():
    target = soup.find_all('div', class_='ball_tx ball_green')
    print("威力彩")
    list = ""
    for i in target:
        list += i.text
    print("開出順序: " + list[:18])
    print("大小順序: " + list[18:36])
    target = soup.find_all('div', class_='ball_red')
    list = ""
    for i in target:
        list += i.text
    print("第二區: " + list[2:4])
    print()


def lottery38():
    target = soup.find_all('div', class_='ball_tx ball_green')
    print("38樂台彩")
    list = ""
    for i in target:
        list += i.text
    print("開出順序: " + list[36:54])
    print("大小順序: " + list[54:72])
    print()


def biglottery():
    target = soup.find_all('div', class_='ball_tx ball_yellow')
    print("大樂透")
    list = ""
    for i in target:
        list += i.text
    print("開出順序: " + list[60:78])
    print("大小順序: " + list[78:96])
    # 特別號
    target = soup.find_all('div', class_='ball_red')
    list = ""
    for i in target:
        list += i.text
    print("特別號:" + list[4:7])
    print()


def lottery49():
    target = soup.find_all('div', class_='ball_tx ball_yellow')
    print("49樂台彩")
    list = ""
    for i in target:
        list += i.text
    print("開出順序: " + list[96:114])
    print("大小順序: " + list[114:132])
    print()


def todaylottery539():
    target = soup.find_all('div', class_='ball_tx ball_lemon')
    print("今彩539")
    list = ""
    for i in target:
        list += i.text
    print("開出順序: " + list[:15])
    print("大小順序: " + list[15:30])
    print()


def lottery39():
    target = soup.find_all('div', class_='ball_tx ball_lemon')
    print("39樂台彩")
    list = ""
    for i in target:
        list += i.text
    print("開出順序: " + list[30:45])
    print("大小順序: " + list[45:63])
    print()


def threestarlottery():
    target = soup.find_all('div', class_='ball_tx ball_purple')
    print("三星彩")
    list = ""
    for i in target:
        list += i.text +" "
    print("中獎號碼: " + list[:6])
    print()


def fourstarlottery():
    target = soup.find_all('div', class_='ball_tx ball_purple')
    print("四星彩")
    list = ""
    for i in target:
        list += i.text + " "
    print("中獎號碼: " + list[6:15])
    print()


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

    statement = input("請問要搜尋哪種彩卷?")
    all_lottery[statement]

ask()
