from tkinter import *

# Function to display the cheapest flight information
def show_cheapest_flight():
    print("Displaying the cheapest flight information")

root = Tk()
root.geometry("2000x1500")

root.title("Cheap Flights")

frame = Frame(root)
frame.pack()

# Entry widget for destination
destination_label = Label(frame, text="Destination:")
destination_label.pack(side=BOTTOM)
destination_var = StringVar()
destination_entry = Entry(frame, textvariable=destination_var)
destination_entry.pack(side=LEFT)

# Entry widget for departure date
departure_date_label = Label(frame, text="Departure Date:")
departure_date_label.pack(side=LEFT)
departure_date_var = StringVar()
departure_date_entry = Entry(frame, textvariable=departure_date_var)
departure_date_entry.pack(side=LEFT)

# Button to search for the cheapest flight
search_button = Button(frame, text="Search", command=show_cheapest_flight)
search_button.pack(side=LEFT)

root.mainloop()
