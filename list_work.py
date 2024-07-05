# import random
# names = ['Anish', 'Binod','Binod', 'Ratna']
'''
# Add item in list
names.append('Jeshik')

# remove item in list
names.pop()

#  find total no. of ocuurances
total_nmae = names.count("Binod")
print(total_nmae)

## find index by value of first item
print(names.index("Jeshik"))

for name in names:
  print(name)

'''

# names.sort()
# names.reverse()
# names.count("Binod")
# print(random.choice(names))


# names2 = names
# print(names2)

'''
number = [1,2,3,4,5,6]   ## list comprehension

even_numbers = [x for x in number if x%2 == 0]
print(even_numbers)
'''

names = ['Anish', 'Binod', 'Ratna', 'Aryan', 'Bibek']

## find all name starting with 'A'

find_letter = [name for name in names if name[0]=='A']

print(find_letter)