import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import save_playlist


def reset():
    source.set("")
    new_playlist.set("")
    print("Reset has been pressed")


def create(*args):
    source_name = source.get()
    playlist_name = new_playlist.get()
    message_box = tk.messagebox.askquestion(
        "Create the playlist",
        "Are you sure you want to create " + playlist_name + "?"
    )
    if message_box == "yes":
        save_playlist.create_playlist(source_name, playlist_name)
        print("We created the " + playlist_name + " playlist")
    else:
        tk.messagebox.showinfo("Return", "It's okay, we can all try again")


def close_app():
    root.destroy()


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
new_pl_entry.grid(column=2, row=1, sticky=E)

ttk.Label(mainframe, text="Source Playlist").grid(column=0, row=0, sticky=W)
ttk.Label(mainframe, text="New Playlist Name").grid(column=0, row=1, sticky=W)

ttk.Button(mainframe, text="Reset", command=reset).grid(column=0, row=2, sticky=E)
ttk.Button(mainframe, text="Create", command=create).grid(column=2, row=2, sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

source_entry.focus()
root.bind('<Return>', create)

root.mainloop()