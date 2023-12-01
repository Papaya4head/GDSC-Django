for i in range(100):
    print(f"{i:02d}, ", end="")
print()
#this prints 0 infront of any nuber less than 10 or 2 caracters

for i in range(1000):
    print(f"{i:03d},",end="")
#this prints 0 infront of any number less than 100 or 3 caracters
for i in range(100):
    print(f"{i:03d}, ",end="")
#this prints 0 infront of any number less than 100 or 3 caracters
for i in range(100):
    prifix= "num: " if  i<100 else""    
    print(f"{prifix}{i:02d}, " , end="")
print()
#this prints the word num infront of every number and 0 infront of any numberless than 10 or 2 caracters
for i in range(100):
    prifix= "num: " if  i<100 else""    
    print(f"{prifix}{i}, " , end="")
print()
#prints just word num infront of every number