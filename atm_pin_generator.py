# ATM PIN GENERATOR


import random
print("WELCOME TO ATM PIN GENERATOR")
print("KINDLY DO NOT SHARE YOUR PASSWORD WITH ANYONE ")
p=int(input("ENTER FIRST TWO DIGITS YOUR PASSWORD \n"))
t=random.randint(0,9)
k=random.randint(0,9)
l=p*100+t*10+k
print("YOUR ATM PIN IS",l)

