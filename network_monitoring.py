import os 
b = 'sudo tshark -i eth0 -R "eth.dst==FF:FF:FF:FF:FF:FF" -a duration:60>output.txt'

os.popen(b)
f = open('output.txt','r')
count =0
for lines in f:
        if lines.strip():
                 count +=1
           
print("The number of broadcast packets on the network in 1 minute is " , count)
print("To view the type of broadcast packets open the file output.txt")

