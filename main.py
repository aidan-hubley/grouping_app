from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *

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
    grouping.geometry("1150x700")

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

    # Raw Frame
    raw_frame = Frame(grouping, bg="lightgrey")
    raw_frame.place()



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