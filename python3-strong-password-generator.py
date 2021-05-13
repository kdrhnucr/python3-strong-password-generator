import random

character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890!?"
lenght = int(input("How many characters do you want it to be : "))
password =  "".join(random.sample(character,lenght ))

new_password = "Your new strong password is :" 
print (new_password,password)
