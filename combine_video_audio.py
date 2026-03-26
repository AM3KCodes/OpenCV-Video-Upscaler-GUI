"""
Combine Video with Audio:

Module for combining video (MP4) file with audio (MP3) file and encoding/writing the video using MoviePy.
* combine_clips(): Takes video file, audio file, and FPS to encode the video with.
"""

from moviepy import VideoFileClip, AudioFileClip
from pathlib import Path

def combine_clips(file_path, audio_path, fps):
    print("Adding audio to video...")
    video_clip = VideoFileClip(file_path)
    audio_clip = AudioFileClip(audio_path)
    
    final_clip = video_clip.with_audio(audio_clip)
    final_clip.write_videofile(f"{Path(file_path).stem} with audio.mp4", fps, audio_codec="aac")