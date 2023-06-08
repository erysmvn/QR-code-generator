import pyqrcode

link = input("Enter the link: ")

img = pyqrcode.create(link)
img.png('/Users/erysvmn/Desktop/qr.png', scale=8)
img.show()