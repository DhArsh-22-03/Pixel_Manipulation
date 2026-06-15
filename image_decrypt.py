from PIL import Image

# Same secret key used during encryption
key = 50

img = Image.open("encrypted.jpg")
pixels = img.load()

width, height = img.size

# Decryption
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]

        r = (r - key) % 256
        g = (g - key) % 256
        b = (b - key) % 256

        pixels[x, y] = (r, g, b)

img.save("decrypted.jpg")

print("Image Decrypted Successfully!")