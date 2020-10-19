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


#def ask():
bingobingo_dict = {1: "賓果賓果", 2: bingobingo(), 3:"賓果", 4: "bingo"}
win_win_dict    = {1: "雙贏彩", 2: win_win()}
powercolor_dict = {1: "威力彩", 2: powercolor()}
lottery38_dict  = {1: "38樂台彩", 2: lottery38()}
biglottery_dict = {1: "大樂透", 2: biglottery()}
lottery49_dict  = {1: "49樂台彩", 2: lottery49()}
todaylottery539_dict  = {1: "今彩539", 2: todaylottery539()}
lottery39_dict  = {1: "39樂台彩", 2: lottery39()}
threestarlottery_dict = {1: "三星彩", 2: threestarlottery()}
fourstarlottery_dict  = {1: "四星彩", 2: fourstarlottery()}
all_lottery = {
1: bingobingo_dict,
2: win_win_dict,
3: powercolor_dict,
4: lottery38_dict,
5: biglottery_dict,
6: lottery49_dict,
7: todaylottery539_dict,
8: lottery39_dict,
9: threestarlottery_dict,
10: fourstarlottery_dict,
}
statement = input("請問要搜尋哪種彩卷?")
for i in all_lottery:
    lottery_n = all_lottery[i]
    if statement == all_lottery[i]:
        for j in i:
            lottery_n[2]

