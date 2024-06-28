import qrcode
phone_number = "9860568697"
message = "Hi! this msg was sent mistakely"
# sms = f"SMSTO:{phone_number}:{message}"
sms = f"sms:{phone_number}?body={message}"
img = qrcode.make(sms)
type(img)  # qrcode.image.pil.PilImage
img.save("sms.png")

#create qr geneartor that send email to user
#title: My first Emali using Python
# Body: hello this is my first 