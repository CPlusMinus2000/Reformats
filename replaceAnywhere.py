# A script that (hopefully) allows find-and-replace-anywhere functionality

import tkinter as tk
import pyperclip as pyp

# lines = list(pyp.paste().split('\n'))

def findReplace():
    find = e1.get()
    repl = e2.get()

    pyp.copy(pyp.paste().replace(find, repl))

def findReplaceQuit():
    findReplace()
    master.quit()

master = tk.Tk()
master.title("Find and Replace")
tk.Label(master, text="Find").grid(row=0)
tk.Label(master, text="Replace").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, text='Replace', 
            command=findReplace).grid(row=3, 
                                      column=1, 
                                      sticky=tk.W, 
                                      pady=4)

tk.Button(master, text='Replace and Quit',
            command=findReplaceQuit).grid(row=3,
                                          column=2,
                                          sticky=tk.W,
                                          pady=4)

tk.mainloop()