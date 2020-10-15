import requests
from bs4 import BeautifulSoup

# from selenium import webdriver


r = requests.get("http://www.taiwanlottery.com.tw/")
html_str = r.text
soup = BeautifulSoup(html_str, "html.parser")


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

def 雙贏彩():
    target = soup.find_all('div', class_='ball_tx ball_blue')
    print("雙贏彩")
    list = ""
    for i in target:
        list += i.text
    print("開出順序: " + list[:36])
    print("大小順序: " + list[36:])
    print()


def 威力彩():
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


def 樂台彩38():
    target = soup.find_all('div', class_='ball_tx ball_green')
    print("38樂台彩")
    list = ""
    for i in target:
        list += i.text
    print("開出順序: " + list[36:54])
    print("大小順序: " + list[54:72])
    print()


def 大樂透():
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


def 樂台彩49():
    target = soup.find_all('div', class_='ball_tx ball_yellow')
    print("49樂台彩")
    list = ""
    for i in target:
        list += i.text
    print("開出順序: " + list[96:114])
    print("大小順序: " + list[114:132])
    print()


def 今彩539():
    target = soup.find_all('div', class_='ball_tx ball_lemon')
    print("今彩539")
    list = ""
    for i in target:
        list += i.text
    print("開出順序: " + list[:15])
    print("大小順序: " + list[15:30])
    print()


def 樂台彩39():
    target = soup.find_all('div', class_='ball_tx ball_lemon')
    print("39樂台彩")
    list = ""
    for i in target:
        list += i.text
    print("開出順序: " + list[30:45])
    print("大小順序: " + list[45:63])
    print()


def 三星彩():
    target = soup.find_all('div', class_='ball_tx ball_purple')
    print("三星彩")
    list = ""
    for i in target:
        list += i.text +" "
    print("中獎號碼: " + list[:6])
    print()


def 四星彩():
    target = soup.find_all('div', class_='ball_tx ball_purple')
    print("四星彩")
    list = ""
    for i in target:
        list += i.text + " "
    print("中獎號碼: " + list[6:15])
    print()


bingobingo()
雙贏彩()
威力彩()
樂台彩38()
大樂透()
樂台彩49()
今彩539()
樂台彩39()
三星彩()
四星彩()

'''
mid = len(lst) // 2
st = lst[:mid]
nd = lst[mid:]
'''

'''
url = "http://www.facebook.com/"
email = input("Email plz ")
password = input("Password plz ")

Chrome_driver_path = "D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=Chrome_driver_path)
driver.maximize_window()
driver.get(url)

driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_id("loginbutton").click()
'''
