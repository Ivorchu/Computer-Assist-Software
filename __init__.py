#coding:UTF-8

import tkinter as tk 
from tkinter import * 
from tkinter import font as tkFont
from youtube import youtube
from stock import stocks
#from magnifier import activateMagnifier
from lottery import main
#from reminder import *
from news import refreshNews


#Initialize Window
window = tk.Tk()
window.geometry("700x430")
window.resizable(0, 0)
window.title('Computer Assist Software') 
font = tkFont.Font(family = "Arial", size = 12)
font_chi = tkFont.Font(family = "Times New Roman", size = 12)

#Frames
frame_opt = tk.Frame(window, height= 700, width=430, bg='#33383E')
frame_opt.pack(side='left')

#Content
canvas = tk.Frame(window, height = 500, width = 600)
canvas.pack()

# clear frame (canvas)
def clearFrame(frame):
	for widget in frame.winfo_children():
		widget.destroy()
		frame.pack_forget()
		frame.pack()
	

#Buttons
btn_home = tk.Button(frame_opt, text='主畫面', width=12, height=2, bd=0, bg = "#33383E", fg = "white", anchor = "center", command = lambda: [clearFrame(canvas)])
btn_home["font"] = font 
btn_passw = tk.Button(frame_opt, text='帳號密碼管理', width=12, height=2, bd=0, bg = "#33383E", fg = "white", anchor = "center", command = lambda: [clearFrame(canvas)])
btn_passw["font"] = font 
btn_mag = tk.Button(frame_opt, text='Magnifier', width=12, height=2, bd=0, bg = "#33383E", fg = "white", anchor = "center", command = lambda: activateMagnifier(font))
btn_mag["font"] = font 
btn_stocks = tk.Button(frame_opt, text='股票', width=12, height=2, bd=0, bg = "#33383E", fg = "white", anchor = "center", command = lambda: [clearFrame(canvas),stocks(canvas, font)])
btn_stocks["font"] = font 
btn_lottery = tk.Button(frame_opt, text='彩卷', width=12, height=2, bd=0, bg = "#33383E", fg = "white", anchor = "center", command = lambda: [clearFrame(canvas),main(canvas, font)])
btn_lottery["font"] = font 
btn_remd = tk.Button(frame_opt, text='提醒 & 行事曆', width=12, height=2, bd=0, bg = "#33383E", fg = "white", anchor = "center", command = lambda: [clearFrame(canvas),printAll(canvas, font)])
btn_remd["font"] = font 
btn_music = tk.Button(frame_opt, text='音樂 & Youtube', width=12, height=2, bd=0, bg = "#33383E", fg = "white", anchor = "center", command = lambda: [clearFrame(canvas), youtube(canvas, font)])
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

#mainloop
tk.mainloop()