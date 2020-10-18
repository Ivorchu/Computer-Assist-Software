import tkinter as tk
from tkinter import * 
from tkinter import font as tkFont
from tkinter import ttk
from Youtube import youtube 
#from runautohotkey import 
#from webcrawler import 
#from magnifier import 
#from stock import stock
#from lottery import 
#from reminder import 
#from news import 
#from texting import 
#from autoscheduleplanner import

#Initialize Window
window = tk.Tk()
window.geometry("550x367")
window.resizable(0, 0)
window.title('Computer Assist Software') 
font = tkFont.Font(family = "Arial", size = 9) 

#Frames
frame_opt = tk.Frame(window, height=450, width=200, bg='#34495E')
frame_opt.pack(side='left')

#Content
canvas = tk.Frame(window, height = 400, width = 500, bg = "#FFFFFF")
canvas.pack()

#Buttons
btn_home = tk.Button(frame_opt, text='Home', width=8, height=2, bd=0, bg = "#34495E", fg = "white", anchor = "w")
btn_home["font"] = font 
btn_passw = tk.Button(frame_opt, text='Password', width=8, height=2, bd=0, bg = "#34495E", fg = "white", anchor = "w")
btn_passw["font"] = font 
btn_mag = tk.Button(frame_opt, text='Magnifier', width=8, height=2, bd=0, bg = "#34495E", fg = "white", anchor = "w")
btn_mag["font"] = font 
btn_stocks = tk.Button(frame_opt, text='Stocks', width=8, height=2, bd=0, bg = "#34495E", fg = "white", anchor = "w")
btn_stocks["font"] = font 
btn_lottery = tk.Button(frame_opt, text='Lottery', width=8, height=2, bd=0, bg = "#34495E", fg = "white", anchor = "w")
btn_lottery["font"] = font 
btn_cal = tk.Button(frame_opt, text='Calender', width=8, height=2, bd=0, bg = "#34495E", fg = "white", anchor = "w")
btn_cal["font"] = font 
btn_music = tk.Button(frame_opt, text='Music', width=8, height=2, bd=0, bg = "#34495E", fg = "white", anchor = "w", command = lambda: youtube(canvas, font))
btn_music["font"] = font 
btn_news = tk.Button(frame_opt, text='News', width=8, height=2, bd=0, bg = "#34495E", fg = "white", anchor = "w") 
btn_news["font"] = font 

#Packs
btn_home.grid(row=0, padx = (5, 7), pady = (20, 3))
btn_passw.grid(row=1, padx = (5, 7), pady = 3)
btn_mag.grid(row=2, padx = (5, 7), pady = 3)
btn_stocks.grid(row=3, padx = (5, 7), pady = 3)
btn_lottery.grid(row=4, padx = (5, 7), pady = 3)
btn_cal.grid(row=5, padx = (5, 7), pady = 3)
btn_music.grid(row=6, padx = (5, 7), pady = 3)
btn_news.grid(row=7, padx = (5, 7), pady = (3, 20))

#mainloop
tk.mainloop()