# Create a QR Code Generator That Sends an Email to a User
# Subject: My First Email Using Python
# Body: Hello, this is my first email using Python

import qrcode
email_address = "phuyaljeshik10@gmail.com"
subject = "My First Email Using Python"
body = "Hello, this is my first email using Python" 
mailto = f"mailto:{email_address}?subject={subject}&body={body}"
img = qrcode.make(mailto)
type(img)  # qrcode.image.pil.PilImage
img.save("email.png")

