from teacher import Teacher

tota_tch = int(input("How many teacher data you want to insert: "))

lists = []
for i in range(tota_tch):
  name = input(f"Enter teacher {i+1} name: ")
  phone = input(f"Enter teacher {i+1} phone: ")
  s = Teacher(name, phone)
  ## Save to File
  f = open("contact.csv", "a")
  f.write(f"{s.name},{s.phone}\n")
  f.close()





