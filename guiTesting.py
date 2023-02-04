
#tkinter import
from tkinter import *

#main window
root = Tk()
root.geometry("1000x1000")
frame = Frame(root)

frame.pack()

#Label
label = Label(frame, text="Choose Your Adventure!",font = ('Comic Sans MS', 40))
label.pack()

#Read Me
button1 = Button(frame, text="Button 1")
button1.place(x=0, y=0)
button1.pack(padx = 3, pady = 3)

#Search Bar
location_entry = Entry(frame, width=50)
location_entry.insert(0,'City, State')
location_entry.pack(padx = 3, pady = 3)

date_entry = Entry(frame, width=50)
date_entry.insert(0,'Date')
date_entry.pack(padx = 3, pady = 3)

people_entry = Entry(frame, width=50)
people_entry.insert(0,'Number of People')
people_entry.pack(padx = 3, pady = 3)

#Search Button
button2 = Button(frame, text="Search")
button2.place(x=500, y=500)
button2.pack(padx = 3, pady = 3)




root.title("Test")
root.mainloop()
