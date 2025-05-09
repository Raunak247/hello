n=13
a,b = 0,1
if n<0:
    print('negative')
else:
    for i in range(n):
        print(a)
        a,b = b,a+b