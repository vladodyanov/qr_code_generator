import pyqrcode
import png
from pyqrcode import QRCode

address = input('copy the https:// address of the site')
url = pyqrcode.create(address)
url.png('qr_code.png',scale = 8)