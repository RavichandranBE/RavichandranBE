try:
	n1=input('enter the number')
	n2=input('enter the number')
	while(n2!=0):
		t=n2
		n2=n1%n2
		n1=t
	print(n1)
except:
	print('invalid')
