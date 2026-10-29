import qrcode

text = input("Enter the text or URL: ")
img = qrcode.make(text)
img.save("qrcode.png")

print("QR code saved as qrcode.png")
