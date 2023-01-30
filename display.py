import os
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog


def open_folder():
    # Open a file dialog and get the selected directory
    folder_path = filedialog.askdirectory()
    # Get list of image files in the selected directory
    image_files = [f for f in os.listdir(folder_path) if f.endswith(".jpg") or f.endswith(".png")]

    # Create a new frame to hold the images
    images_frame = Frame(root)
    images_frame.pack(fill="both", expand=True)

    # Create a canvas to hold the images and add it to the frame
    canvas = Canvas(images_frame, bg='white')
    canvas.pack(fill="both", expand=True)

    # Create a scrollbar and add it to the frame
    scrollbar = Scrollbar(images_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame to hold the images and add it to the canvas
    images_inner_frame = Frame(canvas, bg='white')
    canvas.create_window((0, 0), window=images_inner_frame, anchor="nw")

    # Load and display the images
    for i in range(len(image_files)):
        image = Image.open(os.path.join(folder_path, image_files[i]))
        image = image.resize((250, 250), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        label = Label(images_inner_frame, image=image, bg='white')
        label.image = image
        label.pack()
        label.bind("<Button-1>", on_label_click)


def on_label_click(event):
    label = event.widget
    # Add or remove the label from the selection
    if label in selected_labels:
        label.configure(borderwidth=0)
        selected_labels.remove(label)
    else:
        label.configure(borderwidth=2, relief="solid")
        selected_labels.append(label)


root = Tk()
root.title("Open Folder")
root.geometry("800x600")

# Create a frame to hold the "Open Folder" button
button_frame = Frame(root, bg='white')
button_frame.pack(padx=10, pady=10, side="left")

open_folder_button = Button(button_frame, text="Open Folder", command=open_folder)
open_folder_button.pack()

# List to store the selected labels
selected_labels = []
root.mainloop()
