num=int(input("Enter the number:"))
ans=1
flag=0
for x in range(1,1000):
	ans=ans*2
	print(ans)
	if ans==num:
		flag=1
		break
if flag==1:
	print("Yes")
else:
	print("No")
© 2018 GitHub, Inc.
p
