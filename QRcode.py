import pyqrcode

import png

from pyqrcode import QRCode

# Paste any url or type anything you want to display it in the qrcode
QRstring = "https://www.linkedin.com/in/engismail2020/"

url = pyqrcode.create(QRstring)

url.png('Desktop\\qr.png', scale = 9)
