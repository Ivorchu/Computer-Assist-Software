#coding:UTF-8
from selenium import webdriver
import tkinter as tk
from tkinter import * 
from tkinter import font as tkFont
from PIL import ImageTk, Image
from stock import stocks
from magnifier import activateMagnifier
from lottery import main
from reminder import *
from news import refreshNews
from password import run
from youtube import youtube
import os

#Initialize Window
window = tk.Tk()
window.geometry("700x430")
window.resizable(0, 0)
window.title('Computer Assist Software') 
font = tkFont.Font(family = "Arial", size = 12)
font_chi = tkFont.Font(family = "Times New Roman", size = 12)
window["bg"] = "#ABB2B9" 
#Frames
frame_opt = tk.Frame(window, height= 450, width=700, bg='#33383E')
frame_opt.pack(side='left')

#Content
canvas = tk.Frame(window, height = 700, width = 430)
canvas.pack()
canvas["bg"] = "#ABB2B9"
# clear frame (canvas)
def clearFrame(frame):
	for widget in frame.winfo_children():
		widget.destroy()
		frame.pack_forget()
		frame.pack()

def Home(window):
	image = Image.open('profile_img.png')
	image = image.resize((450, 320), Image.ANTIALIAS)
	image = image.crop([0,0,450,300])
	img = ImageTk.PhotoImage(image) 
	panel = tk.Label(window, image = img, borderwidth = 0, highlightthickness = 0)
	#panel.pack(side = "bottom", fill = "both", expand = "yes")
	panel.grid(row = 0, column = 0, pady = (10, 20)) 
	entry_ggl = tk.Entry(window, width = 50) 
	entry_ggl.grid(row = 1, column = 0, pady = 5) 
	def ggl_search():
		#Chromedriver setup 
		options = webdriver.ChromeOptions()
		options.add_argument("start-maximized")
		options.add_argument("disable-infobars")
		options.add_argument("--disable-extensions")
		options.add_experimental_option("detach", True)
		driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe", options=options)
		url = "https://www.google.com/search?q=" + entry_ggl.get() 
		driver.get(url)
	button_ggl = tk.Button(window, text = "搜尋", width = 5, height = 1, bg = "#D35400", fg = "white", command = ggl_search)
	button_ggl.grid(row = 2, column = 0) 
	window.mainloop() 

#Buttons
btn_home = tk.Button(frame_opt, text='主畫面', width=12, height=2, bd=0, bg = "#33383E", fg = "white", anchor = "center", command = lambda: [clearFrame(canvas), Home(canvas)])
btn_home["font"] = font 
btn_passw = tk.Button(frame_opt, text='帳號 & 密碼管理', width=12, height=2, bd=0, bg = "#33383E", fg = "white", anchor = "center", command = lambda: [clearFrame(canvas), run(canvas, font)])
btn_passw["font"] = font 
btn_mag = tk.Button(frame_opt, text='放大鏡', width=12, height=2, bd=0, bg = "#33383E", fg = "white", anchor = "center", command = lambda: [clearFrame(canvas),activateMagnifier(font)])
btn_mag["font"] = font 
btn_stocks = tk.Button(frame_opt, text='股票', width=12, height=2, bd=0, bg = "#33383E", fg = "white", anchor = "center", command = lambda: [clearFrame(canvas),stocks(canvas, font)])
btn_stocks["font"] = font 
btn_lottery = tk.Button(frame_opt, text='彩卷', width=12, height=2, bd=0, bg = "#33383E", fg = "white", anchor = "center", command = lambda: [clearFrame(canvas),main(canvas, font)])
btn_lottery["font"] = font 
btn_remd = tk.Button(frame_opt, text='提醒 & 行事曆', width=12, height=2, bd=0, bg = "#33383E", fg = "white", anchor = "center", command = lambda: [clearFrame(canvas),printAll(canvas, font)],activateTime())
btn_remd["font"] = font 
btn_music = tk.Button(frame_opt, text='音樂 & Youtube', width=12, height=2, bd=0, bg = "#33383E", fg = "white", anchor = "center", command = lambda: [clearFrame(canvas),youtube(canvas, font)])
btn_music["font"] = font 
btn_news = tk.Button(frame_opt, text='新聞', width=12, height=2, bd=0, bg = "#33383E", fg = "white", anchor = "center", command = lambda: [clearFrame(canvas),refreshNews(canvas, font)]) 
btn_news["font"] = font

#Packs
btn_home.grid(row=0, padx = (5, 7), pady = (10, 3))
btn_passw.grid(row=1, padx = (5, 7), pady = 3)
btn_mag.grid(row=2, padx = (5, 7), pady = 3)
btn_stocks.grid(row=3, padx = (5, 7), pady = 3)
btn_lottery.grid(row=4, padx = (5, 7), pady = 3)
btn_remd.grid(row=5, padx = (5, 7), pady = 3)
btn_music.grid(row=6, padx = (5, 7), pady = 3)
btn_news.grid(row=7, padx = (5, 7), pady = (3, 10))
Home(canvas)
#mainloop
tk.mainloop()