import random

character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890!?"
lenght = int(input("How many characters do you want it to be : "))
password =  "".join(random.sample(character,lenght ))

print (password)