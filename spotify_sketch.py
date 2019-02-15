from tkinter import *
from tkinter import ttk


def reset():
    source.set("")
    new_playlist.set("")
    print("Reset has been pressed")


def create(*args):
    print("Create has been pressed")


root = Tk()
root.title("Spotify Playlist Saver")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

source = StringVar()
new_playlist = StringVar()

source_entry = ttk.Entry(mainframe, width=30, textvariable=source)
source_entry.grid(column=2, row=0, sticky=(W, E))
new_pl_entry = ttk.Entry(mainframe, width=30, textvariable=new_playlist)
new_pl_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, text="Source Playlist").grid(column=0, row=0, sticky=W)
ttk.Label(mainframe, text="New Playlist Name").grid(column=0, row=1, sticky=W)

ttk.Button(mainframe, text="Reset", command=reset).grid(column=0, row=2, sticky=E)
ttk.Button(mainframe, text="Create", command=create).grid(column=2, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

source_entry.focus()
root.bind('<Return>', create)

root.mainloop()