# for randomization
# Gnerate random number in python

'''
import random
random_number = random.randint(1,1000)
print(random_number) '''

# RNDOM NUMBER GUESS Game
'''
import random

random_number = random.randint(1,20)
user_inut = int(input(f"Enter number between 1 to 20: "))
print(f"Actual random no. is: {random_number}")

persons = ['Ram', 'Sita', 'Menuka', 'Hari', 'Jeshik']
winner =  random.choice(persons)
print(winner) '''

# Create a program to find random no betn -20 and -10
'''
import random
random_number = random.randint(-20,-10)
print(f"the random number is: {random_number}")

'''

# persons = ['Ram', 'Sita', 'Menuka', 'Hari', 'Jeshik']
# for person in persons:
#   if person < 10:
#    print(f"enter the name of a person: ")

# winner =  random.choice(persons)
# print(winner)

#------------------- PASSWORD GENERTOR ----------------

import random
alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
alphabet_upper = alphabet.upper()
numbers = '1,2,3,4,5,6,7,8,9,0'

all_combine = alphabet + alphabet_upper + numbers
all_combine_to_list = all_combine.split(",")

random1 = random.choice(all_combine_to_list)
random2 = random.choice(all_combine_to_list)
random3 = random.choice(all_combine_to_list)
random4 = random.choice(all_combine_to_list)
random5 = random.choice(all_combine_to_list)
random6 = random.choice(all_combine_to_list)
random7 = random.choice(all_combine_to_list)
random8 = random.choice(all_combine_to_list)
random9 = random.choice(all_combine_to_list)
random10 = random.choice(all_combine_to_list)

password = random1 + random2 + random3 + random4 + random5 + random6 + random7 + random8 + random9 + random10
print(f"Generated password is: {password}")

#Type conversion

number1 = int(input(" Enter number 1: "))
number2 = int(input(" Enter number 2: "))
sum = number1 + number2
print(f" Total is {sum}")