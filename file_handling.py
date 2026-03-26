import tkinter as tk
from tkinter import filedialog

def select_file():
    root = tk.Tk()
    root.withdraw() # hide initial window
    file_path = filedialog.askopenfilename(title="Select a video", 
                                           initialdir=r"C:/", # universality
                                           filetypes=(("MP4 files", "*.mp4"), ("All files", "*.*"))
                                           )
    if file_path: # check if file path exists
        return file_path
    else:
        print("File does was not selected or filedialog window was closed.")