from pyzbar.pyzbar import decode
from PIL import Image

image_path = "image4.jpg" 

image = Image.open(image_path)
decoded = decode(image)

for obj in decoded:
    print("Decoded Data:", obj.data.decode("utf-8"))
