# A script that allows easier creation of Maple plots.

import tkinter as tk
import pyperclip as pyp

'''
$plot3 = plotmaple("plots[display]([plot((x-4)^2+$const-4, x = -4..8, 
discont = [showremovable = [color = blue, symbolsize = 15]], 
labels = [``,``], color = blue, tickmarks = [spacing(1), spacing(1)],  
axis[1] = [gridlines = [spacing(1), majorlines = 1, color = grey]], 
axis[2] = [gridlines = [spacing(1), majorlines = 1, color = grey]]),
plots[textplot]([8, 0, 'x'], align = {above, left}, font = [TIMES, ROMAN, 12]),  
plots[textplot]([0, 10, 'y'], align = {below, right}, font = [TIMES, ROMAN, 12])],
view = [-4 .. 8, -6 .. 10]), plotoptions = 'width=400, height=400'");
'''

master = tk.Tk()
tk.Label(master, text = "Add Text").grid(row = 0)
tk.Label(master, text = "Add Point").grid(row = 1)
tk.Label(master, text = "Create!").grid(row = 2)
tk.Label(master, text = "Quit").grid(row = 3)

e1 = tk.Entry(master) # Name
e2 = tk.Entry(master) # Function
e3 = tk.Entry(master) # Colour (Default: Blue)
e4 = tk.Entry(master) # x-label (Default: ``)
e5 = tk.Entry(master) # y-label (Default: ``)
e6 = tk.Entry(master) # x-ticks (Default: [])
e7 = tk.Entry(master) # y-ticks (Default: [])
e8 = tk.Entry(master) # x-axis spacing (Default: spacing(1))
e9 = tk.Entry(master) # x-majorlines (Default: 1)
e10 = tk.Entry(master) # y-axis spacing (Default: spacing(1))
e11 = tk.Entry(master) # y-majorlines (Default: 1)
e12 = tk.Entry(master) # axis colour (Default: grey)
e13 = tk.Entry(master) # Lower x-view (Default: -6)
e14 = tk.Entry(master) # Upper x-view (Default: 6)
e15 = tk.Entry(master) # Lower y-view (Default: -6)
e16 = tk.Entry(master) # Upper y-view (Default: 6)
e17 = tk.Entry(master) # Width (Default: 400)
e18 = tk.Entry(master) # Height (Default: 400)
