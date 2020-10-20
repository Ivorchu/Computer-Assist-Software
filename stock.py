from selenium import webdriver
import tkinter as tk
import selenium 
def stocks(window, font):
	def exec():
		#Chromedriver 
		url = "https://tw.stock.yahoo.com/q/bc?s=" + entry2.get()
		options = webdriver.ChromeOptions()
		options.add_argument("start-maximized")
		options.add_argument("disable-infobars")
		options.add_argument("--disable-extensions")
		options.add_experimental_option("detach", True)
		driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe", options=options)
		driver.get(url)

	entry2 = tk.Entry(window)
	entry2.grid(row = 1, column = 1, pady = (150, 10), padx = 160)
	btn_exe = tk.Button(window, text='Browse', width=6, height=1, bd=0, bg = "#D35400", fg = "white", anchor = "w", command = exec)
	btn_exe["font"] = font
	btn_exe.grid(row = 2, column = 1, pady = (10, 150), padx = 160)