import os
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import webbrowser



# ______________________________________________________________________________________________________________________
# Phase 4: Final Page
# ______________________________________________________________________________________________________________________

# takes in the name of a file and adds a hyphen and the group number to it
def rename_file(file_name, group_num):
    if file_name.endswith('.dng'):
        file_new_name = file_name[:len(file_name) - 4] + '-' + str(group_num + 1) + '.dng'
        # renames file
        os.rename(folder_path + '/' + file_name, folder + '/' + file_new_name)
    else:
        print("File is not of type dng")


def open_final():
    global folder
    folder = folder_path[folder_path.rfind('/') + 1:]
    i = 0
    for group in groups:
        for image_file in group:
            rename_file(image_file, i)
        i += 1

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
    select = Button(final, text="Select New Folder", command=lambda: select_folder(final))
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
    if (len(image_files) > 0):
        print("Please group all Raws")
    else:
        print("All Raws are grouped")
        grouping.destroy()
        global review
        review = Tk()
        review.title("Review Page")
        review.geometry("650x700")
        review.maxsize(650, 700)
        review.minsize(650, 700)

        # Buttons + Label
        reselect = Button(review, text="< Reselect Groups", command=grouping_page_rerun)
        reselect.place(relx=.05, rely=.04, anchor=NW)
        save_groups = Button(review, text="Save Groups >", command=open_final)
        save_groups.place(relx=.95, rely=.04, anchor=NE)
        grouped_label = Label(review, text="Review Groups", font=20)
        grouped_label.place(relx=.5, rely=.1, anchor=CENTER)

        # Display Groups
        review_height = 110
        review_width = 165
        review_pad = 5

        # Review Canvas
        review_canvas = Canvas(review, bd="3", bg="lightgrey", height=580, width=600)
        review_canvas.place(relx=.5, rely=.55, anchor=CENTER)
        print(len(groups))

        # Dynamic Width
        dynamic_width = 600

        for group in groups:
            if (len(group) > 3):
                dynamic_width = ((review_pad + review_width + review_pad) * (len(group) - 3) + 600)

        review_canvas.config(scrollregion=[0, 0, dynamic_width, len(groups) * (review_height + review_pad + review_pad)])

        # Review Canvas Scrolling Function
        review_canvas.yview_moveto(0)
        review_canvas.xview_moveto(0)

        global grouped_images
        fill_grouped_images()

        for i in range(len(groups)):
            group_str = "Group " + str(i + 1)
            review_canvas.create_text(38, 60 + (review_height + review_pad * 2) * i, text=group_str)
            review_canvas.create_line(0, (review_height + review_pad * 2) + (i * (review_height + review_pad * 2)), dynamic_width,
                                      (review_height + review_pad * 2) + (i * (review_height + review_pad * 2)))

            group_images_review = grouped_images[i]

            for j in range(len(groups[i])):
                # print(str(groups[i][j]) + " displayed in group to be reviewed")
                group_images_review[j] = group_images_review[j].resize((review_width, review_height), Image.LANCZOS)
                group_images_review[j] = ImageTk.PhotoImage(group_images_review[j])
                label = Label(review_canvas, image=group_images_review[j])
                x_pos = j * (review_width + review_pad * 2) + int(review_width / 2) + review_pad + 70
                y_pos = i * (review_height + review_pad * 2) + int(review_height / 2) + review_pad
                review_canvas.create_window(x_pos, y_pos, window=label)

        # print(str(len(groups)) + " group(s) displayed to be reviewed")

        # Review Canvas Scrollbar
        ybar = Scrollbar(review_canvas, orient=VERTICAL)
        ybar.place(relx=0, rely=0, height=590, anchor=NW)
        ybar.config(command=review_canvas.yview)
        review_canvas.config(yscrollcommand=ybar.set)

        xbar = Scrollbar(review_canvas, orient=HORIZONTAL)
        xbar.place(relx=1, rely=1, width=600, anchor=SE)
        xbar.config(command=review_canvas.xview)
        review_canvas.config(xscrollcommand=xbar.set)

        review.mainloop()


# ______________________________________________________________________________________________________________________
# Phase 2: Group Photos
# ______________________________________________________________________________________________________________________

def on_image_click(index, event):  # event
    global selected
    global image_files
    image = image_files[index]  # event.widget
    # Add or remove the label from the selection
    if image in selected:
        event.widget.config(background="white")
        selected.remove(image)
        print("Image deselected: " + image)
    else:
        event.widget.config(background="black")
        selected.append(image)
        print("Image selected: " + image)


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
            print("Group created consisting of: " + str(group))

        display_raws()
        display_groups()

        selected = []
    else:
        print("No images selected")

#Add file to existing group -- in progress
def add_to_group(image_name, group_num):
    global groups
    global image_files
    if image_name in image_files:
        if group_num > len(groups):
            for i in range(len(groups), group_num):
                groups.append([])
        groups[group_num].append(image_name)
        image_files.remove(image_name)
    else:
        print('File not found in image files')

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

    global raw_height
    global raw_width
    global raw_pad

    # Raw Canvas
    global raw_canvas
    raw_canvas = Canvas(grouping, bd="3", bg="lightgrey", height=520, width=510)
    raw_canvas.place(relx=.02, rely=.2, anchor=NW)
    raw_canvas.config(scrollregion=[0, 0, 500, int(len(image_files) / 2) * (raw_height + raw_pad) + raw_pad])

    # Raw Canvas Scrolling Function
    raw_canvas.yview_moveto(0)

    # Raw Canvas Scrollbar
    ybar = Scrollbar(raw_canvas, orient=VERTICAL)
    ybar.place(relx=0, rely=0, height=530, anchor=NW)
    ybar.config(command=raw_canvas.yview)
    raw_canvas.config(yscrollcommand=ybar.set)


    # Load and display the raw images
    display_raws()

    # Grouped Canvas
    global grouped_canvas
    grouped_canvas = Canvas(grouping, bd="3", bg="lightgrey", height=520, width=510)
    grouped_canvas.place(relx=.975, rely=.2, anchor=NE)
    # review_canvas.config(scrollregion=[0, 0, 600, len(groups) * (review_height + review_pad) + review_pad + 100])
    grouped_canvas.config(scrollregion=[0, 0, 570, 1000])

    # Grouped Canvas Scrolling Function
    grouped_canvas.yview_moveto(0)
    grouped_canvas.xview_moveto(0)

    # Load and display the grouped images
    fill_grouped_images()
    display_groups()

    grouping.mainloop()


def fill_grouped_images():
    global groups
    global grouped_images
    grouped_images = []
    for i in range(len(groups)):
        global group_images
        group_images = []
        for j in range(len(groups[i])):
            print(str(groups[i][j]) + " added to image group " + str(i + 1))
            group_images.append(Image.open(os.path.join(folder_path, groups[i][j])))
        grouped_images.append(group_images)


def fill_raw_images():
    global raw_images
    raw_images = []
    for i in range(len(image_files)):
        raw_images.append(Image.open(os.path.join(folder_path, image_files[i])))

def ungroup(index):
    global groups
    print(groups)
    for image in groups[index]:
        image_files.append(image)

    del groups[index]
    print(groups)

    display_groups()
    display_raws()

def display_groups():
    height = 110
    width = 165
    pad = 5

    global grouped_images
    global groups

    grouped_canvas.delete("all")
    fill_grouped_images()

    dynamic_width = 510

    for group in groups:
        if(len(group) > 2):
            dynamic_width = (pad + width + pad) * (len(group)-2) + 420

    grouped_canvas.config(scrollregion=[0, 0, dynamic_width, len(groups) * (height + pad + pad)])

    displayed = 0

    for i in range(len(groups)):
        displayed = i + 1
        group_str = "Group " + str(i + 1)
        grouped_canvas.create_text(42, 30 + (height + pad * 2) * i, text=group_str)
        label = Label(grouped_canvas, text = "Ungroup")
        label.bind("<Button-1>", lambda event, index=i: ungroup(index))
        grouped_canvas.create_window(42, 80 + (height + pad * 2) * i, window=label)
        grouped_canvas.create_line(0, (height + pad * 2) + (i * (height + pad * 2)), dynamic_width,
                                   (height + pad * 2) + (i * (height + pad * 2)))
        group_images = grouped_images[i]

        for j in range(len(groups[i])):
            group_images[j] = group_images[j].resize((width, height), Image.LANCZOS)
            group_images[j] = ImageTk.PhotoImage(group_images[j])
            label = Label(grouped_canvas, image=group_images[j])
            x_pos = j * (width + pad * 2) + int(width / 2) + pad + 70
            y_pos = i * (height + pad * 2) + int(height / 2) + pad
            grouped_canvas.create_window(x_pos, y_pos, window=label)

    print(str(displayed) + " group(s) displayed")

    # Grouped Canvas Scrollbar
    ybar = Scrollbar(grouped_canvas, orient=VERTICAL)
    ybar.place(relx=0, rely=0, height=530, anchor=NW)
    ybar.config(command=grouped_canvas.yview)
    grouped_canvas.config(yscrollcommand=ybar.set)

    xbar = Scrollbar(grouped_canvas, orient=HORIZONTAL)
    xbar.place(relx=1, rely=1, width=505, anchor=SE)
    xbar.config(command=grouped_canvas.xview)
    grouped_canvas.config(xscrollcommand=xbar.set)


def display_raws():
    global raw_height
    global raw_width
    global raw_pad

    raw_canvas.delete("all")
    fill_raw_images()

    for i in range(len(image_files)):
        raw_images[i] = raw_images[i].resize((raw_width, raw_height), Image.LANCZOS)
        raw_images[i] = ImageTk.PhotoImage(raw_images[i])
        label = Label(raw_canvas, image=raw_images[i], background="white")
        label.bind("<Button-1>", lambda event, index=i: on_image_click(index, event))
        x_pos = ((raw_width + raw_pad) * (i % 2)) + 138
        y_pos = ((raw_height + raw_pad) * (int(i / 2))) + 83
        raw_canvas.create_window(x_pos, y_pos, window=label)


# ______________________________________________________________________________________________________________________
# Phase 1: Landing Page
# ______________________________________________________________________________________________________________________

#Check for existing groups -- In progress
# def make_groups():
#     for imagefile in image_files:
#         group_num_string = ''
#         for i in range(imagefile.rfind('-')+1, len(imagefile)-1):
#             if imagefile[i] in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
#                 group_num_string += imagefile[i]
#
#         if group_num_string != '':
#             add_to_group(imagefile, int(group_num_string)-1)

# Select Folder from directory
def select_folder(page):
    global folder_path
    global image_files
    global grouped_images
    global groups
    grouped_images = []
    groups = []
    folder_path = filedialog.askdirectory()
    image_files = [f for f in os.listdir(folder_path) if f.endswith(".dng")]
    # make_groups()

    # print(folder_path, image_files) # debug
    page.destroy()
    open_grouping()

def readmelink():
    webbrowser.open("https://github.com/aidan-hubley/grouping_app/blob/main/README.md")

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
    select.place(relx=0.44, rely=0.6, anchor=CENTER)
    readme = Button(landing, text="?", width=3, command=readmelink)
    readme.place(relx=0.66, rely=0.6, anchor=CENTER)

    landing.mainloop()


# ______________________________________________________________________________________________________________________
# Phase 0: Global Variables
# ______________________________________________________________________________________________________________________

raw_height = 145
raw_width = 235
raw_pad = 10

raw_images = []
grouped_images = []
image_files = []

selected = []
groups = []
open_landing()

# ______________________________________________________________________________________________________________________
