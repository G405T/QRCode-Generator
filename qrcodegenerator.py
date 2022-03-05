import qrcode

# QRCode (Redirecting to URL or Text)

img = qrcode.make("// add text or a url here \\")
img.save("qrcode.jpg")
