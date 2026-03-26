"""
OpenCV Frame Extraction:

Module for extracting frames from video, creates folder in local path for frames in JPG format.
* select_file(): Prompts user to select a video (MP4) file from their local directory.
* extract_frames(): Performs the frame extraction. 
"""

import cv2
import os
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

# DEPRECATED START

# def get_fps(file_path):
#     video = cv2.VideoCapture(file_path)
#     if not video.isOpened():
#         print("Error: Could not open video file.")
#         return None
    
#     fps = video.get(cv2.CAP_PROP_FPS)
#     video.release()
#     return fps

# def get_resolution(file_path):
#     video = cv2.VideoCapture(file_path)
    
#     if not video.isOpened():
#         print("Error: Could not open video file.")
#         return None, None
    
#     width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
#     video.release()
    
#     return width, height
    
# DEPRECATED END

def extract_frames(file_path):
    print("Extracting frames...")
    folder_name = f"frames_{Path(file_path).name}"
    video_capture = cv2.VideoCapture(file_path)
    os.makedirs(folder_name, exist_ok=True)
    frame_count = 0
    
    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if not ret: break
        cv2.imwrite(f"{folder_name}/frame_{frame_count:04d}.jpg", frame)
        frame_count += 1
    
    video_capture.release()
    return folder_name
    
# extract_frames(file_path=select_file())
