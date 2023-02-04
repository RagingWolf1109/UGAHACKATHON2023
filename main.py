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

button = Button(frame, text="Show Website", command=show_website)
button.pack(side=LEFT)

button1 = Button(leftframe, text="Button 1")
button1.pack(padx = 3, pady = 3)

search_entry = Entry(frame)
search_entry.pack(side=LEFT)

search_button = Button(frame, text="Search", command=search)
search_button.pack(side=LEFT)

root.mainloop()
