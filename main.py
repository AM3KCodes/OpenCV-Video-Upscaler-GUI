from gui import window

window()

# SCRIPT FRAMEWORK

# files = [] # initialize empty list of folders for cleanup function argument
# folders = [] # initialize empty list of folders for cleanup function argument

# file_path = select_file()

# scale_factor = int(input("Enter scale factor: "))
# fps = int(input("Enter video FPS: "))

# frames = extract_frames(file_path)
# audio = extract_audio_file(file_path, Path(file_path).parent)
# files.append(audio)

# folder_to_upscale = f"{Path(frames).name}"
# folders.append(folder_to_upscale)

# upscaled_frames_folder = recursive_upscale(folder_to_upscale, scale_factor)
# folders.append(upscaled_frames_folder)

# # COMBINE VIDEO AND AUDIO
# video_clip = frames_to_video(file_path, fps, upscaled_frames_folder)
# files.append(video_clip)
# combine_clips(video_clip, audio, fps)

# # CLEANUP
# cleanup_files(files)
# cleanup_folders(folders)