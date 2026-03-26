"""
GUI:

Module for providing upscaler GUI that uses other modules to handle processes.
* window(): Uses all other modules to handle logic with interactive GUI elements. 
"""

from file_handling import select_file
from opencv_frame_extraction import extract_frames
from opencv_upscale_recursive import recursive_upscale
from opencv_frames_to_video import frames_to_video
from extract_audio import extract_audio_file
from combine_video_audio import combine_clips
from cleanup import cleanup_files, cleanup_folders
import tkinter as tk
from tkinter import ttk
from pathlib import Path
from ttkthemes import ThemedTk
import threading

def window():
    root = ThemedTk(theme="adapta")
    root.title('OpenCV Video Upscaler')
    root.geometry('500x350')
    root.resizable = (False, False)

    style = ttk.Style(root)
    
    style.configure('Title.TLabel',
                    font=("Franklin Gothic Medium", 24)
                    )

    style.configure('TButton',
                    font=("Franklin Gothic Medium", 18),
                    padding=[15, 10, 15, 10])

    style.configure('Custom.TLabel',
                    font=("Franklin Gothic Medium", 14))
    
    style.configure("ValueEntry.TEntry",
                    font=("Franklin Gothic Medium", 8))

    selected_path = None

    def file_selection():
        nonlocal selected_path
        file_path = select_file()
        selected_path = file_path
        print(selected_path)
        if file_path:
            file_selected_label.configure(text=f"{Path(file_path).name} selected.")
            file_selected_label.pack(side="top")

            upscale_factor_entry.delete(0, tk.END)
            fps_entry.delete(0, tk.END)
            
            upscale_factor_label.pack(side='top')
            upscale_factor_entry.pack(side='top')
            
            fps_label.pack(side='top')
            fps_entry.pack(side='top')
            confirm_button.pack(side='top')            
                        
        if file_path == None:
            file_selected_label.configure(text="No file was selected.")
            
            upscale_factor_entry.delete(0, tk.END)
            fps_entry.delete(0, tk.END)
            
            upscale_factor_label.pack_forget()
            upscale_factor_entry.pack_forget()
            
            fps_label.pack_forget()
            fps_entry.pack_forget()
            confirm_button.pack_forget()
            
    def pipeline():
        sf = scale_factor.get()
        frame_rate = fps.get()
        
        if not selected_path:
            warning_label.configure(text="File not found. Try again.")
            warning_label.pack(side="top")
            return
        
        if sf <= 0 or frame_rate <= 0:
            warning_label.pack(side='top')
            return
        
        warning_label.pack_forget()

        confirm_button.config(state="disabled")

        thread = threading.Thread(
            target=run_pipeline,
            args=(sf, frame_rate, selected_path),
            daemon=True
        )
        thread.start()   
    
    def run_pipeline(sf, frame_rate, path):
        files = []
        folders = []

        try:
            frames = extract_frames(path)

            audio = extract_audio_file(path, Path(path).parent)
            files.append(audio)

            folder_to_upscale = f"{Path(frames).name}"
            folders.append(folder_to_upscale)

            upscaled_frames_folder = recursive_upscale(folder_to_upscale, sf)
            folders.append(upscaled_frames_folder)

            video_clip = frames_to_video(path, frame_rate, upscaled_frames_folder)
            files.append(video_clip)

            combine_clips(video_clip, audio, frame_rate)

        finally:
            cleanup_files(files)
            cleanup_folders(folders)

            root.after(0, lambda: confirm_button.config(state="normal"))
        
    top_text = ttk.Label(root, text="OpenCV Video Upscaler", style="Title.TLabel")
    top_text.pack(side='top')


    selection_button = ttk.Button(root, text="Select File...", command=file_selection)
    selection_button.pack(side='top', pady=10)
    
    file_selected_label = ttk.Label(root, text="", style="Custom.TLabel", foreground="red")

    scale_factor = tk.IntVar()
    upscale_factor_label = ttk.Label(root, text="Upscale Factor:", style="Custom.TLabel")
    upscale_factor_entry = ttk.Entry(root, textvariable=scale_factor, width=5, style="ValueEntry.TEntry")
    
    fps = tk.IntVar()
    fps_label = ttk.Label(root, text="FPS:", style="Custom.TLabel")
    fps_entry = ttk.Entry(root, textvariable=fps, width=5, style="ValueEntry.TEntry")
    
    warning_label = ttk.Label(root, text="FPS and/or upscale factor are negative or equal to 0. Please enter another value.", style="Custom.TLabel", foreground="red")
    
    confirm_button = ttk.Button(root, text="Upscale", command=pipeline)

    root.mainloop()