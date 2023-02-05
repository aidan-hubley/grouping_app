import os
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

# ______________________________________________________________________________________________________________________
# Phase 4: Final Page
# ______________________________________________________________________________________________________________________

def open_final():
    review.destroy()
    global final
    final = Tk()
    final.title("Final Page")
    final.geometry("250x250")
    final.maxsize(250, 250)
    final.minsize(250, 250)

    saved = Label(final, text="Grouped Saved!", font=(10))
    saved.place(relx=0.5, rely=0.3, anchor=CENTER)

    # Buttons
    select = Button(final, text="Select Folder", command=lambda: select_folder(final))
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
    review.maxsize(500, 700)
    review.minsize(500, 700)

    # Buttons + Label
    reselect = Button(review, text="< Reselect Groups", command=grouping_page_rerun)
    reselect.place(relx=.05, rely=.04, anchor=NW)
    save_groups = Button(review, text="Save Groups >", command=open_final)
    save_groups.place(relx=.95, rely=.04, anchor=NE)
    grouped_label = Label(review, text="Review Groups", font=20)
    grouped_label.place(relx=.5, rely=.1, anchor=CENTER)

    # Canvas
    review_canvas = Canvas(review, bd="3", bg="lightgrey", height=580, width=450)
    review_canvas.place(relx=.5, rely=.55, anchor=CENTER)
    review_canvas.config(scrollregion=[0, 0, 450, 1000])

    # Raw Canvas Scrolling Function
    review_canvas.yview_moveto(0)

    # Raw Canvas Scrollbar
    ybar = Scrollbar(review_canvas, orient=VERTICAL)
    ybar.place(relx=0, rely=0, height=590, anchor=NW)
    ybar.config(command=review_canvas.yview)
    review_canvas.config(yscrollcommand=ybar.set)

    review.mainloop()

# ______________________________________________________________________________________________________________________
# Phase 2: Group Photos
# ______________________________________________________________________________________________________________________

def on_image_click(index): #event
    global selected
    global image_files
    image = image_files[index] #event.widget
    print(image)
    # Add or remove the label from the selection
    if image in selected:
        #image.configure(borderwidth=1, relief="solid")
        selected.remove(image)
        print("Image deselected")
    else:
        #image.configure(borderwidth=5, relief="solid")
        selected.append(image)
        print("Image selected")

def create_group():
    global selected
    global groups
    global image_files

    if selected != []:
        group = []
        for image in selected:
            if image in image_files:
                group.append(image)
                image_files.remove(image)
            else:
                print('File not found in image files')

        if group != []:
            groups.append(group)
            selected = []
            print("Group created")

        #display_groups()
        #################

        grouped_canvas.update_idletasks()
        # grouped_canvas.update()
        height = 110
        width = 165
        pad = 5
        for i in range(len(groups)):
            group_str = "Group " + str(i + 1)
            grouped_canvas.create_text(35, 60 + (height * i) + pad, text=group_str)
            grouped_canvas.create_line(0, 120 + (i * 120), 570, 120 + (i * 120))
            images = []
            for j in range(len(groups[i])):
                images.append(Image.open(os.path.join(folder_path, groups[i][j])))

            for j in range(len(groups[i])):
                images[j] = images[j].resize((width, height), Image.LANCZOS)
                images[j] = ImageTk.PhotoImage(images[j])
                label = Label(grouped_canvas, image=images[j])
                x_pos = j * width + int(width / 2) + pad
                y_pos = i * height + int(height / 2) + pad
                grouped_canvas.create_window(x_pos, y_pos, window=label)

            # grouped_canvas.create_rectangle(60, 5, 225, 115, width=1) # img 1
            # grouped_canvas.create_rectangle(230, 5, 395, 115, width=1) # img 2
            # grouped_canvas.create_rectangle(400, 5, 565, 115, width=1) # img 3
            # grouped_canvas.create_line(0, 120, 570, 120)

        print("Group displayed")

        #################
    else:
        print("No images selected")

def open_grouping():
    global grouping
    grouping = Tk()
    grouping.title("Grouping Page")
    grouping.geometry("1200x700")
    grouping.maxsize(1200, 700)
    grouping.minsize(1200, 700)

    # Buttons
    reselect = Button(grouping, text="< Reselect Folder", command=lambda: select_folder(grouping))
    reselect.place(relx=.05, rely=.04, anchor=NW)
    group_photos = Button(grouping, text="Group Photos", command=create_group)
    group_photos.place(relx=.5, rely=.1, anchor=N)
    review_groups = Button(grouping, text="Review Groups >", command=open_review)
    review_groups.place(relx=.95, rely=.04, anchor=NE)

    # Text
    raw_label = Label(grouping, text="Raw Photos", font=(20))
    raw_label.place(relx=.2, rely=.1, anchor=NW)
    grouped_label = Label(grouping, text="Grouped Photos", font=(20))
    grouped_label.place(relx=.8, rely=.1, anchor=NE)

    # Raw Canvas
    global raw_canvas
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

    images = []
    for i in range(len(image_files)):
        images.append(Image.open(os.path.join(folder_path, image_files[i])))

    # Load and display the images
    for i in range(len(image_files)):
        print(images[i])
        images[i] = images[i].resize((235, 145), Image.LANCZOS)
        images[i] = ImageTk.PhotoImage(images[i])
        label = Label(raw_canvas, image=images[i])
        # label.bind("<Button-1>", on_image_click)
        label.bind("<Button-1>", lambda event, index=i: on_image_click(index))
        x_pos = (245 * (i % 2)) + 138  # (118*i)+128
        y_pos = (155 * (int(i / 2))) + 83  # (73*(i%2))+83
        raw_canvas.create_window(x_pos, y_pos, window=label)

    # Grouped Canvas
    global grouped_canvas
    grouped_canvas = Canvas(grouping, bd="3", bg="lightgrey", height=520, width=510)
    grouped_canvas.place(relx=.975, rely=.2, anchor=NE)
    grouped_canvas.config(scrollregion=[0, 0, 570, 1000])

    # Grouped Canvas Scrolling Function
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

    # display_groups()

    grouping.mainloop()

def display_groups():
    grouped_canvas.update_idletasks()
    # grouped_canvas.update()
    height = 110
    width = 165
    pad = 5
    for i in range(len(groups)):
        group_str = "Group " + str(i+1)
        grouped_canvas.create_text(35, 60 + (height * i) + pad, text=group_str)
        grouped_canvas.create_line(0, 120+(i*120), 570, 120+(i*120))
        images = []
        for j in range(len(groups[i])):
            images.append(Image.open(os.path.join(folder_path, groups[i][j])))

        for j in range(len(groups[i])):
            images[j] = images[j].resize((width, height), Image.LANCZOS)
            images[j] = ImageTk.PhotoImage(images[j])
            label = Label(grouped_canvas, image=images[j])
            x_pos = j * width + int(width/2) + pad
            y_pos = i * height + int(height/2) + pad
            grouped_canvas.create_window(x_pos, y_pos, window=label)


        # grouped_canvas.create_rectangle(60, 5, 225, 115, width=1) # img 1
        # grouped_canvas.create_rectangle(230, 5, 395, 115, width=1) # img 2
        # grouped_canvas.create_rectangle(400, 5, 565, 115, width=1) # img 3
        # grouped_canvas.create_line(0, 120, 570, 120)

    print("Group displayed")

# ______________________________________________________________________________________________________________________
# Phase 1: Landing Page
# ______________________________________________________________________________________________________________________

# Select Folder from directory
def select_folder(page):
    global folder_path
    global image_files
    folder_path = filedialog.askdirectory()
    image_files = [f for f in os.listdir(folder_path) if f.endswith(".dng")]
    print(folder_path, image_files)
    page.destroy()
    open_grouping()

def open_landing():
    global landing
    landing = Tk()
    landing.title("Landing Page")
    landing.geometry("250x250")
    landing.maxsize(250, 250)
    landing.minsize(250, 250)

    hi = Label(landing, text="Welcome", font=(10))
    hi.place(relx=0.5, rely=0.3, anchor=CENTER)
    select = Button(landing, text="Select Folder", command=lambda: select_folder(landing))
    select.place(relx=0.5, rely=0.6, anchor=CENTER)
    landing.mainloop()

# ______________________________________________________________________________________________________________________
# Phase 0: Global Variables
# ______________________________________________________________________________________________________________________

global selected
selected = []
global groups
groups = []
open_landing()

# ______________________________________________________________________________________________________________________

