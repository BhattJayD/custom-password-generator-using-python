import random #for random password genration

#taking input for random charecters
print("enter charecters:")
chars=str(input()) 

#taking input for strangth of password
print("how strong you want password:")
n=int(input())

#generating random password
password=""
for i in range(n):
	password+=random.choice(chars)
print(password)
