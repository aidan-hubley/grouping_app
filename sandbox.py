# import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

# create window
master = Tk()
master.title("Tkinter Sandbox")
master.config(bg="lightgrey")

# get screen size, make window fullscreen
width = master.winfo_screenwidth()
height = master.winfo_screenheight()
master.geometry("%dx%d" % (width, height))

# Buttons Frame
Buttons_Frame = Frame(master)
Buttons_Frame.grid(row=1, column=1, padx=5, pady=5)

# Top-Left Buttons
File_Button = Button(Buttons_Frame, text="Open Raw Folder")
File_Button.grid(row=1, column=1, padx=7, pady=7)
Review_Button = Button(Buttons_Frame, text="Review Groups")
Review_Button.grid(row=1, column=2, padx=7, pady=7)
Save_Button = Button(Buttons_Frame, text="Save")
Save_Button.grid(row=1, column=3, padx=7, pady=7)
Close_Button = Button(Buttons_Frame, text="Close", command=master.destroy)
Close_Button.grid(row=1, column=4, padx=7, pady=7)

# Raws
Label(master, text="Raw Photos", font=(45), bg="lightgrey").grid(row=2, column=1, padx=7, pady=7)

# Raws Frame
Raws_Frame = Frame(master)
Raws_Frame.grid(row=3, column=1, columnspan=2, padx=5)

# house1 = ImageTk.PhotoImage(Image.open('house.jpg'))
# house2 = ImageTk.PhotoImage(Image.open('house.jpg'))
# house3 = ImageTk.PhotoImage(Image.open('house.jpg'))
# Raws = [house1, house2, house3]
#
# def next_raw():
#     i = Raws_Scrollbar.get()
#     print(i)
#     canvas.create_image(20, 20, image=Raws[int(i[0])])
#
# # Raws Frame Scrollbar Frame
# Raws_Scrollbar = Scrollbar(Raws_Frame, orient=VERTICAL)
# Raws_Scrollbar.pack(side=LEFT, fill=Y)
# canvas = Canvas(master, yscrollcommand=Raws_Scrollbar.set)
# canvas.pack()
# Raws_Scrollbar.config(comand=next_raw)

# mainloop is always called last, runs the window function properly
master.mainloop()


