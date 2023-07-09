import random
n = int(input("Enter number"))
m=0
for i in range(0,n,1):
	black= random.randint(1,6)
	green = random.randint(1,6)
	if black > green:
		m += 1 
print("the probability will be:",m/n)