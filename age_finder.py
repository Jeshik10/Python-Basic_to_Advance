# def age_finder(birth_year):
#   age = 2024 - birth_year
#   print(f"Age is {age}")


# def test_function():  ## "Pass" doesnot do anything
#   pass

# age_finder(2000)



# def display_name():
#   name =  "JESHIK phuyal"
#   print(name)
# display_name()  


## function that reverse string
def reverse_string(text):
  name = text

  reverse_string = ""
  for i in range(len(name) -1 , -1, -1):
    reverse_string += name[i]
  return reverse_string

result = reverse_string("jeshik")
print(result)
  

