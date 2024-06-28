## for loop
## Multiply table of 9 using for loop

'''
for i in range(1,11):
  print(f"9 * {i} = {9 *i}")

'''

## Using i and j loop to multiply numbers

'''
start = int(input("Enter start no. : "))
end = int(input("Enter end no. : "))

for i in range(start,end+1):
  for j in range(1,11):
    print(f"{i} * {j} : {i*j}")
  print("\n-------\n")  

'''

## while loop
'''
atm_pin = '1456'
user_pin = ''

max_attempts = 4
attempt = 0
 
while atm_pin != user_pin and attempt < max_attempts:
  if attempt > 0:
    print("Invalid pincode.")
    print(f"Total attempt left :  {max_attempts - attempt}")       
  user_pin = input("Enter ATM Pin: ")
  attempt += 1

if atm_pin == user_pin:
    print("Access Granted. How much do you want to withdraw?")
else:
    print("Maximum attempts reached. Your card has been blocked.")
'''

## result print

results_set = {
  '012323230J' : '4',
  '021312312W' : '3',
  '012321317K' : '2',
}

symbol_no = input("Enter your symbol no. : ")

result = ""
for i in results_set.keys():
  if symbol_no == i:
    result = results_set[i]
    break
  else:
    result = ''  

if result != "":
  print(f"Your result is: {result}")
else:
  print("Symbol no. is error")
    