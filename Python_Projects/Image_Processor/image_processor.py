from PIL import Image, ImageFilter

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

img = Image.open('./astro.jpg')

img.resize((300, 300))

img.thumbnail((400, 200))  # Helps image keep aspect ratio

img.save('thumbnail.jpg')
