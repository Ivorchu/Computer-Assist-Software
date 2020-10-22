from data.ahk import autohotkey
from tkinter import *


label1 = tk.Label(window, text = "Enter lottery", bg = "white")
label1.grid(row = 1, column = 1, pady = (150, 10)) 
content = tk.Entry(window)
content.grid(row = 2, column = 1, pady = (10, 10), padx = 160) 