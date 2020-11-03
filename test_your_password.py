# A simple program to check how strong and secure is your password !  by/ Ismail_Ahmed

import re

pwd = input("Enter your password : ")
if re.search("[a-z]", pwd) and \
   re.search("[A-Z]", pwd) and \
   re.search("\d",pwd):
   print("Your password is stronger!")
else:
   print("Weak password! You should change it right nowwww!")
