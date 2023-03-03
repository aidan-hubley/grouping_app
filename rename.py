import os
import tkinter as tk
from tkinter import filedialog

def select_folder():
    # Prompt user to select a folder
    folder_path = filedialog.askdirectory()
    if folder_path:
        # Update the label to show the selected folder path
        folder_label.config(text=folder_path)
        # Process the files in the selected folder
        process_files(folder_path)

def process_files(folder_path):
    # Loop through all files in the selected folder
    for filename in os.listdir(folder_path):
        # Check if the file name contains a dash
        if '-' in filename:
            # Split the file name into two parts using the dash as a delimiter
            parts = filename.split('-')
            # Remove the first part (prefix) and join the remaining parts with a dash
            new_filename = '-'.join(parts[1:]).strip()
            # Rename the file
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

# Create the main window
root = tk.Tk()
root.title('Select a folder')

# Set the default window size
root.geometry('500x300')

# Create the label to show the selected folder path
folder_label = tk.Label(root, text='')
folder_label.pack()

# Create the button to open the file dialog
select_folder_button = tk.Button(root, text='Select Folder', command=select_folder)
select_folder_button.pack(pady=10)

# Create the button to close the window
close_button = tk.Button(root, text='Close', command=root.destroy)
close_button.pack(pady=10)

# Start the main event loop
root.mainloop()
