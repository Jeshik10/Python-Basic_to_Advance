import time
# Get the curent hour
current_hour = time.localtime().tm_hour

# Check the current hour and print the corresponding greeting

if current_hour >= 5 and current_hour < 12:
    print("Good morning!")
elif current_hour >= 12 and current_hour < 18:
    print("Good afternoon!")
elif current_hour >= 18 and current_hour < 22:
    print("Good evening!")
else:
    print("Good night!")