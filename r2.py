def multiple(a, b):
 
    c = range(b, (a * b)+1, b)
     
    print(*c)
a= int(input('enter the number a:'))
b= int(input('enter the number b:'))
multiple(a, b)
