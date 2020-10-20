import tkinter
from PIL import ImageGrab, ImageTk

def activateMagnifier():
	root = tkinter.Tk()
	screenWidth = root.winfo_screenwidth()
	screenHeight = root.winfo_screenheight()
	root.geometry(str(screenWidth)+'x'+str(screenHeight)+'+0+0')
	root.overrideredirection(True)

	root.resizable(False, False)

	canvas = tkinter.Canvas(root, bg='white', width=screenWidth, height=screenHeight)
	image = ImageTk.PhotoImage(ImageGrab.grab())
	canvas.create_image(screenWidth//2, screenHeight//2, image=image)

	def onMouseRightClick(event):
		root.destroy()

	canvas.bind('<Button-3>', onMouseRightClick)

	radius=20
	def onMouseMove(event):
		global lastIm
		try:
			canvas.delete(lastIm)
		except:
			pass
		x = event.x
		y = event.y

		subIm = ImageGrab.grab((x-radius, y-radius, x+radius, y+radius))
		subIm = subIm.resize((radius*6, radius*6))
		subIm = ImageTk.PhotoImage(subIm)
		lastIm = canvas.create_image(x-70, y-70, image=subIm)
		canvas.update()

	canvas.bind('<Motion>', onMouseMove)

	canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)

	root.mainloop()
