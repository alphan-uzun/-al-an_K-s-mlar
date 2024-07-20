# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 17:12:47 2024

@author: User
"""_

import os
from PIL import Image

def save_png_files_with_pillow(source_dir, dest_dir):
    # Create destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Iterate over files in the source directory
    for filename in os.listdir(source_dir):
        # Check if the file is a PNG image
        if filename.lower().endswith('.png'):
            source_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, filename)
            # Open and save the file using Pillow
            with Image.open(source_path) as img:
                img.save(dest_path)
            print(f"Saved {filename} to {dest_dir}")

if __name__ == "__main__":
    source_directory = "C:/Users/User/Desktop/Bilkent ee/EEE-492-Project/13052024/t_0"  # Replace with your source directory
    destination_directory = "C:/Users/User/Desktop/Bilkent ee/EEE-492-Project/13052024_png"  # Replace with your destination directory

    save_png_files_with_pillow(source_directory, destination_directory)
