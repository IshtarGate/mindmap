# Listing 4
#!/usr/bin/env python

import tkinter
import tkinter.messagebox

def show_alert() :
    root.bell()
    tkinter.messagebox.showinfo("Ready!", "DING DING DING!")
    quit()

def start_timer() :
    # Next line should be * 60000, but use 1000 to speed debugging:
    root.after(scale.get() * 1000, show_alert)

root = tkinter.Tk()

minutes = tkinter.Label(root, text="Minutes:")
minutes.grid(row=0, column=0)

scale = tkinter.Scale(root, from_=1, to=45, orient=tkinter.HORIZONTAL, length=300)
scale.grid(row=0, column=1)

button = tkinter.Button(root, text="Start timing", command=start_timer)
button.grid(row=1, column=1, pady=5, sticky=tkinter.E)

root.mainloop()
 