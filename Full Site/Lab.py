 x=int(input("enter your number: "))

y=x%10
z=x//10

print("separated digits: ",z, y)

print("reverse umber is: ",(y*10 + z))


x=int(input("enter your number: "))

print("last two digits are: ",x%100)



x=int(input("enter 1st number: "))
y=int(input("enter 2nd number: "))

z=x*100+y
print("concatenated number is: ",z)


 x=int(input("enter your number: "))
y=x%100
z=x//100
print("The new number is: ",(y*100+z))


week=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
k=int(input())
if 1<=k<=365:
	n=k%7
	if n<4:
		n+=3
		print( str(week[n]))
	else:
		n-=4
		print(str(week[n]))
else:
	print("\nYour number is invalid.")