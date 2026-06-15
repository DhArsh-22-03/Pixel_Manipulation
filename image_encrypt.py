from PIL import Image

# Secret key
key = 50

# Open image
img = Image.open("image.jpg")
pixels = img.load()

width, height = img.size

# Encryption
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]

        r = (r + key) % 256
        g = (g + key) % 256
        b = (b + key) % 256

        pixels[x, y] = (r, g, b)

img.save("encrypted.jpg")

print("Image Encrypted Successfully!")