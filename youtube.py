from selenium import webdriver 
import tkinter as tk 
import selenium 

def youtube(window, font):
    def watch():
        #Webdriver  
        url = "https://www.youtube.com/results?search_query=" + entry1.get()
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions") 
        options.add_experimental_option("detach", True) 
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe", options=options)
        driver.get(url) 

        #Retreive link
        vid = driver.find_element_by_xpath("//*[@id='dismissable']/ytd-thumbnail/a").get_attribute("href")
        driver.get(vid) 
    #Main 
    label1 = tk.Label(window, text = "請輸入音樂關鍵字", bg = "#ABB2B9")
    label1["font"] = font
    label1.grid(row = 1, column = 1, pady = (130, 20), padx = 140)
    entry1 = tk.Entry(window)
    entry1.grid(row = 2, column = 1, pady = 10, padx = 160) 
    btn_exe = tk.Button(window, text='搜尋', width=5, height=1, bd=0, bg = "#D35400", fg = "white", command = watch)
    btn_exe["font"] = font 
    btn_exe.grid(row = 3, column = 1, pady = (10, 160), padx = 160) 

    
