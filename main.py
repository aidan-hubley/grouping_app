import os
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

# ______________________________________________________________________________________________________________________
# Phase 4: Final Page
# ______________________________________________________________________________________________________________________

def landing_page_rerun_2():
    final.destroy()
    open_landing()

def open_final():
    review.destroy()
    global final
    final = Tk()
    final.title("Final Page")
    final.geometry("250x250")

    saved = Label(final, text="Grouped Saved!", font=(10))
    saved.place(relx=0.5, rely=0.3, anchor=CENTER)

    # Buttons
    select = Button(final, text="Select Folder", command=landing_page_rerun_2)
    select.place(relx=0.5, rely=0.5, anchor=CENTER)
    close = Button(final, text="Close", command=final.destroy)
    close.place(relx=0.5, rely=0.7, anchor=CENTER)

    final.mainloop()

# ______________________________________________________________________________________________________________________
# Phase 3: Review Groups
# ______________________________________________________________________________________________________________________

def grouping_page_rerun():
    review.destroy()
    open_grouping()

def open_review():
    grouping.destroy()
    global review
    review = Tk()
    review.title("Review Page")
    review.geometry("500x700")

    # Buttons
    reselect = Button(review, text="< Reselect Groups", command=grouping_page_rerun)
    reselect.place(relx=.05, rely=.04, anchor=NW)
    save_groups = Button(review, text="Save Groups >", command=open_final)
    save_groups.place(relx=.95, rely=.04, anchor=NE)

    review.mainloop()

# ______________________________________________________________________________________________________________________
# Phase 2: Group Photos
# ______________________________________________________________________________________________________________________

def landing_page_rerun():
    grouping.destroy()
    open_landing()

def open_grouping():
    global grouping
    grouping = Tk()
    grouping.title("Grouping Page")
    grouping.geometry("1200x700")

    # Buttons
    reselect = Button(grouping, text="< Reselect Folder", command=landing_page_rerun)
    reselect.place(relx=.05, rely=.04, anchor=NW)
    group_photos = Button(grouping, text="Group Photos")
    group_photos.place(relx=.5, rely=.1, anchor=N)
    review_groups = Button(grouping, text="Review Groups >", command=open_review)
    review_groups.place(relx=.95, rely=.04, anchor=NE)

    # Text
    raw_label = Label(grouping, text="Raw Photos", font=(20))
    raw_label.place(relx=.2, rely=.1, anchor=NW)
    grouped_label = Label(grouping, text="Grouped Photos", font=(20))
    grouped_label.place(relx=.8, rely=.1, anchor=NE)

    # Raw Canvas
    raw_canvas = Canvas(grouping, bd="3", bg="lightgrey", height=520, width=500)
    raw_canvas.place(relx=.025, rely=.2, anchor=NW)
    raw_canvas.config(scrollregion=[0, 0, 500, 1000])

    # Raw Canvas Scrolling Function
    raw_canvas.yview_moveto(1.0)

    # Raw Canvas Scrollbar
    ybar = Scrollbar(raw_canvas, orient=VERTICAL)
    ybar.place(side=LEFT, fill=Y)
    ybar.config(command=raw_canvas.yview)
    raw_canvas.config(yscrollcommand=ybar.set)

    # Images in Raw Canvas
    house1 = Image.open("house.jpg")
    temp_house1 = house1.resize((235, 145), Image.LANCZOS)
    re_house1 = ImageTk.PhotoImage(temp_house1)
    raw_canvas.create_image(10, 10, anchor=NW, image=re_house1)

    house2 = Image.open("house.png")
    temp_house2 = house2.resize((235, 145), Image.LANCZOS)
    re_house2 = ImageTk.PhotoImage(temp_house2)
    raw_canvas.create_image(255, 10, anchor=NW, image=re_house2)

    # Grouped Canvas
    grouped_canvas = Canvas(grouping, bd="3", bg="lightgrey", width=500, height=520)
    grouped_canvas.place(relx=.975, rely=.2, anchor=NE)

    grouping.mainloop()

# ______________________________________________________________________________________________________________________
# Phase 1: Landing Page
# ______________________________________________________________________________________________________________________

# Select Folder from directory
def select_folder():
    global folder_path
    folder_path = filedialog.askdirectory()
    global image_files
    image_files = [f for f in os.listdir(folder_path) if f.endswith(".jpg") or f.endswith(".png")]
    print(folder_path)
    landing.destroy()
    open_grouping()

def open_landing():
    global landing
    landing = Tk()
    landing.title("Landing Page")
    landing.geometry("250x250")

    hi = Label(landing, text="Welcome", font=(10))
    hi.place(relx=0.5, rely=0.3, anchor=CENTER)
    select = Button(landing, text="Select Folder", command=select_folder)
    select.place(relx=0.5, rely=0.6, anchor=CENTER)
    landing.mainloop()

open_landing()

# ______________________________________________________________________________________________________________________