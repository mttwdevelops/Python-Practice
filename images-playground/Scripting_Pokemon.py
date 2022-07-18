# Created 7/18/2022

from statistics import mode
from PIL import Image, ImageFilter

img = Image.open('./images-playground/Pokedex/pikachu.jpg')
print(img)

print(img.format) # gives us JPG
print(img.size) # gives us (640, 640)
print(img.mode) # gives us RGB

filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save("blur.png", 'png') # we use PNG in this case since using JPG may result in some issues

grey_img = img.convert("L")
grey_img.save("grey.png", 'png')

grey_img.show() # shows image in photoviewer\

