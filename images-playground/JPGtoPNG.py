# Created 7/18/2022

import sys, os
from PIL import Image

# using sys module grab first and second arguments from the command line
starting_folder = sys.argv[1]
ending_folder = sys.argv[2]

# check if new folder exists, then create it using os
if not os.path.exists(ending_folder):
    os.makedirs(ending_folder)

for filename in os.listdir(starting_folder):
    img = Image.open(f"{starting_folder}{filename}")
    clean_name = os.path.splitext(filename)[0] # need to do this to get just the name of the file rather than .jpg extension
    img.save(f"{ending_folder}{clean_name}.png", "png")
    print("All done.")


# to use: python3 JPGtoPNG.py Pokedex/ EndingFolder/