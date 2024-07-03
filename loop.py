for i in range(1,10):
  if i == 5:
   continue
  print(i)

# write a program that prin 70 to 100 but not [77,78,81]

for i in range(70, 101):
    if i not in [77, 78, 81]:
        print(i)