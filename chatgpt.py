from tkinter import *
from PIL import Image, ImageTk


def show_images(image_list):
    # Create a new frame to hold the images
    images_frame = Frame(root)
    images_frame.pack(fill="both", expand=True)

    # Create a canvas to hold the images and add it to the frame
    canvas = Canvas(images_frame)
    canvas.pack(side="right", fill="both", expand=True)

    # Create a scrollbar and add it to the frame
    scrollbar = Scrollbar(images_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="left", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame to hold the images and add it to the canvas
    images_inner_frame = Frame(canvas)
    images_inner_frame.pack()
    canvas.create_window((0, 0), window=images_inner_frame, anchor="nw", width=250, height=250)

    # Load and display the images
    for i in range(len(image_list)):
        image = Image.open(image_list[i])
        image = image.resize((250, 250), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        label = Label(images_inner_frame, image=image)
        label.image = image
        label.pack()


# Example image list
image_list = ["house.jpg", "house.jpg", "house.jpg", "house.jpg", "house.jpg"]

root = Tk()
root.title("Image Viewer")
root.geometry("800x600")

show_images(image_list)
root.mainloop()