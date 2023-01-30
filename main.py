#@author Joshua Phillips
#with help from Aidan Hubley
#Stackoverflow users referenced : John1024,
from tkinter import filedialog, Label, Button, PhotoImage, Tk
import glob

main = Tk()

image1 = PhotoImage(file='C:/Users/gltig/OneDrive/Pictures/Saved Pictures/Stuff.png')
updated_image = image1.subsample(3, 3)

folder_path = None

def file_select():
    global folder_path
    folder_path = filedialog.askdirectory()
    print(folder_path)
    image_label = Label(main, image=updated_image)
    image_label.pack()


def rename_file(file_name, group_num):
    if file_name.endswith('.dng'):
        file_new_name = file_name[:len(file_name)-4] + '-' + str(group_num) + '.dng'
        print(file_name + '\n' + file_new_name)
        #uncomment when ready to implement:
        # os.rename(file_name, file_new_name)
    else:
        print("File is not of type dng")


folder_label = Label(main, text = "Select a Folder")

folder_button = Button(main, text="Open File Explorer", command=file_select,
                 padx = 50, pady = 20, bg="grey", fg="blue", highlightbackground="black")

if folder_path is None:
    folder_label.grid(row=0, column=0)
    folder_button.grid(row=1, column=0)
else:
    filelist = glob.glob(folder_path + '/*.dng')
    for file in filelist:
        #convert dng to jpg
        #display
    #grouping

#print(rename_file('input.dg', 1))

main.mainloop()
