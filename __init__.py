#coding:UTF-8
import tkinter as tk
from tkinter import * 
from tkinter import font as tkFont
from tkinter import ttk
from youtube import youtube
from stock import stocks
#from magnifier import activateMagnifier
from lottery import main
from reminder import *
#from news import 


#Initialize Window
window = tk.Tk()
window.geometry("600x400")
window.resizable(0, 0)
window.title('Computer Assist Software') 
font = tkFont.Font(family = "Arial", size = 11) 
font_chi = tkFont.Font(family = "Times New Roman", size = 11)

#Frames
frame_opt = tk.Frame(window, height= 500, width=200, bg='#33383E')
frame_opt.pack(side='left', fill = "both" ,expand="yes")

#Content
canvas = tk.Frame(window, height = 500, width = 500, bg = "#FFFFFF")
canvas.pack()

# clear frame (canvas)
def clear_frame():
	#canvas.destroy()
	#canvas.pack_forget()
	#canvas.grid_forget()
	return 0

#Buttons
btn_home = tk.Button(frame_opt, text='Home', width=15, height=2, bd=0, bg = "#33383E", fg = "white", anchor = "center")
btn_home["font"] = font 
btn_passw = tk.Button(frame_opt, text='Password', width=15, height=2, bd=0, bg = "#33383E", fg = "white", anchor = "center")
btn_passw["font"] = font 
btn_mag = tk.Button(frame_opt, text='Magnifier', width=15, height=2, bd=0, bg = "#33383E", fg = "white", anchor = "center")
btn_mag["font"] = font 
btn_stocks = tk.Button(frame_opt, text='Stocks', width=15, height=2, bd=0, bg = "#33383E", fg = "white", anchor = "center", command = lambda: stocks(canvas, font))
btn_stocks["font"] = font 
btn_lottery = tk.Button(frame_opt, text='Lottery', width=15, height=2, bd=0, bg = "#33383E", fg = "white", anchor = "center", command = lambda: main(canvas, font))
btn_lottery["font"] = font 
btn_cal = tk.Button(frame_opt, text='Calender', width=15, height=2, bd=0, bg = "#33383E", fg = "white", anchor = "center")
btn_cal["font"] = font 
btn_music = tk.Button(frame_opt, text='Youtube', width=15, height=2, bd=0, bg = "#33383E", fg = "white", anchor = "center", command = lambda: youtube(canvas, font))
btn_music["font"] = font 
btn_news = tk.Button(frame_opt, text='News', width=15, height=2, bd=0, bg = "#33383E", fg = "white", anchor = "center") 
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