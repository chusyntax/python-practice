from PIL import Image, ImageFilter
import os
import sys

# img = Image.open('./Pokedex/pikachu.jpg')

# filtered_img = img.filter(ImageFilter.BLUR)  # Filter a picture

# filtered_img = img.convert("L")  # Grey out a picture

# filtered_img.save("Blurred.png", "png")

# filtered_img.show()  # Opens and shows image

# filtered_img.rotate(90)  # Rotates image

# filtered_img.resize((250, 300))  # Resizes image - Takes in a tuple

# # To crop, first save the four pixel corners in a tuple variable then use that with the crop function

# box = (100, 300, 400, 200)

# region = filtered_img.crop(box)

# img = Image.open('./astro.jpg')

# img.resize((300, 300))

# img.thumbnail((400, 200))  # Helps image keep aspect ratio

# img.save('thumbnail.jpg')


# PNG to JPEG convertor

# 1 ~ Grab frist and second argument
image_folder = sys.argv[1]  # Index 0 for argv is always the file name
output_folder = sys.argv[2]

# 2 ~ Check if new foler exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# 3 ~ Loop through Pokedex
# 4 ~ Convert images to png
# 5 ~ Save to new folder

for filename in os.listdir(image_folder):

    img = Image.open(f'{image_folder}{filename}')

    # Use 0 as splitext will split name and extention into a tuple.
    clean_name = os.path.splitext(filename)[0]

    img.save(f'{output_folder}{clean_name}.png', 'png')
