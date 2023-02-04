
#tkinter import
from tkinter import *

#main window
root = Tk()
root.geometry("200x150")
frame = Frame(root)

frame.pack()

#left frame
leftframe = Frame(root)
leftframe.pack(side=LEFT)

#right frame
rightframe = Frame(root)
rightframe.pack(side=RIGHT)

#Label
label = Label(frame, text="This is a label")
label.pack()

#Button
button1 = Button(leftframe, text="Button 1")
button1.pack(padx = 3, pady = 3)


root.title("Test")
root.mainloop()
