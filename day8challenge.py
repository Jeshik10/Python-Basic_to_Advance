## Create a function that generate a random password
## Option: Use parameter for no. of character in password
## passwordgenerator()

import random
import string

def generate_password(length=12):
  characters = string.ascii_letters + string.digits + string.punctuation
  
  password = ''
  for i in range(length):
     password += random.choice(characters)

  return password

print(generate_password(5))   