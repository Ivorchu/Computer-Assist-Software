import tkinter as tk
from tkinter import ttk
#from runautohotkey import 
#from webcrawler import 
#from magnifier import 
#from stock import 
#from lottery import 
#from reminder import 
#from youtube import 
#from news import 
#from texting import 
#from autoscheduleplanner import

#Initialize Window
window = tk.Tk()
window.geometry("550x367")
window.resizable(0, 0)
window.title('Computer Assist Software')

#Frames
frame_opt = tk.Frame(window, height=450, width=200, bg='#3E4149')
frame_opt.pack(side='left')

#Buttons
btn_home = tk.Button(frame_opt, text='Home', width=8, height=2, bd=0, highlightbackground='#3E4149')
btn_passw = tk.Button(frame_opt, text='Password', width=8, height=2, bd=0, highlightbackground='#3E4149')
btn_mag = tk.Button(frame_opt, text='Magnifier', width=8, height=2, bd=0, highlightbackground='#3E4149')
btn_stocks = tk.Button(frame_opt, text='Stocks', width=8, height=2, bd=0, highlightbackground='#3E4149')
btn_lottery = tk.Button(frame_opt, text='Lottery', width=8, height=2, bd=0, highlightbackground='#3E4149')
btn_cal = tk.Button(frame_opt, text='Calender', width=8, height=2, bd=0, highlightbackground='#3E4149')
btn_music = tk.Button(frame_opt, text='Music', width=8, height=2, bd=0, highlightbackground='#3E4149')
btn_news = tk.Button(frame_opt, text='News', width=8, height=2, bd=0, highlightbackground='#3E4149')

#Packs
btn_home.grid(row=0, padx = 1, pady = 1)
btn_passw.grid(row=1, padx = 1, pady = 1)
btn_mag.grid(row=2, padx = 1, pady = 1)
btn_stocks.grid(row=3, padx = 1, pady = 1)
btn_lottery.grid(row=4, padx = 1, pady = 1)
btn_cal.grid(row=5, padx = 1, pady = 1)
btn_music.grid(row=6, padx = 1, pady = 1)
btn_news.grid(row=7, padx = 1, pady = 1)


#mainloop
tk.mainloop()