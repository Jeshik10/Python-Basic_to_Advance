## Ask user to enter n number of people names
## and print all names statrting with 'B'
## if there is no name it should print "No Name Found"

def get_name(n):
  names = []
  for i in range(n):
    name =  input(f"Enter name {i+1}: ")
    names.append(name)
  return names

def find_b_names(names):
  return [name for name in names if name.lower().startswith('b')]

def print_results(b_names):
  if b_names:
    print("\nNames starting with 'B': ")
    for name in b_names:
      print(name)
  else:
    print("\n No Name Found!")

n = int(input("Enter the number of people: "))      
names= get_name(n)
b_names = find_b_names(names)  
print_results(b_names)


