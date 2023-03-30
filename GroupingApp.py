import os
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import webbrowser
import atexit
import math

# ______________________________________________________________________________________________________________________
# Phase 4: Final Page
# ______________________________________________________________________________________________________________________

# takes in the name of a file and adds a hyphen and the group number to it
def rename_file(file_name, group_num):
    grouped = False
    ungrouped_file_name = file_name
    if file_name.endswith('.dng'):

        if file_name.find('-') != -1:
            grouped = True
            for i in range(0, file_name.find('-')):
                if file_name[i] not in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
                    grouped = False
            if grouped:
                ungrouped_file_name = file_name[file_name.find('-')+1:]

        file_new_name = str(group_num+1) + "-" + ungrouped_file_name
        # renames file
        os.rename(folder_path + '/' + file_name, folder_path + '/' + file_new_name)
    else:
        print("File is not of type dng")


# opens the final confirmation page
def open_final():
    # Unhide the working folder
    os.system('attrib -h "' + folder_path + '"')

    #global folder
    #folder = folder_path[folder_path.rfind('/') + 1:]
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
    # final.maxsize(250, 250)
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

# reopens grouping page from review page
def grouping_page_rerun():
    review.destroy()
    open_grouping()

# opens final review page from grouping page
def open_review():
    if (len(image_files) > 0):
        print("Please group all Raws")
    else:
        # print("All Raws are grouped")
        grouping.destroy()
        global review
        review = Tk()
        review.title("Review Page")

        review.state('zoomed')

        # Buttons + Label
        reselect = Button(review, text="< Reselect Groups", command=grouping_page_rerun)
        reselect.place(relx=.05, rely=.04, anchor=NW)
        save_groups = Button(review, text="Save Groups >", command=open_final)
        save_groups.place(relx=.95, rely=.04, anchor=NE)
        grouped_label = Label(review, text="Review Groups", font=20)
        grouped_label.place(relx=.5, rely=.1, anchor=CENTER)
        count_label = Label(review, text=f"Expected Final Count: {len(groups)}")
        count_label.place(relx=.5, rely=0.06, anchor=CENTER)

        # Display Groups
        review_height = 110
        review_width = 165
        review_pad = 5

        # Review Canvas
        review_canvas = Canvas(review, bd="3", bg="lightgrey", height=580, width=600)
        review_canvas.place(relx=.5, rely=.55, anchor=CENTER)

        # Dynamic Width
        dynamic_width = 600

        for group in groups:
            if len(group) > 3:
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

# on image being clicked, add image to selection and highlights image
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

def create_group_event(event):
    create_group()

# makes selected images into a new group
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

#Add file to existing group
def add_to_group(image_name, group_num):
    global groups
    global image_files
    if image_name in image_files:
        if group_num > len(groups)-1:
            for i in range(len(groups), group_num+1):
                groups.append([])
        groups[group_num].append(image_name)
        image_files.remove(image_name)

        # print("raws: " + str(image_files))
        # print("groups: " + str(groups))

    else:
        print('File not found in image files')

# opens grouping page
def open_grouping():
    global grouping
    grouping = Tk()
    grouping.title("Grouping Page")
    # grouping.geometry("1200x700")
    # grouping.maxsize(1200, 700)
    # grouping.minsize(1200, 700)

    grouping.state('zoomed')

    grouping.bind('<Return>', create_group_event)
    #grouping.bind('<Configure>', on_resize)

    # Buttons
    reselect = Button(grouping, text="< Reselect Folder", command=lambda: select_folder(grouping))
    reselect.place(relx=.05, rely=.04, anchor=NW)
    group_photos = Button(grouping, text="Group Photos", command=create_group)
    group_photos.place(relx=.5, rely=.1, anchor=N)
    ungroupall = Button(grouping, text="Ungroup All", command=ungroup_all)
    ungroupall.place(relx=.5, rely=.9, anchor=N)
    review_groups = Button(grouping, text="Review Groups >", command=open_review)
    review_groups.place(relx=.95, rely=.04, anchor=NE)

    # Text
    raw_label = Label(grouping, text="Raw Photos", font = (20))
    raw_label.place(relx=.2, rely=.1, anchor=NW)
    grouped_label = Label(grouping, text="Grouped Photos", font = (20))
    grouped_label.place(relx=.8, rely=.1, anchor=NE)

    global raw_height
    global raw_width
    global raw_pad
    # global height_mult
    # global width_mult

    # Old Aspect Ratio in px: 1200, 700
    # New Aspect Ratio in px: 1920, 1080

    # height_mult = grouping.winfo_height()/700
    # width_mult = grouping.winfo_width()/1200

    #print(grouping.winfo_height(), height_mult)


    # Raw Canvas
    global raw_canvas
    raw_canvas = Canvas(grouping, bd="3", bg="lightgrey")#, height=520 * height_mult, width=510 * height_mult)

    raw_canvas.place(relx=.02, rely=.2, relheight=520/700, relwidth = 510/1200, anchor = NW)
    #resize_multipliers(raw_canvas)
    print(raw_canvas.winfo_width(), raw_canvas.winfo_height())
    raw_canvas.config(scrollregion=[0, 0, 500, int(len(image_files) / 2) * (raw_height + raw_pad) + raw_pad])

    # Raw Canvas Scrolling Function
    raw_canvas.yview_moveto(0)

    # Raw Canvas Scrollbar
    ybar = Scrollbar(raw_canvas, orient=VERTICAL)
    ybar.place(relx=0, rely=0, relheight = 1, anchor=NW) #relheight=520/700 * height_mult,
    ybar.config(command=raw_canvas.yview)
    raw_canvas.config(yscrollcommand=ybar.set)

    # Load and display the raw images
    display_raws()

    # Grouped Canvas
    global grouped_canvas
    grouped_canvas = Canvas(grouping, bd="3", bg="lightgrey")#, height=520 * height_mult, width=510 * width_mult)
    grouped_canvas.place(relx=.975, rely=.2, relheight = 520/700, relwidth=510/1200, anchor=NE)
    #resize_multipliers(grouped_canvas)
    grouped_canvas.config(scrollregion=[0, 0, 570, 1000])

    # Grouped Canvas Scrolling Function
    grouped_canvas.yview_moveto(0)
    grouped_canvas.xview_moveto(0)

    # Load and display the grouped images
    fill_grouped_images()
    display_groups()

    grouping.mainloop()


# displays grouped images in grouped canvas
def display_groups():
    # Old Aspect Ratio in px: 1200, 700
    # Multiply: Width x 1.6 - Height x 1.54
    # New Aspect Ratio in px: 1920, 1080
    #height_mult = int(grouping.winfo_height()/700) #move to params?
    #width_mult = int(grouping.winfo_width()/1200)

    height = 170
    width = 264
    height_pad = 5
    width_pad = 5

    global grouped_images
    global groups

    grouped_canvas.delete("all")
    fill_grouped_images()

    # set scrollbar length
    dynamic_width = 510
    for group in groups:
        group_width = (width_pad + width + width_pad) * (len(group) - 2) + 420
        if(group_width > dynamic_width):
            dynamic_width = group_width
    grouped_canvas.config(scrollregion=[0, 0, dynamic_width, len(groups) * (height + height_pad + height_pad)])

    displayed = 0

    for i in range(len(groups)):
        displayed = i + 1
        group_str = "Group " + str(i + 1)
        grouped_canvas.create_text(42, 30 + (height + height_pad * 2) * i, text=group_str)
        label = Label(grouped_canvas, text = "Ungroup")
        label.bind("<Button-1>", lambda event, index=i: ungroup(index))
        grouped_canvas.create_window(42, 80 + (height + height_pad * 2) * i, window=label)
        grouped_canvas.create_line(0, (height + height_pad * 2) + (i * (height + height_pad * 2)), dynamic_width,
                                   (height + height_pad * 2) + (i * (height + height_pad * 2)))
        group_images = grouped_images[i]

        for j in range(len(groups[i])):
            #group_images[j] = group_images[j].resize((width, height), Image.LANCZOS)
            group_images[j] = ImageTk.PhotoImage(group_images[j])
            label = Label(grouped_canvas, image=group_images[j])
            x_pos = j * (width + width_pad * 2) + int(width / 2) + width_pad + 70
            y_pos = i * (height + height_pad * 2) + int(height / 2) + height_pad
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

# displays raw images in raw canvas
def display_raws():
    global raw_height
    global raw_width
    global raw_pad

    raw_canvas.delete("all")
    fill_raw_images()

    raw_canvas.config(scrollregion=[0, 0, 510, (math.ceil(len(image_files) / 2)  * (raw_height + raw_pad) + raw_pad)])

    for i in range(len(image_files)):
        print(raw_canvas.winfo_width(), raw_canvas.winfo_height())
        raw_images[i] = raw_images[i].resize((raw_width, raw_height), Image.LANCZOS)
        raw_images[i] = ImageTk.PhotoImage(raw_images[i])
        label = Label(raw_canvas, image=raw_images[i], background="white")
        label.bind("<Button-1>", lambda event, index=i: on_image_click(index, event))
        x_pos = int( (((raw_width + raw_pad) * (i % 2)) + raw_width/2 + raw_pad + 10))#138
        y_pos = int( (((raw_height + raw_pad) * (int(i / 2))) + raw_height/2 + raw_pad) )#83
        raw_canvas.create_window(x_pos, y_pos, window=label)

    print("Raws Displayed")


# updates grouped image file array from grouped file path array
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

# updates raw image file array from raw file path array
def fill_raw_images():
    global raw_images
    raw_images = []
    for i in range(len(image_files)):
        raw_images.append(Image.open(os.path.join(folder_path, image_files[i])))

# removes a group
def ungroup(index):
    global groups
    for image in groups[index]:
        image_files.append(image)

    del groups[index]

    display_groups()
    display_raws()

# removes all groups
def ungroup_all():
    global groups
    for index in range(len(groups)-1, -1, -1):
        for image in groups[index]:
            image_files.append(image)

        del groups[index]

    display_raws()
    display_groups()


# ______________________________________________________________________________________________________________________
# Phase 1: Landing Page
# ______________________________________________________________________________________________________________________

# Check for existing groups
def make_groups():
    for i in range(len(image_files)-1, -1, -1):
        group_num_string = ''
        if image_files[i].find("-") != -1:
            for j in range(0, image_files[i].find('-')):
                if image_files[i][j] in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
                    group_num_string += image_files[i][j]
                else:
                    group_num_string = ''
                    break

        if group_num_string != '':
            add_to_group(image_files[i], int(group_num_string)-1)

# Select Folder from directory
def select_folder(page):
    global folder_path
    global image_files
    global grouped_images
    global groups

    # selecting new folder from final page
    # if (page == 'final'):
    if (folder_path != ''):
        os.system('attrib -h "' + folder_path + '"')

    folder_path = filedialog.askdirectory()

    # check if folder is hidden
    if bool(os.stat(folder_path).st_file_attributes & 2):
        print("Hidden!")
    else:
        # hide folder
        os.system('attrib +h "' + folder_path + '"')

        clear_global_lists()

        image_files = [f for f in os.listdir(folder_path) if f.endswith(".dng")]
        make_groups()

        # print(folder_path, image_files) # debug
        page.destroy()
        open_grouping()

# removes hidden tag from folder on close
def on_exit():
    os.system('attrib -h "' + folder_path + '"')

# opens readme doc on GitHub
def readmelink():
    webbrowser.open("https://github.com/aidan-hubley/grouping_app/blob/main/ReadMe.md")

# opens landing page
def open_landing():
    global landing
    landing = Tk()
    landing.title("Landing Page")
    landing.geometry("250x250")
    # landing.maxsize(250, 250)
    landing.minsize(250, 250)

    hi = Label(landing, text="Welcome", font=(10))
    hi.place(relx=0.5, rely=0.3, anchor=CENTER)
    select = Button(landing, text="Select Folder", command=lambda: select_folder(landing))
    select.place(relx=0.5, rely=0.6, anchor=CENTER)
    readme = Button(landing, text="Info", command=readmelink)
    readme.place(relx=0.5, rely=0.7, anchor=CENTER)

    landing.mainloop()

# def resize_multipliers(canvas):
#     global height_mult
#     global width_mult
#     height_mult = canvas.winfo_height()/700
#     width_mult = canvas.winfo_width()/1200
#     print(canvas.winfo_height())
#     print(height_mult)


# ______________________________________________________________________________________________________________________
# Phase 0: Global Variables
# ______________________________________________________________________________________________________________________

def clear_global_lists():
    global raw_images
    global grouped_images
    global image_files
    global selected
    global groups
    raw_images = list()
    grouped_images = list()
    image_files = list()
    selected = list()
    groups = list()

raw_height = 181 #145
raw_width = 294 #235
raw_pad = 13
# height_mult = 1
# width_mult = 1

raw_images = list() # list of raw image files
grouped_images = list() # 2d list of grouped image files
image_files = list() # list of raw image file names
selected = list() # list of selected raws
groups = list() # 2d list of grouped file names
folder_path = ""

atexit.register(on_exit)

open_landing()

# ______________________________________________________________________________________________________________________
