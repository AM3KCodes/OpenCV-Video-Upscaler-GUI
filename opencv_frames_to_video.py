"""
Frames to Video:

Module for turning frames into video file minus the audio.
* frames_to_video: Takes input video (MP4) file, FPS (integer), and folder path to encode video into.
"""

import cv2
import numpy as np
from pathlib import Path

def frames_to_video(file_path, frame_rate, folder_path):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_name = f"{Path(file_path).stem} - upscaled.mp4"

    
    frame_files = sorted((Path(folder_path)).glob("*"))
    
    first_frame = cv2.imread(str(frame_files[0]))
    height, width = first_frame.shape[:2]
    
    out = cv2.VideoWriter(output_name, fourcc, frame_rate, (width, height))
    frame_count = 0
    print("Converting upscaled frames into video...")
    for frame_file in frame_files:
        
            image = cv2.imread(str(frame_file))
            
            if image is not None:
                out.write(image)
                frame_count += 1
            else:
                print("Skipping until next frame is found.")
    
    out.release()
    
    print(f"Video saved as {output_name}")
    print(f"Frames written: {frame_count}")
    
    return output_name