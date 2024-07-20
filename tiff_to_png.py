# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:04:48 2024

@author: User
"""

import os
from PIL import Image

# Specify the source directory where TIFF images are stored
source_dir ="C:/Users/User/Desktop/Bilkent ee/EEE-492-Project/15052024/t-2"
# 'C:/Users/User/Desktop/Bilkent ee/EEE-492-Project/ai_spheroid/22042024/dox'
# Specify the target directory where PNG images will be saved
target_dir = "C:/Users/User/Desktop/Bilkent ee/EEE-492-Project/15052024_png"
#'C:/Users/User/Desktop/Bilkent ee/EEE-492-Project/ai_spheroid_png/dox'

# Create the target directory if it doesn't exist
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# Iterate through each file in the source directory
for filename in os.listdir(source_dir):
    if filename.endswith('.tif') or filename.endswith('.tiff'):
        # Generate the full file path
        file_path = os.path.join(source_dir, filename)
        # Open the image file
        with Image.open(file_path) as img:
            # Define the output filename, replacing the extension with .png
            output_filename = os.path.splitext(filename)[0] + '.png'
            output_path = os.path.join(target_dir, output_filename)
            # Convert and save the image as PNG
            img.convert('RGB').save(output_path, 'PNG')

print("Conversion complete. PNG files are saved in", target_dir)