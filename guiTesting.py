
#tkinter import
from tkinter import *

#main window
root = Tk()
root.geometry("1000x1000")

frame = Frame(root)
searching = Frame(root)
frame.pack()


def change_to_search():
    searching.pack(fill = 'both', expand = 1)
    frame.pack_forget()


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

# Entry widget for destination
#destination_label = Label(frame, text="Destination:")
#destination_label.pack(side=LEFT)
destination_var = StringVar()
destination_entry = Entry(frame, textvariable=destination_var)
destination_entry.pack(side=LEFT)

# Entry widget for departure date
#departure_date_label = Label(frame, text="Departure Date:")
#departure_date_label.pack(side=LEFT)
departure_date_var = StringVar()
departure_date_entry = Entry(frame, textvariable=departure_date_var)
departure_date_entry.pack(side=LEFT)

#Search Button
button2 = Button(frame, text="Search",command = change_to_search)
button2.pack(padx = 3, pady = 3)

#Loading Screen Button
#If Done Searching Display Button
button3 = Button(searching, text="Begin Your Adventure!")
button3.pack(padx = 30, pady = 30)

root.title("Test")
root.mainloop()
