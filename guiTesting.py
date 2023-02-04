
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

#Search Bar
location_label = Label(frame, text="City, State:")
location_label.pack(padx = 3, pady = 3)
location_entry = Entry(frame, width=50)
location_entry.insert(0,'')
location_entry.pack(padx = 3, pady = 3)

date_label = Label(frame, text="Date:")
date_label.pack(padx = 3, pady = 3)
date_entry = Entry(frame, width=50)
date_entry.insert(0,'')
date_entry.pack(padx = 3, pady = 3)

people_label = Label(frame, text="Number of People:")
people_label.pack(padx = 3, pady = 3)
people_entry = Entry(frame, width=50)
people_entry.insert(0,'')
people_entry.pack(padx = 3, pady = 3)

destination_label = Label(frame, text="Destination:")
destination_label.pack(padx = 3, pady = 3)
destination_entry = Entry(frame, width=50)
destination_entry.insert(0,'')
destination_entry.pack(padx = 3, pady = 3)

departure_date_label = Label(frame, text="Departure Date:")
departure_date_label.pack(padx = 3, pady = 3)
departure_date_entry = Entry(frame, width=50)
departure_date_entry.insert(0,'')
departure_date_entry.pack(padx = 3, pady = 3)

#Search Button
button2 = Button(frame, text="Search",command = change_to_search)
button2.pack(padx = 3, pady = 3)

#Read Me
button1 = Button(frame, text="How-To")
button1.pack(padx = 3, pady = 3)

#Loading Screen Button
#If Done Searching Display Button
button3 = Button(searching, text="Begin Your Adventure!")
button3.pack(padx = 30, pady = 30)

root.title("Test")
root.mainloop()
