"""
Cleanup:

Module for removing generated files such as frames, videos, or audio using the OS to facilitate deletions.
Accepts list of file paths to iterate through to prior to deletion.
* cleanup_files(): Takes in list of files to be deleted recursively.
* cleanup_folders(): Takes in list of folders to be deleted recursively.
"""

import os
import shutil
from pathlib import Path

def cleanup_files(files):
    for file in files:
        print(f"Attempting to clean up file {Path(file).name}...")
        if os.path.exists(file):
            os.remove(file)
            print(f"File {Path(file).name} has been deleted.")
        else:
            print(f"File {Path(file).name} was not found or does not exist.")
            
def cleanup_folders(folders):
    for folder in folders:
        print(f"Attempting to clean up folder {Path(folder).name}...")
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"Folder {Path(folder).name} has been deleted.")
        else:
            print(f"Folder {Path(folder).name} was not found or does not exist.")