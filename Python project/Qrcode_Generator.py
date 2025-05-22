import qrcode as qr
from PIL import Image

# Get URL input from the user
user_url = input("Enter the URL for the QR code: ")

# Create QR code
img = qr.QRCode(
    version=1,
    error_correction=qr.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
img.add_data(user_url)
img.make(fit=True)

# Generate image
pic = img.make_image(fill_color="white", back_color="black")

# Save image
filename = "qr_code.png"
pic.save(filename)

# Display image (if using Jupyter or google colab)
try:
    from IPython.display import display
    display(pic)
except ImportError:
    print(f"QR code saved as {filename}")
