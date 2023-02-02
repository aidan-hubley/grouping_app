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

    # Buttons + Label
    reselect = Button(review, text="< Reselect Groups", command=grouping_page_rerun)
    reselect.place(relx=.05, rely=.04, anchor=NW)
    save_groups = Button(review, text="Save Groups >", command=open_final)
    save_groups.place(relx=.95, rely=.04, anchor=NE)
    grouped_label = Label(review, text="Review Groups", font=(20))
    grouped_label.place(relx=.5, rely=.1, anchor=CENTER)

    # Canvas
    review_canvas = Canvas(review, bd="3", bg="lightgrey", height=580, width=450)
    review_canvas.place(relx=.5, rely=.55, anchor=CENTER)
    review_canvas.config(scrollregion=[0, 0, 450, 1000])

    # Raw Canvas Scrolling Function
    review_canvas.yview_moveto(1.0)

    # Raw Canvas Scrollbar
    ybar = Scrollbar(review_canvas, orient=VERTICAL)
    ybar.place(relx=0, rely=0, height=590, anchor=NW)
    ybar.config(command=review_canvas.yview)
    review_canvas.config(yscrollcommand=ybar.set)

    review.mainloop()

# ______________________________________________________________________________________________________________________
# Phase 2: Group Photos
# ______________________________________________________________________________________________________________________

def landing_page_rerun():
    grouping.destroy()
    open_landing()

def on_image_click(event):
    image = event.widget
    # Add or remove the label from the selection
    if image in selected:
        image.configure(borderwidth=2, relief="transparent", bordercolor="white")
        selected.remove(image)
    else:
        image.configure(borderwidth=2, relief="solid", bordercolor="blue")
        selected.append(image)

def create_group():
    if selected != []:
        group = []
        for image in selected:
            group.append(image)

        groups.append(group)
    else:
        # error
        print("No images selected")



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
    raw_canvas = Canvas(grouping, bd="3", bg="lightgrey", height=520, width=510)
    raw_canvas.place(relx=.02, rely=.2, anchor=NW)
    raw_canvas.config(scrollregion=[0, 0, 500, 1000])

    # Raw Canvas Scrolling Function
    raw_canvas.yview_moveto(0)

    # Raw Canvas Scrollbar
    ybar = Scrollbar(raw_canvas, orient=VERTICAL)
    ybar.place(relx=0, rely=0, height=530, anchor=NW)
    ybar.config(command=raw_canvas.yview)
    raw_canvas.config(yscrollcommand=ybar.set)

    # Images in Raw Canvas
    # house1 = Image.open("house.jpg")
    # temp_house1 = house1.resize((235, 145), Image.LANCZOS)
    # re_house1 = ImageTk.PhotoImage(temp_house1)
    # raw_canvas.create_image(20, 10, anchor=NW, image=re_house1)
    #
    # house2 = Image.open("house.png")
    # temp_house2 = house2.resize((235, 145), Image.LANCZOS)
    # re_house2 = ImageTk.PhotoImage(temp_house2)
    # raw_canvas.create_image(265, 10, anchor=NW, image=re_house2)

    # Load and display the images
    for i in range(len(image_files)):
        print(len(image_files))
        image = Image.open(os.path.join(folder_path, image_files[i]))
        image = image.resize((235, 145), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        label = Label(raw_canvas, image=image, background="white")
        # label.image = image
        raw_canvas.place(image, relx=i*245+20, rely=10, anchor=NW)
        image.bind("<Button-1>", on_image_click)

    # Grouped Canvas
    global grouped_canvas
    grouped_canvas = Canvas(grouping, bd="3", bg="lightgrey", height=520, width=510)
    grouped_canvas.place(relx=.975, rely=.2, anchor=NE)
    grouped_canvas.config(scrollregion=[0, 0, 570, 1000])

    # Raw Canvas Scrolling Function
    grouped_canvas.yview_moveto(0)
    grouped_canvas.xview_moveto(0)

    # Raw Canvas Scrollbar
    ybar = Scrollbar(grouped_canvas, orient=VERTICAL)
    ybar.place(relx=0, rely=0, height=530, anchor=NW)
    ybar.config(command=grouped_canvas.yview)
    grouped_canvas.config(yscrollcommand=ybar.set)

    xbar = Scrollbar(grouped_canvas, orient=HORIZONTAL)
    xbar.place(relx=1, rely=1, width=505, anchor=SE)
    xbar.config(command=grouped_canvas.xview)
    grouped_canvas.config(xscrollcommand=xbar.set)

    # for i in range(len(groups)):
    #     display_new_group(i)

    display_new_group(1)

    grouping.mainloop()

def display_new_group(num):
    group = "Group " + str(num)
    grouped_canvas.create_text(35, 60, text=group)
    grouped_canvas.create_rectangle(60, 5, 225, 115, width=1)
    grouped_canvas.create_rectangle(230, 5, 395, 115, width=1)
    grouped_canvas.create_rectangle(400, 5, 565, 115, width=1)
    grouped_canvas.create_line(0, 120, 570, 120)

# ______________________________________________________________________________________________________________________
# Phase 1: Landing Page
# ______________________________________________________________________________________________________________________

# Select Folder from directory
def select_folder():
    global folder_path
    folder_path = filedialog.askdirectory()
    global image_files
    image_files = [f for f in os.listdir(folder_path) if f.endswith(".jpg") or f.endswith(".png")]  # change to dng
    print(folder_path, image_files)
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

# ______________________________________________________________________________________________________________________
# Phase 0: Global Variables
# ______________________________________________________________________________________________________________________

selected = []
groups = []
open_landing()

# ______________________________________________________________________________________________________________________

