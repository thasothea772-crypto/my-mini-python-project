import qrcode

wifiname = input("Enter the wifi name: ")
password = input("Enter the wifi password: ")

wifi_string = f"WIFI:T:WPA;S:{wifiname};P:{password};;"
img = qrcode.make(wifi_string)
img.save("wifi_qr.png")

print("Wifi QRCode saved as wifi_qr.png")
