from tkinter import *

root = Tk()
root.geometry("2000x1500")
root.config(bg="#87CEEB")
root.title("Search")
frame = Frame(root)
frame.pack()

def search():
    query = search_entry.get()
    print("Searching for:", query)

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

def show_website():
    print("Displaying website")

def show_options():
    options = []
    if option1_var.get():
        options.append("Option 1")
    if option2_var.get():
        options.append("Option 2")
    if option3_var.get():
        options.append("Option 3")


option1_var = BooleanVar()
option2_var = BooleanVar()
option3_var = BooleanVar()


option1 = Checkbutton(frame, text="Option 1", variable=option1_var)
option1.pack(side=LEFT)

option2 = Checkbutton(frame, text="Option 2", variable=option2_var)
option2.pack(side=LEFT)

option3 = Checkbutton(frame, text="Option 3", variable=option3_var)
option3.pack(side=LEFT)

button = Button(frame, text="Show Website", command=show_website)
button.pack(side=LEFT)

button1 = Button(leftframe, text="Button 1")
button1.pack(padx = 3, pady = 3)

search_entry = Entry(frame)
search_entry.pack(side=LEFT)

search_button = Button(frame, text="Search", command=search)
search_button.pack(side=LEFT)

root.mainloop()

