#tkinter import
from tkinter import *

#main window
root = Tk()
root.geometry('1000x1000')

bgimg = PhotoImage(file="background.png")
limg= Label(root, image=bgimg)
limg.place(x=0, y=0)

def change_to_search():
    location = location_entry.get()
    date = date_entry.get()
    people = people_entry.get()
    destination = destination_entry.get()
    departure_date = departure_date_entry.get()
    label.destroy()
    location_label.destroy()
    location_entry.destroy()
    date_label.destroy()
    date_entry.destroy()
    people_label.destroy()
    people_entry.destroy()
    destination_label.destroy()
    destination_entry.destroy()
    departure_date_label.destroy()
    departure_date_entry.destroy()
    button2.destroy()
    button1.destroy()
    #Loading Screen
    button3 = Button(root, text="Begin Your Adventure!")
    button3.place(x = 400, y = 500)

def change_to_results():
    limg.destroy()
    




    
   
#Label
label = Label(root, text="Choose Your Adventure!",font = ('Comic Sans MS', 40))
label.place(x = 200, y = 0)
#label.pack()

#Search Bar: Location, Date, Number of People, Destination, Departure Date
location_label = Label(root, text="City, State:")
location_entry = Entry(root, width=50)
location_entry.insert(0,'')
location_label.place(x = 240, y = 200)
location_entry.place(x = 350, y = 200)

date_label = Label(root, text="Date:")
date_entry = Entry(root, width=50)
date_entry.insert(0,'')
date_label.place(x = 240, y = 250)
date_entry.place(x = 350, y = 250)

people_label = Label(root, text="Number of People:")
people_entry = Entry(root, width=50)
people_entry.insert(0,'')
people_label.place(x = 240, y = 300)
people_entry.place(x = 350, y = 300)

destination_label = Label(root, text="Destination:")
destination_entry = Entry(root, width=50)
destination_entry.insert(0,'')
destination_label.place(x = 240, y = 350)
destination_entry.place(x = 350, y = 350)

departure_date_label = Label(root, text="Departure Date:")
departure_date_entry = Entry(root, width=50)
departure_date_entry.insert(0,'')
departure_date_label.place(x = 240, y = 400)
departure_date_entry.place(x = 350, y = 400)

#Search Button
#button2 = Button(root, text="Search",command =lambda:[change_to_search,get_input])
button2 = Button(root, text="Search",command = change_to_search)
button2.place(x = 400, y = 450)
#Read Me
button1 = Button(root, text="How-To")
button1.place(x = 500, y = 450)


root.title("Adventure Finder")
root.mainloop()
