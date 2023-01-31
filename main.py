from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *

# ______________________________________________________________________________________________________________________
# Phase 3: Review Groups
# ______________________________________________________________________________________________________________________

def open_review():
    grouping.destroy()
    review = Tk()
    review.title("Review Page")
    review.geometry("500x700")

    review.mainloop()

# ______________________________________________________________________________________________________________________
# Phase 2: Group Photos
# ______________________________________________________________________________________________________________________

def landing_page_rerun():
    grouping.destroy()
    landing_page()

def open_grouping():
    global grouping
    grouping = Tk()
    grouping.title("Grouping Page")

    # Make Grouping Page Fullscreen
    # width = grouping.winfo_screenwidth()
    # height = grouping.winfo_screenheight()
    # grouping.geometry("%dx%d" % (width, height))
    grouping.geometry("500x500")

    # Grouping Page
    reselect = Button(grouping, text="Reselect Groups", command=landing_page_rerun)
    reselect.place(relx=.08, rely=.07, anchor=NW)
    group_photos = Button(grouping, text="Group Photos")
    group_photos.place(relx=.5, rely=.07, anchor=N)
    review_groups = Button(grouping, text="Review Groups", command=open_review)
    review_groups.place(relx=.92, rely=.07, anchor=NE)

    grouping.mainloop()

# ______________________________________________________________________________________________________________________
# Phase 1: Landing Page
# ______________________________________________________________________________________________________________________

# Select Folder from directory
def select_folder():
    global folder_path
    folder_path = filedialog.askdirectory()
    print(folder_path)
    landing.destroy()
    open_grouping()

def landing_page():
    # Landing Page Creation
    global landing
    landing = Tk()
    landing.title("Landing Page")
    landing.geometry("250x250")

    hi = Label(landing, text="Welcome", font=(10))
    hi.place(relx=0.5, rely=0.3, anchor=CENTER)
    select = Button(landing, text="Select Folder", command=select_folder)
    select.place(relx=0.5, rely=0.6, anchor=CENTER)
    landing.mainloop()

landing_page()

# ______________________________________________________________________________________________________________________