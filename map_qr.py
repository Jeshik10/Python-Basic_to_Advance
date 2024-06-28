import qrcode

latitude = "27.701299278561173"
longitude = "85.38262738789932"
map = f"https://www.google.com/maps?q={latitude},{longitude}"
img = qrcode.make(map)
type(img)  # qrcode.image.pil.PilImage
img.save("map.png")