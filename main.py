from tkinter import *

root = Tk()
root.geometry("200x150")
frame = Frame(root)

frame.pack()

leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)

label = Label(frame, text="This is a label")
label.pack()

button1 = Button(leftframe, text="Button 1")
button1.pack(padx = 3, pady = 3)


root.title("Test")
root.mainloop()

