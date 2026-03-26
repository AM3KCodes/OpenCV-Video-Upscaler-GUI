"""
Extract Audio:

Module for extracting raw audio from video files using MoviePy.
* extract_audio_file(): Takes input video (MP4) file and extracts the audio as an MP3 file. 
"""

from moviepy import VideoFileClip
from pathlib import Path
import os


def extract_audio_file(file_path, output_path):
    output_path = f"{Path(file_path).parent}/{Path(file_path).name}_audio.mp3"
    if not os.path.exists(file_path):
        print("Error: Files does not exist or was not found.")
        return
    
    try:
        video = VideoFileClip(file_path)
        
        audio = video.audio
        
        audio.write_audiofile(output_path, codec="mp3")
        
        audio.close()
        video.close()
        print(f"Audio extracted to {output_path}")
        return output_path
        
    except Exception as e:
        print(f"An error occurred: {e}")
        