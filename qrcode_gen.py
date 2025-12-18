
import os
import sys
import qrcode

data = input("Enter the text or URL: ").strip()
if not data:
    print("No data provided; aborting.")
    sys.exit(1)

filename = input("Enter the filename (default: qrcode.png): ").strip()
if not filename:
    filename = "qrcode.png"
if not os.path.splitext(filename)[1]:
    filename += ".png"

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill_color="black", back_color="white")


try:
    from PIL import Image  
except Exception:
    print("Pillow is required to save the image. Install with: python -m pip install pillow")
    sys.exit(1)

try:
    image.save(filename)
except Exception as e:
    print(f"Failed to save QR image: {e}")
    sys.exit(1)

print(f"QR saved as {filename}")