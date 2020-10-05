# fake is a python module provide a fake email, url, name ... etc. 


from faker import Faker
from datetime import datetime



print("-"*100)
print(datetime.now())
print("-"*100)

print('''
(1) get email 
(2) get name
(3) get URL 
(4) get country name
(5) get text
''') 

get = Faker()

order = int(input(" select a number : "))

if order == 1 :
            print(get.email())
elif order == 2 :
            print(get.name())
elif order == 3 :
            print(get.url())
elif order == 4 :
            print(get.country())
elif order == 5 :
            print(get.text())
            
            
else:
         print("invalid input... please try again! ")
