"""
OpenCV Recursive Upscale:

Module for recursively upscaling based on a provided scale factor. Accepts JPG files and creates folder in local path for upscaled frames in JPG format.
* read_folder(): Prompts user to select folder of frames/images to be upscaled.
* recusirve_upscale(): Iterates through folder for images and upscales them.
"""

import cv2
import os
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

def read_folder():
    root = tk.Tk()
    root.withdraw()
    
    folder_path = filedialog.askdirectory(title="Select a folder", 
                                     initialdir=r"C:/" # universality
                                     ) 
    if folder_path:
        print(f"Selected {folder_path}")
        return folder_path

    else:
        print("File not selected, closing application.")
        exit()
        
def recursive_upscale(folder_path, scale_factor):
    print("Upscaling frames...")
    output_name = f"upscaled_{Path(folder_path).name}"
    os.makedirs(output_name,exist_ok=True)
    frame_count = 0
    for file_path in Path(folder_path).iterdir():
            image = cv2.imread(str(file_path))
            height, width = image.shape[:2]
            new_height = int(height * scale_factor)
            new_width = int(width * scale_factor)

            upscaled = cv2.resize(src=image,
                                dsize=(new_width, new_height),
                                interpolation=cv2.INTER_LANCZOS4)
            
            cv2.imwrite(f"upscaled_{Path(folder_path).name}/upscaled_frame_{frame_count:04d}.jpg", upscaled)
            frame_count += 1
    
    return output_name