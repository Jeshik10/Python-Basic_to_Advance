
# img = qrcode.make('Jeshik Phuyal')
# type(img)  # qrcode.image.pil.PilImage
# img.save("jeshik.png")

## WIFI Link
import qrcode
wifi_type = "WPA"
wifi_ssid = "ALHN-3976"
wifi_password = "e3R37Si3s9"
wifi = f"WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;"
img = qrcode.make(wifi)
type(img)  # qrcode.image.pil.PilImage
img.save("wifi.png")