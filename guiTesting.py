#imports
from tkinter import *
import sys
import os
import time

#main window
root = Tk()
root.geometry('1000x1000')

#background image
bgimg = PhotoImage(file="background.png")
limg= Label(root, image=bgimg)
limg.place(x=0, y=0)

#variables
location = ""
date = ""
people = ""
destination = ""
departure_date = ""

#Creating the read me
def read_me():
    top = Toplevel(root)
    top.geometry('750x250')
    top.title("How-To")
    Label(top,text="Welcome to Adventure Finder!").place(x=0,y=0)
    Label(top,text="To begin, enter the city,state you are traveling from.").place(x=0,y=20)
    Label(top,text="Next, enter the date you are traveling on in the form mm/dd/yyyy.").place(x=0,y=40)
    Label(top,text="Next, enter the number of people you are traveling with.").place(x=0,y=60)
    Label(top,text="Finally, enter the date you are leaving in the form mm/dd/yyyy.").place(x=0,y=80)
    Label(top,text="This application was created by: Liam Hosfeld, Andrew Grahm, Riley Elwood, and Christopher Ghattas during UGA Hackathon 2023").place(x=0,y=100)
    Label(top,text="Enjoy your adventure!").place(x=0,y=140)

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

date_label = Label(root, text="Arrival Date:")
date_entry = Entry(root, width=50)
date_entry.insert(0,'')
date_label.place(x = 240, y = 250)
date_entry.place(x = 350, y = 250)

people_label = Label(root, text="Number of People:")
people_entry = Entry(root, width=50)
people_entry.insert(0,'')
people_label.place(x = 240, y = 300)
people_entry.place(x = 350, y = 300)

departure_date_label = Label(root, text="Departure Date:")
departure_date_entry = Entry(root, width=50)
departure_date_entry.insert(0,'')
departure_date_label.place(x = 240, y = 350)
departure_date_entry.place(x = 350, y = 350)

#changing screens after receving input
def change_to_search():
    location = location_entry.get()
    date = date_entry.get()
    people = people_entry.get()
    departure_date = departure_date_entry.get()
    label.destroy()
    location_label.destroy()
    location_entry.destroy()
    date_label.destroy()
    date_entry.destroy()
    people_label.destroy()
    people_entry.destroy()
    departure_date_label.destroy()
    departure_date_entry.destroy()
    button2.destroy()
    button1.destroy()
    #Loading Screen
    button3 = Button(root, text="Begin Your Adventure!",command = lambda:[change_to_results(),button3.destroy()])
    button3.place(x = 400, y = 500)



#Search Button
#button2 = Button(root, text="Search",command =lambda:[change_to_search,get_input])
button2 = Button(root, text="Search",command = change_to_search)
button2.place(x = 400, y = 450)
#Read Me
button1 = Button(root, text="How-To",command = read_me)
button1.place(x = 500, y = 450)

#changing to results screen
def change_to_results():
    limg.destroy()
    results_label = Label(root, text="Results For" + location)
    results_label.place(x = 0, y = 0)
    hotel_label = Label(root, text="Hotels:")
    hotel_label.place(x = 100, y = 0)
    travel_label = Label(root, text="Travel:")
    travel_label.place(x = 300, y = 0)
    restart_button = Button(root, text="Restart",command = lambda:[restart(),restart_button.destroy()])
    restart_button.place(x = 0, y = 600)
    #printing out api results here

#restart function
def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)

root.title("Adventure Finder")
root.mainloop()