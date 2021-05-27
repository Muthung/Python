########### Used to encode and decode data into machine-readable form.

########### Black Panther Trailer

import pyqrcode 

from pyqrcode import QRCode

# String which represent the QR code

s = "https://www.youtube.com/watch?v=xjDjIWPwcPU"

# Generate QQr code 

url = pyqrcode.create(s)

# Create and save the png file naming "qrcode.png"

url.svg("panther.svg", scale = 8 )

