num=int(input("Enter the number:"))
for x in range(2,num):
	if (x==2 or x==3 or x==5 or x==7):
		print(x,"is a prime number")
	elif(x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0):
		print(x,"is a prime number")
	else:
		print(x,"is not prime")